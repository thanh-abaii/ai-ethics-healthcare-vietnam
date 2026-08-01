# Deviation truy hồi VBPL qua trình duyệt

**Trạng thái:** `RETRIEVAL_TIMEOUT_NO_RAW_RESPONSE`  
**Ngày:** 31/07/2026  
**Locator:** `https://vbpl.vn/TW/Pages/vbpq-van-ban-goc.aspx?ItemID=175587`

Sau khi direct HTTP/curl capture đối với locator VBPL của `55/2025/NĐ-CP` timeout, một lần truy hồi dự phòng bằng trình duyệt thật cũng timeout ở bước điều hướng trước khi có DOM hoặc phản hồi có thể lưu giữ.

Lượt này chỉ xác nhận giới hạn truy cập kỹ thuật qua một bề mặt khác. Không tạo raw source mới, không xác nhận nội dung hoặc hiệu lực của văn bản, không thay đổi đồ thị quan hệ, không thay thế evidence bằng search-engine snippet, và không làm nhánh pháp lý đạt `PASS`.
