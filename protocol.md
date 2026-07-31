# Protocol tổng quan phạm vi và phân tích khoảng trống

## 1. Thông tin kiểm soát

| Trường                                           | Giá trị                                                                                                   |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `protocol_version`                               | `0.6-registered`                                                                                          |
| Trạng thái đăng ký                            | `REGISTERED_PUBLIC`                                                                                       |
| Mức sẵn sàng                                    | `READY_FOR_FEASIBILITY_PILOT`                                                                             |
| Ngày lập bản này                               | 31/07/2026                                                                                                |
| Ngày khóa cục bộ protocol                     | 31/07/2026, theo `PR-03`, sau khi toàn bộ dependency tiền đăng ký đạt yêu cầu                             |
| Đăng ký công khai                               | OSF Registries, 31/07/2026; [OSF: 62b8w](https://osf.io/62b8w/); [DOI: 10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W) |
| Ngày dự kiến bắt đầu tìm kiếm chính thức | Sau khi protocol được đăng ký, locator được kiểm tra và G4–G5 đạt `PASS`                                  |
| Ngày dự kiến hoàn thành                       | 30/11/2026                                                                                                |
| Phương pháp                                     | Tổng quan phạm vi theo JBI; báo cáo theo PRISMA-ScR                                                     |

Protocol đã hoàn tất các điều kiện tiền đăng ký, được khóa cục bộ thành gói bất biến ngày 31/07/2026 và được đăng ký công khai trên OSF cùng ngày. Bản đăng ký công khai là bản lưu bất biến; phiên bản này chỉ ghi nhận tình trạng hậu đăng ký theo `PR-04`, không sửa ngược snapshot. Pilot khả thi G4–G5 nay được phép bắt đầu; tìm kiếm chính thức, sàng lọc và trích xuất dữ liệu chính thức vẫn chỉ được mở khi các cổng tương ứng đạt điều kiện. Hoạt động `pre-registration search-development validation` tại Mục 9.3 đã hoàn tất ngày 31/07/2026 nhưng không tạo corpus hoặc count PRISMA.

Phiên bản `0.2-pre-registration` làm rõ câu hỏi và trường trích xuất về thể chế hóa, áp dụng, giám sát và bằng chứng kết quả/tác động. Phiên bản `0.3-pre-registration` ghi sửa đổi tiền đăng ký `PR-01` ngày 31/07/2026: thêm lý do loại toàn văn `EX09_WRONG_LANGUAGE` để sửa thiếu sót giữa tiêu chí chỉ nhận tiếng Việt/Anh và danh mục lý do loại chuẩn hóa. Phiên bản `0.4-pre-registration` ghi sửa đổi tiền đăng ký `PR-02` ngày 31/07/2026 tại [`protocol-amendment-pr-02.md`](protocol-amendment-pr-02.md): bỏ vai trò chuyên gia y tế và `TEAM_EXPERTISE_GATE`, giữ Đào Trung Thành và Lộc Đặng là hai người rà soát, đồng thời khóa ranh giới không thẩm định hoặc khuyến nghị lâm sàng độc lập. Phiên bản `0.5-ready-for-registration` ghi sửa đổi `PR-03` ngày 31/07/2026 tại [`protocol-amendment-pr-03.md`](protocol-amendment-pr-03.md): bỏ mốc chờ hành chính 15/08/2026 và cho phép khóa cục bộ ngay khi dependency tiền đăng ký đã đạt. Phiên bản `0.6-registered` ghi nhận hậu đăng ký `PR-04` ngày 31/07/2026 tại [`protocol-amendment-pr-04.md`](protocol-amendment-pr-04.md), với locator/DOI công khai; không thay đổi phương pháp, truy vấn, tiêu chí hay codebook.

### Trạng thái các cổng có liên quan

| Cổng/dependency                                      | Trạng thái hiện tại              | Hệ quả                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| G4 — thu hồi nguồn mốc | `PASS` | Đã kiểm thử và thu hồi thành công raw export từ PubMed, OpenAlex, nguồn chính thức VN và citation chasing tại nhật ký [`g4-g5-feasibility-pilot-2026-07-31.md`](g4-g5-feasibility-pilot-2026-07-31.md). |
| G5 — độ giàu dữ liệu trực tiếp | `PASS` | Đã xác minh 183 nguồn trực tiếp/bối cảnh về AI y tế Việt Nam, đạt điều kiện cho `NHÁNH A (Scoping Review)`. |
| `TEAM_EXPERTISE_GATE`                               | `NOT_APPLICABLE_SCOPE_NARROWED`    | `PR-02` loại vai trò chuyên gia y tế khỏi thiết kế đang hoạt động. Không có hồ sơ chuyên gia y tế trong bộ tài liệu nghiên cứu hiện hành.                                                                                                                                                               |
| `SCREENING_EXTRACTION_CODEBOOK_GATE`                | `PASS`                             | Chủ trì xác nhận hiệu chuẩn của Lộc Đặng ngày 31/07/2026 đã bao phủ ba vòng và đạt ngưỡng protocol; artifact tại[`calibration-attestation-2026-07-31.md`](calibration-attestation-2026-07-31.md).                                                                                                              |
| `PRISMA_SCR_PROTOCOL_MAP_GATE`                      | `PASS`                             | [`prisma-scr-checklist.md`](prisma-scr-checklist.md) có 22 mục duy nhất được lập bản đồ; trạng thái pending được ghi trung thực và mỗi mục chưa hoàn tất có chủ thể, dependency và bằng chứng đích.                                                                                                |
| `PRISMA_SCR_MANUSCRIPT_GATE`                        | `NOT_PASS_FOR_MANUSCRIPT`          | Không chặn đăng ký; chỉ được chuyển`PASS` khi bản thảo và dữ liệu cuối đáp ứng checklist trước nộp.                                                                                                                                                                                                       |
| Chiến lược tìm kiếm chính xác                  | `PASS`                             | `search-strategy.md` phiên bản `0.2-pre-registration-search-development` đã qua validation ngày 31/07/2026.                                                                                                                                                                                                      |
| Bộ chuẩn quốc tế cuối cùng                      | `PASS`                             | Đã được người rà soát thứ hai độc lập Lộc Đặng rà soát và khóa ngày 31/07/2026 (`PASS_BY_LOC_DANG_REVIEW` tại [`international-benchmark.md`](international-benchmark.md)).                                                                                                                                     |
| Competitive checkpoint trước khóa                  | `PASS_WITH_NARROWED_CLAIM`         | Đã kiểm tra ngày 31/07/2026 tại[`competitive-checkpoint-2026-07-31.md`](competitive-checkpoint-2026-07-31.md).                                                                                                                                                                                                    |
| Khai báo tài trợ                                   | `PASS`                             | Chủ trì xác nhận ngày 31/07/2026 rằng nghiên cứu không có tài trợ chuyên biệt; vai trò bên tài trợ là`NOT_APPLICABLE`. Bằng chứng tại [`funding-declaration.md`](funding-declaration.md).                                                                                                                |
| Đăng ký OSF công khai                               | `PASS`                             | Registration `62b8w` đã được chấp nhận/công khai ngày 31/07/2026; [URL](https://osf.io/62b8w/), [DOI](https://doi.org/10.17605/OSF.IO/62B8W). |

G2, `SCREENING_EXTRACTION_CODEBOOK_GATE`, `PRISMA_SCR_PROTOCOL_MAP_GATE`, G4, G5, chiến lược tìm kiếm chính xác, bộ chuẩn quốc tế, competitive checkpoint, khai báo tài trợ và đăng ký OSF công khai đều đã có bằng chứng đạt yêu cầu (`PASS`). Pilot khả thi G4–G5 đã hoàn tất và kết luận đi theo `NHÁNH A (Scoping Review)`. Tìm kiếm chính thức, sàng lọc và trích xuất dữ liệu nay sẵn sàng khởi chạy.

## 2. Tiêu đề

**Tiếng Việt**

Từ nguyên tắc đến yêu cầu vận hành: tổng quan phạm vi nguồn công khai và phân tích khoảng trống đạo đức, quản trị AI y tế tại Việt Nam

**Tiếng Anh**

From principles to operational requirements: a scoping review of public evidence and gap analysis of AI ethics and governance for healthcare in Vietnam

## 3. Lý do nghiên cứu

Các tổng quan quốc tế gần đây đã lập bản đồ nhiều khung đạo đức và quản trị AI trong y tế, kể cả cấu trúc trách nhiệm, quy trình vòng đời, giám sát và theo dõi. Một bản đồ toàn cầu khác sẽ có nguy cơ lặp lại phần việc này. Khoảng tri thức còn có ý nghĩa nằm ở việc xác minh các nguồn công khai trực tiếp tại Việt Nam, phân biệt tầng thẩm quyền của nguồn và đánh giá mức độ các nguyên tắc đã được chuyển thành chủ thể chịu trách nhiệm, quyền quyết định, kiểm soát và bằng chứng vận hành.

Tại giai đoạn phát triển protocol, Việt Nam đã có Luật Trí tuệ nhân tạo số `134/2025/QH15` (hiệu lực 01/03/2026), Nghị định `142/2026/NĐ-CP` (hiệu lực 01/05/2026) và Thông tư `05/2026/TT-BKHCN` ban hành Khung đạo đức trí tuệ nhân tạo quốc gia. Luật quy định thời hạn chuyển tiếp 18 tháng đối với các hệ thống AI trong lĩnh vực y tế đã hoạt động trước ngày Luật có hiệu lực. Bối cảnh này làm cho câu hỏi khoa học chuyển từ “Việt Nam đã có nguyên tắc hay chưa” sang: yêu cầu nào có tính ràng buộc hoặc khuyến khích, cơ chế nào đã được thể chế hóa, và có bằng chứng công khai nào về áp dụng, giám sát hay kết quả trong khoảng thời gian triển khai thực tế. Các locator và bản Công báo được giữ trong artifact phát triển tìm kiếm; trạng thái pháp lý phải được kiểm tra lại tại ngày đóng tìm kiếm và trước nộp bài.

Nghiên cứu chỉ suy luận từ tài liệu và bằng chứng công khai đủ điều kiện. Sự vắng mặt trong tập nguồn không chứng minh một cơ chế không tồn tại trong thực hành, và dữ liệu bàn giấy không cho phép kết luận về năng lực thực tế của toàn bộ bệnh viện hoặc hệ thống y tế Việt Nam.

## 4. Mục tiêu, câu hỏi và tuyên bố đóng góp

### 4.1. Mục tiêu

Xác lập bản đồ có thể kiểm tra của các nguyên tắc, trách nhiệm, quyền quyết định, kiểm soát, bằng chứng và quyền của người bệnh được thể hiện trong nguồn công khai trực tiếp về AI y tế tại Việt Nam; phân biệt văn bản chuẩn tắc với thể chế hóa, áp dụng, giám sát và bằng chứng kết quả/tác động; đối chiếu chúng với một bộ chuẩn quốc tế xác định trước; và phân loại khoảng trống với giới hạn suy luận tương ứng.

### 4.2. Câu hỏi chính

Các nguồn công khai trực tiếp hiện hành/đủ điều kiện mô tả những nguyên tắc, trách nhiệm, quyền quyết định, kiểm soát và bằng chứng nào cho AI trong y tế Việt Nam, và khoảng trống nào xuất hiện khi đối chiếu với bộ chuẩn quốc tế định trước?

### 4.3. Ba câu hỏi phụ

1. Các cấu phần được thể hiện ở mức nào theo nguồn Việt Nam và tầng thẩm quyền?
2. Những khoảng trống chuẩn tắc, chuyển hóa, trách nhiệm, bằng chứng và điều kiện năng lực công bố nào còn lại, với giới hạn suy luận nào?
3. Bằng chứng công khai cho thấy các cấu phần đã được thể chế hóa, áp dụng, giám sát hoặc đánh giá kết quả trong thực hành y tế Việt Nam ở mức nào, với chất lượng và giới hạn suy luận nào?

### 4.4. Tuyên bố đóng góp đã khóa

Tổng quan này cập nhật và xác minh tập nguồn công khai trực tiếp về đạo đức và quản trị AI y tế tại Việt Nam, bao gồm nguồn tiếng Việt và cổng chính thức; dùng một schema vận hành làm công cụ tổng hợp quốc gia để truy vết chủ thể, thẩm quyền quyết định, cơ chế thực hiện/kiểm soát/thực thi và bằng chứng/giám sát; đồng thời phân tầng kết luận theo thẩm quyền pháp lý và giới hạn của nguồn công khai.

Schema vận hành là công cụ tổng hợp quốc gia, không phải một khung quản trị mới. Tuyên bố này phải được kiểm tra lại tại bốn competitive checkpoint: trước khóa protocol, trước pilot khả thi G4–G5, khi đóng tìm kiếm và trước nộp bài.

## 5. Nhóm nghiên cứu, năng lực và xung đột lợi ích

### 5.1. Vai trò dự kiến

| Thành viên/cơ chế | Vai trò                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Đào Trung Thành    | Chủ trì câu hỏi; chuyên môn đạo đức AI; quản lý nguồn sách; tham gia phân tích và viết bản thảo; chịu trách nhiệm chung về tính toàn vẹn của nghiên cứu.                                                                                                                                                                                                                                                                                                 |
| Lộc Đặng           | Người sàng lọc độc lập; thực hiện nhánh mã hóa quy nạp trước khi xem mã từ Chương 10; kiểm tra dữ liệu và các trường quyết định khoảng trống. G2=`PASS` ngày 31/07/2026 theo [`loc-dang-reviewer-confirmation.md`](loc-dang-reviewer-confirmation.md).                                                                                                                                                                                              |
| Cơ chế phân xử    | Hai người rà soát thảo luận bất đồng dựa trên tiêu chí, codebook và bằng chứng nguồn. Ở vòng tiêu đề/tóm tắt, bất đồng chưa giải quyết được được chuyển sang toàn văn. Ở toàn văn hoặc mã hóa, nếu chưa đạt đồng thuận sau khi kiểm tra lại locator, trường liên quan được giữ`UNCLEAR`, không dùng để tạo một kết luận khoảng trống hay khuyến nghị; quyết định và lý do được ghi trong nhật ký. |

Tư cách đồng tác giả không phát sinh tự động từ vai trò được đề xuất. Tên tác giả chỉ được quyết định theo đóng góp thực tế và tiêu chí của ICMJE/tạp chí: đóng góp đáng kể; soạn thảo hoặc sửa chữa nội dung học thuật quan trọng; duyệt bản cuối; và đồng ý chịu trách nhiệm giải trình. Người không đáp ứng đầy đủ được ghi nhận đóng góp theo hình thức thích hợp.

### 5.2. Ranh giới chuyên môn y tế và giới hạn diễn giải

Nhóm đang hoạt động gồm hai người rà soát và không có thành viên được giao vai trò thẩm định lâm sàng hoặc y tế công cộng. Vì vậy, nghiên cứu giới hạn ở phân tích đạo đức, quản trị, thẩm quyền, cơ chế kiểm soát và bằng chứng công khai được mô tả trong tài liệu. Khi nguồn đề cập an toàn, hiệu quả, giá trị lâm sàng, quyền người bệnh hoặc tác động y tế, nhóm chỉ:

- trích xuất nội dung, locator, chủ thể phát biểu và tầng thẩm quyền của nguồn;
- phân loại loại bằng chứng và mức độ nguồn tự báo cáo giới hạn;
- đối chiếu sự hiện diện của yêu cầu quản trị đã định trước;
- không tự xác nhận tính đầy đủ lâm sàng, hiệu quả điều trị, an toàn thực tế hoặc tính phù hợp cho một chuyên khoa.

Một nội dung cần phán đoán lâm sàng mà nguồn không cung cấp đủ căn cứ được mã `UNCLEAR` và không dùng để tạo kết luận khoảng trống, đánh giá hiệu quả hay khuyến nghị điều trị. Bản thảo phải công bố ranh giới này trong phương pháp và hạn chế. `TEAM_EXPERTISE_GATE` được chuyển thành `NOT_APPLICABLE_SCOPE_NARROWED`; việc mở rộng sang thẩm định hoặc khuyến nghị lâm sàng đòi hỏi amendment thực chất và bổ sung năng lực phù hợp trước khi thực hiện.

### 5.3. Xung đột lợi ích trí tuệ và biện pháp kiểm soát

Đào Trung Thành là tác giả Chương 10 về y tế trong sách *Đạo đức AI: Nguyên tắc và Thực hành* và có đầu tư trí tuệ vào các khái niệm được xem xét. Đây là xung đột lợi ích trí tuệ cần công bố. Biện pháp kiểm soát gồm:

- đóng dấu thời gian protocol và khóa codebook trước phân tích chính thức;
- để người không phải tác giả Chương 10 hoàn tất nhánh mã hóa quy nạp trước khi tiếp cận mã riêng của chương;
- lưu riêng `inductive_code` và `chapter10_only_code`;
- phân tích độ nhạy có và không có nhánh Chương 10;
- chủ động tìm ca âm tính và trường hợp phản ví dụ;
- không dùng Chương 10 để tự xác nhận kết quả;
- công bố vai trò kép trong protocol và bản thảo.

## 6. Thiết kế và khung PCC

Nghiên cứu áp dụng phương pháp tổng quan phạm vi của JBI và báo cáo theo PRISMA-ScR.

| Thành phần PCC | Định nghĩa                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Participants     | Không áp dụng; không giới hạn nhóm người tham gia vì đơn vị phân tích là nguồn và cấu phần quản trị.           |
| Concept          | Đạo đức, trách nhiệm, quản trị, quyền quyết định, kiểm soát, bằng chứng, giám sát và quyền trong vòng đời AI. |
| Context          | AI trong y học, chăm sóc sức khỏe, bệnh viện hoặc hệ thống y tế có liên hệ trực tiếp với Việt Nam.                 |

PRISMA-ScR được dùng để minh bạch hóa nhận diện, sàng lọc, lựa chọn và trình bày nguồn. Checklist không phải bằng chứng tự thân cho độ đúng của kết luận chuẩn tắc hoặc kết luận về Việt Nam.

Hai cổng PRISMA có chức năng khác nhau. `PRISMA_SCR_PROTOCOL_MAP_GATE=PASS` xác nhận 22 mục đã được lập bản đồ trung thực trong [`prisma-scr-checklist.md`](prisma-scr-checklist.md), gồm locator hiện có và owner/dependency/evidence cho mục pending. `PRISMA_SCR_MANUSCRIPT_GATE=NOT_PASS_FOR_MANUSCRIPT` phản ánh nghiên cứu chưa có kết quả và bản thảo cuối; trạng thái này không chặn đăng ký nhưng phải chuyển `PASS` trước khi nộp.

## 7. Tiêu chí đủ điều kiện

### 7.1. Tiêu chí đưa vào tập nghiên cứu chính

Nguồn phải:

1. trực tiếp đề cập ít nhất một cấu phần đạo đức hoặc quản trị AI trong y tế Việt Nam;
2. có toàn văn hoặc nội dung chính thức đủ để xác minh nguồn gốc, phạm vi và phát biểu liên quan;
3. thuộc một trong các nhóm:
   - văn bản pháp luật/quy định còn hiệu lực hoặc văn bản chính thức xác định được trạng thái;
   - chính sách, chiến lược hoặc hướng dẫn chính thức;
   - nghiên cứu/tổng quan bình duyệt;
   - báo cáo chính thức, báo cáo dự án hoặc nguồn xám có thể kiểm chứng;
4. bằng tiếng Việt hoặc tiếng Anh.

Mốc 01/01/2019 áp dụng cho nghiên cứu, báo cáo mới và hướng dẫn mới. Mọi văn bản pháp luật, quy định hoặc công cụ chính thức còn hiệu lực tại ngày tìm kiếm được xem xét bất kể năm ban hành; phải ghi ngày ban hành, sửa đổi, thay thế và hiệu lực. Một văn bản cũ đã hết hiệu lực chỉ được giữ như dữ liệu lịch sử khi cần giải thích trực tiếp trạng thái hoặc chuỗi sửa đổi của một văn bản đủ điều kiện và không được tính như yêu cầu hiện hành.

Ngày 01/01/2019 là ranh giới thực dụng về tính cập nhật cho lĩnh vực nghiên cứu, báo cáo và hướng dẫn AI biến đổi nhanh, không được diễn giải như một mốc tự nhiên hay thời điểm khởi đầu của quản trị AI y tế. Nguy cơ bỏ sót chuẩn mực ra đời sớm nhưng còn giá trị được giảm thiểu bằng cách đưa vào mọi văn bản pháp luật, quy định và công cụ chính thức vẫn còn hiệu lực bất kể năm; truy tìm trích dẫn; và kiểm tra văn bản được dẫn chiếu, sửa đổi, thay thế hoặc bãi bỏ.

Giới hạn tiếng Việt và tiếng Anh phản ánh năng lực sàng lọc của nhóm và các kênh chính có liên quan trực tiếp đến câu hỏi. Đây là giới hạn khả thi phải được báo cáo trong bản thảo. Nguồn bằng ngôn ngữ khác được phát hiện qua tìm kiếm hoặc trích dẫn phải được ghi nhận là bị loại theo giới hạn ngôn ngữ đã định trước; không được âm thầm quy thành vắng mặt hoặc dùng để gán trạng thái “chưa tìm thấy”.

Việc bao gồm cả nghiên cứu bình duyệt và nguồn xám chính thức/có thể kiểm chứng nhằm đồng thời thu nhận học thuật, thẩm quyền chuẩn tắc và bằng chứng triển khai công khai. Tin tức, marketing và nguồn không thể xác minh bị loại vì không cho phép kiểm tra ổn định nguồn gốc, phiên bản, phạm vi hoặc phát biểu, làm suy giảm khả năng tái lập.

### 7.2. Nguồn nền ngoài tập PRISMA

Nguồn nền chỉ được dùng khi một nghĩa vụ pháp lý trực tiếp đã được định trước liên kết với cấu phần chuẩn đối chiếu. Không mở nhánh tìm kiếm chung về y tế số, dữ liệu, an ninh mạng hoặc quyền riêng tư. Nguồn nền:

- được ghi trong registry riêng với lý do sử dụng;
- không được đưa vào count của tập nghiên cứu chính hoặc sơ đồ PRISMA;
- chỉ dùng để giải thích bối cảnh pháp lý của một phát hiện đã hình thành từ tập nghiên cứu chính;
- không được tạo bằng chứng dương tính hoặc âm tính, thay đổi một trong bốn trạng thái đối chiếu, thay đổi loại/số lượng gap hoặc kết luận có cơ chế quản trị AI y tế hoàn chỉnh;
- không được dùng để bù số lượng nguồn trực tiếp.

Nếu nhóm muốn dùng nguồn nền như bằng chứng phân tích, trước khi nhận diện hoặc lựa chọn nguồn phải đăng amendment thực chất và thiết kế một secondary legal-context corpus tái lập, với tiêu chí, danh mục nguồn, registry, provenance, quy tắc chọn–loại và flow riêng. Không được chọn nguồn nền hậu nghiệm theo hướng ủng hộ kết luận sẵn có.

### 7.3. Tiêu chí loại

Mỗi document bị loại ở toàn văn nhận đúng một mã chính trong chín mã chuẩn hóa:

1. `EX01_NOT_VIETNAM` — không thuộc Việt Nam;
2. `EX02_NOT_HEALTHCARE` — không thuộc y tế;
3. `EX03_NO_AI` — không đề cập AI;
4. `EX04_NO_ETHICS_GOVERNANCE` — không có nội dung đạo đức/quản trị;
5. `EX05_WRONG_SOURCE_TYPE` — sai loại nguồn, gồm tin phổ thông, marketing hoặc tài liệu không thể xác minh;
6. `EX06_DATE_OUTSIDE_NO_LEGAL_EXCEPTION` — ngoài mốc thời gian và không thuộc ngoại lệ văn bản còn hiệu lực;
7. `EX07_DUPLICATE_NO_NEW_DATA` — phiên bản trùng hoặc không đóng góp dữ liệu;
8. `EX08_FULL_TEXT_UNAVAILABLE` — không thể truy cập đủ nội dung sau quy trình tìm toàn văn đã định trước;
9. `EX09_WRONG_LANGUAGE` — toàn văn không phải tiếng Việt/Anh và không có bản dịch Việt/Anh đủ tin cậy sau quy trình tìm toàn văn.

`EX09_WRONG_LANGUAGE` chỉ dùng ở toàn văn. Khi ngôn ngữ metadata chưa rõ hoặc có bản dịch Việt/Anh nhưng khả năng sử dụng chưa được xác minh, record/document giữ `UNCERTAIN` hoặc `PENDING_ADJUDICATION` cho đến khi hai reviewer xác minh; không loại sớm theo suy đoán.

Không loại nguồn dựa trên kết quả hoặc vì giới hạn 8 trang/25 tài liệu tham khảo sau khi đã biết nội dung.

## 8. Đơn vị và quản lý phiên bản

- **Record:** một mục được thu hồi từ một kênh tìm kiếm, có mã nguồn, locator và provenance riêng; cùng một tài liệu có thể tạo nhiều record.
- **Document/report:** một hiện vật nội dung có thể đọc và trích xuất, như bài báo, văn bản pháp luật, hướng dẫn hoặc báo cáo; nhiều record hoặc phiên bản có thể quy về cùng một document.
- **Framework/policy:** một cấu trúc chuẩn tắc hay tổ chức có danh tính, phạm vi và cơ quan/tác giả xác định, được thể hiện trong một hoặc nhiều document; mỗi framework/policy có mã riêng và liên kết đến các document cấu thành.

Khử trùng lặp ưu tiên mã định danh bền vững, sau đó dùng tiêu đề, cơ quan/tác giả, ngày, số hiệu, phiên bản và nội dung. Registry giữ mọi kênh phát hiện ngay cả khi chỉ một record đại diện được đưa sang sàng lọc. Bản hợp nhất, bản sửa đổi, bản thay thế và bản dịch được liên kết thành một họ phiên bản. Phiên bản có hiệu lực tại ngày tìm kiếm là bản phân tích chính; phiên bản khác chỉ giữ khi bổ sung nội dung hoặc giải thích thay đổi có liên quan.

Registry vận hành dùng [`record-registry-codebook.md`](record-registry-codebook.md) và [`record-registry-template.csv`](record-registry-template.csv) theo event ledger append-only. Mỗi manifestation/alias giữ `record_id` riêng; canonicalization nối alias đến `canonical_record_id` và `document_id` mà không xóa record. Provenance nhiều–nhiều được ghi bằng event riêng cho từng channel/query/seed/direction/raw artifact. Quan hệ document–framework nhiều–nhiều dùng một `FRAMEWORK_LINK` cho mỗi `document_id × framework_id`. Quyết định reviewer, phân xử và thay đổi metadata là event có version/supersedes link; không ghi đè lịch sử.

## 9. Nguồn thông tin và chiến lược tìm kiếm

### 9.1. Kênh bắt buộc

1. PubMed qua NCBI, gồm record MEDLINE và record PubMed ngoài MEDLINE.
2. OpenAlex.
3. Cổng Thông tin điện tử Chính phủ và Công báo.
4. Cơ sở dữ liệu pháp luật chính thức của Việt Nam.
5. Bộ Y tế và các đơn vị trực thuộc được định danh trong chiến lược tìm kiếm.
6. Bộ Khoa học và Công nghệ.
7. UNESCO RAM Việt Nam.
8. WHO tại Việt Nam.
9. Các nguồn pháp lý/chính thức khác chỉ khi được một văn bản đủ điều kiện dẫn chiếu trực tiếp.
10. Truy tìm trích dẫn một thế hệ ngược và một thế hệ xuôi cho tập Việt Nam.

Google Scholar và web học thuật chỉ hỗ trợ định vị toàn văn hoặc kiểm tra trích dẫn. Chúng không phải cơ sở dữ liệu chính và không thay thế nhật ký tìm kiếm tái lập.

### 9.2. Logic khái niệm

Chiến lược sử dụng ba cụm:

- AI: artificial intelligence, machine learning, generative AI, large language model và biến thể tiếng Việt;
- đạo đức/quản trị: ethics, governance, accountability, responsibility, transparency, fairness, bias, privacy, oversight và biến thể tiếng Việt;
- Việt Nam/y tế: Vietnam, Viet Nam kết hợp health, healthcare, medicine, clinical, hospital và biến thể tiếng Việt.

Ngôn ngữ đủ điều kiện là tiếng Việt và tiếng Anh. Mốc thời gian tuân theo Mục 7.1; bộ lọc giao diện không được làm mất ngoại lệ pháp lý.

### 9.3. `Pre-registration search-development validation`

Trước đăng ký, nhóm được thực hiện một giai đoạn phát triển chiến lược tìm kiếm có giới hạn, tách khỏi pilot khả thi G4–G5. Giai đoạn này thực hiện phần phát triển của cách tiếp cận ba bước theo JBI:

1. chạy limited search trên PubMed và OpenAlex, cùng kiểm tra mẫu trên các portal chính thức phù hợp;
2. phân tích text words trong tiêu đề/tóm tắt và index terms/subject headings của các nguồn mốc;
3. thử bản dịch thuật ngữ Việt–Anh, cú pháp/field/filter theo nền tảng và khả năng thu hồi seed thuộc phạm vi từng kênh;
4. ghi thay đổi từ truy vấn thử sang truy vấn ứng viên cuối, kèm lý do và ảnh hưởng dự kiến.

Đây là `search-development validation`, không phải scientific/feasibility pilot. Mọi lượt mang nhãn `PRE_REGISTRATION_SEARCH_DEVELOPMENT`; count và artifact được lưu riêng, không tạo corpus, không đi vào flow/PRISMA, không dùng đánh giá G4–G5 và không tạo quyết định đưa vào/loại. Record nhìn thấy trong giai đoạn này chỉ được dùng để phát triển từ khóa, kiểm tra nền tảng, seed retrieval và field-test biểu mẫu; chúng không tự động trở thành record của tìm kiếm chính thức. Tìm kiếm toàn bộ theo chiến lược đã khóa và bước citation chasing hệ thống chỉ diễn ra sau đăng ký theo Mục 9.6–9.7.

### 9.4. Dependency khóa chiến lược chính xác

Trước khi đăng ký, `search-strategy.md` phải khóa nguyên văn:

- chuỗi cuối cùng cho từng cơ sở dữ liệu và bản dịch logic giữa các nền tảng;
- PubMed query gốc, query translation dự kiến lưu, trường/bộ lọc và phương thức xuất;
- OpenAlex Boolean/phrase/API URL, filter, `per_page`, cursor, trường selected và phương thức xuất;
- từng portal/miền, truy vấn tiếng Việt–Anh, số tầng liên kết, giới hạn trang/kết quả, điều kiện bão hòa và tiêu chí dừng;
- danh sách đơn vị thuộc Bộ Y tế và nguồn pháp lý chính thức;
- quy trình tìm toàn văn, quản lý phiên bản, truy tìm văn bản dẫn chiếu và văn bản sửa đổi/thay thế;
- quy tắc registry, provenance, khử trùng lặp và citation chasing.

Chiến lược tìm kiếm chính xác chỉ đạt `PASS` khi có nhật ký validation, bảng text words/index terms, kết quả seed retrieval theo kênh, bằng chứng thử bản dịch/cú pháp trên từng nền tảng và lịch sử quyết định truy vấn. Dependency này có giá trị `NOT_RUN` ở phiên bản 0.1 và đã đạt `PASS` ngày 31/07/2026 theo `search-strategy.md`. Kết quả validation không thay thế ngày chạy và count của tìm kiếm chính thức sau đăng ký.

### 9.5. Nhật ký và artifact

Với **PubMed**, mỗi lượt phải lưu nhãn giai đoạn, query gốc, query translation do NCBI trả về, múi giờ/ngày giờ chạy, filter, tổng số record, số record thực xuất, raw `.nbib` hoặc XML/CSV, tên tệp/locator và checksum.

Với **OpenAlex**, mỗi lượt phải lưu nhãn giai đoạn, API URL/truy vấn percent-encoded không chứa secret, ngày giờ, filter, `per_page`, phương thức cursor, trường selected, `meta.count`, số record thực xuất, chênh lệch, ngày chụp dữ liệu, raw JSON, tên tệp/locator và checksum. Khi pilot khả thi hoặc tìm kiếm chính thức, phải xuất toàn bộ qua cursor: giữ toàn bộ cursor chain và metadata mỗi page (`cursor_in`, `next_cursor`, `meta.count`, `meta.per_page`, số result, HTTP status, timestamp, checksum), lặp cho đến khi `next_cursor=null` **và** `results` rỗng. Một trang có `next_cursor=null` nhưng còn result không được coi là hết dữ liệu. Khử trùng lặp theo OpenAlex ID; manifest phải ghi raw results, unique IDs, duplicate IDs, cursor loop/page error và chuỗi `meta.count`. Nếu count drift hay có chênh lệch, lập discrepancy log và không tuyên bố export đầy đủ cho đến khi rerun sạch hoặc amendment quyết định xử lý. CSV/RIS chuyển từ JSON là artifact dẫn xuất, phải có nhãn và checksum riêng. OpenAlex là lựa chọn theo nguồn lực, không được tuyên bố tương đương tuyệt đối với Scopus hay cơ sở dữ liệu thương mại; hạn chế về metadata, lập chỉ mục và cập nhật phải được báo cáo.

Để tìm bằng chứng triển khai ở cấp Sở Y tế/bệnh viện mà không mở một tìm kiếm vô hạn, chiến lược dùng case-finding có chủ đích, maximum-variation, với một sampling frame hữu hạn đã khóa: ba Sở Y tế (Hà Nội, Đà Nẵng, TP.HCM) và sáu bệnh viện sentinel (Bạch Mai, Trung ương Huế, Chợ Rẫy, Vinmec Times City, Tâm Anh TP.HCM, Đại học Y Dược TP.HCM). Frame phân tầng Bắc/Trung/Nam, tuyến trung ương, công/tư và đại học; domain, lý do, query set, trần và độ sâu nằm trong `implementation-case-sampling-frame.csv`. Mỗi case chỉ chạy quy tắc đã khóa trong `search-strategy.md`; người rà soát thứ hai tái xác minh ownership/domain trước run, và không thay case theo kết quả nếu không có amendment. Đây không phải mẫu xác suất hay frame toàn quốc: kết quả chỉ mô tả bằng chứng công khai trong các case đã xét, không suy prevalence, mức áp dụng hay hiệu quả của toàn hệ thống. File frame và việc chạy nhánh này hiện `NOT_RUN`.

Với **nguồn chính thức**, phải lưu nhãn giai đoạn, URL gốc, URL ổn định nếu có, ngày truy cập, ảnh chụp/PDF/HTML, số hiệu, phiên bản, trạng thái hiệu lực, quan hệ sửa đổi/thay thế và checksum. Mỗi portal chỉ được chạy theo quy tắc dừng đã khóa.

Count của kiểm tra kỹ thuật, novelty audit, `PRE_REGISTRATION_SEARCH_DEVELOPMENT`, pilot khả thi G4–G5 và tìm kiếm chính thức được lưu tách biệt. Không count nào của ba giai đoạn đầu tự động trở thành count PRISMA cuối cùng.

### 9.6. Pilot khả thi sau đăng ký và tìm kiếm chính thức

G4–G5 là pilot khả thi khoa học sau đăng ký, dùng chiến lược đã khóa để kiểm tra end-to-end: thu hồi nguồn mốc theo kênh, xuất và checksum, registry/provenance, khử trùng lặp, flow nguồn chính thức, citation chasing pilot và độ giàu dữ liệu trực tiếp. Pilot này có registry/count riêng và không tự động tạo corpus hoặc count PRISMA cuối cùng.

Nếu pilot cho thấy cần thay đổi thực chất truy vấn, tiêu chí, danh mục nguồn, quy tắc dừng, citation chasing hoặc codebook, nhóm phải đăng amendment, tăng phiên bản và đặt lại các cổng phụ thuộc trước khi chạy lại G4–G5. Tìm kiếm chính thức chỉ bắt đầu sau khi protocol đã đăng ký, G4 và G5 đều `PASS`, mọi amendment từ pilot đã được công bố và ngày bắt đầu chính thức được ghi trong search log. Khi đó nhóm chạy lại toàn bộ chiến lược trên mọi kênh; record pilot không tự động được chuyển vào corpus.

### 9.7. Citation chasing

Citation chasing chỉ áp dụng cho tập Việt Nam và dùng registry chung với mọi kênh. Ở pilot khả thi G4–G5, seed phải là nguồn mốc định trước hoặc nguồn được cả hai người rà soát xác nhận đủ điều kiện cho mục đích pilot. Trong tìm kiếm chính thức, seed chỉ được lấy từ nguồn đã đủ điều kiện sau sàng lọc kép.

Mỗi seed chỉ truy một thế hệ backward và một thế hệ forward. Có thể dừng sớm khi một hướng không tạo record mới sau khử trùng lặp toàn cục. Mỗi lượt ghi seed/document ID, hướng, nền tảng/cách truy, ngày, số record đã xem, số record mới, quyết định/điểm đến, điểm dừng và locator. Không bắt đầu citation chasing pilot G4–G5 khi protocol chưa đăng ký hoặc G2 hay `SCREENING_EXTRACTION_CODEBOOK_GATE` chưa đạt `PASS`.

### 9.8. Competitive checkpoints

Tại bốn mốc — trước khóa protocol, trước pilot khả thi G4–G5, khi đóng tìm kiếm và trước nộp — nhóm phải tìm output mới theo tiêu đề, DOI, tên tác giả, PROSPERO và PMID của protocol *Mapping National Governance of AI for Health* của Wang M và cộng sự (PMID 42490596), gồm trang tạp chí, preprint, dataset/supplement, cited-by và bài kết quả.

Nếu output mới đã trả lời phần lớn câu hỏi chính hoặc làm phần đóng góp còn lại không đủ quan trọng cho một bài riêng, G3 chuyển `FAIL`, nghiên cứu dừng để `REFRAME`; không được chỉ đổi tên schema để giữ tuyên bố tính mới.

## 10. Bộ chuẩn đối chiếu quốc tế

Bộ chuẩn gồm tối đa năm nguồn được định trước và không phải một tổng quan phạm vi toàn cầu thứ hai. Các vị trí ứng viên bao gồm:

1. nguồn WHO chuyên biệt về đạo đức/quản trị AI cho y tế;
2. khung liên chính phủ toàn cầu về đạo đức AI;
3. hướng dẫn quản trị AI y tế có khả năng áp dụng ở cấp cơ sở;
4. tổng quan quốc tế toàn diện và cập nhật gần nhất về quản trị AI trong tổ chức/hệ thống y tế;
5. tối đa một nguồn châu Á/Đông Nam Á nếu bổ sung yêu cầu bối cảnh độc lập.

`international-benchmark.md` ghi nguồn ứng viên/chọn–loại, tình trạng cập nhật, quan hệ dẫn chiếu, ma trận khung sơ cấp và bộ thay thế khi có ứng viên tương đương. [`component-benchmark-register.md`](component-benchmark-register.md) ghi các `component_id`, định nghĩa thao tác và quy tắc gộp tối đa tám miền. Lộc Đặng đã hoàn tất rà soát độc lập ngày 31/07/2026; bộ chuẩn đạt `PASS_BY_LOC_DANG_REVIEW` và mapping cấp cấu phần đã khóa.

Một cấu phần chỉ được xác lập là chuẩn đối chiếu khi xuất hiện trong ít nhất hai framework sơ cấp độc lập, trong đó có ít nhất một nguồn chuyên biệt y tế. Tính độc lập được đánh giá theo nguồn gốc khung và chuỗi dẫn chiếu ở cấp cấu phần. Tổng quan/bản đồ bao phủ, gồm Wang và Alami, chỉ hỗ trợ kiểm tra phạm vi, định vị khung sơ cấp và mô tả giới hạn bằng chứng; không được tính là xác nhận độc lập cho framework sơ cấp nằm trong tập của chúng. Cấu phần đơn nguồn liên quan trực tiếp đến quyền cơ bản hoặc nguy cơ nghiêm trọng đối với an toàn người bệnh được báo cáo riêng là “vấn đề mới nổi có hệ quả cao”, nêu locator và lý do hệ quả cao, nhưng không được đếm như một khoảng trống hoặc dùng để nâng ngưỡng.

## 11. Lựa chọn nguồn và sàng lọc kép

### 11.1. `SCREENING_EXTRACTION_CODEBOOK_GATE`

Gate có trạng thái `NOT_RUN` tại phiên bản 0.1 và chỉ đạt `PASS` khi codebook/biểu mẫu cùng phiên bản đã khóa:

1. tiêu chí đủ điều kiện và lý do loại thao tác được ở tiêu đề/tóm tắt và toàn văn;
2. toàn bộ trường data-charting và định nghĩa trường;
3. ví dụ dương tính, âm tính và ca biên cho tiêu chí, bốn trạng thái và trường quyết định gap;
4. quy tắc tổng hợp từ data chart cấp source/document lên trạng thái aggregate `component_id × scope_id`;
5. cách xử lý nhiều nguồn chỉ thể hiện một phần, nguồn xung đột, tầng thẩm quyền và khác biệt phạm vi;
6. quy tắc gán nhiều nhãn gap cho cùng cấu phần;
7. đơn vị đếm: coverage dùng `component_id × scope_id`; gap dùng `component_id × gap_type × scope_id` và chỉ đếm một lần trong mỗi tổ hợp, bất kể có bao nhiêu nguồn hỗ trợ; số document/framework được báo cáo riêng bằng ID để tránh double count;
8. `record-registry-codebook.md` và `record-registry-template.csv` đã khóa schema manifestation, provenance nhiều–nhiều, canonicalization, framework link, screening/adjudication, missingness và audit append-only; template header-only có kiểm tra UTF-8/RFC 4180;
9. kết quả field-test biểu mẫu và hiệu chuẩn theo Mục 11.2.

Khi tổng hợp, nhiều nguồn có bằng chứng chưa đủ từng phần chỉ được gán aggregate `REPRESENTED` nếu chúng cùng áp dụng cho một `scope_id`, có thẩm quyền/phạm vi tương thích, cùng nhau đáp ứng toàn bộ yếu tố cốt lõi và không có xung đột chưa giải quyết. Nguồn có phạm vi hẹp không được suy rộng thành bao phủ quốc gia. Với yêu cầu chuẩn tắc, nguồn có thẩm quyền cao hơn chi phối trong phần phạm vi chồng lấp; nguồn cấp thấp hơn có thể bổ sung bằng chứng triển khai nhưng không ghi đè nghĩa vụ cấp cao hơn. Xung đột cùng tầng hoặc phạm vi không thể quy đổi được giữ ở aggregate `INSUFFICIENT_INFORMATION` hoặc trình bày phân tầng cho đến khi phân xử. Một cấu phần có thể nhận nhiều loại gap, nhưng mỗi tổ hợp `component_id × gap_type × scope_id` chỉ được đếm một lần sau khi trạng thái aggregate đã đồng thuận; không tạo gap count từ việc một source riêng không phát biểu.

Field-test biểu mẫu trước đăng ký dùng record/document từ `PRE_REGISTRATION_SEARCH_DEVELOPMENT` hoặc nguồn mốc chỉ cho mục đích huấn luyện/kiểm tra công cụ. Kết quả không tạo corpus, count PRISMA hoặc quyết định đủ điều kiện chính thức.

### 11.2. Hiệu chuẩn

Hai người dùng độc lập cùng codebook và biểu mẫu:

1. **Tiêu đề/tóm tắt:** lấy ngẫu nhiên 25 record từ pool validation; nếu pool có dưới 25 thì dùng toàn bộ. Nhật ký lưu cách lấy mẫu và random seed. Điều kiện đạt là đồng thuận ban đầu ít nhất 75% và mọi bất đồng được thảo luận/ghi lý do. Nếu việc thảo luận làm thay đổi codebook có thể ảnh hưởng quyết định, lặp lại trên một mẫu mới 25 record hoặc toàn bộ pool mới nếu dưới 25; tiếp tục cho đến khi đạt.
2. **Toàn văn:** chọn có chủ đích 8 document, hoặc toàn bộ nếu pool có dưới 8, để tối đa hóa đa dạng loại nguồn, tầng thẩm quyền, ngôn ngữ và gồm ít nhất một ca biên nếu có. Hai người quyết định độc lập. Điều kiện đạt là đồng thuận ban đầu ít nhất 75%, mọi bất đồng được giải quyết/ghi lại; thay đổi codebook ảnh hưởng quyết định buộc lặp trên mẫu đa dạng mới theo cùng cỡ.
3. **Trích xuất:** field-test biểu mẫu trên 8 document đa dạng hoặc toàn bộ nếu pool có dưới 8. Hai người trích xuất độc lập các trường quyết định gap; điều kiện đạt là ít nhất 75% đồng thuận theo trường phân loại không rỗng, mọi locator và bất đồng được kiểm tra. Thay đổi định nghĩa trường, aggregation hoặc gap có thể ảnh hưởng kết quả buộc lặp trên mẫu mới theo cùng cỡ.

Có thể báo cáo kappa như chỉ số mô tả, nhưng không dùng kappa làm hard gate. `SCREENING_EXTRACTION_CODEBOOK_GATE` chỉ đạt khi cả ba bước đạt, toàn bộ bất đồng đã được xử lý và codebook/biểu mẫu/version log được khóa.

### 11.3. Sàng lọc chính thức

Không có sàng lọc chính thức khi G2, `SCREENING_EXTRACTION_CODEBOOK_GATE` hoặc calibration chưa đạt `PASS`. Khi đủ điều kiện, quy trình gồm:

1. nhập mọi record của tìm kiếm chính thức vào registry chung, giữ provenance và khử trùng lặp toàn cục;
2. hai người sàng lọc tiêu đề/tóm tắt độc lập; nguồn không có tóm tắt được chuyển theo tiêu đề/metadata sang toàn văn khi không thể loại chắc chắn;
3. hai người sàng lọc toàn văn độc lập;
4. ghi một lý do loại chuẩn hóa cho mỗi document bị loại ở toàn văn;
5. thảo luận bất đồng; trường hợp chưa giải quyết được chuyển người phân xử theo Mục 5.1;
6. khóa phiên bản quyết định và nhật ký trước khi tổng hợp.

Các trường quyết định một nguồn đủ điều kiện hoặc quyết định khoảng trống phải được mã hóa bởi hai người. Trường mô tả có thể do một người trích xuất và người thứ hai kiểm tra.

## 12. Trích xuất dữ liệu

Mỗi document đủ điều kiện được trích xuất tối thiểu:

- ID record/document/framework;
- trích dẫn, năm, ngôn ngữ, loại nguồn, cơ quan/tác giả;
- tầng thẩm quyền, tình trạng pháp lý, ngày hiệu lực và phạm vi áp dụng;
- quy định chuyển tiếp/hạn tuân thủ và thời gian triển khai khả dụng đến ngày tìm kiếm;
- loại AI và bối cảnh y tế;
- nguyên tắc/giá trị;
- actor chịu trách nhiệm;
- quyền quyết định/phê duyệt/dừng hoặc khiếu nại;
- kiểm soát, cơ chế thực hiện hoặc thực thi;
- hồ sơ/bằng chứng/giám sát;
- quyền người bệnh;
- điều kiện năng lực được quy định hoặc ghi nhận công khai;
- trạng thái bằng chứng triển khai;
- phạm vi và chủ thể triển khai;
- bằng chứng thành lập, nhiệm vụ và hoạt động của cơ quan/hội đồng, nếu có;
- chỉ số/đầu ra giám sát, sự cố, khiếu nại và hành động khắc phục, nếu có;
- miền kết quả/tác động, thiết kế đánh giá, nhóm so sánh/thời điểm đo và giới hạn quy kết, nếu có;
- đánh giá chất lượng;
- nguồn tài trợ của source/document;
- vai trò của bên tài trợ, nếu source/document có báo cáo;
- xung đột lợi ích của source/document, nếu có báo cáo;
- mã quy nạp, mã chỉ từ Chương 10, người trích xuất và ghi chú.

Ba trường tài trợ/xung đột lợi ích dùng các giá trị kiểm soát `NOT_REPORTED` khi loại tài liệu có thể báo cáo nhưng không tìm thấy thông tin sau khi kiểm tra toàn văn/phần khai báo, và `NOT_APPLICABLE` khi trường đó không phù hợp về cấu trúc đối với loại nguồn hoặc không có bên tài trợ để mô tả vai trò. `SCREENING_EXTRACTION_CODEBOOK_GATE` chỉ được `PASS` khi codebook định nghĩa từng trường, locator cần lưu và quy tắc phân biệt giá trị tường minh, `NOT_REPORTED` và `NOT_APPLICABLE`.

**Bằng chứng dương tính** là phát biểu tường minh hoặc tương đương về chức năng trong một nguồn trực tiếp đủ điều kiện, có locator và đủ ngữ cảnh để gắn với cấu phần. Sự xuất hiện của phát biểu chỉ chứng minh cấu phần được thể hiện trong nguồn; nó không chứng minh cơ chế đã được triển khai hoặc có hiệu quả.

Ở cấp source/document, các trường chỉ chart: bằng chứng dương tính có locator; `NO_STATEMENT_IN_SOURCE` khi source đủ đọc nhưng không phát biểu; `UNCERTAIN_SOURCE_EVIDENCE` khi có dấu vết nhưng locator/nghĩa/phạm vi chưa đủ chắc; hoặc `NOT_APPLICABLE`. `NOT_REPORTED` dành cho trường khai báo phù hợp như tài trợ/COI. Không gán `REPRESENTED`, `PARTIALLY_REPRESENTED`, `NOT_FOUND` hay `INSUFFICIENT_INFORMATION` cho một source/document, và không diễn giải `NO_STATEMENT_IN_SOURCE` thành bằng chứng không tồn tại.

### 12.1. Phân tầng bằng chứng triển khai và kết quả

Mỗi phát biểu về việc một khung, chính sách, cơ quan hoặc hội đồng “đi vào đời sống” được mã hóa theo loại bằng chứng, không suy từ hiệu lực pháp lý sang vận hành:

| Mã                      | Loại bằng chứng                | Điều kiện tối thiểu                                                                                                                                                                  |
| ------------------------ | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NORMATIVE_LEGAL_ONLY` | Chuẩn tắc/pháp lý             | Có văn bản, nguyên tắc hoặc khung được ban hành/xác minh; chưa có bằng chứng triển khai trong chính nguồn đó.                                                         |
| `INSTITUTIONALIZATION` | Thể chế hóa                    | Có quyết định thành lập, nhiệm vụ, thành viên/chủ thể, quy trình, nguồn lực hoặc công cụ thực hiện có locator.                                                       |
| `ADOPTION_ACTIVITY`    | Áp dụng/hoạt động            | Có bằng chứng công khai về thí điểm, sử dụng, đào tạo, tự đánh giá, kiểm tra, phiên họp hoặc hoạt động tại cơ quan/cơ sở xác định.                         |
| `MONITORING_OUTPUT`    | Giám sát/đầu ra               | Có chỉ số, biên bản, báo cáo kiểm tra/audit, sự cố, khiếu nại, khắc phục hoặc kết quả giám sát được công bố.                                                      |
| `OUTCOME_EVALUATION`   | Đánh giá kết quả/tác động | Có đo lường thay đổi liên quan an toàn, công bằng, quyền riêng tư, tự chủ người bệnh, trách nhiệm giải trình, tiếp cận hoặc quy trình/chất lượng chăm sóc. |

Các mã có thể cùng xuất hiện đối với một framework nhưng phải gắn với document, phạm vi, thời gian và locator riêng; chúng không được cộng thành một điểm trưởng thành tuyến tính. Đối với `OUTCOME_EVALUATION`, trích xuất thêm thiết kế nghiên cứu/đánh giá, nhóm so sánh nếu có, thời điểm đo, miền kết quả, nguồn dữ liệu và giới hạn sai lệch/quy kết. Chỉ dùng từ “tác động” theo nghĩa nhân quả khi thiết kế nguồn hỗ trợ; các báo cáo mô tả hoặc tự báo cáo chỉ chứng minh có hoạt động/kết quả được công bố.

Khi văn bản có thời kỳ chuyển tiếp hoặc hạn tuân thủ chưa kết thúc tại ngày tìm kiếm, phân tích phải ghi `TRANSITION_PERIOD_ACTIVE`, ngày hết hạn và số tháng triển khai khả dụng. Việc chưa tìm thấy bằng chứng hoạt động/kết quả trong giai đoạn này được mô tả là khoảng trống bằng chứng triển khai sớm; không được tự động mã hóa thành thất bại thực thi hoặc thất bại chính sách.

Nếu tìm thấy văn bản thành lập một Hội đồng đạo đức AI quốc gia hoặc cơ chế tương đương, sự tồn tại pháp lý, nhiệm vụ, thành phần, hoạt động, đầu ra giám sát và kết quả/tác động phải được mã hóa tách biệt. Không tìm thấy một lớp bằng chứng sau quy trình đầy đủ chỉ được báo cáo là “chưa tìm thấy trong nguồn công khai đã tìm theo protocol”.

## 13. Đánh giá thẩm quyền và chất lượng nguồn

Đánh giá không dùng để tạo một điểm chất lượng chung hoặc loại cơ học nguồn đủ điều kiện. Kết quả được dùng để giới hạn sức mạnh suy luận:

- văn bản pháp luật/quy định: loại văn bản, cơ quan ban hành, phạm vi, hiệu lực, sửa đổi/thay thế và tính ràng buộc;
- hướng dẫn/chính sách chính thức: thẩm quyền, phương pháp xây dựng, đối tượng, phạm vi và mức ràng buộc;
- nghiên cứu: công cụ JBI phù hợp với thiết kế;
- nguồn xám: AACODS, xét thẩm quyền, độ chính xác, độ bao phủ, tính khách quan, thời điểm và ý nghĩa; thay công cụ cần amendment trước khi áp dụng.

Bao phủ quy định và chất lượng bằng chứng triển khai là hai trục riêng. Một quy định mạnh về thẩm quyền không tự chứng minh triển khai; một báo cáo triển khai đơn lẻ không tự tạo nghĩa vụ toàn hệ thống.

## 14. Mã hóa trạng thái đối chiếu ở tầng tổng hợp

Bốn trạng thái chỉ được gán một lần cho mỗi aggregate `component_id × scope_id`, sau khi tìm kiếm chính thức và mọi kênh bắt buộc hoàn tất, toàn bộ nguồn đủ điều kiện trong scope được chart, version/dẫn chiếu được kiểm tra, các trường quyết định được mã hóa kép và hai reviewer đã đồng thuận hoặc phân xử. Không dùng bốn trạng thái ở cấp source/document hoặc trong bảng trích xuất từng nguồn.

| Trạng thái aggregate       | Quy tắc thao tác                                                                                                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REPRESENTED`              | Tập nguồn đủ điều kiện của đúng scope, xét theo thẩm quyền, đáp ứng đủ chủ thể, hành động/kiểm soát và bằng chứng cốt lõi.                                                                       |
| `PARTIALLY_REPRESENTED`    | Tổng hợp có nội dung tương ứng nhưng còn thiếu ít nhất một chi tiết vận hành cốt lõi, bị giới hạn phạm vi/đối tượng hoặc chỉ có khuyến nghị yếu; phần có và phần thiếu được nêu rõ.  |
| `NOT_FOUND`                | Sau toàn bộ quy trình, không có source đủ điều kiện đáp ứng cấu phần trong scope. Chỉ nghĩa là chưa tìm thấy trong tập nguồn công khai đã tìm theo protocol, không khẳng định không tồn tại. |
| `INSUFFICIENT_INFORMATION` | Sau tổng hợp, có dấu vết nhưng toàn bộ bằng chứng vẫn thiếu locator, thẩm quyền, version hoặc phạm vi để phân loại chắc chắn; ghi rõ thông tin thiếu và không quy về`NOT_FOUND`.                 |

Phân tích chính chỉ sử dụng trạng thái aggregate đã đồng thuận. Các trường source-level quyết định khoảng trống được mã hóa kép; ca `NO_STATEMENT_IN_SOURCE`, `UNCERTAIN_SOURCE_EVIDENCE`, phát biểu mâu thuẫn và khác biệt theo tầng nguồn được giữ trong bảng chi tiết. Coverage/status đếm một lần mỗi `component_id × scope_id`. Gap chỉ được gán sau aggregate consensus và đếm một lần mỗi `component_id × gap_type × scope_id`, bất kể số source hỗ trợ.

## 15. Tổng hợp và phân tích khoảng trống

### 15.1. Tổng hợp mô tả

Nghiên cứu trình bày:

- lưu đồ PRISMA-ScR cho tập Việt Nam;
- phân bố document theo năm, loại, tầng thẩm quyền, phạm vi và trạng thái hiệu lực;
- phân bố bằng chứng theo `NORMATIVE_LEGAL_ONLY`, `INSTITUTIONALIZATION`, `ADOPTION_ACTIVITY`, `MONITORING_OUTPUT` và `OUTCOME_EVALUATION`, kèm loại thiết kế và giới hạn suy luận;
- một bảng tích hợp tối đa tám miền quản trị, nối nguyên tắc với actor, quyền quyết định, kiểm soát, bằng chứng và quyền người bệnh;
- chi tiết mở rộng trong research record/phụ lục nếu được phép, nhưng không thay thế báo cáo cốt lõi của từng nguồn trong bài chính.

Trong bài chính, mỗi nguồn Việt Nam được phân tích phải truy vết được qua trích dẫn; đặc điểm tối thiểu gồm năm, loại và thẩm quyền hoặc phạm vi; kết quả riêng của nguồn liên quan câu hỏi; đánh giá/hạn chế; nguồn tài trợ, vai trò bên tài trợ và xung đột lợi ích bằng giá trị tường minh hoặc `NOT_REPORTED`/`NOT_APPLICABLE`. Các trường này có thể được trình bày gọn qua bảng tích hợp và phần diễn giải, nhưng không được chuyển toàn bộ sang research record/phụ lục.

### 15.2. Năm loại khoảng trống

1. **Khoảng trống chuẩn tắc:** chuẩn đối chiếu đủ điều kiện chưa được thể hiện hoặc chỉ được thể hiện một phần trong nguồn Việt Nam đủ thẩm quyền.
2. **Khoảng trống chuyển hóa:** nguyên tắc có mặt nhưng chưa được chuyển thành yêu cầu/quy trình/kiểm soát vận hành đủ rõ.
3. **Khoảng trống trách nhiệm:** thiếu hoặc mơ hồ actor chịu trách nhiệm, quyền quyết định, quyền dừng, cơ chế giám sát hoặc tuyến giải trình.
4. **Khoảng trống bằng chứng:** thiếu yêu cầu về hồ sơ, kiểm định, theo dõi, audit, báo cáo sự cố hoặc bằng chứng triển khai được công bố.
5. **Khoảng trống điều kiện năng lực công bố:** nguồn công khai chưa mô tả đủ điều kiện nhân lực, chuyên môn, dữ liệu, hạ tầng hoặc năng lực tổ chức cần cho yêu cầu quản trị.

Một gap chỉ được tính khi cấu phần đã đạt ngưỡng chuẩn quốc tế tại Mục 10 và trạng thái Việt Nam đã được xác lập theo Mục 14. Vấn đề đơn nguồn có hệ quả nghiêm trọng được trình bày riêng, không gộp vào số gap. Kết luận phải phân biệt:

- bao phủ trong quy định/chính sách;
- chất lượng bằng chứng triển khai công khai;
- điều kiện năng lực được văn bản quy định hoặc nguồn công khai ghi nhận.

Nghiên cứu không suy diễn sự vắng mặt của bằng chứng công khai thành không tồn tại trong thực tế; không tuyên bố năng lực thực tế của bệnh viện Việt Nam nếu không có dữ liệu thực địa.

## 16. Vai trò của Chương 10 và kiểm soát ảnh hưởng

Chương 10 của *Đạo đức AI: Nguyên tắc và Thực hành* được dùng như nguồn khái niệm:

- mục tiêu, điểm đau và trục giá trị lâm sàng–an toàn người bệnh–khả năng kiểm chứng: tr. 413–418;
- quyền tự quyết của người bệnh: tr. 451–452;
- danh sách tự rà soát cùng các mục trách nhiệm, kiểm soát và bằng chứng vận hành: tr. 453–455.

Các định vị trên được kiểm tra từ bản full chuẩn: `C:\Users\DELL\Documents\2. Research & Writing\AI Ethics Book\Extracted\Dao_duc_AI_20.5.26_full.md`. Không dùng file chương tách để dẫn trang.

Chương 10 chỉ là lăng kính khái niệm và không được tự xác nhận kết quả. Người không phải tác giả chương hoàn tất nhánh quy nạp trước khi xem mã riêng của Chương 10. Nhóm so sánh:

1. kết quả chỉ từ mã quy nạp và bộ chuẩn quốc tế;
2. kết quả sau khi thêm mã Chương 10.

Mọi thay đổi về số gap, phân loại hoặc diễn giải được báo cáo như phân tích độ nhạy. Mã chỉ xuất hiện từ Chương 10 nhưng không có bằng chứng trực tiếp đủ điều kiện không được nâng thành kết quả.

## 17. Quản trị protocol và sai lệch

### 17.1. Phân loại amendment

| Loại                      | Ví dụ                                                                                                  | Xử lý                                                                                                                                                                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hành chính               | Sửa lỗi chính tả, đường dẫn hoặc trình bày không đổi quyết định                         | Tăng phiên bản phụ, ghi nhật ký và xác nhận không ảnh hưởng dữ liệu/quyết định.                                                                                         |
| Làm rõ phương pháp    | Làm rõ thuật ngữ hoặc quy tắc nhưng không đổi tập đủ điều kiện                           | Ghi trước khi áp dụng, đánh giá ảnh hưởng và để hai người phê duyệt.                                                                                                     |
| Thực chất                | Đổi câu hỏi, PCC, tiêu chí, nguồn, truy vấn, benchmark, ngưỡng gap hoặc quy trình tổng hợp | Tăng phiên bản, nêu lý do và ảnh hưởng, đặt lại các cổng phụ thuộc; nếu đã đóng dấu thời gian thì đăng amendment công khai trước khi áp dụng khi có thể. |
| Sai lệch không dự kiến | Không thể thực hiện một bước đã khóa hoặc có biến cố sau khi bắt đầu                    | Ghi deviation với thời điểm phát hiện, nguyên nhân, tác động, biện pháp giảm thiểu và báo cáo trong bản thảo.                                                         |

Mỗi amendment có ID, phiên bản/ngày, người đề xuất, lý do, thay đổi, ảnh hưởng đến dữ liệu/cổng/kết luận, người phê duyệt và locator. Thay đổi mở rộng nghiên cứu sang thẩm định hoặc khuyến nghị lâm sàng phải bổ sung năng lực y tế phù hợp trước khi áp dụng. Không sửa hồi tố mà không để lại lịch sử.

Sau đăng ký, mọi thay đổi thực chất phát sinh từ pilot khả thi G4–G5 phải được công bố như amendment trước khi chạy lại pilot hoặc tìm kiếm chính thức. Không được âm thầm thay truy vấn, codebook, tiêu chí, nguồn, quy tắc dừng hoặc aggregation rồi ghép count từ các phiên bản.

### 17.2. Đăng ký và lưu trữ công khai

Khi G2, `SCREENING_EXTRACTION_CODEBOOK_GATE`, `PRISMA_SCR_PROTOCOL_MAP_GATE`, exact search strategy sau validation, bộ chuẩn quốc tế, competitive checkpoint và khai báo tài trợ đều đạt `PASS`, nhóm tạo một bản protocol bất biến và các phụ lục khóa, tải lên OSF hoặc kho công khai ổn định có dấu thời gian, rồi ghi URL/DOI thực tế vào manifest nghiên cứu. `TEAM_EXPERTISE_GATE=NOT_APPLICABLE_SCOPE_NARROWED` và không thuộc điều kiện đăng ký. `PRISMA_SCR_MANUSCRIPT_GATE` cũng không thuộc điều kiện đăng ký. Trạng thái chỉ chuyển khỏi `NOT_REGISTERED` khi locator công khai được kiểm tra. Bản đăng ký phải kèm:

- protocol đã khóa;
- artifact [`prisma-scr-checklist.md`](prisma-scr-checklist.md) chứng minh `PRISMA_SCR_PROTOCOL_MAP_GATE=PASS`;
- chiến lược tìm kiếm đầy đủ và artifact `PRE_REGISTRATION_SEARCH_DEVELOPMENT`;
- bộ chuẩn quốc tế;
- codebook sàng lọc/trích xuất;
- codebook và template registry record;
- manifest phiên bản và checksum.

## 18. Quản lý dữ liệu và khả năng tái lập

- Dữ liệu bảng dùng UTF-8 CSV; tài liệu phương pháp dùng Markdown/PDF; raw export giữ nguyên định dạng nguồn.
- Mỗi record, document, framework, query, search run và amendment có ID ổn định.
- Raw export, ảnh chụp, manifest và checksum là bất biến; file dẫn xuất được định danh riêng.
- Tên tệp chứa ngày theo ISO, kênh, loại artifact và phiên bản; manifest ghi kích thước, checksum SHA-256, ngày tạo, người tạo và quan hệ với tệp nguồn.
- Registry lưu provenance đa kênh, quyết định khử trùng lặp, phiên bản, người sàng lọc, ngày và lý do.
- Dữ liệu công khai được lưu trong workspace kiểm soát truy cập trong quá trình nghiên cứu và công bố ở mức pháp luật/bản quyền cho phép. Tài liệu có hạn chế bản quyền chỉ công bố metadata, locator và dữ liệu trích xuất hợp lệ.
- Bản protocol, codebook, search log, registry đã khử thông tin nhạy cảm, bảng trích xuất, script chuyển đổi và manifest cuối được bảo quản trên OSF/kho ổn định và một bản sao lưu cục bộ. Thời hạn bảo quản tuân theo quy định của cơ quan và tạp chí; không tự đặt thời hạn ngắn hơn yêu cầu của các bên này.

## 19. Đạo đức nghiên cứu và sử dụng AI

Đây là nghiên cứu bàn giấy trên tài liệu công khai, không tuyển người tham gia và không thu dữ liệu cá nhân mới. Nhiều cơ quan có thể không yêu cầu thẩm định đạo đức cho dạng nghiên cứu này, nhưng nhóm phải kiểm tra quy định của cơ quan chủ trì và tạp chí trước khi bắt đầu; protocol không tuyên bố miễn thẩm định có giá trị phổ quát.

`FUNDING_DECLARATION_GATE=PASS`. Ngày 31/07/2026, chủ trì xác nhận nghiên cứu không nhận grant, hợp đồng, tài trợ hiện vật hay hỗ trợ có điều kiện dành riêng cho tổng quan này. Không có bên tài trợ tham gia thiết kế, xây dựng protocol, tìm kiếm, lựa chọn, trích xuất, phân tích, viết hoặc quyết định công bố; vai trò bên tài trợ là `NOT_APPLICABLE`. Locator: [`funding-declaration.md`](funding-declaration.md).

AI có thể hỗ trợ tổ chức cấu trúc, hiệu chỉnh ngôn ngữ, kiểm tra nhất quán, định dạng truy vấn hoặc gợi ý phát hiện trùng. AI không được:

- tự chủ quyết định đưa vào/loại;
- thay người rà soát trong sàng lọc;
- tự chủ trích xuất hoặc mã hóa trường quyết định gap;
- tạo trích dẫn không được con người kiểm tra;
- phân xử bất đồng.

Mọi đầu ra AI được con người kiểm tra với nguồn gốc, ghi công cụ/phiên bản, ngày, mục đích và phần bị tác động. Con người chịu trách nhiệm về chiến lược tìm kiếm, lựa chọn nguồn, trích xuất, trích dẫn, phân tích và diễn giải. AI không được ghi là tác giả. Bản thảo phải khai báo việc sử dụng AI theo chính sách tạp chí.

## 20. Cổng khả thi xuất bản

Bài dự kiến tối đa 8 trang A4, gồm bảng, hình và tài liệu tham khảo; tối đa 25 tài liệu tham khảo. Ngân sách tài liệu:

| Nhóm                              |     Tối đa |
| ---------------------------------- | -----------: |
| Phương pháp JBI/PRISMA-ScR      |            2 |
| Benchmark quốc tế và tính mới |            6 |
| Chương 10                        |            1 |
| Việt Nam/bối cảnh               |           16 |
| **Tổng**                    | **25** |

Sản phẩm trong bài gồm một sơ đồ PRISMA và một bảng tích hợp tối đa tám miền quản trị kèm phần diễn giải. `reference-budget-ledger.md` là ledger chung theo `reference_id`: một nguồn chỉ chiếm một slot ngân sách, dù được dùng ở nhiều phần; sáu slot benchmark/tính mới gồm năm nguồn B1–B5 và citation NIST cho phân tích độ nhạy. Protocol Wang M (`N-01`) là `COMPETITIVE_RESERVE_NOT_IN_FINAL_BUDGET`; nếu cần dẫn trong bản cuối, nó phải thay một slot benchmark/tính mới khác hoặc kích hoạt `RESCOPE`. Ledger phải chỉ rõ nhóm chính, vai trò, locator, trạng thái chọn/loại và tổng bốn nhóm là 25. Chi tiết mở rộng có thể lưu trong research record/phụ lục nếu tạp chí cho phép nhưng không thay thế báo cáo cốt lõi của từng nguồn trong bài chính theo Mục 15.1.

Trước sàng lọc chính thức, G6 phải chứng minh ngân sách 25 nguồn khả thi. G7 chỉ đạt `PASS` khi một bản thử theo đúng định dạng tạp chí gồm hai tóm tắt, một sơ đồ PRISMA giả lập, một bảng tích hợp tối đa tám hàng kèm phần diễn giải, 25 tài liệu tham khảo đại diện và 16 nguồn Việt Nam mô phỏng; với từng nguồn mô phỏng, bài chính phải truy vết được trích dẫn, đặc điểm tối thiểu gồm năm/loại/thẩm quyền hoặc phạm vi, kết quả riêng liên quan câu hỏi, đánh giá/hạn chế, nguồn tài trợ, vai trò bên tài trợ và xung đột lợi ích bằng giá trị tường minh hoặc `NOT_REPORTED`/`NOT_APPLICABLE`. Toàn bài phải không quá 7,4 trang nội dung và giữ 0,6 trang dự phòng, tổng không quá 8,0 trang.

Nếu bản thử không đáp ứng bất kỳ điều kiện nào, G7=`FAIL` và nghiên cứu `STOP` trước sàng lọc chính thức. Nhóm phải thiết kế lại bảng, thu hẹp nội dung theo tiêu chí định trước hoặc chuyển tạp chí; không được loại nguồn hậu nghiệm sau khi biết kết quả. Phụ lục không được dùng để che việc bài chính thiếu báo cáo cốt lõi.

## 21. Điều kiện chuyển giai đoạn

| Giai đoạn                                        | Điều kiện                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Pre-registration search-development validation` | Chỉ phát triển/kiểm tra chiến lược theo Mục 9.3; artifact và count tách riêng; không tạo corpus, PRISMA hoặc quyết định đủ điều kiện.                                                                                                                                                                                                                  |
| Đóng dấu thời gian/đăng ký                  | G2,`SCREENING_EXTRACTION_CODEBOOK_GATE`, `PRISMA_SCR_PROTOCOL_MAP_GATE`, exact search strategy đã qua validation, benchmark tối đa năm nguồn, competitive checkpoint và khai báo tài trợ đều `PASS`; `TEAM_EXPERTISE_GATE=NOT_APPLICABLE_SCOPE_NARROWED`; `PRISMA_SCR_MANUSCRIPT_GATE` không chặn giai đoạn này; version và checksum đã khóa. |
| Pilot khả thi G4–G5                              | Protocol đã đăng ký; G1–G3 còn hiệu lực trên cùng phiên bản; hai người sẵn sàng; chiến lược, codebook và quy tắc dừng đã khóa; count tách khỏi PRISMA.                                                                                                                                                                                           |
| Tìm kiếm chính thức                            | G4–G5 đều`PASS`; mọi thay đổi thực chất từ pilot đã được đăng amendment và kiểm tra lại; ngày bắt đầu chính thức được ghi.                                                                                                                                                                                                                     |
| Sàng lọc chính thức                            | Tìm kiếm chính thức đã tạo registry đầu vào; G6=`PASS`; G7=`PASS` theo toàn bộ hợp đồng bản thử tại Mục 20; `SCREENING_EXTRACTION_CODEBOOK_GATE` và calibration còn hiệu lực; G7=`FAIL` buộc `STOP`, và không có dependency nào ở trạng thái `PENDING_CONFIRMATION`, `NOT_RUN`, `FAIL` hoặc `BLOCKED`.                     |
| Phân tích/kết luận                             | Trích xuất kép các trường quyết định gap; nhánh quy nạp hoàn tất trước khi mở mã Chương 10; đánh giá tầng nguồn/chất lượng hoàn tất; bất đồng đã phân xử.                                                                                                                                                                                |
| Nộp bài                                          | `PRISMA_SCR_MANUSCRIPT_GATE=PASS`; competitive checkpoint cuối đạt; sai lệch/amendment, giới hạn, xung đột lợi ích và AI use được báo cáo.                                                                                                                                                                                                                 |

Tại phiên bản `0.6-registered`, quyết định hợp lệ là thực hiện pilot khả thi G4–G5 theo chiến lược và codebook đã khóa. Tìm kiếm chính thức và sàng lọc vẫn bị chặn cho đến khi G4–G5 đạt `PASS` và mọi amendment cần thiết từ pilot đã được công bố.
