# Hướng dẫn PI Đào Trung Thành phân xử Bất đồng Vòng 2

**Phiếu phân xử:** `docs/governance/round-2-adjudication-form-2026-08-02.csv` (74 dòng bất đồng)
**Ma trận đầy đủ:** `docs/governance/round-2-full-text-adjudication-matrix-2026-08-02.csv` (166 dòng)
**Tài liệu hỗ trợ:** `docs/audits/round-2-full-text-retrieval-ledger-2026-08-02.csv` (title + locator DOI/PMID để mở toàn văn kiểm chứng)

---

## 1. Vai trò & phạm vi

- PI là người **duy nhất** quyết định kết quả của 74 dòng bất đồng.
- Quyết định phải dựa trên **rà soát toàn văn thật** (mở từng locator) theo codebook frozen `0.1-draft`.

## 2. Cách điền từng dòng trong phiếu phân xử

Chỉ sửa đúng 3 cột cuối (để mặc định những cột còn lại):

| Cột | Quy định điền |
| --- | --- |
| `pi_decision` | `INCLUDE` hoặc `EXCLUDE` |
| `pi_exclusion_reason` | Nếu `INCLUDE`: để trống. Nếu `EXCLUDE`: đúng 1 mã EX01–EX09. |
| `pi_notes` | (không bắt buộc) căn cứ toàn văn ngắn gọn |
| `pi_date` | `2026-08-02` |

## 3. Hai dạng bất đồng trong phiếu

**A. `DISAGREEMENT_DECISION` (55 dòng)** — Thành `INCLUDE`, Lộc `EXCLUDE`.
→ PI chốt `INCLUDE` hoặc `EXCLUDE`; nếu chọn `EXCLUDE` thì ghi đúng 1 mã lý do.

**B. `DISAGREEMENT_EXCLUDE_REASON` (19 dòng)** — Cả hai đều `EXCLUDE` nhưng khác mã.
→ PI chốt đúng 1 mã lý do là căn cứ chính, ghi vào `pi_exclusion_reason`.

**Lưu ý:** `pi_decision` luôn `EXCLUDE` cho nhóm B; vẫn ghi mã theo PI chọn.

## 4. Không được làm

- Không sửa 7 cột cố định còn lại của phiếu.
- Không tự tạo mã lý do mới (chỉ EX01–EX09).
- Không giữ trạng thái treo — mỗi dòng bắt buộc `INCLUDE` hoặc `EXCLUDE`.

## 5. Sau khi phân xử xong

Báo tôi: **"PI đã phân xử xong 74 dòng"** → tôi sẽ:
1. Ghi kết quả vào cột `adjudicated_decision/reason/adjudicator` của **Ma trận Bất đồng Vòng 2**.
2. Hợp nhất thành danh sách `INCLUDE` cuối cùng Vòng 2 (danh sách đưa vào trích xuất dữ liệu).
