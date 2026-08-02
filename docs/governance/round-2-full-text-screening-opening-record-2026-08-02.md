# Biên bản mở screening vòng 2: toàn văn kép độc lập

**Ngày mở:** 2026-08-02
**Căn cứ mở:** `SCREENING = ROUND_1_ADJUDICATION_COMPLETE_2026-08-02`; ma trận phân xử Vòng 1 do PI phê duyệt.
**Corpus:** 166 `CANON-*` có `next_workflow_status=ADVANCE_TO_FULL_TEXT_DUAL_SCREENING` trong `round-1-adjudication-matrix-2026-08-02.csv`.
**Trạng thái:** `ROUND_2_FULL_TEXT_DUAL_SCREENING_OPEN`

## Biểu mẫu đã tạo

| Reviewer | Tệp | Dòng dữ liệu | Quyết định/lý do/ghi chú/ngày tiền điền | SHA-256 |
| --- | --- | ---: | ---: | --- |
| `DAO_TRUNG_THANH` | `round-2-full-text-dao-trung-thanh-2026-08-02.csv` | 166 | 0 | `5a6823392add514e13439732def8ae676f1f0f81f26fb96a86cf47bb65384f45` |
| `LOC_DANG` | `round-2-full-text-loc-dang-2026-08-02.csv` | 166 | 0 | `aa9390ba260d36fa9ead02ef9ef301960acb9b25241e625b4d1a585327b458f0` |

Mỗi tệp có cùng tập 166 `record_id`, không trùng ID, `stage=FULL_TEXT`, đúng một reviewer theo codebook và các cột `inclusion_decision`, `exclusion_reason`, `notes`, `date` đều trống khi mở.

## Xác minh đầu vào

- SHA-256 ma trận nguồn: `178e3ce4f577a9fa4b9370369141ba2c6ba0e8780ea9f1bf6f59a5fef3e9d044` — khớp biên bản phân xử Vòng 1.
- Tập chuyển toàn văn được trích cơ học từ `next_workflow_status=ADVANCE_TO_FULL_TEXT_DUAL_SCREENING`; không dùng quyết định nguyên gốc Vòng 1 để điền vào biểu mẫu mới.
- Chưa tạo, suy đoán hoặc gợi ý bất kỳ quyết định Vòng 2 nào. Không mở citation chasing.

## Quy tắc vận hành

1. PI và Lộc Đặng chỉ làm việc trên biểu mẫu của mình; không xem, sao chép hoặc đối chiếu quyết định của nhau trước khi cả hai xác nhận khóa.
2. Vòng 2 chỉ dùng `INCLUDE` hoặc `EXCLUDE`. Mỗi `EXCLUDE` có đúng một mã `EX01`–`EX09`; `INCLUDE` để trống `exclusion_reason`.
3. `EX08_FULL_TEXT_UNAVAILABLE` chỉ được dùng sau khi hoàn tất quy trình truy hồi toàn văn; locator, ngày truy hồi, nguồn và SHA-256 (nếu có tệp) phải được lưu trong artifact hậu đăng ký.
4. Sau hai xác nhận khóa độc lập, mới kiểm tra cơ học tập ID, schema, giá trị, lý do loại, provenance và checksum; mọi bất đồng được giữ nguyên để PI/cơ chế đã đăng ký phân xử.

Biên bản này không thay đổi `protocol.md`, codebook hoặc bất kỳ tệp snapshot OSF đã đóng băng nào.
