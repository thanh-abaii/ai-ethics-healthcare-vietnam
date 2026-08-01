# Hướng dẫn PI và Lộc Đặng điền biểu mẫu screening vòng 1

**Vòng đang thực hiện:** Screening tiêu đề/tóm tắt kép độc lập  
**Corpus:** 385 `CANON-*`  
**Codebook áp dụng:** `screening-codebook.md` phiên bản frozen `0.1-draft`

## 1. Mỗi người dùng đúng một tệp

| Người rà soát | Tệp được dùng |
| --- | --- |
| Đào Trung Thành | `round-1-title-abstract-dao-trung-thanh-2026-08-02.csv` |
| Lộc Đặng | `round-1-title-abstract-loc-dang-2026-08-02.csv` |

Không xem, gửi, so sánh hay sao chép cột quyết định của người kia trước khi cả hai đã hoàn tất và khóa tệp.

## 2. Cách điền từng dòng

Không sửa `record_id`, `stage`, `reviewer`, `source_type` hoặc phần tiêu đề/nguồn trong `notes`. Với mỗi record, chỉ điền các cột sau:

| Cột | Cách điền ở vòng 1 |
| --- | --- |
| `inclusion_decision` | Ghi đúng một trong: `INCLUDE`, `EXCLUDE`, `UNCERTAIN`. |
| `exclusion_reason` | **Để trống** ở vòng tiêu đề/tóm tắt. |
| `notes` | Có thể thêm nhận xét ngắn sau nội dung có sẵn, ví dụ: `| Abstract thiếu; chuyển toàn văn`. Không xóa title/source có sẵn. |
| `date` | Ngày tự ra quyết định theo `YYYY-MM-DD`, ví dụ `2026-08-02`. |

## 3. Quy tắc chọn quyết định

### `INCLUDE`

Chọn khi tiêu đề/tóm tắt cho thấy khá rõ nguồn có thể đáp ứng: liên quan AI, y tế, Việt Nam và có nội dung về đạo đức/quản trị (nguyên tắc, trách nhiệm, kiểm soát, giám sát, quyền người bệnh, bằng chứng trách nhiệm…). Record sẽ đi tiếp vòng toàn văn.

### `EXCLUDE`

Chỉ chọn khi có căn cứ **chắc chắn** ngay từ tiêu đề/tóm tắt rằng nguồn nằm ngoài phạm vi, chẳng hạn bài hoàn toàn về AI kỹ thuật không có y tế hay quản trị/đạo đức; hoàn toàn không liên quan Việt Nam; hoặc rõ là tin tức/tiếp thị không xác minh được nguồn gốc.

Không ghi mã `EX01`–`EX09` ở vòng này. Mã lý do loại được chốt ở screening toàn văn.

### `UNCERTAIN`

Chọn khi thiếu abstract, mô tả chưa đủ, có khả năng áp dụng tại Việt Nam nhưng chưa rõ, hoặc có dấu hiệu nội dung quản trị/đạo đức cần đọc toàn văn mới xác định. Khi phân vân giữa `EXCLUDE` và `UNCERTAIN`, chọn `UNCERTAIN`.

## 4. Những việc không làm ở vòng 1

- Không dùng `PENDING_ADJUDICATION`: đây không phải quyết định cá nhân ban đầu.
- Không dùng `EX08_FULL_TEXT_UNAVAILABLE` hoặc `EX09_WRONG_LANGUAGE`.
- Không tìm toàn văn, citation chasing, trích xuất hay adjudication trong lúc điền vòng 1.
- Không xóa record, thay ID, gộp trùng hoặc sửa provenance.
- Không dùng giới hạn 8 trang/25 tài liệu tham khảo để quyết định.

## 5. Ví dụ minh họa cách điền

| Tình huống | `inclusion_decision` | `exclusion_reason` | `notes` gợi ý |
| --- | --- | --- | --- |
| Hướng dẫn bệnh viện Việt Nam nêu phê duyệt và giám sát AI | `INCLUDE` | *(trống)* | `Có kiểm soát quản trị; chuyển toàn văn.` |
| Bài dự báo lũ bằng ML, không có y tế hay Việt Nam | `EXCLUDE` | *(trống)* | `Ngoài PCC, căn cứ rõ từ title/abstract.` |
| Bài về AI y tế tại Việt Nam nhưng abstract không nói rõ governance | `UNCERTAIN` | *(trống)* | `Cần toàn văn xác định nội dung governance.` |

## 6. Khi hoàn tất tệp cá nhân

1. Kiểm tra 385 dòng đều có `INCLUDE`, `EXCLUDE` hoặc `UNCERTAIN` và có ngày.
2. Lưu tệp, không sửa tiếp.
3. Báo Agent: “Tôi, [tên reviewer], đã khóa vòng 1.”
4. Agent chỉ khi đó mới kiểm tra schema/checksum tệp của người đó. Agent không so sánh quyết định hai người cho đến khi có xác nhận khóa của **cả hai**.

Sau khi cả hai khóa, Agent lập bảng đối chiếu. Bất đồng được giữ nguyên để PI/cơ chế phân xử xử lý; không ai được ghi đè quyết định gốc.
