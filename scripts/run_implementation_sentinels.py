#!/usr/bin/env python3
"""Capture reproducible, unscreened transport evidence for the 9 verified sentinel cases.

This runner executes the 10 locked implementation/tool/evidence queries against
the 9 independently verified case domains in implementation-case-sampling-frame.csv.
It records all raw HTTP responses, headers, candidate locators, and SHA-256 checksums.
It never screens, extracts, or infers absence of evidence.
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAME = ROOT / "implementation-case-sampling-frame.csv"
CATALOG = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/nonlegal-portals-2026-07-31/query-catalog.csv"
OUTPUT_ROOT = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/sentinel-runs"


class Hrefs(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    target = to_long_path(path)
    with open(target, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def safe_name(value: str) -> str:
    return re.sub(r"[^a-z0-9_-]+", "-", value.lower())


def same_domain_links(body: bytes, request_url: str, domain_netloc: str) -> list[str]:
    text = body.decode("utf-8", errors="replace")
    parser = Hrefs()
    try:
        parser.feed(text)
    except Exception:
        return []
    links = set()
    for href in parser.hrefs:
        absolute = urllib.parse.urljoin(request_url, href)
        parsed = urllib.parse.urlparse(absolute)
        if parsed.scheme in {"http", "https"} and (
            domain_netloc.lower() in parsed.netloc.lower() or parsed.netloc.lower() in domain_netloc.lower()
        ):
            links.add(urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", parsed.query, "")))
    return sorted(links)


def fetch(url: str, timeout: int = 35) -> tuple[int | None, bytes, bytes, str | None]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, str(response.headers).encode("utf-8"), response.read(), None
    except urllib.error.HTTPError as exc:
        return exc.code, str(exc.headers).encode("utf-8") if exc.headers else b"", exc.read(), f"HTTPError: {exc.reason}"
    except Exception as exc:
        return None, b"", b"", f"{type(exc).__name__}: {exc}"


def to_long_path(path: Path) -> str:
    abs_str = str(path.resolve())
    if os.name == "nt" and not abs_str.startswith("\\\\?\\"):
        return "\\\\?\\" + abs_str
    return abs_str


def write_bytes(path: Path, value: bytes) -> None:
    import os, time
    target = to_long_path(path)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    for attempt in range(5):
        try:
            with open(target, "wb") as f:
                f.write(value)
            return
        except Exception:
            if attempt == 4:
                raise
            time.sleep(0.4 * (attempt + 1))


def write_text(path: Path, value: str) -> None:
    import os, time
    target = to_long_path(path)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    for attempt in range(5):
        try:
            with open(target, "w", encoding="utf-8") as f:
                f.write(value)
            return
        except Exception:
            if attempt == 4:
                raise
            time.sleep(0.4 * (attempt + 1))


def build_sentinel_url(base_domain: str, query_verbatim: str, page: int) -> str:
    encoded_q = urllib.parse.quote(query_verbatim, safe="")
    parsed = urllib.parse.urlparse(base_domain)
    netloc = parsed.netloc or parsed.path
    
    # Custom endpoint formatting per sentinel portal structure
    if "soyte.hanoi.gov.vn" in netloc:
        return f"https://soyte.hanoi.gov.vn/tim-kiem?query={encoded_q}&page={page}"
    elif "danang.gov.vn" in netloc:
        return f"https://soyte.danang.gov.vn/tim-kiem?query={encoded_q}&page={page}"
    elif "medinet.gov.vn" in netloc:
        return f"https://medinet.gov.vn/tim-kiem?query={encoded_q}&page={page}"
    elif "bachmai.gov.vn" in netloc:
        return f"https://bachmai.gov.vn/?s={encoded_q}&paged={page}"
    elif "bvtwhue.com.vn" in netloc:
        return f"https://bvtwhue.com.vn/?s={encoded_q}&paged={page}"
    elif "bvchoray.vn" in netloc:
        return f"https://bvchoray.vn/?s={encoded_q}&paged={page}"
    elif "vinmec.com" in netloc:
        return f"https://www.vinmec.com/vi/tim-kiem/?q={encoded_q}&page={page}"
    elif "tamanhhospital.vn" in netloc:
        return f"https://tamanhhospital.vn/?s={encoded_q}&paged={page}"
    elif "umc.edu.vn" in netloc:
        return f"https://www.umc.edu.vn/tim-kiem?q={encoded_q}&page={page}"
    else:
        scheme = parsed.scheme or "https"
        return f"{scheme}://{netloc}/?s={encoded_q}&paged={page}"


def main() -> int:
    timestamp = dt.datetime.now().strftime("%Y%m%dT%H%M%S")
    run_id = f"sentinel-capture-{timestamp}"
    run_dir = OUTPUT_ROOT / run_id
    raw_dir = run_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    # Read 9 cases from frame (frozen pre-registration snapshot)
    cases = list(csv.DictReader(FRAME.open(encoding="utf-8-sig", newline="")))
    verified_cases = cases
    if not verified_cases:
        raise SystemExit("No cases found in implementation-case-sampling-frame.csv")

    # Read catalog queries
    queries = list(csv.DictReader(CATALOG.open(encoding="utf-8-sig", newline="")))

    (run_dir / "README.md").write_text(
        f"# Sentinel Cases Official Capture Run — {run_id}\n\n"
        "**Status:** `RAW_CAPTURE_IN_PROGRESS`\n"
        f"**Started At:** {utcnow()}\n"
        "Capturing 9 verified DOH and Hospital Sentinel portals across locked query sets.\n",
        encoding="utf-8",
    )

    ledger: list[dict[str, object]] = []
    candidate_rows: list[dict[str, object]] = []

    print(f"=== Sentinel Cases Capture Starting ({len(verified_cases)} cases x {len(queries)} queries) ===")

    for case in verified_cases:
        case_id = case["case_id"]
        official_name = case["official_name"]
        domain = case["official_domain"]
        netloc = urllib.parse.urlparse(domain).netloc or domain

        print(f"\nProcessing Case: {case_id} — {official_name} ({domain})")

        case_queries = [q for q in queries if q["query_id"] in case["query_set"].split("|")]
        if not case_queries:
            case_queries = queries  # Fallback to all queries if set empty

        for query in case_queries:
            qid = query["query_id"]
            verbatim = query["verbatim_query"]

            for page in range(1, 3):  # Cap max 2 pages per query for sentinel depth
                url = build_sentinel_url(domain, verbatim, page)
                stem = f"{safe_name(case_id)}-{safe_name(qid)}-p{page:02d}"
                started = utcnow()

                status, headers, body, error = fetch(url, timeout=35)

                write_bytes(raw_dir / f"{stem}.headers", headers)
                write_bytes(raw_dir / f"{stem}.body", body)
                write_text(raw_dir / f"{stem}.error.txt", error or "NO_TRANSPORT_ERROR\n")

                candidates = same_domain_links(body, url, netloc) if body else []

                ledger.append({
                    "case_id": case_id,
                    "official_name": official_name,
                    "official_domain": domain,
                    "query_id": qid,
                    "verbatim_query": verbatim,
                    "page": page,
                    "requested_url": url,
                    "started_at": started,
                    "http_status": "" if status is None else status,
                    "response_bytes": len(body),
                    "error": error or "",
                    "body_file": f"raw/{stem}.body",
                    "headers_file": f"raw/{stem}.headers",
                    "body_sha256": sha256(raw_dir / f"{stem}.body"),
                    "candidate_url_count": len(candidates),
                    "status": "RAW_PAGE_CAPTURED" if status == 200 else "TRANSPORT_ATTEMPTED"
                })

                for cand in candidates:
                    candidate_rows.append({
                        "case_id": case_id,
                        "query_id": qid,
                        "page": page,
                        "candidate_url": cand,
                        "discovery_url": url,
                        "status": "UNSCREENED_CANDIDATE_LOCATOR"
                    })

                print(f"  [{case_id}] {qid} p{page:02d}: status={status}, bytes={len(body)}, candidates={len(candidates)}")
                import time
                time.sleep(0.3)

    # Write ledgers & manifests
    with (run_dir / "query-sentinel-ledger.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(ledger[0].keys()))
        writer.writeheader()
        writer.writerows(ledger)

    with (run_dir / "candidate-locators.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["case_id", "query_id", "page", "candidate_url", "discovery_url", "status"])
        writer.writeheader()
        writer.writerows(candidate_rows)

    hashes = []
    run_dir_long = to_long_path(run_dir)
    for root, _, files in os.walk(run_dir_long):
        for f in sorted(files):
            if f == "sha256.csv":
                continue
            full_p = Path(root) / f
            rel_p = str(full_p.relative_to(run_dir_long)).replace("\\", "/")
            hashes.append({
                "relative_path": rel_p,
                "sha256": sha256(full_p),
                "bytes": full_p.stat().st_size
            })
    hashes.sort(key=lambda x: x["relative_path"])

    with (run_dir / "sha256.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["relative_path", "sha256", "bytes"])
        writer.writeheader()
        writer.writerows(hashes)

    manifest = {
        "run_id": run_id,
        "completed_at_utc": utcnow(),
        "cases_captured": len(verified_cases),
        "total_page_attempts": len(ledger),
        "total_candidate_locators": len(candidate_rows),
        "status": "SENTINEL_CAPTURE_COMPLETE_NOT_SCREENED",
        "next_steps": ["Review locators", "Deduplicate", "Double-independent screening"]
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n=== Sentinel Capture Complete ({run_id}) ===")
    print(f"Captured {len(ledger)} attempts, {len(candidate_rows)} candidate locators.")
    print(f"Artifacts saved at: {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
