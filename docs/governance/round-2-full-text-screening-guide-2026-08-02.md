# Hướng dẫn PI và Lộc Đặng điền biểu mẫu screening vòng 2

**Vòng đang thực hiện:** Sàng lọc toàn văn kép độc lập Vòng 2 (Round 2 Full-Text Dual Screening)
**Corpus:** 166 record `CANON-*` đã được chốt chuyển sang Vòng 2 theo `round-1-adjudication-matrix-2026-08-02.csv`
**Sổ cái tra cứu toàn văn:** `docs/audits/round-2-full-text-retrieval-ledger-2026-08-02.csv`
**Codebook áp dụng:** `screening-codebook.md` phiên bản frozen `0.1-draft`

---

## 1. Phân tách tệp độc lập

Mỗi reviewer làm việc độc lập trên đúng tệp của mình, không xem, chia sẻ hay sao chép kết quả của nhau trước khi cả hai bấm khóa tệp:

| Người rà soát | Tệp biểu mẫu Vòng 2 được dùng |
| --- | --- |
| Đào Trung Thành | `docs/governance/round-2-full-text-dao-trung-thanh-2026-08-02.csv` |
| Lộc Đặng | `docs/governance/round-2-full-text-loc-dang-2026-08-02.csv` |

---

## 2. Cách điền từng dòng

**KHÔNG** sửa các cột cố định: `record_id`, `stage` (`FULL_TEXT`), `reviewer`.
Đối với mỗi record, reviewer điền đúng các cột sau:

| Cột | Quy định điền ở Vòng 2 |
| --- | --- |
| `inclusion_decision` | Chọn **đúng một** trong hai giá trị: `INCLUDE` hoặc `EXCLUDE`. |
| `exclusion_reason` | - Nếu `INCLUDE`: **Bắt buộc để trống**.<br>- Nếu `EXCLUDE`: **Bắt buộc chọn đúng 1 mã chuẩn hóa** từ `EX01` đến `EX09`. |
| `notes` | Nhận xét ngắn về căn cứ toàn văn/locator nếu cần (không bắt buộc). |
| `date` | Ngày ra quyết định theo định dạng `YYYY-MM-DD` (ví dụ `2026-08-02`). |

---

## 3. Quy tắc chọn quyết định và mã lý do loại

### A. Quyết định `INCLUDE`
- Chọn khi sau khi rà soát toàn văn (file PDF, văn bản quy phạm pháp luật, báo cáo...), tài liệu đáp ứng đủ tiêu chí PCC:
  - Trực tiếp liên quan đến **AI/machine learning/GenAI**;
  - Áp dụng trong bối cảnh **y tế/chăm sóc sức khỏe** tại **Việt Nam**;
  - Có nội dung có thể kiểm chứng về **đạo đức/quản trị** (nguyên tắc, trách nhiệm pháp lý, giám sát, quyền bệnh nhân, kiểm soát an toàn...).
- Cột `exclusion_reason` phải **để trống**.

### B. Quyết định `EXCLUDE` & Mã loại chuẩn hóa (`EX01`–`EX09`)
Nếu toàn văn không đáp ứng đủ tiêu chí, chọn `EXCLUDE` và ghi **đúng 1 mã** sau vào cột `exclusion_reason`:

