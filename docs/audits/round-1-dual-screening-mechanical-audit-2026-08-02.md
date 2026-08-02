# Kiểm toán cơ học và ma trận đối soát vòng 1

**Ngày tạo:** 2026-08-02  
**Phạm vi:** đối soát sau khóa độc lập cho 385 `CANON-*`; báo cáo không tự đưa ra quyết định phân xử mà chỉ ghi nhận quyết định do PI ban hành.

## Kiểm tra đầu vào

- Tập ID của mỗi reviewer khớp Master Input Registry: **PASS** (385/385, không trùng).
- Reviewer/stage/schema/giá trị quyết định: **PASS**.
- `exclusion_reason` ở vòng tiêu đề/tóm tắt: **PASS** (đều trống).
- SHA-256 tệp PI: `adb127e9fac328946d9cac5a2479f17f0ecab0b03b6d0dbcab7e6d0f398252a3` — **PASS**.
- SHA-256 tệp Lộc Đặng: `3252babc45529bffff1c4562e453cd03455838dae1cbdecd79a409b451c69430` — **PASS**.

## Provenance khóa

- PI xác nhận khóa ngày 2026-08-02 tại `docs/governance/pi-round-1-lock-confirmation-2026-08-02.md`.
- Lộc Đặng xác nhận khóa ngày 2026-08-02 tại `docs/governance/loc-dang-round-1-lock-confirmation-2026-08-02.md`.
- Hai biên bản chỉ ghi ngày, không ghi giờ khóa; không suy diễn thêm mốc thời gian.

## Ma trận quyết định

| PI \ Lộc | INCLUDE | EXCLUDE | UNCERTAIN | Tổng |
| --- | ---: | ---: | ---: | ---: |
| INCLUDE | 34 | 1 | 58 | 93 |
| EXCLUDE | 1 | 213 | 16 | 230 |
| UNCERTAIN | 0 | 0 | 62 | 62 |
| Tổng | 35 | 214 | 136 | 385 |

## Đồng thuận và trạng thái kế tiếp

- Đồng thuận quan sát: **309/385 (80.26%)**.
- Cohen's Kappa không trọng số (ba mức `INCLUDE`/`EXCLUDE`/`UNCERTAIN`): **0.6649**. Đây là chỉ số mô tả, không phải hard gate.
- Chuyển toàn văn sàng lọc kép: **96** bản ghi có đồng thuận `INCLUDE` hoặc `UNCERTAIN`.
- Loại đồng thuận tại tiêu đề/tóm tắt: **213** bản ghi; không xóa record hay provenance.
- Giữ nguyên để phân xử: **76** bản ghi với trạng thái `PENDING_ADJUDICATION`.

## Ranh giới thẩm quyền và kết quả phân xử của PI

- Biên bản kiểm toán này được lập sau khi khóa độc lập.
- **Quyết định phân xử của PI:** Ngày 02/08/2026, PI Đào Trung Thành đã trực tiếp xem xét và ra quyết định phân xử chính thức cho toàn bộ 76 bản ghi bất đồng tại [`docs/governance/pi-round-1-adjudication-decision-record-2026-08-02.md`](../governance/pi-round-1-adjudication-decision-record-2026-08-02.md).
- **Kết quả phân xử:**
  - **Loại tại Vòng 1:** 6 bản ghi thuộc Cụm 1 (ngoài phạm vi y tế) theo mã `EX02_NOT_HEALTHCARE`.
  - **Chuyển sang Vòng 2 (Sàng lọc toàn văn kép):** 70 bản ghi thuộc Cụm 2 (ML lâm sàng/dịch tễ) và Cụm 3 (AI y tế & Giáo dục Y khoa) theo nguyên tắc bộ lọc mở rộng Vòng 1.
- **Tổng kết PRISMA-ScR Vòng 1:**
  - Tổng số bản ghi bị loại Vòng 1: **219** (213 đồng thuận + 6 phân xử).
  - Tổng số bản ghi chuyển sang Vòng 2 sàng lọc toàn văn kép: **166** (96 đồng thuận + 70 phân xử).
  - Số bản ghi chờ phân xử: **0**.
  - SHA-256 tệp ma trận đối soát & phân xử đã cập nhật: `178e3ce4f577a9fa4b9370369141ba2c6ba0e8780ea9f1bf6f59a5fef3e9d044`.
