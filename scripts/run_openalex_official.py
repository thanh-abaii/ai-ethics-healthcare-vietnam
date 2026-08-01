"""Run the locked OpenAlex search as a clean, fail-closed post-registration harvest.

Credentials are read only from OPENALEX_API_KEY and OPENALEX_MAILTO. They are
never copied to a URL log, raw artifact name, manifest, or terminal output.
"""
from __future__ import annotations

import csv
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FROZEN_STRATEGY = ROOT / "artifacts" / "protocol-registration-lock-2026-07-31" / "files" / "search-strategy.md"
OUTPUT_ROOT = ROOT / "artifacts" / "search-rerun-01-2026-07-31" / "openalex"
API_BASE = "https://api.openalex.org/works"
SELECT = "id,doi,display_name,publication_year,publication_date,type,language,ids,primary_location,authorships,abstract_inverted_index"
PER_PAGE = 25
MAX_RETRIES = 4


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def extract_locked_query() -> str:
    text = FROZEN_STRATEGY.read_text(encoding="utf-8")
    match = re.search(r"### 5\.1\. Verbatim Boolean query string\s*```text\s*(.*?)\s*```", text, flags=re.S)
    if not match:
        raise RuntimeError("LOCKED_OPENALEX_QUERY_NOT_FOUND")
    return match.group(1).strip()


def public_url(params: dict[str, str]) -> str:
    safe = dict(params)
    for name in ("api_key", "mailto"):
        if name in safe:
            safe[name] = "REDACTED"
    return API_BASE + "?" + urllib.parse.urlencode(safe)


