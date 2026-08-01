"""Fail-closed provenance audit and global deduplication candidate builder.

This post-registration utility reads only raw exports referenced by manifests in
``artifacts/search-rerun-01-2026-07-31``.  It does not screen, extract, edit the
event registry, or calculate a PRISMA count.  It instead produces an auditable
manifestation inventory and deterministic duplicate candidates for later
canonicalization in the append-only registry.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARTIFACT_ROOT = ROOT / "artifacts" / "search-rerun-01-2026-07-31"
INVENTORY_FIELDS = [
    "manifestation_id", "source_channel", "source_record_id", "title", "year",
    "doi", "pmid", "openalex_id", "raw_artifact_locator", "raw_artifact_checksum",
    "retrieval_run_id", "query_locator", "provenance_status",
]
CANDIDATE_FIELDS = [
    "candidate_id", "match_basis", "match_value", "member_manifestation_ids",
    "member_sources", "recommendation", "rationale",
]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def norm_doi(value: str | None) -> str:
    value = (value or "").strip().lower()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value)
    return value.rstrip(" .;,)")


def year_from(value: str | None) -> str:
    match = re.search(r"\b(19|20)\d{2}\b", value or "")
    return match.group(0) if match else "UNKNOWN"


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def check_file(path: Path, expected_sha: str, failures: list[str]) -> bool:
    if not path.is_file():
        failures.append(f"MISSING_RAW_ARTIFACT: {path}")
        return False
    actual = file_sha256(path)
    if actual.lower() != expected_sha.lower():
        failures.append(f"CHECKSUM_MISMATCH: {path} expected={expected_sha} actual={actual}")
        return False
    return True


def pubmed_inventory(artifact_root: Path, failures: list[str]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for manifest_path in sorted((artifact_root / "pubmed").glob("*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("status") != "RAW_EXPORT_CAPTURED_NOT_SCREENED":
            continue
        run_dir = manifest_path.parent
        files = {item["file"]: item["sha256"] for item in manifest.get("files", [])}
        required = ["esearch-response.raw", "esummary-batch-000000-response.raw"]
        if any(name not in files for name in required):
            failures.append(f"PUBMED_MANIFEST_INCOMPLETE: {manifest_path}")
            continue
        if not all(check_file(run_dir / name, files[name], failures) for name in required):
            continue
        summary_file = run_dir / "esummary-batch-000000-response.raw"
        try:
            payload = json.loads(summary_file.read_text(encoding="utf-8"))
            result = payload["result"]
            uids = result["uids"]
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            failures.append(f"PUBMED_PARSE_ERROR: {summary_file}: {exc}")
            continue
        if len(uids) != int(manifest.get("raw_record_count", -1)):
            failures.append(f"PUBMED_COUNT_MISMATCH: {manifest_path} manifest={manifest.get('raw_record_count')} parsed={len(uids)}")
            continue
        for uid in uids:
            item = result.get(str(uid), {})
            ids = {entry.get("idtype", ""): entry.get("value", "") for entry in item.get("articleids", [])}
            records.append({
                "manifestation_id": f"PMID:{uid}", "source_channel": "PUBMED",
                "source_record_id": str(uid), "title": item.get("title", "").strip(),
                "year": year_from(item.get("pubdate") or item.get("epubdate")),
                "doi": norm_doi(ids.get("doi")), "pmid": str(uid), "openalex_id": "",
                "raw_artifact_locator": str(summary_file.relative_to(artifact_root)).replace("\\", "/"),
                "raw_artifact_checksum": files[summary_file.name].lower(),
                "retrieval_run_id": manifest.get("run_id", "UNKNOWN"),
                "query_locator": str((run_dir / manifest.get("query_file", "pubmed-query-verbatim.txt")).relative_to(artifact_root)).replace("\\", "/"),
                "provenance_status": "VERIFIED_RAW_MANIFEST",
            })
    return records


def openalex_inventory(artifact_root: Path, failures: list[str]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for manifest_path in sorted((artifact_root / "openalex").glob("*/manifest.json")):
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        # Failed/obsolete runs remain preserved for audit, but are deliberately
        # excluded from the official rerun corpus and its derived inventory.
        if manifest.get("status") != "RAW_EXPORT_CAPTURED_NOT_SCREENED":
            continue
        run_dir = manifest_path.parent
        pages = manifest.get("pages", [])
        if not pages or any(page.get("http_status") != 200 for page in pages):
            failures.append(f"OPENALEX_MANIFEST_NOT_COMPLETE: {manifest_path}")
            continue
        expected_count = pages[0].get("meta_count")
        expected_ids: set[str] = set()
        parsed_rows: list[tuple[dict[str, Any], dict[str, Any]]] = []
        for page in pages:
            raw = run_dir / page["raw_file"]
            if not check_file(raw, page["raw_sha256"], failures):
                continue
            try:
                payload = json.loads(raw.read_text(encoding="utf-8"))
                results = payload["results"]
            except (json.JSONDecodeError, KeyError, TypeError) as exc:
                failures.append(f"OPENALEX_PARSE_ERROR: {raw}: {exc}")
                continue
            if len(results) != page.get("results_count"):
                failures.append(f"OPENALEX_PAGE_COUNT_MISMATCH: {raw}")
                continue
            for item in results:
                work_id = item.get("id", "").rsplit("/", 1)[-1]
                expected_ids.add(work_id)
                parsed_rows.append((item, page))
        if expected_count is None or len(expected_ids) != expected_count:
            failures.append(f"OPENALEX_TOTAL_COUNT_MISMATCH: {manifest_path} manifest={expected_count} parsed_unique={len(expected_ids)}")
            continue
        for item, page in parsed_rows:
            work_id = item["id"].rsplit("/", 1)[-1]
            ids = item.get("ids") or {}
            pmid = (ids.get("pmid") or "").rsplit("/", 1)[-1]
            records.append({
                "manifestation_id": f"OPENALEX:{work_id}", "source_channel": "OPENALEX",
                "source_record_id": work_id, "title": (item.get("display_name") or "").strip(),
                "year": str(item.get("publication_year") or "UNKNOWN"), "doi": norm_doi(item.get("doi")),
                "pmid": pmid, "openalex_id": work_id,
                "raw_artifact_locator": str((run_dir / page["raw_file"]).relative_to(artifact_root)).replace("\\", "/"),
                "raw_artifact_checksum": page["raw_sha256"].lower(),
                "retrieval_run_id": manifest.get("run_id", run_dir.name),
                "query_locator": str((run_dir / "query-spec.json").relative_to(artifact_root)).replace("\\", "/"),
                "provenance_status": "VERIFIED_RAW_MANIFEST",
            })
    return records


def build_candidates(records: list[dict[str, str]]) -> list[dict[str, str]]:
    by_identifier: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for record in records:
        for basis, field in (("DOI", "doi"), ("PMID", "pmid")):
            if record[field]:
                by_identifier[(basis, record[field])].append(record)
    candidates = []
    for number, ((basis, value), members) in enumerate(sorted(by_identifier.items()), 1):
        if len({m["manifestation_id"] for m in members}) < 2:
            continue
        candidates.append({
            "candidate_id": f"DUP-C{number:05d}", "match_basis": basis, "match_value": value,
            "member_manifestation_ids": " | ".join(sorted(m["manifestation_id"] for m in members)),
            "member_sources": " | ".join(sorted({m["source_channel"] for m in members})),
            "recommendation": "CANONICALIZATION_REVIEW_REQUIRED",
            "rationale": "Deterministic shared identifier; do not merge automatically. Review for append-only canonicalization after all direct-search channels in the declared scope are loaded.",
        })
    return candidates


def additional_inventory(path: Path, artifact_root: Path, failures: list[str]) -> list[dict[str, str]]:
    """Accept later legal/citation manifestations only with raw-file evidence.

    The input is an RFC 4180 CSV with exactly the inventory columns.  It is a
    transport file, not the registry: every locator must remain below the
    rerun artifact root and its SHA-256 is independently rechecked here.
    """
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows or set(INVENTORY_FIELDS) - set(rows[0]):
        failures.append(f"ADDITIONAL_INVENTORY_SCHEMA_INVALID: {path}")
        return []
    accepted = []
    for number, row in enumerate(rows, 2):
        item = {field: (row.get(field) or "").strip() for field in INVENTORY_FIELDS}
        if any(not item[field] for field in ("manifestation_id", "source_channel", "source_record_id", "raw_artifact_locator", "raw_artifact_checksum")):
            failures.append(f"ADDITIONAL_INVENTORY_REQUIRED_FIELD_MISSING: {path}:{number}")
            continue
        raw = (artifact_root / item["raw_artifact_locator"]).resolve()
        if artifact_root not in raw.parents or not check_file(raw, item["raw_artifact_checksum"], failures):
            failures.append(f"ADDITIONAL_INVENTORY_LOCATOR_OUTSIDE_ROOT_OR_INVALID: {path}:{number}")
            continue
        item["doi"] = norm_doi(item["doi"])
        item["provenance_status"] = "VERIFIED_RAW_MANIFEST"
        accepted.append(item)
    return accepted


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", type=Path, default=DEFAULT_ARTIFACT_ROOT)
    parser.add_argument("--additional-inventory", type=Path, action="append", default=[],
                        help="Later legal/citation inventory CSV; every raw locator/checksum is revalidated.")
    parser.add_argument("--required-channel", action="append", default=[],
                        help="Fail closed unless this source channel has verified manifestations.")
    parser.add_argument("--replace", action="store_true", help="Replace this audit's derived outputs.")
    args = parser.parse_args()
    root = args.artifact_root.resolve()
    registry = root / "registry"
    logs = root / "logs"
    outputs = [registry / "raw-manifestation-inventory.csv", registry / "global-dedup-candidates.csv", logs / "provenance-dedup-audit.json"]
    if not args.replace and any(path.exists() for path in outputs):
        raise SystemExit("Derived audit output already exists; use --replace only for a deliberate re-audit.")
    failures: list[str] = []
    records = pubmed_inventory(root, failures) + openalex_inventory(root, failures)
    for inventory_path in args.additional_inventory:
        records.extend(additional_inventory(inventory_path.resolve(), root, failures))
    duplicate_ids = [key for key, count in Counter(row["manifestation_id"] for row in records).items() if count > 1]
    if duplicate_ids:
        failures.append(f"DUPLICATE_MANIFESTATION_ID: {duplicate_ids[:10]}")
    observed_channels = Counter(row["source_channel"] for row in records)
    for channel in args.required_channel:
        if not observed_channels[channel]:
            failures.append(f"REQUIRED_SOURCE_CHANNEL_MISSING: {channel}")
    candidates = build_candidates(records)
    registry.mkdir(parents=True, exist_ok=True)
    logs.mkdir(parents=True, exist_ok=True)
    write_csv(outputs[0], INVENTORY_FIELDS, sorted(records, key=lambda row: row["manifestation_id"]))
    write_csv(outputs[1], CANDIDATE_FIELDS, candidates)
    summary = {
        "audit_type": "POST_REGISTRATION_PROVENANCE_AND_GLOBAL_DEDUP_PREPARATION",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "artifact_root": str(root),
        "records_with_verified_raw_manifest": len(records),
        "source_counts": dict(observed_channels),
        "required_channels": args.required_channel,
        "deterministic_duplicate_candidates": len(candidates),
        "integrity_failures": failures,
        "status": "PASS_CURRENT_RAW_SOURCES_NOT_FINAL" if records and not failures else "FAIL_CLOSED",
        "scope_limit": "No screening, extraction, PRISMA count, registry event, or final canonicalization is created by this script.",
        "next_gate": "Re-run after every direct-search channel in the declared completion scope has a verified raw inventory. This prepares the unscreened corpus for the next registered gate; no screening, extraction, PRISMA count, or citation-chasing work is created here.",
    }
    outputs[2].write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["status"].startswith("PASS") else 2


if __name__ == "__main__":
    sys.exit(main())
