# Codebook sàng lọc

**Trạng thái:** `PASS_CALIBRATED_PRE_REGISTRATION`  
**Phiên bản:** `0.1-draft`  
**Phạm vi:** tập nguồn trực tiếp về đạo đức và quản trị AI trong y tế Việt Nam theo `protocol.md` phiên bản `0.6-registered`; nội dung phương pháp được kế thừa không đổi từ `0.4-pre-registration` theo `PR-03` và được ghi nhận đăng ký tại `PR-04`.

Registry liên kết: `record-registry-codebook.md` và `record-registry-template.csv`. Mọi quyết định độc lập/phân xử được thêm như event mới; biểu mẫu sàng lọc không được dùng để ghi đè alias, provenance hoặc quyết định trước.

Tài liệu này đã được ghi nhận hiệu chuẩn ngày 31/07/2026 theo [`calibration-attestation-2026-07-31.md`](calibration-attestation-2026-07-31.md). Lộc Đặng là người rà soát/mã hóa độc lập, G2=`PASS`. Đào Trung Thành là người chủ trì. Trạng thái này không xác nhận G4/G5, corpus, count PRISMA hoặc sàng lọc chính thức.

## Đơn vị, phạm vi và trạng thái biểu mẫu

Mỗi dòng `screening-form.csv` là một `record_id × reviewer × stage`: một quyết định độc lập của một người tại một giai đoạn. `record_id` được giữ xuyên suốt registry chung; khử trùng lặp toàn cục diễn ra trước sàng lọc. `stage` dùng `TITLE_ABSTRACT` hoặc `FULL_TEXT`; `decision` dùng `INCLUDE`, `EXCLUDE`, `UNCERTAIN`, `DUPLICATE_LINKED` hoặc `PENDING_ADJUDICATION`.

- `TITLE_ABSTRACT`: chỉ loại khi có căn cứ chắc chắn; thiếu tóm tắt hoặc chưa đủ rõ chuyển `UNCERTAIN` sang toàn văn.
- `FULL_TEXT`: quyết định đủ điều kiện cuối chỉ được chốt sau hai quyết định độc lập và phân xử nếu cần.
- `exclusion_reason`: để trống với `INCLUDE`, `UNCERTAIN`, `DUPLICATE_LINKED` và `PENDING_ADJUDICATION`; với `EXCLUDE` ở toàn văn, ghi đúng một mã chính. Có thể nêu căn cứ phụ trong `notes`, không tạo mã mới.
- `date`: ISO 8601 `YYYY-MM-DD`; `notes` ghi locator ngắn, phiên bản và lý do suy luận, không ghi dữ liệu nhạy cảm.

`source_type` là mô tả sơ bộ, một trong `LEGAL_REGULATION`, `OFFICIAL_GUIDANCE_POLICY`, `ACADEMIC_STUDY`, `OFFICIAL_REPORT`, `GREY_REPORT`, `OTHER_UNCLEAR`. Đây không thay thế `source_tier` ở trích xuất. Không dùng biểu mẫu để đưa nguồn nền ngoài tập PRISMA vào tập chính.

## Tiêu chí thao tác

Đưa vào khi nguồn có thể kiểm chứng, tiếng Việt/Anh, trực tiếp đề cập ít nhất một nguyên tắc, trách nhiệm, kiểm soát hoặc bằng chứng đạo đức/quản trị AI trong y tế Việt Nam. Nghiên cứu, báo cáo và hướng dẫn mới phải từ `2019-01-01`; văn bản pháp luật/quy định/hướng dẫn chính thức còn hiệu lực được xét bất kể năm ban hành. Bản gốc trước 2019 chỉ là ngoại lệ nền tảng khi một nguồn đủ điều kiện xác định nó là văn bản gốc và ngoại lệ đã được ghi trong protocol.

Không đưa vào bài hiệu năng thuần kỹ thuật; nội dung AI chung không có khả năng áp dụng trực tiếp cho y tế Việt Nam; tin tức/tiếp thị/bình luận không xác định được tác giả hoặc cơ quan; hay bản trùng/bản thứ cấp không đóng góp dữ liệu.

### Ví dụ hiệu chuẩn tiêu chí đủ điều kiện

