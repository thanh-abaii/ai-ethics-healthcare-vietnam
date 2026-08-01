# Lượt chạy hủy trước ledger

**Trạng thái:** `ABORTED_BEFORE_LEDGER_OR_SOURCE_ACQUISITION`  
**Thời điểm:** 2026-08-01  

Các phản hồi thô trực tiếp có thể đã được tạo trước khi trình chạy gặp giới hạn đường dẫn Windows lúc ghi ledger. Vì không có ledger, manifest, checksum inventory hay thu hồi cấp tài liệu hoàn chỉnh, toàn bộ thư mục này không được dùng cho kiểm toán, tổng hợp hay sàng lọc. Runner đã được hiệu chỉnh trước lượt chạy tiếp theo.
