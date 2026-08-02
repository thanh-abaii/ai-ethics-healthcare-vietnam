#!/usr/bin/env python3
"""Mechanically reconcile locked title/abstract screening decisions.

This script never edits reviewer files.  It validates the locked inputs against
the Master Input Registry, writes a per-record reconciliation matrix, and
creates a concise audit report with unweighted Cohen's kappa.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from collections import Counter
from datetime import date
from pathlib import Path


DECISIONS = ("INCLUDE", "EXCLUDE", "UNCERTAIN")
REVIEWER_COLUMNS = (
    "record_id",
    "stage",
    "reviewer",
    "source_type",
    "inclusion_decision",
    "exclusion_reason",
    "notes",
    "date",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        return reader.fieldnames or [], list(reader)


def validate_reviewer_file(
    path: Path,
    reviewer: str,
    expected_hash: str,
    master_ids: set[str],
) -> dict[str, dict[str, str]]:
    actual_hash = sha256(path)
    if actual_hash != expected_hash.lower():
        raise ValueError(f"Checksum mismatch for {path}: {actual_hash}")

    headers, rows = read_csv(path)
    if tuple(headers) != REVIEWER_COLUMNS:
        raise ValueError(f"Unexpected schema in {path}: {headers}")
    if len(rows) != len(master_ids):
        raise ValueError(f"Unexpected row count in {path}: {len(rows)}")

    by_id: dict[str, dict[str, str]] = {}
    for row in rows:
        record_id = row["record_id"]
        if record_id in by_id:
            raise ValueError(f"Duplicate record_id in {path}: {record_id}")
        if row["reviewer"] != reviewer:
            raise ValueError(f"Unexpected reviewer in {path}: {row['reviewer']}")
        if row["stage"] != "TITLE_ABSTRACT":
            raise ValueError(f"Unexpected stage in {path}: {row['stage']}")
        if row["inclusion_decision"] not in DECISIONS:
            raise ValueError(f"Invalid decision in {path}: {row['inclusion_decision']}")
        if row["exclusion_reason"].strip():
            raise ValueError(f"Premature exclusion reason in {path}: {record_id}")
        by_id[record_id] = row

    if set(by_id) != master_ids:
        raise ValueError(f"record_id set does not match Master Input Registry: {path}")
    return by_id


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    headers = [
        "record_id", "source_type", "dao_trung_thanh_decision",
        "loc_dang_decision", "agreement_status", "next_workflow_status",
        "adjudication_status", "dao_file_sha256", "loc_file_sha256",
    ]
    with path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dao", type=Path, required=True)
    parser.add_argument("--loc", type=Path, required=True)
    parser.add_argument("--master", type=Path, required=True)
    parser.add_argument("--dao-sha256", required=True)
    parser.add_argument("--loc-sha256", required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    master_headers, master_rows = read_csv(args.master)
    if "canonical_record_id" not in master_headers:
        raise ValueError("Master Input Registry has no canonical_record_id column")
    master_ids = {row["canonical_record_id"] for row in master_rows}
    if len(master_ids) != len(master_rows):
        raise ValueError("Master Input Registry has duplicate canonical_record_id values")

    dao = validate_reviewer_file(args.dao, "DAO_TRUNG_THANH", args.dao_sha256, master_ids)
    loc = validate_reviewer_file(args.loc, "LOC_DANG", args.loc_sha256, master_ids)

    contingency = {left: Counter() for left in DECISIONS}
    rows: list[dict[str, str]] = []
    for record_id in sorted(master_ids):
        dao_decision = dao[record_id]["inclusion_decision"]
        loc_decision = loc[record_id]["inclusion_decision"]
        contingency[dao_decision][loc_decision] += 1
        if dao_decision == loc_decision == "EXCLUDE":
            agreement, workflow, adjudication = "AGREED_EXCLUDE", "TITLE_ABSTRACT_EXCLUDE_AGREED", "NO_ADJUDICATION_REQUIRED"
        elif dao_decision == loc_decision:
            agreement, workflow, adjudication = "AGREED_ADVANCE", "ADVANCE_TO_FULL_TEXT_DUAL_SCREENING", "NO_ADJUDICATION_REQUIRED"
        else:
            agreement, workflow, adjudication = "DISAGREEMENT", "PENDING_ADJUDICATION", "PENDING_ADJUDICATION"
        rows.append({
            "record_id": record_id,
            "source_type": dao[record_id]["source_type"],
            "dao_trung_thanh_decision": dao_decision,
            "loc_dang_decision": loc_decision,
            "agreement_status": agreement,
            "next_workflow_status": workflow,
            "adjudication_status": adjudication,
            "dao_file_sha256": args.dao_sha256.lower(),
            "loc_file_sha256": args.loc_sha256.lower(),
        })
    write_csv(args.matrix, rows)

    total = len(rows)
    agreed = sum(contingency[d][d] for d in DECISIONS)
    po = agreed / total
    dao_counts = {decision: sum(contingency[decision].values()) for decision in DECISIONS}
    loc_counts = {decision: sum(contingency[left][decision] for left in DECISIONS) for decision in DECISIONS}
    pe = sum(dao_counts[d] * loc_counts[d] for d in DECISIONS) / (total * total)
    kappa = (po - pe) / (1 - pe)
    status_counts = Counter(row["next_workflow_status"] for row in rows)

    report = f"""# Kiểm toán cơ học và ma trận đối soát vòng 1\n\n**Ngày tạo:** {date.today().isoformat()}  \n**Phạm vi:** đối soát sau khóa độc lập cho 385 `CANON-*`; không chứa quyết định phân xử.\n\n## Kiểm tra đầu vào\n\n- Tập ID của mỗi reviewer khớp Master Input Registry: **PASS** (385/385, không trùng).\n- Reviewer/stage/schema/giá trị quyết định: **PASS**.\n- `exclusion_reason` ở vòng tiêu đề/tóm tắt: **PASS** (đều trống).\n- SHA-256 tệp PI: `{args.dao_sha256.lower()}` — **PASS**.\n- SHA-256 tệp Lộc Đặng: `{args.loc_sha256.lower()}` — **PASS**.\n\n## Provenance khóa\n\n- PI xác nhận khóa ngày 2026-08-02 tại `docs/governance/pi-round-1-lock-confirmation-2026-08-02.md`.\n- Lộc Đặng xác nhận khóa ngày 2026-08-02 tại `docs/governance/loc-dang-round-1-lock-confirmation-2026-08-02.md`.\n- Hai biên bản chỉ ghi ngày, không ghi giờ khóa; không suy diễn thêm mốc thời gian.\n\n## Ma trận quyết định\n\n| PI \\ Lộc | INCLUDE | EXCLUDE | UNCERTAIN | Tổng |\n| --- | ---: | ---: | ---: | ---: |\n| INCLUDE | {contingency['INCLUDE']['INCLUDE']} | {contingency['INCLUDE']['EXCLUDE']} | {contingency['INCLUDE']['UNCERTAIN']} | {dao_counts['INCLUDE']} |\n| EXCLUDE | {contingency['EXCLUDE']['INCLUDE']} | {contingency['EXCLUDE']['EXCLUDE']} | {contingency['EXCLUDE']['UNCERTAIN']} | {dao_counts['EXCLUDE']} |\n| UNCERTAIN | {contingency['UNCERTAIN']['INCLUDE']} | {contingency['UNCERTAIN']['EXCLUDE']} | {contingency['UNCERTAIN']['UNCERTAIN']} | {dao_counts['UNCERTAIN']} |\n| Tổng | {loc_counts['INCLUDE']} | {loc_counts['EXCLUDE']} | {loc_counts['UNCERTAIN']} | {total} |\n\n## Đồng thuận và trạng thái kế tiếp\n\n- Đồng thuận quan sát: **{agreed}/{total} ({po:.2%})**.\n- Cohen's Kappa không trọng số (ba mức `INCLUDE`/`EXCLUDE`/`UNCERTAIN`): **{kappa:.4f}**. Đây là chỉ số mô tả, không phải hard gate.\n- Chuyển toàn văn sàng lọc kép: **{status_counts['ADVANCE_TO_FULL_TEXT_DUAL_SCREENING']}** bản ghi có đồng thuận `INCLUDE` hoặc `UNCERTAIN`.\n- Loại đồng thuận tại tiêu đề/tóm tắt: **{status_counts['TITLE_ABSTRACT_EXCLUDE_AGREED']}** bản ghi; không xóa record hay provenance.\n- Giữ nguyên để phân xử: **{status_counts['PENDING_ADJUDICATION']}** bản ghi với trạng thái `PENDING_ADJUDICATION`.\n\n## Ranh giới thẩm quyền\n\nMa trận kèm theo chỉ ghi hai quyết định gốc và trạng thái quy trình. Agent không quyết định kết quả của bất kỳ bất đồng nào; mọi phân xử phải do PI hoặc cơ chế phân xử đã đăng ký, đồng thời giữ nguyên audit trail.\n"""
    args.report.write_text(report, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
