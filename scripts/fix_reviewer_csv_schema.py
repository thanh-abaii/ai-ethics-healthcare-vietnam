#!/usr/bin/env python3
"""Create clean, decision-empty round-1 screening forms from the canonical registry.

This utility never creates a screening decision.  It is only valid after the
PI has confirmed DIRECT_SEARCH_COMPLETE and fails rather than overwriting a
previously created form.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "artifacts/search-rerun-01-2026-07-31/registry/master-record-registry.csv"
GOVERNANCE_DIR = ROOT / "docs/governance"
OPEN_DATE = "2026-08-02"
FIELDS = [
    "record_id", "stage", "reviewer", "source_type",
    "inclusion_decision", "exclusion_reason", "notes", "date",
]
REVIEWERS = {
    "dao-trung-thanh": "DAO_TRUNG_THANH",
    "loc-dang": "LOC_DANG",
}


def source_type(source_channels: str) -> str:
    if "LEGAL" in source_channels:
        return "LEGAL_REGULATION"
    if "PR07" in source_channels:
        return "OFFICIAL_REPORT"
    if "PUBMED" in source_channels or "OPENALEX" in source_channels:
        return "ACADEMIC_STUDY"
    return "OTHER_UNCLEAR"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    with REGISTRY_PATH.open(encoding="utf-8-sig", newline="") as handle:
        records = list(csv.DictReader(handle))
    if len(records) != 385 or len({r["canonical_record_id"] for r in records}) != 385:
        raise SystemExit("FAIL_CLOSED: expected exactly 385 unique canonical records")

    outputs: list[Path] = []
    for slug, reviewer in REVIEWERS.items():
        output = GOVERNANCE_DIR / f"round-1-title-abstract-{slug}-{OPEN_DATE}.csv"
        if output.exists():
            raise SystemExit(f"FAIL_CLOSED: refusing to overwrite {output}")
        rows = [{
            "record_id": item["canonical_record_id"],
            "stage": "TITLE_ABSTRACT",
            "reviewer": reviewer,
            "source_type": source_type(item["source_channels"]),
            "inclusion_decision": "",
            "exclusion_reason": "",
            "notes": f"Title: {item['title']} | Source: {item['source_channels']}",
            "date": "",
        } for item in records]
        with output.open("x", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        outputs.append(output)

    print(json.dumps({
        "status": "ROUND_1_FORMS_CREATED_DECISION_EMPTY",
        "canonical_records": len(records),
        "outputs": [{"path": str(path), "sha256": sha256(path)} for path in outputs],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
