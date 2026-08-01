# Trạng thái lượt chạy dở dang

**Trạng thái:** `INTERRUPTED_NOT_A_COMPLETE_SEARCH_RUN`  
**Thời điểm dừng:** 2026-08-01 (Asia/Ho_Chi_Minh)

Lượt này bị dừng có chủ ý sau khi ghi các HTTP attempt đầu tiên của ba cổng Bộ
Y tế, vì nhiều endpoint không phản hồi trong giới hạn 15 giây. Thư mục `raw/`
chỉ là bằng chứng vận chuyển từng phần; chưa có `completion-status.json`,
`sha256.csv`, danh mục kết quả hay ledger nguồn hoàn chỉnh.

Không được dùng thư mục này để suy ra số nguồn, độ bão hòa, sự vắng mặt của
bằng chứng, hoàn tất tìm kiếm chính thức, hoặc để mở sàng lọc. Có thể kiểm
toán các payload/header đã sinh, nhưng mọi quyết định nghiên cứu phải dùng một
lượt hoàn chỉnh khác hoặc một biện pháp fallback được ghi nhận riêng.
