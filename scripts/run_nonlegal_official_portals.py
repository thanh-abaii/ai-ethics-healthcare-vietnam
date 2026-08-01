#!/usr/bin/env python3
"""Capture a reproducible, *unscreened* official-portal search run.

This is deliberately a capture tool, not a relevance/eligibility classifier.
It keeps transport evidence for every query/channel/page attempt and derives
only a conservative list of same-domain candidate links.  It never infers that
an empty or inaccessible page means that evidence does not exist.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/nonlegal-portals-2026-07-31/query-catalog.csv"
# Short name is intentional: the Windows workspace path is already long and
# raw filenames must remain below the legacy MAX_PATH boundary.
RUNS = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/nl-runs"

# Portal-specific URL templates are an access method, not a claim that every
# portal has a working internal-search API.  `page` is recorded even where a
# portal ignores it, so duplicate-page stop evidence remains auditable.
CHANNELS = {
    "MOH": ("moh.gov.vn", "https://moh.gov.vn/tim-kiem?query={q}&page={page}"),
    "MOH-ASTT": ("asttmoh.vn", "https://asttmoh.vn/?s={q}&paged={page}"),
    "MOH-KCB": ("kcb.vn", "https://kcb.vn/?site=2005611&page=search&keyword={q}&p={page}"),
    "MOH-HTTB": ("imda.moh.gov.vn", "https://imda.moh.gov.vn/?s={q}&paged={page}"),
    "MOH-NHIC": ("ttyqg.vn", "https://ttyqg.vn/?s={q}&paged={page}"),
    "MOH-PC": ("vuphapche.moh.gov.vn", "https://vuphapche.moh.gov.vn/?s={q}&paged={page}"),
    "MOH-HSPI": ("hspi.org.vn", "https://hspi.org.vn/news/find?txtKw={q}&page={page}"),
    "MST": ("most.gov.vn", "https://most.gov.vn/search?q={q}&page={page}"),
    "UNESCO-RAM": ("www.unesco.org", "https://www.unesco.org/ethics-ai/en/search?category=Global%20AI%20Ethics%20and%20Governance%20Observatory&query={q}&page={page}"),
    "WHO-VNM": ("www.who.int", "https://www.who.int/vietnam/search?query={q}&page={page}"),
}


class Hrefs(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)


class SearchResultAnchors(HTMLParser):
    """Conservative result-link extractor.

    A same-domain link in a portal page is often navigation, a stylesheet or a
    tag page.  This extractor records an anchor only when it appears inside an
    element whose class signals a search/article result.  It deliberately
    prefers false negatives: an empty result list is transport evidence, never
    evidence that the portal contains no relevant document.
    """
    RESULT_MARKERS = ("search-result", "search_result", "entry-title", "post-title", "article-title", "result-item", "item-result", "news-item")

    def __init__(self) -> None:
        super().__init__()
        self.stack: list[bool] = []
        self.current: dict[str, str] | None = None
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        classes = attr.get("class", "").lower()
        parent_is_result = self.stack[-1] if self.stack else False
        is_result = parent_is_result or any(marker in classes for marker in self.RESULT_MARKERS)
        self.stack.append(is_result)
        if tag.lower() == "a" and is_result and attr.get("href"):
            self.current = {"href": attr["href"], "text": ""}

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"] += data

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self.current is not None:
            text = " ".join(self.current["text"].split())
            if text:
                self.current["text"] = text
                self.items.append(self.current)
            self.current = None
        if self.stack:
            self.stack.pop()


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def to_long_path(path: Path) -> str:
    abs_str = str(path.resolve())
    if os.name == "nt" and not abs_str.startswith("\\\\?\\"):
        return "\\\\?\\" + abs_str
    return abs_str


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    target = to_long_path(path)
    with open(target, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def safe_name(value: str) -> str:
    return re.sub(r"[^a-z0-9_-]+", "-", value.lower())


def same_domain_links(body: bytes, request_url: str, domain: str) -> list[str]:
    # This is a transparent, intentionally broad candidate locator.  It cannot
    # determine search-result semantics, and its count is never a PRISMA count.
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
        if parsed.scheme in {"http", "https"} and parsed.netloc.lower().endswith(domain.lower()):
            links.add(urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", parsed.query, "")))
    return sorted(links)


def search_result_links(body: bytes, request_url: str, domain: str) -> list[dict[str, str]]:
    """Return result-level links, with their visible anchor text, without screening."""
    parser = SearchResultAnchors()
    try:
        parser.feed(body.decode("utf-8", errors="replace"))
    except Exception:
        return []
    seen: set[str] = set()
    output: list[dict[str, str]] = []
    for item in parser.items:
        absolute = urllib.parse.urljoin(request_url, item["href"])
        parsed = urllib.parse.urlparse(absolute)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc.lower().endswith(domain.lower()):
            continue
        clean = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", parsed.query, ""))
        # Asset and feed URLs are not documents returned as search results.
        if any(part in parsed.path.lower() for part in ("/wp-content/", "/wp-includes/", "/feed/")):
            continue
        if clean in seen:
            continue
        seen.add(clean)
        output.append({"source_url": clean, "anchor_text": item["text"]})
    return output


def fetch(url: str, timeout: int) -> tuple[int | None, bytes, bytes, str | None]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.headers.as_bytes(), response.read(), None
    except urllib.error.HTTPError as exc:
        return exc.code, exc.headers.as_bytes() if exc.headers else b"", exc.read(), f"HTTPError: {exc.reason}"
    except Exception as exc:
        return None, b"", b"", f"{type(exc).__name__}: {exc}"


def write_bytes(path: Path, value: bytes) -> None:
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
            return
        except Exception:
            if attempt == 4:
                raise
            time.sleep(0.3 * (attempt + 1))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channels", nargs="*", choices=list(CHANNELS), default=list(CHANNELS))
    ap.add_argument("--max-pages", type=int, default=5)
    ap.add_argument("--timeout-seconds", type=int, default=35)
    ap.add_argument("--pause-seconds", type=float, default=0.25)
    ap.add_argument("--max-result-sources-per-channel-query", type=int, default=50)
    ap.add_argument("--run-id", help="optional stable run directory name")
    args = ap.parse_args()
    if args.max_pages < 1 or args.max_pages > 5:
        ap.error("--max-pages must be 1..5, the locked non-legal portal cap")

    run_id = args.run_id or ("official-nonlegal-" + dt.datetime.now().strftime("%Y%m%dT%H%M%S"))
    run = RUNS / run_id
    if run.exists():
        raise SystemExit(f"Refusing to append to existing run: {run}")
    raw = run / "raw"
    raw.mkdir(parents=True)
    # This repository is sometimes materialized with Windows' ReadOnly bit on
    # newly created directories.  Clear it only on this new run directory;
    # never alter a prior run, the registered protocol, or its snapshot.
    try:
        os.chmod(run, stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
        os.chmod(raw, stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
    except OSError:
        pass
    queries = list(csv.DictReader(CATALOG.open(encoding="utf-8-sig", newline="")))
    expected_query_ids = {
        "DQ-IMPL-01", "DQ-IMPL-02", "DQ-IMPL-03", "DQ-IMPL-04", "DQ-IMPL-05",
        "DQ-TOOL-01", "DQ-TOOL-02", "DQ-EVID-01", "DQ-EVID-02", "DQ-EVID-03",
        "DQ-EVID-04", "DQ-EVID-05",
    }
    if len(queries) != 12 or {x["query_id"] for x in queries} != expected_query_ids:
        raise SystemExit("Locked query catalog is missing or duplicated")

    (run / "README.md").write_text(
        "# Lượt tìm cổng không-pháp lý chính thức\n\n"
        "**Trạng thái ban đầu:** `RAW_CAPTURE_IN_PROGRESS`  \n"
        f"**Bắt đầu:** {utcnow()}  \n"
        "Mỗi HTTP attempt được giữ nguyên (body/header/error/status). Candidate URL chỉ là locator máy suy ra; chưa có sàng lọc, trích xuất, hay suy luận về vắng mặt/bão hòa.\n",
        encoding="utf-8",
    )
    (run / "run-parameters.json").write_text(json.dumps({
        "run_id": run_id, "started_at": utcnow(), "catalog": str(CATALOG),
        "catalog_sha256": sha256(CATALOG), "channels": args.channels,
        "max_pages": args.max_pages, "timeout_seconds": args.timeout_seconds,
        "stop_rule": "50 results or 5 internal pages; stop at cap or two consecutive pages with no new candidate URL; fallback site: requires separately recorded discovery run",
        "depth": 2,
        "scope": "transport/candidate-locator capture only; no screening, source acquisition, extraction, citation chasing, or PRISMA count",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ledger: list[dict[str, object]] = []
    candidate_rows: list[dict[str, object]] = []
    result_rows: list[dict[str, object]] = []
    for channel in args.channels:
        domain, template = CHANNELS[channel]
        for query in queries:
            no_new_streak = 0
            cumulative: set[str] = set()
            for page in range(1, args.max_pages + 1):
                encoded = urllib.parse.quote(query["verbatim_query"], safe="")
                url = template.format(q=encoded, page=page)
                stem = f"{safe_name(channel)}-{safe_name(query['query_id'])}-p{page:02d}"
                started = utcnow()
                status, headers, body, error = fetch(url, args.timeout_seconds)
                write_bytes(raw / f"{stem}.headers", headers)
                write_bytes(raw / f"{stem}.body", body)
                # Keep the paired evidence file non-empty. In this synced
                # workspace, a zero-byte `.error.txt` is removed before it can
                # be reopened; the ledger remains the authoritative empty
                # error value for successful transport.
                write_text(raw / f"{stem}.error.txt", error or "NO_TRANSPORT_ERROR\n")
                candidates = same_domain_links(body, url, domain) if body else []
                result_links = search_result_links(body, url, domain) if body else []
                new = sorted(set(candidates) - cumulative)
                cumulative.update(candidates)
                no_new_streak = no_new_streak + 1 if not new else 0
                stop = "CONTINUE"
                if page == args.max_pages:
                    stop = "LOCKED_PAGE_CAP_REACHED"
                elif no_new_streak >= 2:
                    stop = "TWO_CONSECUTIVE_PAGES_WITH_NO_NEW_CANDIDATE_URL"
                ledger.append({
                    "channel_id": channel, "domain": domain, "query_id": query["query_id"], "query_family": query["query_family"],
                    "query_verbatim": query["verbatim_query"], "page_attempt": page, "requested_url": url, "started_at": started,
                    "http_status": "" if status is None else status, "response_bytes": len(body), "error": error or "",
                    "body_file": f"raw/{stem}.body", "headers_file": f"raw/{stem}.headers", "error_file": f"raw/{stem}.error.txt",
                    "body_sha256": sha256(raw / f"{stem}.body"), "headers_sha256": sha256(raw / f"{stem}.headers"),
                    "candidate_url_count_machine_derived": len(candidates), "new_candidate_url_count_machine_derived": len(new),
                    "cumulative_candidate_url_count_machine_derived": len(cumulative), "stop_decision": stop,
                    "interpretation": "Raw capture only; URL candidates are not verified search results and are not screened or counted for PRISMA."
                })
                for candidate in new:
                    candidate_rows.append({"channel_id": channel, "query_id": query["query_id"], "page_attempt": page,
                                           "candidate_url": candidate, "discovery_url": url,
                                           "status": "UNSCREENED_CANDIDATE_LOCATOR_NOT_ACQUIRED"})
                for result in result_links:
                    result_rows.append({"channel_id": channel, "query_id": query["query_id"], "page_attempt": page,
                                        "source_url": result["source_url"], "anchor_text": result["anchor_text"],
                                        "discovery_url": url, "status": "DISCOVERED_RESULT_LEVEL_SOURCE_NOT_SCREENED"})
                if stop != "CONTINUE":
                    break
                time.sleep(args.pause_seconds)

    fields = list(ledger[0]) if ledger else []
    with (run / "query-portal-ledger.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(ledger)
    with (run / "candidate-url-locators.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["channel_id","query_id","page_attempt","candidate_url","discovery_url","status"]); writer.writeheader(); writer.writerows(candidate_rows)
    # Deduplicate only repeated manifestations of the exact same result URL
    # within a channel/query.  Cross-query duplication remains visible as
    # separate provenance rows for the later registry audit.
    unique_results: list[dict[str, object]] = []
    seen_results: set[tuple[str, str, str]] = set()
    for row in result_rows:
        key = (str(row["channel_id"]), str(row["query_id"]), str(row["source_url"]))
        if key not in seen_results:
            seen_results.add(key); unique_results.append(row)
    with (run / "result-source-discovery.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["channel_id","query_id","page_attempt","source_url","anchor_text","discovery_url","status"]); writer.writeheader(); writer.writerows(unique_results)

    # Acquire only result-level URLs.  Broad candidate-url-locators are kept
    # for audit but are never promoted to source records by this script.
    source_raw = run / "source-raw"
    source_raw.mkdir(exist_ok=True)
    acquisition: list[dict[str, object]] = []
    per_pair: dict[tuple[str, str], int] = {}
    for row in unique_results:
        pair = (str(row["channel_id"]), str(row["query_id"]))
        if per_pair.get(pair, 0) >= args.max_result_sources_per_channel_query:
            continue
        per_pair[pair] = per_pair.get(pair, 0) + 1
        source_url = str(row["source_url"])
        stem = "src-" + hashlib.sha256((pair[0] + "|" + pair[1] + "|" + source_url).encode("utf-8")).hexdigest()[:20]
        started = utcnow()
        status, headers, body, error = fetch(source_url, args.timeout_seconds)
        write_bytes(source_raw / f"{stem}.headers", headers)
        write_bytes(source_raw / f"{stem}.body", body)
        write_text(source_raw / f"{stem}.error.txt", error or "NO_TRANSPORT_ERROR\n")
        acquisition.append({
            **row, "acquired_at": started, "http_status": "" if status is None else status,
            "response_bytes": len(body), "error": error or "", "body_file": f"source-raw/{stem}.body",
            "headers_file": f"source-raw/{stem}.headers", "error_file": f"source-raw/{stem}.error.txt",
            "body_sha256": sha256(source_raw / f"{stem}.body"), "headers_sha256": sha256(source_raw / f"{stem}.headers"),
            "status": "ACQUIRED_UNSCREENED" if status and 200 <= status < 300 else "ACQUISITION_FAILED_UNSCREENED",
        })
        time.sleep(args.pause_seconds)
    with (run / "result-source-acquisition-ledger.csv").open("w", encoding="utf-8", newline="") as f:
        fields = ["channel_id","query_id","page_attempt","source_url","anchor_text","discovery_url","acquired_at","http_status","response_bytes","error","body_file","headers_file","error_file","body_sha256","headers_sha256","status"]
        writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(acquisition)
    hashes = []
    for path in sorted(p for p in run.rglob("*") if p.is_file()):
        if path.name == "sha256.csv": continue
        hashes.append({"relative_path": str(path.relative_to(run)).replace("\\", "/"), "sha256": sha256(path), "bytes": path.stat().st_size})
    with (run / "sha256.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["relative_path", "sha256", "bytes"]); writer.writeheader(); writer.writerows(hashes)
    expected = len(args.channels) * len(queries)
    executed = len({(x["channel_id"], x["query_id"]) for x in ledger})
    failed = sum(1 for x in ledger if not str(x["http_status"]).startswith("2"))
    (run / "completion-status.json").write_text(json.dumps({
        "completed_at": utcnow(), "expected_channel_query_pairs": expected, "executed_channel_query_pairs": executed,
        "page_attempts": len(ledger), "non_2xx_attempts": failed,
        "result_level_sources_discovered_by_conservative_semantic_parser": len(unique_results),
        "result_level_source_acquisition_attempts": len(acquisition),
        "result_level_source_acquisition_non_2xx": sum(1 for x in acquisition if not str(x["http_status"]).startswith("2")),
        "status": "RAW_PORTAL_AND_RESULT_SOURCE_CAPTURE_COMPLETE_DEPTH_2_NOT_RUN",
        "not_permitted_claims": ["OFFICIAL_SEARCH_COMPLETE", "search saturation", "absence of evidence", "PRISMA identification count", "eligibility", "implementation/outcome finding"],
        "required_next_work": ["human audit of portal-specific result semantics", "perform recorded site: fallback where necessary", "perform second-depth traversal from acquired official sources under the locked rule", "global provenance/dedup audit"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # `completion-status.json` is itself evidence and must be covered.  A
    # manifest cannot hash itself, so re-write the checksum inventory only
    # after the terminal status has been written.
    hashes = []
    for path in sorted(p for p in run.rglob("*") if p.is_file()):
        if path.name == "sha256.csv":
            continue
        hashes.append({"relative_path": str(path.relative_to(run)).replace("\\", "/"), "sha256": sha256(path), "bytes": path.stat().st_size})
    with (run / "sha256.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["relative_path", "sha256", "bytes"]); writer.writeheader(); writer.writerows(hashes)
    print(run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
