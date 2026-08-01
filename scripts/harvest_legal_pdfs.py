#!/usr/bin/env python3
"""Extract candidate PDF links from captured legal portal HTML pages, harvest full-text PDFs, and compute SHA-256 checksums.

This script processes raw HTML search pages captured from vanban.chinhphu.vn and congbao.chinhphu.vn,
identifies candidate document attachments (.pdf / document detail pages), downloads full-text PDFs,
computes SHA-256 checksums, and creates a transparent audit ledger.
"""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import os
import re
import ssl
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGAL_RUN_DIR = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/legal-portals-20260801T092029"
OUTPUT_DIR = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/legal-pdf-harvest-20260801"


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def to_long_path(path: Path) -> str:
    abs_str = str(path.resolve())
    if os.name == "nt" and not abs_str.startswith("\\\\?\\"):
        return "\\\\?\\" + abs_str
    return abs_str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    target = to_long_path(path)
    with open(target, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        if tag.lower() == "a":
            attr_dict = dict(attrs)
            href = attr_dict.get("href")
            text = attr_dict.get("title", "")
            if href:
                self.links.append((href, text))


def fetch_resource(url: str, timeout: int = 30) -> tuple[int | None, dict, bytes, str | None]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/pdf,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as response:
            return response.status, dict(response.headers.items()), response.read(), None
    except Exception as exc:
        return None, {}, b"", f"{type(exc).__name__}: {exc}"


def main() -> int:
    timestamp = dt.datetime.now().strftime("%Y%m%dT%H%M%S")
    raw_pdf_dir = OUTPUT_DIR / "pdfs"
    os.makedirs(to_long_path(raw_pdf_dir), exist_ok=True)

    raw_dir = LEGAL_RUN_DIR / "raw"
    html_files = sorted(raw_dir.glob("*.html"))
    print(f"Found {len(html_files)} HTML search result pages to process.")

    pdf_candidates: set[tuple[str, str, str]] = set()

    for html_file in html_files:
        content = html_file.read_bytes()
        text = content.decode("utf-8", errors="replace")
        parser = LinkExtractor()
        try:
            parser.feed(text)
        except Exception:
            continue

        base_url = "https://vanban.chinhphu.vn" if "gov-vb" in html_file.name else "https://congbao.chinhphu.vn"

        for href, link_text in parser.links:
            abs_url = urllib.parse.urljoin(base_url, href)
            # Filter for direct PDF files or document detail pages
            if ".pdf" in abs_url.lower() or "pageid=27160" in abs_url.lower() or "chi-tiet-van-ban" in abs_url.lower() or "vbpq-todaw.aspx" in abs_url.lower():
                pdf_candidates.add((abs_url, html_file.name, link_text))

    print(f"Extracted {len(pdf_candidates)} candidate document/PDF URLs.")

    ledger: list[dict[str, object]] = []

    for index, (candidate_url, source_file, title) in enumerate(sorted(pdf_candidates), start=1):
        print(f"[{index}/{len(pdf_candidates)}] Harvesting: {candidate_url[:80]}...")

        # If it's an HTML detail page, check if it embeds a direct PDF link
        target_url = candidate_url
        if not candidate_url.lower().endswith(".pdf"):
            st, hdrs, bdy, err = fetch_resource(candidate_url)
            if bdy:
                text_detail = bdy.decode("utf-8", errors="replace")
                pdf_matches = re.findall(r'href=["\']([^"\']+\.pdf)["\']', text_detail, re.IGNORECASE)
                if pdf_matches:
                    base_detail = candidate_url
                    target_url = urllib.parse.urljoin(base_detail, pdf_matches[0])
                    print(f"   -> Resolved embedded PDF: {target_url[:80]}")

        status, headers, pdf_bytes, error = fetch_resource(target_url)

        filename_stem = f"legal-doc-{index:03d}"
        if error or not pdf_bytes or len(pdf_bytes) < 500:
            ext = "error.txt"
            save_bytes = (error or "HTTP_EMPTY_OR_FAILED").encode("utf-8")
            row_status = "FETCH_FAILED"
        else:
            ext = "pdf" if target_url.lower().endswith(".pdf") or pdf_bytes.startswith(b"%PDF") else "html"
            save_bytes = pdf_bytes
            row_status = "PDF_CAPTURED" if ext == "pdf" else "HTML_DOC_CAPTURED"

        pdf_path = raw_pdf_dir / f"{filename_stem}.{ext}"
        long_pdf_path = to_long_path(pdf_path)
        with open(long_pdf_path, "wb") as f:
            f.write(save_bytes)

        file_hash = sha256_bytes(save_bytes)

        ledger.append({
            "doc_id": filename_stem,
            "candidate_url": candidate_url,
            "target_download_url": target_url,
            "source_html_file": source_file,
            "link_title": title[:100],
            "http_status": status or "",
            "bytes": len(save_bytes),
            "sha256": file_hash,
            "format": ext,
            "file_path": f"pdfs/{filename_stem}.{ext}",
            "status": row_status,
            "harvested_at_utc": utcnow()
        })

    # Save query ledger
    ledger_path = OUTPUT_DIR / "pdf-harvest-ledger.csv"
    with open(to_long_path(ledger_path), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(ledger[0].keys()) if ledger else ["doc_id"])
        writer.writeheader()
        writer.writerows(ledger)

    # Generate sha256.csv
    hashes = []
    out_dir_long = to_long_path(OUTPUT_DIR)
    for root, _, files in os.walk(out_dir_long):
        for f_name in sorted(files):
            if f_name == "sha256.csv":
                continue
            full_p = Path(root) / f_name
            rel_p = str(full_p).replace("\\\\?\\", "").replace(str(OUTPUT_DIR.resolve()), "").lstrip("\\/").replace("\\\\", "/").replace("\\", "/")
            hashes.append({
                "relative_path": rel_p,
                "sha256": sha256_file(full_p),
                "bytes": full_p.stat().st_size
            })

    hashes.sort(key=lambda x: x["relative_path"])
    with open(to_long_path(OUTPUT_DIR / "sha256.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["relative_path", "sha256", "bytes"])
        writer.writeheader()
        writer.writerows(hashes)

    captured_pdfs = sum(1 for r in ledger if r["status"] == "PDF_CAPTURED")
    captured_htmls = sum(1 for r in ledger if r["status"] == "HTML_DOC_CAPTURED")

    manifest = {
        "run_id": f"pdf-harvest-{timestamp}",
        "completed_at_utc": utcnow(),
        "total_candidate_urls": len(pdf_candidates),
        "pdf_files_captured": captured_pdfs,
        "html_doc_files_captured": captured_htmls,
        "failed_downloads": len(ledger) - captured_pdfs - captured_htmls,
        "status": "RAW_LEGAL_PDF_HARVEST_COMPLETE_UNSCREENED",
        "limitations": [
            "Full-text PDFs and document detail HTML pages captured from official government portals.",
            "Documents are raw and unscreened.",
            "No screening, extraction, or PRISMA decision has been made."
        ]
    }
    (OUTPUT_DIR / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nPDF Harvesting Complete: {OUTPUT_DIR}")
    print(f"Captured: {captured_pdfs} PDFs, {captured_htmls} HTML docs, {len(ledger)} total ledgered.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