| Mã chuẩn | Lý do | Quy tắc áp dụng tại Vòng 2 |
| --- | --- | --- |
| `EX01_NOT_VIETNAM` | Không thuộc Việt Nam | Không có phân tích, bối cảnh hay khả năng áp dụng trực tiếp cho Việt Nam. |
| `EX02_NOT_HEALTHCARE` | Không thuộc y tế | Thuộc lĩnh vực khác, không liên quan y tế/chăm sóc sức khỏe/bệnh viện. |
| `EX03_NO_AI` | Không đề cập AI | Chỉ là số hóa/phần mềm thông thường, không chứa AI/ML/GenAI. |
| `EX04_NO_ETHICS_GOVERNANCE` | Không có đạo đức/quản trị | Bài thuần hiệu năng kỹ thuật/thuật toán, không bàn về quản trị hay đạo đức. |
| `EX05_WRONG_SOURCE_TYPE` | Sai loại nguồn | Tin tức, tiếp thị, bình luận không xác minh được tác giả hay cơ quan. |
| `EX06_DATE_OUTSIDE_NO_LEGAL_EXCEPTION` | Ngoài mốc thời gian | Xuất bản trước 2019 và không phải văn bản pháp lý còn hiệu lực/ngoại lệ nền tảng. |
| `EX07_DUPLICATE_NO_NEW_DATA` | Trùng lặp/không thêm dữ liệu | Bản sao hoặc bản thứ cấp không bổ sung dữ liệu mới. |
| `EX08_FULL_TEXT_UNAVAILABLE` | Không tìm được toàn văn | Chỉ dùng sau khi đã áp dụng đủ quy trình nỗ lực truy hồi theo protocol mà vẫn không có toàn văn. |
| `EX09_WRONG_LANGUAGE` | Sai ngôn ngữ | Toàn văn không phải tiếng Việt/Anh và không có bản dịch tin cậy. |

---

## 4. Những việc KHÔNG làm ở Vòng 2

- **Không dùng `UNCERTAIN`:** Vòng 2 bắt buộc phải chốt `INCLUDE` hoặc `EXCLUDE`.
- **Không dùng `PENDING_ADJUDICATION`:** Đây không phải giá trị điền ban đầu của reviewer cá nhân.
- **Không tự tạo mã lý do mới:** Chỉ dùng đúng 9 mã từ `EX01` đến `EX09`.
- **Không trao đổi/chia sẻ quyết định:** Tránh làm ảnh hưởng tính độc lập giữa hai reviewer.
- **Không sửa tệp nguồn:** Không sửa `protocol.md`, codebook hay các tệp frozen OSF.
- **Không dùng tiêu chí trình bày:** Không dùng số trang (ví dụ giới hạn 8 trang) hay số lượng tài liệu tham khảo để loại bài.

---

## 5. Ví dụ minh họa cách điền

| Tình huống rà soát toàn văn | `inclusion_decision` | `exclusion_reason` | `notes` |
| --- | --- | --- | --- |
| Văn bản hướng dẫn triển khai AI y tế có phần quy định trách nhiệm bệnh viện tại Việt Nam | `INCLUDE` | *(trống)* | `Có quy định quản trị y tế ở mục 3.` |
| Bài nghiên cứu AI y tế tại Việt Nam nhưng toàn văn chỉ đo độ chính xác AUC, hoàn toàn không có nội dung đạo đức/quản trị | `EXCLUDE` | `EX04_NO_ETHICS_GOVERNANCE` | `Chỉ báo cáo hiệu năng kỹ thuật.` |
| Báo cáo AI y tế tại Thái Lan, không có dữ liệu hay bối cảnh Việt Nam | `EXCLUDE` | `EX01_NOT_VIETNAM` | `Ngoài phạm vi địa lý.` |
| Không thu hồi được file toàn văn sau khi đã tìm kiếm qua tất cả kênh | `EXCLUDE` | `EX08_FULL_TEXT_UNAVAILABLE` | `Đã hoàn tất nỗ lực tìm kiếm nhưng không có tệp.` |

---

## 6. Quy trình hoàn tất & xác nhận khóa

1. Đảm bảo toàn bộ **166 dòng** trong tệp cá nhân đều đã điền đầy đủ `inclusion_decision`, `exclusion_reason` (nếu `EXCLUDE`) và `date`.
2. Lưu tệp và kiểm tra mã checksum SHA-256.
3. Thông báo cho Agent: `“Tôi, [Đào Trung Thành / Lộc Đặng], đã hoàn tất và khóa Vòng 2.”`
4. Agent sẽ thực hiện kiểm tra cơ học (Mechanical Audit). Sau khi **cả hai reviewer đều bấm khóa**, Agent mới tiến hành lập Ma trận Bất đồng Vòng 2 để PI phân xử.
