# Sửa đổi hậu đăng ký hợp nhất v1

| Trường                 | Giá trị                                       |
| ------------------------ | ----------------------------------------------- |
| Mã tài liệu           | `POST_REGISTRATION_AMENDMENT_CONSOLIDATED_V1` |
| Ngày lập               | 2026-08-01                                      |
| Trạng thái             | `PENDING_PI_APPROVAL_AND_OSF_POSTING`         |
| PI dự kiến phê duyệt | Đào Trung Thành                              |
| Đăng ký gốc          | OSF`62b8w`, DOI `10.17605/OSF.IO/62B8W`     |

## Phạm vi và hiệu lực

Đây là tài liệu hậu đăng ký duy nhất dự kiến công bố tại OSF. Nó hợp nhất các
thay đổi về điều kiện trang cuối OpenAlex, catalogue thực thi non-legal và
corpus nguồn công khai Việt Nam. Registration gốc không bị sửa, thay thế hoặc
xóa. Hiệu lực bắt đầu khi Đào Trung Thành phê duyệt và bản này được công bố ở
project OSF liên kết với `62b8w`.

Các thay đổi trước đăng ký đã nằm trong snapshot OSF và không thuộc tài liệu này.

## Lý do cần sửa đổi

Sửa đổi này được lập sau các lượt kiểm tra khả thi kỹ thuật của nhánh thu hồi
nguồn công khai diện rộng. Các lượt đó **không thu hồi đủ một corpus nguồn cấp
tài liệu có thể truy xuất và kiểm toán**: nhiều cổng không trả về HTML/PDF hay
metadata có locator ổn định; catalogue thực thi ban đầu có lỗi escape; và một
lượt Firecrawl chỉ tạo 757 locator, vượt quy mô có thể kiểm toán cho bài giới
hạn 8 trang mà chưa tạo được tập tài liệu nguồn phù hợp. Vì vậy các lượt này
được ghi là partial, interrupted hoặc fail-closed; chúng không là kết quả tìm
kiếm chính thức và không được đưa vào registry hay sàng lọc.

Ngoài ra, việc yêu cầu G6/G7 trước screening tạo vòng lặp logic, vì tính đủ
điều kiện của nguồn Việt Nam chỉ có thể xác định sau screening kép. Sửa đổi
được công bố trước khi mở sàng lọc chính thức; chưa có quyết định sàng lọc,
trích xuất dữ liệu hay tổng hợp nào được thực hiện.

## OpenAlex và catalogue thực thi

Full export OpenAlex hoàn tất khi `next_cursor = null` và kết quả rỗng, hoặc
trang cuối có ít kết quả hơn `per_page` đồng thời tổng ID duy nhất bằng
`meta.count`. Đây là làm rõ kỹ thuật, không đổi truy vấn, thời gian, PCC hay
tiêu chí chọn–loại. Catalogue non-legal được chép lại theo CSV RFC 4180 vì bản
thực thi cũ có ký tự escape thừa; 12 query ID và nội dung strategy không đổi.
Các lượt dùng catalogue lỗi chỉ là audit trail, không là corpus chính thức.

## Corpus nguồn công khai và thứ tự gate

Thu hồi diện rộng qua cổng và sentinel được supersede do không tạo được kết quả
có thể định vị ổn định trong phạm vi bài 8 trang. Corpus công khai thay bằng tối
đa 16 hồ sơ: 4 văn bản pháp lý quốc gia; tối đa 4 tài liệu Bộ Y tế/Bộ Khoa học
và Công nghệ; tối đa 3 tài liệu WHO Việt Nam/UNESCO; và tối đa 5 ví dụ địa
phương/bệnh viện chỉ mang tính mô tả. Mỗi hồ sơ cần URL chính thức, ngày truy
cập, HTML/PDF hoặc metadata không thu hồi được, SHA-256 khi có tệp, thẩm quyền,
phạm vi và provenance. Không dùng báo chí, fanpage hoặc trang kết quả tìm kiếm.

PubMed, OpenAlex và traversal pháp lý vẫn là corpus lõi. Citation chasing chỉ
bắt đầu sau khi nguồn Việt Nam được chọn qua screening kép.

## Readiness trước screening và kiểm tra trình bày sau screening

Trước screening, nhóm chỉ thực hiện **readiness check**: registry đầu vào phải
có provenance/dedup đã kiểm toán; mỗi slot của khung nguồn công khai phải có
một kết quả truy hồi được ghi nhận; và calibration/codebook phải còn hiệu lực.
Readiness check không đánh giá nguồn nào “đủ điều kiện”, không dự đoán kết quả
và không dùng ngân sách trang hay số tài liệu tham khảo để loại record. Nếu
readiness chưa đạt, nhóm chỉ được hoàn thiện việc ghi nhận/truy hồi theo khung
đã công bố; mọi thay đổi về PCC, tiêu chí hoặc khung nguồn cần được công bố
bằng sửa đổi mới trước screening.

G6/G7 được thay thế về mặt vận hành bằng **kiểm tra khả năng trình bày bản
thảo** sau khi screening toàn văn đã khóa và trước khi hoàn thiện bản thảo nộp
tạp chí. Kiểm tra này dùng pool thực tế đã sàng lọc để đánh giá cách báo cáo
trung thực trong giới hạn 8 trang/25 tài liệu tham khảo. Kết quả chỉ được ghi
`ADEQUATE` hoặc `CONSTRAINED`, không phải `PASS/FAIL` của nghiên cứu và không
thể làm thay đổi corpus, tiêu chí inclusion/exclusion, quyết định screening hay
quy tắc citation chasing.

Lý do của thay đổi này là tính đủ điều kiện và mức độ đa dạng của bằng chứng
chỉ có thể biết sau khi áp dụng cùng một tiêu chí screening cho toàn bộ pool.
Đặt khả năng trình bày bản thảo làm gate trước screening sẽ dùng một dự đoán về
bằng chứng để kiểm soát chính bằng chứng đó. Hai việc vì thế được tách biệt:
phương pháp quyết định corpus; giới hạn của tạp chí chỉ quyết định cách trình
bày corpus đã được xác định.

Khi kết quả là `CONSTRAINED`, nhóm bảo toàn pool đã sàng lọc và chọn cách báo
cáo phù hợp: rút gọn bảng trong thân bài, sử dụng phụ lục nếu tạp chí cho phép,
hoặc chọn tạp chí khác. Không được tìm thêm, loại bớt hoặc tái phân loại nguồn
chỉ để làm bài vừa giới hạn trình bày.

## Điều không thay đổi và minh bạch

PCC, tiêu chí inclusion/exclusion, screening kép độc lập, codebook, dedup,
phương pháp tổng hợp, PRISMA-ScR, giới hạn 8 trang, trần 25 tài liệu tham khảo
và công khai sai lệch vẫn giữ nguyên. Bài báo và OSF sẽ nêu ngày hiệu lực và
các run đã supersede; không suy diễn tình trạng toàn quốc từ sự vắng mặt trong
corpus hữu hạn.
