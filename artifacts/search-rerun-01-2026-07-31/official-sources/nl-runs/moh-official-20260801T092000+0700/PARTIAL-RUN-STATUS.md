# Trạng thái lượt thu hồi Bộ Y tế bị dừng

**Trạng thái:** `STOPPED_TIMEOUT_HEAVY_PARTIAL_RUN_NOT_FOR_COMPLETION`  
**Phạm vi dự kiến:** bảy kênh Bộ Y tế, 12 query ID đã khóa.  
**Phạm vi đã chạm tới:** chỉ một phần kênh `MOH`; không có ledger hoặc manifest hoàn tất.

Lượt chạy được dừng ngày 01/08/2026 sau khi phần lớn request tới `moh.gov.vn` hết thời gian chờ 15 giây và trước khi hoàn tất toàn bộ các cặp kênh--truy vấn. Các raw body/header/error đã có chỉ được giữ làm bằng chứng vận chuyển kỹ thuật. Chúng không được dùng cho kết quả tìm kiếm, candidate registry, dedup, PRISMA, sàng lọc, trích xuất hay bất kỳ suy luận vắng mặt nào.

Một lượt thay thế phải có chiến lược truy hồi phù hợp riêng cho từng cổng, ledger hoàn chỉnh, kiểm tra ngữ nghĩa phân trang và thu hồi nguồn cấp kết quả theo giới hạn đã khóa.
