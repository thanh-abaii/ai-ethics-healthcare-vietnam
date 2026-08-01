# Trạng thái lượt chạy không hoàn chỉnh

`FAIL_CLOSED_PARTIAL_CLIENT_PATH_LIMIT`

Lượt chạy này dừng khi tên tệp header cho query ID dài vượt giới hạn đường dẫn của Windows. Mười ba tệp raw đã ghi là bằng chứng lỗi kỹ thuật, không phải tập kết quả tìm kiếm và không được dùng cho dedup, sàng lọc, PRISMA hay đồ thị pháp lý. Script đã được sửa để dùng mã query ngắn; lượt thay thế có run-id riêng, không ghi đè thư mục này.