| Nhóm tiêu chí quyết định | Ví dụ dương tính — đưa vào/chuyển toàn văn | Ví dụ âm tính — loại | Ca biên — cách xử lý |
| --- | --- | --- | --- |
| PCC — Việt Nam | Nghiên cứu phân tích trách nhiệm khi triển khai AI tại bệnh viện Việt Nam. | Nghiên cứu AI y tế chỉ tại Thái Lan, không có phân tích hay khả năng áp dụng trực tiếp cho Việt Nam (`EX01_NOT_VIETNAM`). | Nghiên cứu đa quốc gia có dữ liệu Việt Nam chưa tách rõ: chuyển toàn văn; chỉ đưa vào khi trích được nội dung Việt Nam hoặc áp dụng trực tiếp, nếu không dùng `EX01_NOT_VIETNAM`. |
| PCC — y tế | Hướng dẫn quản trị AI dành cho bệnh viện hoặc hệ thống y tế Việt Nam. | Khung AI cho thương mại điện tử Việt Nam, không có bối cảnh y tế (`EX02_NOT_HEALTHCARE`). | Chính sách AI đa ngành có điều khoản áp dụng trực tiếp cho y tế: chuyển toàn văn và chỉ mã hóa phạm vi y tế. |
| PCC — AI | Văn bản quy định hệ thống AI/ML/GenAI dùng trong chẩn đoán, điều trị hoặc quản lý y tế. | Văn bản chỉ về số hóa hồ sơ bệnh án, không đề cập AI (`EX03_NO_AI`). | Nguồn dùng tên sản phẩm/“thuật toán thông minh” nhưng chưa rõ là AI: `UNCERTAIN`, kiểm tra phương pháp/toàn văn trước khi quyết định. |
| Concept — đạo đức/quản trị | Nguồn nêu actor, quyền phê duyệt, giám sát, quyền người bệnh hoặc hồ sơ trách nhiệm cho AI y tế. | Bài chỉ báo cáo AUC/độ chính xác, không có nội dung quản trị (`EX04_NO_ETHICS_GOVERNANCE`). | Bài hiệu năng có thêm đánh giá công bằng hoặc giám sát sau triển khai: chuyển toàn văn; chỉ đưa vào nếu phần đó đủ nội dung trực tiếp. |
| Ngôn ngữ | Toàn văn tiếng Việt, tiếng Anh hoặc bản song ngữ có thể kiểm chứng. | Toàn văn chỉ bằng ngôn ngữ khác ngoài phạm vi protocol và không có bản dịch tiếng Việt/Anh đủ tin cậy sau quy trình tìm toàn văn: loại ở toàn văn bằng `EX09_WRONG_LANGUAGE`. | Metadata chưa rõ ngôn ngữ hoặc có bản dịch Việt/Anh nhưng khả năng sử dụng chưa chắc chắn: `UNCERTAIN`/`PENDING_ADJUDICATION` đến khi xác minh. Metadata tiếng Anh nhưng toàn văn tiếng Việt thì dùng ngôn ngữ toàn văn và không loại. |
| Thời gian/ngoại lệ pháp lý | Nghiên cứu năm 2021 hoặc văn bản pháp luật năm 2017 còn hiệu lực tại ngày tìm. | Báo cáo năm 2018, không còn hiệu lực và không thuộc ngoại lệ nền tảng (`EX06_DATE_OUTSIDE_NO_LEGAL_EXCEPTION`). | Văn bản trước 2019 được nguồn đủ điều kiện xác định là văn bản gốc: chỉ dùng theo ngoại lệ đã ghi trong protocol/audit trail, không tự động đưa vào tập chính. |
| Loại nguồn/thẩm quyền | Luật, hướng dẫn chính thức, nghiên cứu bình duyệt hoặc báo cáo triển khai có tác giả/cơ quan và thời điểm kiểm chứng được. | Tin quảng cáo của nhà cung cấp hoặc bài báo phổ thông không có tài liệu gốc (`EX05_WRONG_SOURCE_TYPE`). | Thông cáo báo chí của bệnh viện dẫn một báo cáo kỹ thuật: truy báo cáo gốc; thông cáo chỉ là locator, không tự trở thành nguồn đủ điều kiện nếu thiếu nội dung kiểm chứng. |
| Trùng lặp/phiên bản | Bản sửa đổi hiện hành có thay đổi nghĩa vụ hoặc dữ liệu so với bản trước: giữ document riêng và liên kết cùng framework. | Bản HTML/PDF giống hệt hoặc bản thứ cấp không thêm dữ liệu (`EX07_DUPLICATE_NO_NEW_DATA`). | Bản cũ cần để xác định thay đổi ảnh hưởng kết quả: giữ có lý do và liên kết version; không đếm lặp cấu phần. |
| Khả năng truy cập toàn văn | Toàn văn/ảnh Công báo có locator đủ để hai reviewer kiểm tra. | Không tìm được toàn văn sau toàn bộ quy trình truy cập đã khóa (`EX08_FULL_TEXT_UNAVAILABLE`). | Có abstract hoặc mục lục nhưng thiếu phần quyết định: không loại sớm; hoàn tất quy trình tìm toàn văn, sau đó mới dùng `EX08_FULL_TEXT_UNAVAILABLE` nếu vẫn thiếu. |

## Mã lý do loại chuẩn hóa