def request_page(params: dict[str, str]) -> tuple[int | None, bytes, dict[str, str], str | None]:
    """Return status, raw bytes, response headers, and an intentionally generic error code."""
    url = API_BASE + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "ai-ethics-healthcare-vietnam-review/1.0"},
    )
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                return response.status, response.read(), dict(response.headers.items()), None
        except urllib.error.HTTPError as error:
            raw = error.read()
            headers = dict(error.headers.items()) if error.headers else {}
            if error.code in (429, 500, 502, 503, 504) and attempt < MAX_RETRIES:
                time.sleep(2 ** (attempt - 1))
                continue
            return error.code, raw, headers, f"HTTP_{error.code}"
        except (urllib.error.URLError, TimeoutError):
            if attempt < MAX_RETRIES:
                time.sleep(2 ** (attempt - 1))
                continue
            return None, b"", {}, "NETWORK_OR_TIMEOUT"
    return None, b"", {}, "RETRY_EXHAUSTED"


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--amendment", choices=["PR-05"], help="Apply a prospective, documented method amendment.")
    args = parser.parse_args()
    query = extract_locked_query()
    api_key = os.environ.get("OPENALEX_API_KEY", "").strip()
    # POLITE_EMAIL is shared with the PubMed runner; OPENALEX_MAILTO remains
    # available when a project needs a separate address.
    mailto = os.environ.get("OPENALEX_MAILTO", os.environ.get("POLITE_EMAIL", "")).strip()
    run_id = "openalex-api-" + datetime.now().astimezone().strftime("%Y%m%dT%H%M%S%z")
    run_dir = OUTPUT_ROOT / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    filter_value = "from_publication_date:2019-01-01,to_publication_date:2026-07-31,title_and_abstract.search:" + query
    query_spec = {
        "run_id": run_id,
        "protocol_reference": "OSF 62b8w; frozen search-strategy.md sections 5.1-5.3",
        "query_verbatim": query,
        "filter_verbatim": filter_value,
        "select_fields": SELECT,
        "per_page": PER_PAGE,
        "initial_cursor": "*",
        "api_key_present": bool(api_key),
        "mailto_present": bool(mailto),
        "credential_values_logged": False,
        "amendment_applied": args.amendment,
    }
    write_json(run_dir / "query-spec.json", query_spec)
    manifest: dict[str, object] = {"run_id": run_id, "started_at_utc": utc_now(), "pages": [], "status": "STARTED"}

    if not api_key or not mailto:
        manifest.update({"status": "FAIL_CLOSED_CREDENTIALS_UNSET", "reason": "OPENALEX_API_KEY_OR_OPENALEX_MAILTO_UNSET"})
        manifest["files"] = [{"file": p.name, "sha256": sha256(p), "bytes": p.stat().st_size} for p in sorted(run_dir.iterdir())]
        write_json(run_dir / "manifest.json", manifest)
        print("FAIL_CLOSED_CREDENTIALS_UNSET")
        return 2

    cursor = "*"
    seen_cursors: set[str] = set()
    seen_ids: set[str] = set()
    raw_seen = 0
    duplicate_ids = 0
    counts: list[int] = []
    terminal_reached = False
    failure: str | None = None

    while True:
        if cursor in seen_cursors:
            failure = "CURSOR_LOOP_DETECTED"
            break
        seen_cursors.add(cursor)
        page_no = len(manifest["pages"]) + 1
        params = {"filter": filter_value, "select": SELECT, "per-page": str(PER_PAGE), "cursor": cursor, "api_key": api_key, "mailto": mailto}
        status, raw, headers, error = request_page(params)
        raw_path = run_dir / f"page-{page_no:03d}.raw"
        raw_path.write_bytes(raw)
        headers_path = run_dir / f"page-{page_no:03d}.headers.json"
        write_json(headers_path, headers)
        page_event: dict[str, object] = {
            "page_number": page_no,
            "cursor_in": cursor,
            "request_url_redacted": public_url(params),
            "http_status": status,
            "raw_file": raw_path.name,
            "raw_sha256": sha256(raw_path),
            "headers_file": headers_path.name,
            "retrieved_at_utc": utc_now(),
        }
        if error or status is None or not (200 <= status < 300):
            page_event["error"] = error or "NON_2XX"
            manifest["pages"].append(page_event)
            failure = page_event["error"]
            break
        try:
            payload = json.loads(raw.decode("utf-8"))
            results = payload["results"]
            meta = payload["meta"]
            if not isinstance(results, list) or not isinstance(meta.get("count"), int):
                raise ValueError("INVALID_RESULTS_OR_META_COUNT")
            next_cursor = meta.get("next_cursor")
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError, ValueError) as exc:
            page_event["error"] = "INVALID_JSON_OR_REQUIRED_FIELDS"
            manifest["pages"].append(page_event)
            failure = page_event["error"]
            break
        raw_seen += len(results)
        for work in results:
            work_id = work.get("id") if isinstance(work, dict) else None
            if not isinstance(work_id, str) or not work_id:
                failure = "MISSING_OPENALEX_ID"
                break
            if work_id in seen_ids:
                duplicate_ids += 1
            seen_ids.add(work_id)
        page_event.update({"meta_count": meta["count"], "results_count": len(results), "next_cursor": next_cursor, "unique_openalex_ids_cumulative": len(seen_ids)})
        manifest["pages"].append(page_event)
        counts.append(meta["count"])
        if failure:
            break
        if next_cursor is None:
            if results:
                if args.amendment == "PR-05" and len(results) < PER_PAGE and len(seen_ids) == meta["count"]:
                    terminal_reached = True
                    page_event["terminal_condition"] = "PR-05_PARTIAL_FINAL_PAGE_UNIQUE_IDS_MATCH_META_COUNT"
                else:
                    failure = "PAGING_PROTOCOL_ERROR_NULL_CURSOR_WITH_RESULTS"
            else:
                terminal_reached = True
                page_event["terminal_condition"] = "EMPTY_FINAL_PAGE"
            break
        if not isinstance(next_cursor, str) or not next_cursor:
            failure = "INVALID_NEXT_CURSOR"
            break
        cursor = next_cursor
        time.sleep(0.5)

    manifest.update({
        "completed_at_utc": utc_now(),
        "terminal_cursor_rule_satisfied": terminal_reached,
        "raw_results_seen": raw_seen,
        "unique_openalex_ids": len(seen_ids),
        "duplicate_openalex_ids": duplicate_ids,
        "first_meta_count": counts[0] if counts else None,
        "last_meta_count": counts[-1] if counts else None,
        "meta_count_changed": len(set(counts)) > 1,
        "amendment_applied": args.amendment,
    })
    if terminal_reached and not failure:
        manifest["status"] = "RAW_EXPORT_CAPTURED_NOT_SCREENED"
    else:
        manifest["status"] = "FAIL_CLOSED_RAW_EXPORT_INCOMPLETE"
        manifest["reason"] = failure or "TERMINAL_CURSOR_NOT_REACHED"
    manifest["files"] = [{"file": p.name, "sha256": sha256(p), "bytes": p.stat().st_size} for p in sorted(run_dir.iterdir())]
    write_json(run_dir / "manifest.json", manifest)
    (run_dir / "checksums.sha256").write_text("".join(f"{sha256(p)}  {p.name}\n" for p in sorted(run_dir.iterdir()) if p.name != "checksums.sha256"), encoding="utf-8")
    print(manifest["status"])
    return 0 if manifest["status"] == "RAW_EXPORT_CAPTURED_NOT_SCREENED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
