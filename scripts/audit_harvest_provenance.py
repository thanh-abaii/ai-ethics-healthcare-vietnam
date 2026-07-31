"""Build and validate a reproducibility ledger for a raw-harvest audit trail.

The script never infers a source channel, query, cursor, or checksum.  A record
without those facts remains explicitly unreconciled and cannot be used in PRISMA.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


REQUIRED_AUDIT = {
    "raw_record_id", "source_channel", "title", "doi", "publication_year",
    "authors", "deduplication_status", "merged_into_record_id",
    "deduplication_reason",
}
LEDGER_FIELDS = [
    "raw_record_id", "source_channel_as_supplied", "title", "doi",
    "publication_year", "deduplication_status", "merged_into_record_id",
    "deduplication_reason", "query_id", "source_record_id", "retrieval_date",
    "raw_artifact_locator", "raw_artifact_sha256", "cursor_or_page",
    "reconciliation_status", "reconciliation_note",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-trail", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--evidence-map", type=Path,
                        help="CSV keyed by raw_record_id with the six provenance fields")
    parser.add_argument("--allow-incomplete", action="store_true",
                        help="Write a gap report without declaring the ledger reproducible")
    args = parser.parse_args()

    rows = read_csv(args.audit_trail)
    if not rows:
        raise SystemExit("Audit trail has no rows.")
    missing = REQUIRED_AUDIT - set(rows[0])
    if missing:
        raise SystemExit(f"Audit trail is missing columns: {sorted(missing)}")
    identifiers = [row["raw_record_id"].strip() for row in rows]
    duplicates = [key for key, count in Counter(identifiers).items() if count > 1]
    if duplicates:
        raise SystemExit(f"raw_record_id is not unique: {duplicates[:10]}")

    evidence: dict[str, dict[str, str]] = {}
    if args.evidence_map:
        for item in read_csv(args.evidence_map):
            key = item.get("raw_record_id", "").strip()
            if not key or key in evidence:
                raise SystemExit("Evidence map has blank or duplicate raw_record_id.")
            evidence[key] = item

    args.output_dir.mkdir(parents=True, exist_ok=True)
    ledger_path = args.output_dir / "raw-harvest-provenance-ledger.csv"
    verified = 0
    with ledger_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=LEDGER_FIELDS)
        writer.writeheader()
        for row in rows:
            item = evidence.get(row["raw_record_id"], {})
            provenance = {field: item.get(field, "").strip() for field in
                          ("query_id", "source_record_id", "retrieval_date",
                           "raw_artifact_locator", "raw_artifact_sha256", "cursor_or_page")}
            complete = all(provenance.values())
            if complete:
                status = "VERIFIED_PROVENANCE"
                note = "Evidence map supplied; raw file/checksum verification is a separate run."
                verified += 1
            else:
                status = "UNRECONCILED_PROVENANCE"
                note = "Do not use for PRISMA/corpus until query, source record, date, raw locator, checksum and cursor/page are supplied."
            writer.writerow({
                "raw_record_id": row["raw_record_id"],
                "source_channel_as_supplied": row["source_channel"],
                "title": row["title"], "doi": row["doi"],
                "publication_year": row["publication_year"],
                "deduplication_status": row["deduplication_status"],
                "merged_into_record_id": row["merged_into_record_id"],
                "deduplication_reason": row["deduplication_reason"],
                **provenance, "reconciliation_status": status,
                "reconciliation_note": note,
            })

    summary = {
        "audit_trail": str(args.audit_trail),
        "audit_trail_sha256": sha256(args.audit_trail),
        "raw_records": len(rows),
        "status_counts": Counter(row["deduplication_status"] for row in rows),
        "source_channel_counts": Counter(row["source_channel"] for row in rows),
        "verified_provenance_records": verified,
        "unreconciled_provenance_records": len(rows) - verified,
        "reproducibility_status": "PASS" if verified == len(rows) else "FAIL_PROVENANCE_INCOMPLETE",
        "rule": "No unreconciled record may enter a PRISMA count, official registry, screening, or extraction.",
    }
    (args.output_dir / "harvest-provenance-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, default=dict) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2, default=dict))
    return 0 if verified == len(rows) or args.allow_incomplete else 2


if __name__ == "__main__":
    raise SystemExit(main())
