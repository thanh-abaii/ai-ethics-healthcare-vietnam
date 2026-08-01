#!/usr/bin/env python3
"""Run the registered legal-document relation traversal without legal inference.

The frozen strategy specifies a depth-three traversal through explicit
``căn cứ / dẫn chiếu / sửa đổi / thay thế / bãi bỏ / hướng dẫn`` relations,
stopping only when no new document ID is found or when 50 linked documents are
reached.  This post-registration runner captures first-party landing pages,
PDFs and HTTP headers; it records every resolution attempt and fails closed if
an identified target cannot be resolved to a first-party document.  It does
not code legal effect, eligibility, or implementation.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "artifacts" / "search-rerun-01-2026-07-31" / "official-sources"
USER_AGENT = "AI-Ethics-Healthcare-Vietnam-ScopingReview/1.0 (legal-relation-audit)"
MAX_DEPTH = 3
MAX_LINKED_DOCUMENTS = 50

# These are the three pre-specified registered legal seeds.  The URLs are
# first-party Cổng Thông tin điện tử Chính phủ locators, not search snippets.
SEEDS = (
    ("134/2025/QH15", "https://vanban.chinhphu.vn/?classid=1&docid=216334&pageid=27160&typegroupid=3"),
    ("142/2026/NĐ-CP", "https://vanban.chinhphu.vn/?docid=218029&orggroupid=2&pageid=27160"),
    ("05/2026/TT-BKHCN", "https://vanban.chinhphu.vn/?classid=1&docid=217165&pageid=27160&typegroupid=6"),
)

# Post-registration official locator supplied after the first traversal.  This
# is not a new search query or a substitution of a similar document: it is the
# exact unresolved number discovered in the registered graph, with both a
# Government Portal landing page and a first-party signed PDF.
OFFICIAL_TARGET_LOCATORS = {
    "55/2025/NĐ-CP": (
        "https://vanban.chinhphu.vn/?pageid=27160&docid=213020",
        "https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/3/55-1cp.signed.pdf",
    ),
}

RELATION_PATTERNS = {
    "CAN_CU": r"\bCăn\s+cứ\s+(?:Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định)[^\n]{0,180}?\bsố\s+([0-9]+/[0-9]{4}/(?:QH\d+|NĐ-CP|TT-[A-ZĐ]+|QĐ-TTg))",
    "DAN_CHIEU": r"\b(?:Theo|thực\s+hiện)\s+(?:Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định)[^\n]{0,180}?\bsố\s+([0-9]+/[0-9]{4}/(?:QH\d+|NĐ-CP|TT-[A-ZĐ]+|QĐ-TTg))",
    "SUA_DOI": r"\b(?:sửa\s+đổi|bổ\s+sung)\s+(?:Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định)[^\n]{0,180}?\bsố\s+([0-9]+/[0-9]{4}/(?:QH\d+|NĐ-CP|TT-[A-ZĐ]+|QĐ-TTg))",
    "THAY_THE": r"\bthay\s+thế\s+(?:Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định)[^\n]{0,180}?\bsố\s+([0-9]+/[0-9]{4}/(?:QH\d+|NĐ-CP|TT-[A-ZĐ]+|QĐ-TTg))",
    "BAI_BO": r"\bbãi\s+bỏ\s+(?:Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định)[^\n]{0,180}?\bsố\s+([0-9]+/[0-9]{4}/(?:QH\d+|NĐ-CP|TT-[A-ZĐ]+|QĐ-TTg))",
    "HUONG_DAN": r"\bhướng\s+dẫn\s+(?:thi\s+hành\s+)?(?:Luật|Nghị\s+định|Thông\s+tư|Quyết\s+định)[^\n]{0,180}?\bsố\s+([0-9]+/[0-9]{4}/(?:QH\d+|NĐ-CP|TT-[A-ZĐ]+|QĐ-TTg))",
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def fetch(url: str) -> tuple[str, dict[str, str], bytes, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.1"})
    try:
        with urlopen(request, timeout=45) as response:
            return str(response.status), dict(response.headers.items()), response.read(), "OK"
    except HTTPError as exc:
        return str(exc.code), dict(exc.headers.items()) if exc.headers else {}, exc.read(), "HTTP_ERROR"
    except (URLError, TimeoutError, OSError) as exc:
        return "CLIENT_ERROR", {}, str(exc).encode("utf-8", errors="replace"), f"CLIENT_ERROR:{type(exc).__name__}"


def write_capture(raw: Path, stem: str, extension: str, requested_url: str) -> dict[str, str]:
    status, headers, body, transport = fetch(requested_url)
    payload_path = raw / f"{stem}.{extension}"
    header_path = raw / f"{stem}.headers.json"
    payload_path.write_bytes(body)
    header_path.write_text(json.dumps(headers, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "requested_url": requested_url, "http_status": status, "transport": transport,
        "raw_file": payload_path.relative_to(raw.parent).as_posix(), "raw_sha256": digest(body),
        "raw_bytes": str(len(body)), "headers_file": header_path.relative_to(raw.parent).as_posix(),
        "headers_sha256": digest(header_path.read_bytes()), "headers_bytes": str(header_path.stat().st_size),
    }


def pdf_from_landing(html: bytes) -> str | None:
    match = re.search(r'https?://datafiles\.chinhphu\.vn/[^"\'<>\s]+?\.pdf', html.decode("utf-8", errors="replace"), re.I)
    return match.group(0) if match else None


def text_from_pdf(pdf_path: Path) -> tuple[str, str]:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception as exc:  # pragma: no cover - explicitly logged in artifacts
        return "", f"PDF_TEXT_UNAVAILABLE:{type(exc).__name__}"
    try:
        reader = PdfReader(str(pdf_path))
        text = "\n".join((page.extract_text() or "") for page in reader.pages)
        return text, f"PDF_TEXT_EXTRACTED:{len(reader.pages)}_PAGES:{len(text)}_CHARS"
    except Exception as exc:
        return "", f"PDF_TEXT_EXTRACTION_FAILED:{type(exc).__name__}"


def relation_hits(text: str) -> list[tuple[str, str, str]]:
    hits: list[tuple[str, str, str]] = []
    for relation, pattern in RELATION_PATTERNS.items():
        for match in re.finditer(pattern, text, flags=re.I):
            target = match.group(1).upper().replace("Đ", "Đ")
            excerpt = re.sub(r"\s+", " ", match.group(0)).strip()
            hits.append((relation, target, excerpt))
    return hits


def official_resolution_url(document_number: str) -> str:
    # The legal portal has no stable public number resolver.  This request is
    # retained as raw evidence of the first-party resolution attempt; a generic
    # detail page or a page that does not contain the exact number is failure.
    return "https://vanban.chinhphu.vn/?pageid=27160&tukhoa=" + quote(f'"{document_number}"', safe="")


def contains_exact_number(payload: bytes, number: str) -> bool:
    normalized = payload.decode("utf-8", errors="replace").upper().replace("&NBSP;", " ")
    return number.upper() in normalized


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    run_id = "legal-relation-traversal-" + datetime.now().strftime("%Y%m%dT%H%M%S")
    run_dir = OUT_ROOT / run_id
    raw = run_dir / "raw"
    raw.mkdir(parents=True, exist_ok=False)
    captures: list[dict[str, str]] = []
    nodes: list[dict[str, str]] = []
    edges: list[dict[str, str]] = []
    queue: list[tuple[str, int, str | None]] = []
    known: set[str] = set()

    # Capture all registered anchors in this run.  Their text is assessed only
    # for explicit relation strings; empty scanned-text layers are logged.
    for index, (number, landing_url) in enumerate(SEEDS, 1):
        key = f"seed-{index:02d}"
        landing = write_capture(raw, f"{key}.landing", "html", landing_url)
        captures.append({"capture_kind": "SEED_LANDING", "document_number": number, "depth": "0", **landing})
        pdf_url = pdf_from_landing((run_dir / landing["raw_file"]).read_bytes()) if landing["http_status"] == "200" else None
        if not pdf_url:
            nodes.append({"document_number": number, "depth": "0", "parent_document": "", "landing_url": landing_url, "pdf_url": "", "node_state": "FAIL_CLOSED_NO_FIRST_PARTY_PDF", "text_assessment": "NOT_AVAILABLE"})
            continue
        pdf = write_capture(raw, f"{key}.fulltext", "pdf", pdf_url)
        captures.append({"capture_kind": "SEED_PDF", "document_number": number, "depth": "0", **pdf})
        pdf_path = run_dir / pdf["raw_file"]
        text, text_state = text_from_pdf(pdf_path) if pdf["http_status"] == "200" and pdf_path.read_bytes().startswith(b"%PDF") else ("", "PDF_NOT_RETRIEVED_OR_NOT_PDF")
        nodes.append({"document_number": number, "depth": "0", "parent_document": "", "landing_url": landing_url, "pdf_url": pdf_url, "node_state": "RAW_OFFICIAL_DOCUMENT_CAPTURED", "text_assessment": text_state})
        known.add(number)
        queue.append((number, 0, pdf["raw_file"] if text else None))

    cap_reached = False
    blocked: list[str] = []
    cursor = 0
    while cursor < len(queue):
        source, depth, pdf_rel = queue[cursor]
        cursor += 1
        if depth >= MAX_DEPTH:
            continue
        if not pdf_rel:
            continue
        text, text_state = text_from_pdf(run_dir / pdf_rel)
        if not text:
            continue
        for relation, target, excerpt in relation_hits(text):
            target_known = target in known
            edge_state = "VERIFIED_DIRECT_TEXT" if target_known else "DISCOVERED_TARGET_PENDING_OFFICIAL_RESOLUTION"
            edges.append({"source_document": source, "source_depth": str(depth), "relation_type": relation, "target_document": target, "evidence_excerpt": excerpt, "source_raw_file": pdf_rel, "edge_state": edge_state})
            if target_known:
                continue
            if len(known) >= MAX_LINKED_DOCUMENTS:
                cap_reached = True
                break
            known.add(target)
            locator = OFFICIAL_TARGET_LOCATORS.get(target)
            resolve_url = locator[0] if locator else official_resolution_url(target)
            resolve = write_capture(raw, f"resolve-{len(known):02d}", "html", resolve_url)
            captures.append({"capture_kind": "TARGET_RESOLUTION_ATTEMPT", "document_number": target, "depth": str(depth + 1), **resolve})
            payload = (run_dir / resolve["raw_file"]).read_bytes()
            resolved = resolve["http_status"] == "200" and (contains_exact_number(payload, target) or locator is not None)
            pdf_url = locator[1] if locator else (pdf_from_landing(payload) if resolved else None)
            if resolved and pdf_url:
                pdf = write_capture(raw, f"resolve-{len(known):02d}.fulltext", "pdf", pdf_url)
                captures.append({"capture_kind": "TARGET_PDF", "document_number": target, "depth": str(depth + 1), **pdf})
                pdf_path = run_dir / pdf["raw_file"]
                text, text_state = text_from_pdf(pdf_path) if pdf["http_status"] == "200" and pdf_path.read_bytes().startswith(b"%PDF") else ("", "PDF_NOT_RETRIEVED_OR_NOT_PDF")
                state = "RAW_OFFICIAL_DOCUMENT_CAPTURED" if pdf["http_status"] == "200" else "FAIL_CLOSED_TARGET_PDF_NOT_RETRIEVED"
                nodes.append({"document_number": target, "depth": str(depth + 1), "parent_document": source, "landing_url": resolve["requested_url"], "pdf_url": pdf_url, "node_state": state, "text_assessment": text_state})
                if text:
                    queue.append((target, depth + 1, pdf["raw_file"]))
                elif state.startswith("FAIL_CLOSED"):
                    blocked.append(target)
            else:
                state = "FAIL_CLOSED_TARGET_NOT_RESOLVED_BY_OFFICIAL_PORTAL"
                nodes.append({"document_number": target, "depth": str(depth + 1), "parent_document": source, "landing_url": resolve["requested_url"], "pdf_url": "", "node_state": state, "text_assessment": "NOT_ATTEMPTED_NO_VERIFIABLE_DOCUMENT_LOCATOR"})
            if not resolved:
                blocked.append(target)
            # A target search result is not a legal document.  The runner does
            # not guess document IDs or harvest arbitrary similar-document links.
        if cap_reached:
            break

    if cap_reached:
        status = "FAIL_CLOSED_RELATION_TRAVERSAL_CAP_REACHED_BEFORE_TERMINAL"
        stopping = "CAP_50_LINKED_DOCUMENTS_REACHED"
    elif blocked:
        status = "FAIL_CLOSED_RELATION_TRAVERSAL_BLOCKED_UNRESOLVED_OFFICIAL_TARGET"
        stopping = "BLOCKED_BEFORE_TERMINAL_NO_NEW_DOCUMENT_ID_RULE"
    else:
        status = "RAW_RELATION_TRAVERSAL_TERMINAL_NOT_LEGAL_EFFECT_CODED"
        stopping = "NO_NEW_DOCUMENT_ID_DISCOVERED_WITHIN_DEPTH_3"

    capture_fields = ["capture_kind", "document_number", "depth", "requested_url", "http_status", "transport", "raw_file", "raw_sha256", "raw_bytes", "headers_file", "headers_sha256", "headers_bytes"]
    node_fields = ["document_number", "depth", "parent_document", "landing_url", "pdf_url", "node_state", "text_assessment"]
    edge_fields = ["source_document", "source_depth", "relation_type", "target_document", "evidence_excerpt", "source_raw_file", "edge_state"]
    write_csv(run_dir / "capture-ledger.csv", captures, capture_fields)
    write_csv(run_dir / "node-ledger.csv", nodes, node_fields)
    write_csv(run_dir / "edge-ledger.csv", edges, edge_fields)

    manifest = {
        "run_id": run_id, "completed_at_utc": now(), "protocol_status": status,
        "relation_depth_limit": MAX_DEPTH, "linked_document_cap": MAX_LINKED_DOCUMENTS,
        "stopping_rule_assessment": stopping, "nodes_discovered_or_seeded": len(known),
        "edge_count": len(edges), "unresolved_official_targets": blocked,
        "scope": "Post-registration raw legal relation traversal only. No legal-effect, status, scope, implementation, eligibility, screening, deduplication, PRISMA, or council-existence conclusion.",
        "method_note": "Only explicit relations recovered from reviewable PDF text are entered as edges. Scanned/unextractable PDFs produce no negative relation claim. Official search pages that do not contain the exact target number do not resolve a target.",
    }
    (run_dir / "run-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    files = [p for p in sorted(run_dir.rglob("*")) if p.is_file() and p.name != "sha256.csv"]
    hash_rows = [{"relative_path": p.relative_to(run_dir).as_posix(), "sha256": digest(p.read_bytes()), "bytes": str(p.stat().st_size)} for p in files]
    write_csv(run_dir / "sha256.csv", hash_rows, ["relative_path", "sha256", "bytes"])
    print(json.dumps(manifest, ensure_ascii=False))
    return 0 if status.startswith("RAW_RELATION_TRAVERSAL_TERMINAL") else 2


if __name__ == "__main__":
    raise SystemExit(main())
