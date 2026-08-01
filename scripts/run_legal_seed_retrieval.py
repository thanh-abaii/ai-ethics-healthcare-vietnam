#!/usr/bin/env python3
"""Retrieve the three registered legal seed documents from the official portal.

This is a post-registration execution utility.  It saves the official landing
page, response headers, the linked signed PDF, and SHA-256 checksums.  A run is
accepted only when every seed has an HTTP 200 landing page, one first-party PDF,
and matching recorded checksums.  It deliberately does not infer legal effects,
create registry rows, deduplicate, or open screening.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "artifacts" / "search-rerun-01-2026-07-31" / "official-sources"
SEEDS = (
    ("LAW_134_2025_QH15", "134/2025/QH15", "Luật Trí tuệ nhân tạo", "2025", "https://vanban.chinhphu.vn/?classid=1&docid=216334&pageid=27160&typegroupid=3"),
    ("DECREE_142_2026_ND_CP", "142/2026/NĐ-CP", "Quy định chi tiết một số điều và biện pháp thi hành Luật Trí tuệ nhân tạo", "2026", "https://vanban.chinhphu.vn/?docid=218029&orggroupid=2&pageid=27160"),
    ("CIRCULAR_05_2026_TT_BKHCN", "05/2026/TT-BKHCN", "Ban hành Khung đạo đức trí tuệ nhân tạo quốc gia", "2026", "https://vanban.chinhphu.vn/?classid=1&docid=217165&pageid=27160&typegroupid=6"),
)
USER_AGENT = "AI-Ethics-Healthcare-Vietnam-ScopingReview/1.0 (audit retrieval)"


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def fetch(url: str) -> tuple[int, dict[str, str], bytes]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.1"})
    with urlopen(request, timeout=45) as response:
        return response.status, dict(response.headers.items()), response.read()


def official_pdf_url(page_html: str) -> str | None:
    match = re.search(r'https?://datafiles\.chinhphu\.vn/[^"\'<>\s]+?\.pdf', unescape(page_html), re.IGNORECASE)
    return match.group(0) if match else None


def write_bytes(path: Path, payload: bytes) -> None:
    path.write_bytes(payload)


def main() -> int:
    run_id = "legal-seed-retrieval-" + datetime.now().strftime("%Y%m%dT%H%M%S")
    run_dir = OUTPUT_ROOT / run_id
    raw_dir = run_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=False)
    ledger: list[dict[str, str]] = []

    for sequence, (seed_id, number, title, year, landing_url) in enumerate(SEEDS, 1):
        # Keep raw filenames deliberately short: Windows has a legacy path
        # length boundary and the research artifact root is intentionally deep.
        file_key = f"s{sequence:02d}"
        result = {"seed_id": seed_id, "official_document_number": number, "title": title, "year": year, "landing_url": landing_url,
                  "landing_status": "", "pdf_url": "", "pdf_status": "", "result": "FAIL", "reason": ""}
        try:
            landing_status, landing_headers, landing_body = fetch(landing_url)
            result["landing_status"] = str(landing_status)
            write_bytes(raw_dir / f"{file_key}.landing.html", landing_body)
            (raw_dir / f"{file_key}.landing.headers.json").write_text(json.dumps(landing_headers, ensure_ascii=False, indent=2), encoding="utf-8")
            pdf_url = official_pdf_url(landing_body.decode("utf-8", errors="replace"))
            if landing_status != 200 or not pdf_url:
                result["reason"] = "LANDING_NOT_200_OR_NO_FIRST_PARTY_PDF_LINK"
                ledger.append(result)
                continue
            result["pdf_url"] = pdf_url
            pdf_status, pdf_headers, pdf_body = fetch(pdf_url)
            result["pdf_status"] = str(pdf_status)
            write_bytes(raw_dir / f"{file_key}.signed.pdf", pdf_body)
            (raw_dir / f"{file_key}.pdf.headers.json").write_text(json.dumps(pdf_headers, ensure_ascii=False, indent=2), encoding="utf-8")
            if pdf_status == 200 and pdf_body.startswith(b"%PDF"):
                result["result"] = "PASS_RAW_OFFICIAL_DOCUMENT_CAPTURED"
            else:
                result["reason"] = "PDF_NOT_200_OR_NOT_PDF"
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            result["reason"] = f"TRANSPORT_ERROR:{type(exc).__name__}:{exc}"
        ledger.append(result)

    with (run_dir / "query-ledger.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(ledger[0]))
        writer.writeheader()
        writer.writerows(ledger)

    hashes = []
    for path in sorted(raw_dir.iterdir()):
        if path.is_file():
            hashes.append({"relative_path": path.relative_to(run_dir).as_posix(), "sha256": sha256(path.read_bytes()), "bytes": path.stat().st_size})
    with (run_dir / "sha256.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "sha256", "bytes"])
        writer.writeheader()
        writer.writerows(hashes)

    checksum_by_path = {row["relative_path"]: row["sha256"] for row in hashes}
    inventory_fields = [
        "manifestation_id", "source_channel", "source_record_id", "title", "year", "doi", "pmid", "openalex_id",
        "raw_artifact_locator", "raw_artifact_checksum", "retrieval_run_id", "query_locator", "provenance_status",
    ]
    inventory = []
    for sequence, row in enumerate(ledger, 1):
        if row["result"] != "PASS_RAW_OFFICIAL_DOCUMENT_CAPTURED":
            continue
        file_key = f"s{sequence:02d}"
        pdf_rel = f"official-sources/{run_id}/raw/{file_key}.signed.pdf"
        inventory.append({
            "manifestation_id": f"LEGAL:{row['official_document_number']}", "source_channel": "LEGAL_OFFICIAL_PORTAL",
            "source_record_id": row["official_document_number"], "title": row["title"], "year": row["year"],
            "doi": "", "pmid": "", "openalex_id": "", "raw_artifact_locator": pdf_rel,
            "raw_artifact_checksum": checksum_by_path[f"raw/{file_key}.signed.pdf"], "retrieval_run_id": run_id,
            "query_locator": row["landing_url"], "provenance_status": "VERIFIED_RAW_MANIFEST",
        })
    with (run_dir / "legal-manifestation-inventory.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=inventory_fields)
        writer.writeheader()
        writer.writerows(inventory)

    success = all(row["result"] == "PASS_RAW_OFFICIAL_DOCUMENT_CAPTURED" for row in ledger)
    manifest = {"run_id": run_id, "completed_at_utc": utcnow(), "seed_count": len(SEEDS),
                "successful_seed_count": sum(row["result"] == "PASS_RAW_OFFICIAL_DOCUMENT_CAPTURED" for row in ledger),
                "status": "RAW_OFFICIAL_LEGAL_SEEDS_CAPTURED_NOT_SCREENED" if success else "FAIL_CLOSED_LEGAL_SEED_RETRIEVAL_INCOMPLETE",
                "scope_limit": "Registered seed retrieval only; no legal-effect inference, relation expansion, registry creation, deduplication, screening, extraction, or synthesis.",
                "required_next_step": "Human legal-content verification and registered relation traversal before any evidence claim."}
    (run_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False))
    return 0 if success else 2


if __name__ == "__main__":
    raise SystemExit(main())
