# Trạng thái lượt non-legal dừng kỹ thuật

**Trạng thái:** `FAIL_CLOSED_PARTIAL_RUN_NOT_FOR_COMPLETION`  
**Run ID:** `official-nonlegal-20260731T212700+0700`

Lượt chạy dừng trước khi ghi ledger và manifest cuối vì lỗi ghi `raw/...headers` khi chuyển từ kênh MOH sang MOH-ASTT. Các raw response trước thời điểm dừng được giữ để kiểm toán sự cố, nhưng không được dùng cho provenance, dedup, count PRISMA, screening hoặc kết luận về bất kỳ cổng nào.

Một run mới, với run ID mới và runner đã sửa để bảo đảm thư mục raw đích tồn tại trước mỗi lần ghi, phải thay thế toàn bộ lượt này.
