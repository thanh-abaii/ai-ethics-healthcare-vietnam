# Trạng thái lượt chạy không hoàn chỉnh

`FAIL_CLOSED_PARTIAL_CLIENT_TIMEOUT`

Lượt chạy bị dừng bởi giới hạn thời gian của tiến trình điều phối trước khi hoàn tất ledger/manifest. Các raw/header hiện diện chỉ lưu dấu sự cố truy cập; không được dùng cho dedup, sàng lọc, PRISMA hoặc đồ thị pháp lý. Lượt thay thế rút ngắn theo cổng sau lỗi truy cập đầu tiên và có run-id riêng.
