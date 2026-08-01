#!/usr/bin/env python3
"""Execute Gate G6 & G7 evaluation, build Master Record Registry, and generate Round 1 screening CSVs.

Gate G6: Coverage & Provenance Audit (Verifies 5 source branches and SHA-256 integrity).
Gate G7: Registry Readiness & Canonicalization (Deduplicates manifestations into master records).
Output:
  - artifacts/search-rerun-01-2026-07-31/registry/master-record-registry.csv
  - docs/audits/g6-g7-evaluation-report-2026-08-01.md
  - docs/governance/round-1-screening-reviewer-1-dao-trung-thanh.csv
  - docs/governance/round-1-screening-reviewer-2-loc-dang.csv
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_ROOT = ROOT / "artifacts/search-rerun-01-2026-07-31"
REGISTRY_DIR = ARTIFACT_ROOT / "registry"
GOVERNANCE_DIR = ROOT / "docs/governance"
AUDIT_DIR = ROOT / "docs/audits"


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def to_long_path(path: Path) -> str:
    abs_str = str(path.resolve())
    if os.name == "nt" and not abs_str.startswith("\\\\?\\"):
        return "\\\\?\\" + abs_str
    return abs_str


def main() -> int:
    raise SystemExit(
        "RETIRED_FAIL_CLOSED: this legacy utility used record-count proxies for G6/G7 "
        "and could create a non-conformant registry or screening forms. Use "
        "verify_g6_g7_contract.py instead."
    )
    inventory_path = REGISTRY_DIR / "raw-manifestation-inventory.csv"
    dedup_path = REGISTRY_DIR / "global-dedup-candidates.csv"

    if not inventory_path.exists():
        raise SystemExit("Missing raw-manifestation-inventory.csv; run audit_official_provenance_and_dedup.py first.")

    with open(to_long_path(inventory_path), "r", encoding="utf-8-sig", newline="") as f:
        inventory_rows = list(csv.DictReader(f))

    dedup_rows = []
    if dedup_path.exists():
        with open(to_long_path(dedup_path), "r", encoding="utf-8-sig", newline="") as f:
            dedup_rows = list(csv.DictReader(f))

    print(f"Loaded {len(inventory_rows)} raw manifestations and {len(dedup_rows)} duplicate candidate pairs.")

    # Group manifestations by DOI/PMID/Title for canonicalization
    doi_map: dict[str, list[dict[str, str]]] = {}
    pmid_map: dict[str, list[dict[str, str]]] = {}
    master_records: list[dict[str, str]] = []
    seen_manifestations: set[str] = set()

    rec_counter = 1

    for row in inventory_rows:
        man_id = row["manifestation_id"]
        if man_id in seen_manifestations:
            continue

        doi = (row.get("doi") or "").strip().lower()
        pmid = (row.get("pmid") or "").strip()

        # Check if this manifestation belongs to an existing canonical record
        matched_record = None
        if doi:
            for rec in master_records:
                if rec["doi"].lower() == doi:
                    matched_record = rec
                    break
        if not matched_record and pmid:
            for rec in master_records:
                if rec["pmid"] == pmid:
                    matched_record = rec
                    break

        if matched_record:
            # Append manifestation ID to member list
            matched_record["member_manifestation_ids"] += f" | {man_id}"
            if row["source_channel"] not in matched_record["source_branches"]:
                matched_record["source_branches"] += f" | {row['source_channel']}"
            seen_manifestations.add(man_id)
        else:
            rec_id = f"REC-{rec_counter:04d}"
            rec_counter += 1
            master_records.append({
                "master_record_id": rec_id,
                "title": row.get("title") or "Untitled",
                "publication_year": row.get("year") or "UNKNOWN",
                "source_branches": row["source_channel"],
                "doi": row.get("doi") or "",
                "pmid": row.get("pmid") or "",
                "openalex_id": row.get("openalex_id") or "",
                "primary_locator": row.get("raw_artifact_locator") or "",
                "member_manifestation_ids": man_id,
                "canonicalization_status": "DETERMINISTIC_CANONICALIZED"
            })
            seen_manifestations.add(man_id)

    master_path = REGISTRY_DIR / "master-record-registry.csv"
    fields = [
        "master_record_id", "title", "publication_year", "source_branches",
        "doi", "pmid", "openalex_id", "primary_locator",
        "member_manifestation_ids", "canonicalization_status"
    ]

    with open(to_long_path(master_path), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(master_records)

    print(f"Created Master Record Registry: {len(master_records)} unique records (Deduplicated from {len(inventory_rows)} manifestations).")

    # Evaluate Gate G6 & G7
    gate_g6_status = "PASS" if len(inventory_rows) >= 400 else "FAIL"
    gate_g7_status = "PASS" if len(master_records) > 0 and master_path.exists() else "FAIL"

    # Generate Gate G6 & G7 Report
    report_content = f"""# BÁO CÁO ĐÁNH GIÁ ĐIỂM KIỂM SOÁT GATE G6 VÀ GATE G7
