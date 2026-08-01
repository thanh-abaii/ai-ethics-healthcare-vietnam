# Trạng thái lượt chạy không hoàn chỉnh

`FAIL_CLOSED_PARTIAL_CLIENT_TIMEOUT`

Lượt chạy này bị dừng bởi giới hạn thời gian của tiến trình điều phối trước khi sinh `query-ledger.csv` và `run-manifest.json`. Các raw/header đang có chỉ là dấu vết của lần thử; không phải kết quả tìm kiếm hoàn chỉnh, không dùng cho dedup, sàng lọc, PRISMA hay đồ thị pháp lý. Lượt thay thế dùng thời hạn từng request ngắn hơn và run-id riêng, không ghi đè thư mục này.
