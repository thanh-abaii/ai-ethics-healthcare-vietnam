#!/usr/bin/env python3
"""Capture the legal-portal search layer without making legal conclusions.

This runner deliberately fails closed.  It preserves every raw response and
response header, keeps a page-level ledger, and never treats an HTTP 200 API
payload containing an upstream error as a zero-result search.  It does not
screen, deduplicate, extract, or update a PRISMA count.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import ssl
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


QUERY_SET = [
    ("DQ-LAW-01", '"134/2025/QH15"'),
    ("DQ-LAW-02", '"Luật Trí tuệ nhân tạo" AND (y tế OR "người bệnh" OR bệnh viện)'),
    ("DQ-DEC-01", '"142/2026/NĐ-CP"'),
    ("DQ-FRAME-01", '"05/2026/TT-BKHCN"'),
    ("DQ-FRAME-02", '"Khung đạo đức trí tuệ nhân tạo quốc gia" AND (y tế OR bệnh viện OR "khám chữa bệnh")'),
    ("DQ-REL-01", '("134/2025/QH15" OR "142/2026/NĐ-CP" OR "05/2026/TT-BKHCN") AND (sửa đổi OR thay thế OR hướng dẫn OR triển khai)'),
    ("DQ-COUNCIL-NAME-01", '"Hội đồng đạo đức AI quốc gia"'),
    ("DQ-COUNCIL-NAME-02", '"Hội đồng đạo đức trí tuệ nhân tạo quốc gia"'),
    ("DQ-COUNCIL-NAME-03", '"Ủy ban đạo đức AI quốc gia"'),
    ("DQ-COUNCIL-NAME-04", '"National AI Ethics Council" Vietnam'),
    ("DQ-COUNCIL-NAME-05", '"National Council on AI Ethics" Vietnam'),
    ("DQ-COUNCIL-NAME-06", '"AI ethics committee" Vietnam'),
    ("DQ-COUNCIL-EST-01", '("hội đồng đạo đức AI" OR "hội đồng đạo đức trí tuệ nhân tạo") AND ("quyết định thành lập" OR "quy chế" OR "chức năng nhiệm vụ" OR "thành viên")'),
    ("DQ-COUNCIL-ACT-01", '("hội đồng đạo đức AI" OR "hội đồng đạo đức trí tuệ nhân tạo") AND ("phiên họp" OR "biên bản" OR "báo cáo hoạt động")'),
    ("DQ-COUNCIL-ACT-02", '("National AI Ethics Council" OR "National Council on AI Ethics") AND (decision OR regulation OR mandate OR members OR meeting OR minutes OR "activity report")'),
    # This is a graph target, not an additional locked query ID.
    ("LGRAPH-TARGET-55-2025-ND-CP", '"55/2025/NĐ-CP"'),
]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def to_long_path(path: Path) -> str:
    abs_str = str(path.resolve())
    if os.name == "nt" and not abs_str.startswith("\\\\?\\"):
        return "\\\\?\\" + abs_str
    return abs_str


def write_bytes(path: Path, data: bytes) -> tuple[int, str]:
    long_p = to_long_path(path)
    with open(long_p, "wb") as f:
        f.write(data)
    return len(data), sha256(data)


def request_capture(url: str, method: str, data: bytes | None, timeout: int = 25) -> tuple[int | str, dict, bytes, str]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    if data is not None:
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    request = Request(url, data=data, headers=headers, method=method)
    try:
        with urlopen(request, context=ctx, timeout=timeout) as response:
            return response.status, dict(response.headers.items()), response.read(), "OK"
    except HTTPError as error:
        return error.code, dict(error.headers.items()) if error.headers else {}, error.read(), "HTTP_ERROR"
    except (URLError, OSError) as error:
        return "CLIENT_ERROR", {}, str(error).encode("utf-8"), "CLIENT_ERROR"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default=datetime.now().strftime("%Y%m%dT%H%M%S%z"))
    parser.add_argument("--max-pages", type=int, default=10)
    parser.add_argument("--output-root", type=Path, default=Path(__file__).resolve().parents[1] / "artifacts" / "search-rerun-01-2026-07-31" / "official-sources")
    args = parser.parse_args()
    if not 1 <= args.max_pages <= 10:
        parser.error("--max-pages must be 1..10, the frozen legal-portal cap")

    run_dir = args.output_root / f"legal-portals-{args.run_id}"
    raw_dir = run_dir / "raw"
    os.makedirs(to_long_path(raw_dir), exist_ok=True)
    rows: list[dict[str, object]] = []
    captured_at = datetime.now(timezone.utc).isoformat()

    # 1. GOV-VB Official Portal (vanban.chinhphu.vn)
    print("=== Executing GOV-VB (vanban.chinhphu.vn) ===")
    for query_index, (query_id, query) in enumerate(QUERY_SET, start=1):
        encoded_q = urlencode({"q": query})[2:]
        endpoint = f"https://vanban.chinhphu.vn/?pageid=27160&tukhoa={encoded_q}"
        status, response_headers, content, transport = request_capture(endpoint, "GET", None)
        stem = f"gov-vb-q{query_index:02d}-p01"
        extension = "html" if transport != "CLIENT_ERROR" else "error.txt"
        bytes_count, digest = write_bytes(raw_dir / f"{stem}.{extension}", content)
        header_bytes = json.dumps(response_headers, ensure_ascii=False, indent=2).encode("utf-8")
        header_count, header_digest = write_bytes(raw_dir / f"{stem}.headers.json", header_bytes)
        row_status = "RAW_PAGE_CAPTURED" if transport == "OK" and bytes_count > 1000 else "FAIL_CLOSED"
        rows.append({
            "portal": "GOV-VB",
            "query_id": query_id,
            "locked_query_or_graph_target": query,
            "page": 1,
            "requested_url": endpoint,
            "method": "GET",
            "retrieval_utc": captured_at,
            "http_status": status,
            "transport": transport,
            "api_error": "",
            "reported_total": "",
            "returned_count": "",
            "raw_file": f"raw/{stem}.{extension}",
            "bytes": bytes_count,
            "sha256": digest,
            "headers_file": f"raw/{stem}.headers.json",
            "headers_bytes": header_count,
            "headers_sha256": header_digest,
            "run_status": row_status,
            "stopping_rule_assessment": "RAW_PORTAL_PAGE_CAPTURED; UNSCREENED"
        })

    # 2. GAZ Official Portal (congbao.chinhphu.vn)
    print("=== Executing GAZ (congbao.chinhphu.vn) ===")
    for query_index, (query_id, query) in enumerate(QUERY_SET, start=1):
        for page in range(1, args.max_pages + 1):
            encoded_q = urlencode({"q": query})[2:]
            endpoint = f"https://congbao.chinhphu.vn/tim-kiem?keyword={encoded_q}&page={page}"
            status, response_headers, content, transport = request_capture(endpoint, "GET", None)
            stem = f"gaz-q{query_index:02d}-p{page:02d}"
            extension = "html" if transport != "CLIENT_ERROR" else "error.txt"
            bytes_count, digest = write_bytes(raw_dir / f"{stem}.{extension}", content)
            header_bytes = json.dumps(response_headers, ensure_ascii=False, indent=2).encode("utf-8")
            header_count, header_digest = write_bytes(raw_dir / f"{stem}.headers.json", header_bytes)
            
            # Count distinct document detail links in captured HTML
            found_items = len(re.findall(r'href=["\'](/van-ban/[^"\']+\.htm)["\']', content.decode("utf-8", errors="replace"))) if content else 0
            row_status = "RAW_PAGE_CAPTURED" if transport == "OK" and bytes_count > 1000 else "FAIL_CLOSED"
            
            rows.append({
                "portal": "GAZ",
                "query_id": query_id,
                "locked_query_or_graph_target": query,
                "page": page,
                "requested_url": endpoint,
                "method": "GET",
                "retrieval_utc": captured_at,
                "http_status": status,
                "transport": transport,
                "api_error": "",
                "reported_total": str(found_items),
                "returned_count": str(found_items),
                "raw_file": f"raw/{stem}.{extension}",
                "bytes": bytes_count,
                "sha256": digest,
                "headers_file": f"raw/{stem}.headers.json",
                "headers_bytes": header_count,
                "headers_sha256": header_digest,
                "run_status": row_status,
                "stopping_rule_assessment": f"STOPPING_RULE_10_PAGES_OR_EXHAUSTED; PAGE_{page}_CAPTURED"
            })
            if found_items == 0 and page > 1:
                break

    # 3. VBPL Portal (vbpl.vn)
    print("=== Executing VBPL (vbpl.vn) ===")
    for query_index, (query_id, query) in enumerate(QUERY_SET, start=1):
        encoded_q = urlencode({"q": query})[2:]
        endpoint = f"https://vbpl.vn/TW/Pages/vbpq-timkiem.aspx?Keyword={encoded_q}"
        status, response_headers, content, transport = request_capture(endpoint, "GET", None)
        stem = f"vbpl-q{query_index:02d}-p01"
        extension = "html" if transport != "CLIENT_ERROR" else "error.txt"
        bytes_count, digest = write_bytes(raw_dir / f"{stem}.{extension}", content)
        header_bytes = json.dumps(response_headers, ensure_ascii=False, indent=2).encode("utf-8")
        header_count, header_digest = write_bytes(raw_dir / f"{stem}.headers.json", header_bytes)
        row_status = "RAW_PAGE_CAPTURED" if transport == "OK" and bytes_count > 1000 else "FAIL_CLOSED"
        rows.append({
            "portal": "VBPL",
            "query_id": query_id,
            "locked_query_or_graph_target": query,
            "page": 1,
            "requested_url": endpoint,
            "method": "GET",
            "retrieval_utc": captured_at,
            "http_status": status,
            "transport": transport,
            "api_error": "",
            "reported_total": "",
            "returned_count": "",
            "raw_file": f"raw/{stem}.{extension}",
            "bytes": bytes_count,
            "sha256": digest,
            "headers_file": f"raw/{stem}.headers.json",
            "headers_bytes": header_count,
            "headers_sha256": header_digest,
            "run_status": row_status,
            "stopping_rule_assessment": "RAW_PORTAL_PAGE_CAPTURED; UNSCREENED" if row_status == "RAW_PAGE_CAPTURED" else "CLIENT_CONNECTION_FAILED"
        })

    # 4. GOV-VB UI Backend API (timkiem.chinhphu.vn) - Diagnostic logging
    print("=== Executing GOV-VB UI Backend API (timkiem.chinhphu.vn) ===")
    for query_index, (query_id, query) in enumerate(QUERY_SET, start=1):
        endpoint = "https://timkiem.chinhphu.vn/Home/search"
        body = urlencode({"keyword": query, "cate_id": "", "lang": "vi", "page": 1, "page_size": 15}).encode("utf-8")
        status, response_headers, content, transport = request_capture(endpoint, "POST", body)
        stem = f"gov-api-q{query_index:02d}-p01"
        bytes_count, digest = write_bytes(raw_dir / f"{stem}.json", content)
        header_bytes = json.dumps(response_headers, ensure_ascii=False, indent=2).encode("utf-8")
        header_count, header_digest = write_bytes(raw_dir / f"{stem}.headers.json", header_bytes)
        api_error = None
        total = None
        returned = None
        try:
            payload = json.loads(content.decode("utf-8"))
            api_error = payload.get("error")
            total = payload.get("total")
            returned = payload.get("count") if payload.get("count") is not None else len(payload.get("data") or [])
        except (UnicodeDecodeError, json.JSONDecodeError):
            payload = None
        row_status = "RAW_PAGE_CAPTURED" if transport == "OK" and not api_error else "FAIL_CLOSED"
        rows.append({
            "portal": "GOV-VB_UI_BACKEND",
            "query_id": query_id,
            "locked_query_or_graph_target": query,
            "page": 1,
            "requested_url": endpoint,
            "method": "POST",
            "retrieval_utc": captured_at,
            "http_status": status,
            "transport": transport,
            "api_error": api_error or "",
            "reported_total": total if total is not None else "",
            "returned_count": returned if returned is not None else "",
            "raw_file": f"raw/{stem}.json",
            "bytes": bytes_count,
            "sha256": digest,
            "headers_file": f"raw/{stem}.headers.json",
            "headers_bytes": header_count,
            "headers_sha256": header_digest,
            "run_status": row_status,
            "stopping_rule_assessment": "FAILED_API_RESPONSE" if row_status == "FAIL_CLOSED" else "CONTINUE_UNTIL_10_PAGES_OR_TERMINAL_RESULT_SET"
        })

    fields = list(rows[0])
    with (run_dir / "query-ledger.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    # Generate sha256.csv for all files in run_dir
    hashes = []
    run_dir_long = to_long_path(run_dir)
    for r_dir, _, f_list in os.walk(run_dir_long):
        for f_name in sorted(f_list):
            if f_name == "sha256.csv":
                continue
            full_p = Path(r_dir) / f_name
            rel_p = str(full_p).replace("\\\\?\\", "").replace(str(run_dir.resolve()), "").lstrip("\\/").replace("\\\\", "/").replace("\\", "/")
            hashes.append({
                "relative_path": rel_p,
                "sha256": sha256(full_p.read_bytes()),
                "bytes": full_p.stat().st_size
            })
    hashes.sort(key=lambda x: x["relative_path"])
    with (run_dir / "sha256.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["relative_path", "sha256", "bytes"])
        writer.writeheader()
        writer.writerows(hashes)

    captured_success = sum(1 for r in rows if r["run_status"] == "RAW_PAGE_CAPTURED")
    overall_status = "RAW_LEGAL_PORTAL_CAPTURE_COMPLETE_UNSCREENED" if captured_success > 0 else "FAIL_CLOSED_INCOMPLETE_LEGAL_PORTAL_SEARCH"

    manifest = {
        "run_id": args.run_id,
        "captured_at_utc": captured_at,
        "protocol_status": overall_status,
        "query_count": len(QUERY_SET),
        "ledger_rows": len(rows),
        "successful_raw_captures": captured_success,
        "hash_algorithm": "SHA-256",
        "portals_captured": ["GOV-VB (vanban.chinhphu.vn)", "GAZ (congbao.chinhphu.vn)", "VBPL (vbpl.vn)", "GOV-VB_UI_BACKEND (timkiem.chinhphu.vn)"],
        "limitations": [
            "Raw HTML and JSON transport evidence captured for legal queries.",
            "Locators and document full-texts are unscreened and unextracted.",
            "No screening, deduplication, citation chasing, or PRISMA decision has been made."
        ]
    }
    (run_dir / "run-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nExecution Complete: {run_dir}")
    print(f"Status: {overall_status} ({captured_success}/{len(rows)} raw pages captured successfully)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
