# Nhánh hiệu chuẩn độc lập của Lộc Đặng — 31/07/2026

**Trạng thái:** `PARTIAL_COMPLETED_AWAITING_SECOND_REVIEWER_AND_FULL_TEXT`  
**Loại hoạt động:** `PRE_REGISTRATION_SEARCH_DEVELOPMENT` — field-test công cụ; không phải pilot G4–G5, không tạo corpus, PRISMA count, registry nghiên cứu hay quyết định đủ điều kiện chính thức.  
**Reviewer:** `LOC_DANG`  
**Protocol:** `0.3-pre-registration`  
**Screening codebook:** `0.1-draft`  
**Extraction codebook:** `0.1-draft`

## Mẫu title/abstract

- Pool: 25 record trong `openalex-validation-derived-abstract.csv`, là toàn bộ pool hiện có nên không cần rút mẫu con.
- Seed kiểm tra tái lập: `LOC-G5-CAL-20260731-OPENALEX-25`.
- Đầu vào được đóng tại checksum đã có trong artifact validation OpenAlex; không thêm record từ tìm kiếm mới.
- Quyết định ban đầu độc lập của Lộc nằm tại [`calibration-2026-07-31-loc-dang-title-abstract.csv`](calibration-2026-07-31-loc-dang-title-abstract.csv).

| Kết quả nhánh Lộc | Số record |
| --- | ---: |
| `EXCLUDE` | 10 |
| `UNCERTAIN` chuyển kiểm tra toàn văn | 15 |
| `INCLUDE` ở title/abstract | 0 |

Không có record nào bị loại với mã exclusion ở title/abstract: theo codebook, mã loại chuẩn hóa chỉ ghi ở bước toàn văn. Các ghi chú cho biết căn cứ tạm thời, để reviewer còn lại có thể đối chiếu mà không thay thế audit trail.

## Giới hạn và bước tiếp theo bắt buộc

Nhánh này mới là quyết định độc lập của Lộc ở bước 1/3 của hiệu chuẩn. Nó **không** đủ để tính đồng thuận ban đầu, kappa mô tả, phân xử, khóa codebook hay chuyển `SCREENING_EXTRACTION_CODEBOOK_GATE` sang `PASS`, vì chưa có:

1. quyết định title/abstract độc lập, đã khóa, của `DAO_TRUNG_THANH` để đối chiếu 25 record;
2. mẫu 8 document toàn văn đa dạng và hai nhánh quyết định toàn văn độc lập;
3. trích xuất độc lập 8 document của cả hai reviewer, trong đó nhánh `inductive_code` của Lộc phải hoàn tất trước khi mở `chapter10_only_code`;
4. log bất đồng, kết quả thảo luận/phân xử và kiểm tra xem sửa codebook có ảnh hưởng quyết định hay không.

Vì protocol chưa đăng ký và các gate tiền đăng ký khác vẫn mở, **G5 vẫn là `NOT_RUN`**. Khi hiệu chuẩn hoàn tất, bước kế tiếp vẫn là hoàn tất các dependency, khóa/đăng ký protocol rồi mới được chạy pilot khả thi G4–G5; không được dùng 25 record này làm tập G5.