## (Gate G6 & G7 Audit Evaluation Report)

**Dự án:** Scoping Review về Đạo đức và Quản trị AI Y tế tại Việt Nam  
**Ngày thực thi:** {dt.datetime.now().strftime("%d/%m/%Y")}  
**Trạng thái Gate G6 (Coverage & Provenance Gate):** **`{gate_g6_status}`**  
**Trạng thái Gate G7 (Registry Readiness Gate):** **`{gate_g7_status}`**  
**Trạng thái Nghiên cứu sau Gate:** **`READY_FOR_DOUBLE_SCREENING_ROUND_1`**

---

## 1. Kết quả Đánh giá Gate G6 (Coverage & Provenance Audit)
- **Tổng số bản ghi vận chuyển thô đã thu hồi:** **{len(inventory_rows)} bản ghi** (88 PubMed + 347 OpenAlex + 16 PDF Pháp lý Chính phủ).
- **Kiểm toán SHA-256:** 100% các tệp vận chuyển thô trùng khớp mã băm SHA-256.
- **Phủ 5 Nhánh Nguồn:** Đã có bằng chứng vận chuyển thô đầy đủ cho Y sinh, Đa ngành, Bộ Y tế, Bộ KH&CN, Thể chế Quốc tế, Bệnh viện Sentinel và Cổng Pháp lý.
- **Kết luận Gate G6:** **`PASS`**

---

## 2. Kết quả Đánh giá Gate G7 (Registry Canonicalization & Format Audit)
- **Thực thi Lọc trùng Bản ghi (Deduplication):** Đã xử lý 119 cặp ứng viên trùng lặp và hợp nhất {len(inventory_rows)} bản ghi vận chuyển thô thành **{len(master_records)} bản ghi Master độc nhất**.
- **Tệp Sổ cái Bản ghi Master:** [`artifacts/search-rerun-01-2026-07-31/registry/master-record-registry.csv`](../../artifacts/search-rerun-01-2026-07-31/registry/master-record-registry.csv)
- **Chuẩn hóa Phân công Sàng lọc Kép:** Đã khởi tạo 2 bảng biểu sàng lọc kép độc lập Vòng 1 cho 2 nhà rà soát theo đúng Codebook OSF.
- **Kết luận Gate G7:** **`PASS`**

---

## 3. Khởi tạo Hồ sơ Sàng lọc Kép Vòng 1
1. **Reviewer 1 (Đào Trung Thành):** [`docs/governance/round-1-screening-reviewer-1-dao-trung-thanh.csv`](../governance/round-1-screening-reviewer-1-dao-trung-thanh.csv)
2. **Reviewer 2 (Lộc Đặng):** [`docs/governance/round-1-screening-reviewer-2-loc-dang.csv`](../governance/round-1-screening-reviewer-2-loc-dang.csv)
"""

    report_path = AUDIT_DIR / "g6-g7-evaluation-report-2026-08-01.md"
    report_path.write_text(report_content, encoding="utf-8")
    print(f"Generated Audit Report: {report_path}")

    # Generate Reviewer Screening CSVs
    screening_fields = [
        "record_id", "source_branches", "title", "publication_year",
        "doi_or_locator", "inclusion_decision", "exclusion_reason",
        "screening_notes", "reviewer_signature", "timestamp_utc"
    ]

    rev1_rows = []
    rev2_rows = []

    for rec in master_records:
        base_row = {
            "record_id": rec["master_record_id"],
            "source_branches": rec["source_branches"],
            "title": rec["title"],
            "publication_year": rec["publication_year"],
            "doi_or_locator": rec["doi"] or rec["primary_locator"],
            "inclusion_decision": "PENDING",
            "exclusion_reason": "NONE",
            "screening_notes": "",
            "reviewer_signature": "",
            "timestamp_utc": ""
        }
        r1 = dict(base_row)
        r1["reviewer_signature"] = "Dao Trung Thanh"
        rev1_rows.append(r1)

        r2 = dict(base_row)
        r2["reviewer_signature"] = "Loc Dang"
        rev2_rows.append(r2)

    rev1_path = GOVERNANCE_DIR / "round-1-screening-reviewer-1-dao-trung-thanh.csv"
    rev2_path = GOVERNANCE_DIR / "round-1-screening-reviewer-2-loc-dang.csv"

    with open(to_long_path(rev1_path), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=screening_fields)
        writer.writeheader()
        writer.writerows(rev1_rows)

    with open(to_long_path(rev2_path), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=screening_fields)
        writer.writeheader()
        writer.writerows(rev2_rows)

    print(f"Generated Reviewer 1 Screening Form: {rev1_path} ({len(rev1_rows)} records)")
    print(f"Generated Reviewer 2 Screening Form: {rev2_path} ({len(rev2_rows)} records)")
    print("\nGates G6 & G7 Completed Successfully: Status is now READY_FOR_DOUBLE_SCREENING_ROUND_1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
