# Kiểm toán lượt thu hồi non-legal 2026-08-01

## Kết luận

**`FAIL_CLOSED_NO_DOCUMENT_LEVEL_SOURCE_RETRIEVED`**. Không thể công nhận đây là lượt thu hồi non-legal hoàn chỉnh theo protocol.

## Bằng chứng đã kiểm tra

- Run: `official-nonlegal-complete-20260801T112500`.
- 120/120 cặp kênh–query đã được thử ở cổng nội bộ; 240 response raw đã lưu.
- Vì parser không nhận được URL kết quả có ngữ nghĩa, 120/120 cặp đã đi qua fallback `site:`; 240 response raw đã lưu.
- Không có URL nguồn chính thức nào được parser chấp nhận, nên source acquisition = 0 và traversal tầng 2 = 0.
- `sha256.csv` bao phủ 2 manifest/ledger đầu ra tồn tại tại thời điểm đóng run và 2/2 hash đã đối chiếu đúng. Nó không biến việc không có source thành thành công.

## Khiếm khuyết đã phát hiện và xử lý

Nhãn trong `completion-status.json` đã gọi sai trạng thái là hoàn tất thu hồi cấp tài liệu. Điều kiện runner đã được sửa: các lượt sau chỉ có thể dùng nhãn này khi có ít nhất một record nguồn đã thu. Với lượt hiện tại, `RETRACTION_OF_COMPLETION_CLAIM.md` là diễn giải hậu kiểm bắt buộc.

## Hệ quả gate

Không có thay đổi đối với `DIRECT_SEARCH_IN_PROGRESS`, G6, G7 hay `SCREENING = NOT_OPEN`. Cần sửa/đổi bộ locator có thể giải mã kết quả `site:` và kiểm toán nghĩa của kết quả từng cổng trước khi chạy lại; không thay query catalogue đã khóa.