| Mã ổn định | Lý do | Quy tắc dùng |
| --- | --- | --- |
| `EX01_NOT_VIETNAM` | Không thuộc Việt Nam | Không có bối cảnh, phân tích hoặc khả năng áp dụng trực tiếp cho y tế Việt Nam. |
| `EX02_NOT_HEALTHCARE` | Không thuộc y tế | Không thuộc y học, chăm sóc sức khỏe, bệnh viện hay hệ thống y tế. |
| `EX03_NO_AI` | Không đề cập AI | Không có AI/machine learning/GenAI hay công nghệ tương đương theo protocol. |
| `EX04_NO_ETHICS_GOVERNANCE` | Không có nội dung đạo đức/quản trị | Chỉ nói hiệu năng/kỹ thuật, không có nguyên tắc, trách nhiệm, kiểm soát hay bằng chứng liên quan. |
| `EX05_WRONG_SOURCE_TYPE` | Sai loại nguồn | Tin tức, tiếp thị, bình luận phổ thông hoặc không xác minh được tác giả/cơ quan. |
| `EX06_DATE_OUTSIDE_NO_LEGAL_EXCEPTION` | Ngoài thời gian, không thuộc ngoại lệ pháp lý | Trước 2019 và không phải văn bản còn hiệu lực/ngoại lệ nền tảng được ghi nhận. |
| `EX07_DUPLICATE_NO_NEW_DATA` | Trùng lặp/phiên bản không đóng góp dữ liệu | Bản sao hoặc phiên bản thứ cấp không thêm dữ liệu; liên kết `record_id`/`document_id` chính trong `notes`. |
| `EX08_FULL_TEXT_UNAVAILABLE` | Không truy cập được toàn văn | Chỉ sau quy trình tìm toàn văn theo protocol đã hoàn tất; không dùng tại tiêu đề/tóm tắt. |
| `EX09_WRONG_LANGUAGE` | Sai ngôn ngữ | Toàn văn không phải tiếng Việt/Anh và không có bản dịch Việt/Anh đủ tin cậy sau quy trình tìm toàn văn; chỉ dùng ở toàn văn. Ca chưa rõ ngôn ngữ hoặc khả năng dùng bản dịch vẫn để `UNCERTAIN`/`PENDING_ADJUDICATION`. |

`EX09_WRONG_LANGUAGE` được thêm bằng sửa đổi tiền đăng ký `PR-01` ngày 31/07/2026 để sửa thiếu sót giữa tiêu chí ngôn ngữ đã khóa và danh mục lý do loại. Sửa đổi diễn ra khi chưa đăng ký, chưa pilot G4–G5, chưa tìm kiếm hay sàng lọc chính thức; vì vậy đây không phải lý do loại tạo hậu nghiệm sau khi biết kết quả.

## Quy tắc bất đồng, kiểm soát phiên bản và hiệu chuẩn

Hai người sàng lọc độc lập tiêu đề/tóm tắt và toàn văn, không nhìn quyết định của nhau trước khi khóa vòng. Bất đồng được ghi `PENDING_ADJUDICATION`, thảo luận với locator và codebook; nếu còn bất đồng, chuyển cơ chế phân xử đã nêu. Quyết định đã phân xử giữ cả hai quyết định gốc, người phân xử, ngày, lý do và phiên bản codebook trong audit trail/registry; không ghi đè lịch sử.

Trước đăng ký, chỉ field-test trên `PRE_REGISTRATION_SEARCH_DEVELOPMENT` hoặc nguồn mốc cho huấn luyện công cụ; không tạo corpus, PRISMA count hay quyết định đủ điều kiện. Hiệu chuẩn dự kiến theo protocol:

1. Tiêu đề/tóm tắt: lấy ngẫu nhiên 25 record từ pool validation, hoặc toàn bộ nếu dưới 25; lưu cách lấy mẫu và random seed. Mức đồng thuận ban đầu tối thiểu 75% và mọi bất đồng được ghi/giải quyết.
2. Toàn văn: chọn có chủ đích 8 document đa dạng, hoặc toàn bộ nếu dưới 8, gồm loại nguồn, tầng thẩm quyền, ngôn ngữ và ít nhất một ca biên nếu có. Ngưỡng đồng thuận ban đầu tối thiểu 75%.
3. Nếu sửa codebook có thể đổi quyết định, lặp lại bước bị ảnh hưởng với mẫu mới cùng quy tắc/cỡ mẫu; kappa chỉ là chỉ số mô tả, không phải hard gate.

Không có sàng lọc chính thức đến khi G2, `SCREENING_EXTRACTION_CODEBOOK_GATE` và calibration đều `PASS`, protocol đã đăng ký và các cổng G4–G7 cho phép bước tương ứng. `TEAM_EXPERTISE_GATE=NOT_APPLICABLE_SCOPE_NARROWED` theo `PR-02`; codebook không cho phép người rà soát tự thẩm định hiệu quả, an toàn hoặc tính phù hợp lâm sàng ngoài nội dung và bằng chứng được nguồn công khai mô tả.
