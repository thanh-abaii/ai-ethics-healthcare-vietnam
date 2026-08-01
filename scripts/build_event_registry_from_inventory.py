#!/usr/bin/env python3
"""Build an append-only registry event ledger from verified raw inventory.

The utility intentionally creates only MANIFESTATION and PROVENANCE events.
It does not canonicalize, screen, adjudicate, calculate PRISMA counts, or
replace the prior non-conformant master registry.  Those actions require their
own registered evidence and reviewer decisions.
"""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_ROOT = ROOT / "artifacts" / "search-rerun-01-2026-07-31"
INVENTORY = ARTIFACT_ROOT / "registry" / "raw-manifestation-inventory.csv"
OUTPUT = ARTIFACT_ROOT / "registry" / "registry-event-ledger.csv"
FIELDS = [
    "registry_event_id", "row_type", "record_id", "canonical_record_id", "document_id", "framework_id", "title", "year",
    "language", "doi", "pmid", "openalex_id", "official_document_number", "normalized_url", "manifestation_type",
    "provenance_event_id", "discovery_channel", "query_id", "seed_record_id", "citation_direction", "discovery_date",
    "raw_artifact_locator", "raw_artifact_checksum", "duplicate_status", "duplicate_basis", "preferred_version",
    "preferred_version_reason", "reviewer", "screening_stage", "reviewer_decision", "exclusion_reason", "decision_date",
    "final_adjudication", "adjudicator", "adjudication_date", "screening_codebook_version", "registry_version",
    "supersedes_event_id", "change_type", "change_reason", "notes",
]


def event(event_id: int, row_type: str, **values: str) -> dict[str, str]:
    row = {field: "NOT_APPLICABLE" for field in FIELDS}
    row.update({"registry_event_id": f"REG-E{event_id:06d}", "row_type": row_type, "registry_version": "0.1-draft", "supersedes_event_id": ""})
    row.update(values)
    return row


def main() -> int:
    with INVENTORY.open("r", encoding="utf-8-sig", newline="") as handle:
        inventory = list(csv.DictReader(handle))
    if not inventory:
        raise SystemExit("Verified raw inventory is empty.")
    discovered = datetime.now(timezone.utc).date().isoformat()
    events: list[dict[str, str]] = []
    event_id = 1
    for item in inventory:
        record_id = item["manifestation_id"]
        legal = item["source_channel"] == "LEGAL_OFFICIAL_PORTAL"
        common = {
            "record_id": record_id, "canonical_record_id": "PENDING_CANONICALIZATION", "document_id": "PENDING_DOCUMENT_LINK",
            "framework_id": "NOT_APPLICABLE", "title": item["title"] or "UNKNOWN", "year": item["year"] or "UNKNOWN",
            "language": "UNKNOWN", "doi": item["doi"] or "NOT_REPORTED", "pmid": item["pmid"] or "NOT_APPLICABLE",
            "openalex_id": item["openalex_id"] or "NOT_APPLICABLE", "official_document_number": item["source_record_id"] if legal else "NOT_APPLICABLE",
            "normalized_url": "NOT_REPORTED", "manifestation_type": "PDF" if legal else "JSON", "raw_artifact_locator": item["raw_artifact_locator"],
            "raw_artifact_checksum": item["raw_artifact_checksum"], "duplicate_status": "UNASSESSED", "duplicate_basis": "NOT_APPLICABLE",
            "preferred_version": "PENDING", "preferred_version_reason": "PENDING_CANONICALIZATION", "reviewer": "NOT_APPLICABLE",
            "screening_stage": "NOT_APPLICABLE", "reviewer_decision": "NOT_APPLICABLE", "exclusion_reason": "",
            "decision_date": "NOT_APPLICABLE", "final_adjudication": "PENDING", "adjudicator": "NOT_APPLICABLE",
            "adjudication_date": "NOT_APPLICABLE", "screening_codebook_version": "NOT_APPLICABLE",
        }
        events.append(event(event_id, "MANIFESTATION", **common, change_type="CREATE", change_reason="Verified raw manifestation loaded without canonicalization.", notes=item["provenance_status"]))
        event_id += 1
        events.append(event(event_id, "PROVENANCE", **common, provenance_event_id=f"PROV-{record_id}", discovery_channel=item["source_channel"],
                            query_id=item["query_locator"], seed_record_id="NOT_APPLICABLE", citation_direction="NOT_APPLICABLE",
                            discovery_date=discovered, change_type="ADD_PROVENANCE", change_reason="Raw artifact checksum independently verified.", notes=f"retrieval_run_id={item['retrieval_run_id']}"))
        event_id += 1
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(events)
    print(f"Created {OUTPUT} with {len(events)} append-only events for {len(inventory)} manifestations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
