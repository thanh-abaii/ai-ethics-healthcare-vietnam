# Lượt kiểm tra truy cập PubMed qua trình duyệt — 31/07/2026

**Run ID:** `official-search-rerun-01-2026-07-31-pubmed-browser-01`  
**Thời điểm:** `2026-07-31T19:46:03+07:00`  
**Mục đích:** thử một đường truy cập thay thế để thực thi truy vấn PubMed nguyên văn đã khóa, sau khi xuất NBIB tự động không tạo được bản ghi thô hợp lệ.

## Thực hiện

- Mở đúng URL PubMed với chuỗi truy vấn lưu tại `query-verbatim.txt`; không thay đổi trường, toán tử, giới hạn ngày hay ngôn ngữ.
- Trình duyệt trả về `net::ERR_BLOCKED_BY_CLIENT` trước khi tải được trang kết quả.
- Không có CAPTCHA, không có đăng nhập, không gửi biểu mẫu, không tải tệp và không thu được count hay bản ghi nào.

## Quyết định fail-closed

Lượt này **không** tạo raw export, record registry, count PRISMA, screening hay extraction. Nó bổ sung bằng chứng độc lập cho trạng thái `FAIL_CLOSED_RAW_EXPORT_UNAVAILABLE` trong `manifest.json`; không thay thế hoặc làm thay đổi protocol/snapshot OSF.

## Điều kiện để chạy tiếp PubMed

Thực hiện lại trong môi trường có thể mở PubMed và xuất NBIB nguyên gốc. Khi đó phải lưu raw NBIB, query/translation hiển thị, timestamp, count, checksum và provenance vào chính thư mục rerun này trước deduplication.
