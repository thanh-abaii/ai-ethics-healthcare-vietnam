# Biên bản hoàn tất sàng lọc toàn văn kép (Dual Full-Text Screening) Vòng 2

**Ngày:** 2026-08-02
**Corpus:** 166 record `CANON-*`
**Codebook:** `screening-codebook.md` (frozen `0.1-draft`)
**Trạng thái:** Cả hai reviewer đã khóa → Ma trận Bất đồng Vòng 2 sẵn sàng cho PI phân xử.

---

## 1. Trạng thái khóa của hai reviewer

| Reviewer | Tệp | Số dòng | INCLUDE | EXCLUDE | SHA-256 |
| --- | --- | ---: | ---: | ---: | --- |
| Đào Trung Thành | `round-2-full-text-dao-trung-thanh-2026-08-02.csv` | 166 | 103 | 63 | `9ee07596d5f93373f363fee4960beeab8bce93558b98a847ea1e0744525c2828` |
| Lộc Đặng | `round-2-full-text-loc-dang-2026-08-02.csv` | 166 | 48 | 118 | `94df1846e2bdd53feed710de3d43a1464d747e12a45e0c06759f51cbbdf0b38b` |

Cả hai tệp: `stage=FULL_TEXT`, `reviewer` cố định, `date=2026-08-02`, không dòng trống. Kiểm tra cơ học (Mechanical Audit) đạt 0 lỗi.

---

## 2. Kết quả đối soát & hệ số đồng thuận

### Bảng 2×2 (INCLUDE / EXCLUDE)

|  | Lộc: INCLUDE | Lộc: EXCLUDE |
| --- | ---: | ---: |
| **Thành: INCLUDE** | 48 | 55 |
| **Thành: EXCLUDE** | 0 | 63 |

### Chỉ số

- **Tổng quan sát đồng thuận `po`:** 0.669
- **Đồng thuận ngẫu nhiên kỳ vọng `pe`:** 0.449
- **Cohen's Kappa:** **0.399** (đồng thuận mức trung bình/fair — phù hợp sàng lọc kép có phân chia can thiệp)
- **Số dòng ĐỒNG THUẬN:** 92 (`AGREED_INCLUDE` 48 + `AGREED_EXCLUDE` 44)
- **Số dòng BẤT ĐỒNG cần PI phân xử:** **74**
  - `DISAGREEMENT_DECISION` (INCLUDE vs EXCLUDE): **55** — toàn bộ là Thành=INCLUDE / Lộc=EXCLUDE
  - `DISAGREEMENT_EXCLUDE_REASON` (cùng EXCLUDE, khác mã lý do): **19**

---

## 3. Tệp Ma trận Bất đồng Vòng 2

**`docs/governance/round-2-full-text-adjudication-matrix-2026-08-02.csv`** — 166 dòng, cột:
`record_id, dao_trung_thanh_decision/reason, loc_dang_decision/reason, agreement_status, adjudication_status, next_workflow_status, dao_file_sha256, loc_file_sha256, adjudicated_decision, adjudication_reason, adjudicator`

- `NONE_REQUIRED` → không cần phân xử (92 dòng)
- `PENDING_PI_ADJUDICATION` → chờ PI (74 dòng)

---

## 4. Bước tiếp theo

PI Đào Trung Thành phân xử **74 dòng bất đồng** trong Ma trận (dùng toàn văn theo locator), ghi `adjudicated_decision`, `adjudication_reason`, `adjudicator`; sau đó khớp lại thành danh sách `INCLUDE` cuối cùng Vòng 2 để chuyển sang trích xuất dữ liệu.
