# Sửa đổi protocol tiền đăng ký PR-03

## Kiểm soát

| Trường | Giá trị |
| --- | --- |
| Mã sửa đổi | `PR-03` |
| Ngày | 31/07/2026 |
| Phiên bản trước | `0.4-pre-registration` |
| Phiên bản sau | `0.5-ready-for-registration` |
| Người phê duyệt | Đào Trung Thành |
| Loại thay đổi | Hành chính về thời điểm khóa; không thay đổi phương pháp |
| Trạng thái dữ liệu tại thời điểm sửa | Chưa đăng ký; G4–G5 chưa chạy; chưa tìm kiếm, sàng lọc hoặc trích xuất chính thức |

## Nội dung sửa đổi

Mốc “không sớm hơn 15/08/2026” được bỏ. Protocol được phép khóa cục bộ ngày 31/07/2026 ngay sau khi mọi dependency tiền đăng ký có bằng chứng đạt yêu cầu. Pilot khả thi G4–G5 vẫn chỉ được mở sau khi gói protocol bất biến đã được đăng ký trên OSF hoặc kho ổn định và locator của bản đăng ký đã được kiểm tra.

## Lý do

Ngày 15/08/2026 là mốc kế hoạch nội bộ, không phải yêu cầu phương pháp hay điều kiện của tạp chí. Đến 31/07/2026, Lộc Đặng đã hoàn tất benchmark độc lập, các cấu phần đã được khóa và những dependency tiền đăng ký còn lại đã có bằng chứng `PASS` hoặc trạng thái không áp dụng đã được giải trình. Tiếp tục chờ theo lịch không làm tăng chất lượng phương pháp.

## Đánh giá ảnh hưởng

Sửa đổi này không thay đổi:

- câu hỏi, mục tiêu hoặc PCC;
- tiêu chí chọn–loại;
- cơ sở dữ liệu, truy vấn hoặc quy trình tìm kiếm;
- codebook, biểu mẫu, đơn vị phân tích hoặc quy tắc tổng hợp;
- bộ chuẩn, mapping cấu phần hoặc quyết định benchmark;
- giới hạn tám trang và 25 tài liệu tham khảo;
- điều kiện G4–G7.

Sửa đổi không hợp thức hóa dữ liệu hậu nghiệm vì chưa chạy G4–G5 và chưa tạo corpus chính thức. Trạng thái đăng ký vẫn là `NOT_REGISTERED` cho đến khi có locator OSF/kho ổn định đã kiểm tra.

## Quyết định

`PR-03=APPROVED_PRE_REGISTRATION`

Cho phép tạo snapshot bất biến và checksum ngày 31/07/2026. Không cho phép chạy G4–G5 trước khi hoàn tất đăng ký và kiểm tra locator.
