# Đặc tả vận hành thu hồi nguồn công khai PR07 v1

| Trường | Giá trị |
| --- | --- |
| Mã tài liệu | `PR07_PUBLIC_SOURCE_RETRIEVAL_OPERATIONAL_SPEC_V1` |
| Ngày khóa vận hành | 2026-08-01 |
| Trạng thái | `READY_FOR_PI_REVIEW_BEFORE_RETRIEVAL` |
| Áp dụng cho | 16 slot nguồn công khai trong Amendment v1 |
| Không áp dụng cho | Screening, eligibility, trích xuất, synthesis hoặc PRISMA count |

## 1. Mục đích và ranh giới

Tài liệu này làm rõ cách vận hành corpus hữu hạn đã được Amendment v1 công bố:
4 hồ sơ pháp lý quốc gia, tối đa 4 tài liệu Bộ Y tế/Bộ Khoa học và Công nghệ,
tối đa 3 tài liệu WHO Việt Nam/UNESCO và tối đa 5 ví dụ địa phương/bệnh viện
chỉ mang tính mô tả. Nó không thay đổi PCC, nguồn, query catalogue, tiêu chí
include/exclude, vai trò reviewer, citation chasing, hoặc trần corpus.

Đặc tả chỉ quyết định một lần thu hồi nào được ghi là hoàn tất về mặt kỹ thuật.
Việc một tài liệu có đủ điều kiện cho tổng quan vẫn thuộc screening kép theo
`screening-codebook.md` đã khóa. Không sử dụng trạng thái slot, thứ hạng ứng
viên, số trang hay ngân sách tài liệu tham khảo để tác động vào screening.

Nguồn thẩm quyền: Amendment v1 đã công bố, `pr07-authoritative-public-source-frame.csv`,
`search-strategy.md`, `implementation-case-sampling-frame.csv` và
`record-registry-codebook.md`. Nếu có mâu thuẫn, registration/amendment công
khai và các tệp frozen có ưu tiên; mâu thuẫn được ghi fail-closed, không được
tự diễn giải.

## 2. Đơn vị, artifact và trạng thái chuẩn

Mỗi lần thử URL tạo một raw response gồm body (kể cả rỗng), headers, thông báo
lỗi nếu có, URL yêu cầu, timestamp UTC và SHA-256. Mỗi URL nguồn được ghi trong
locator ledger với slot, domain, query ID, depth, trạng thái và locator raw.
Khi có tệp PDF/HTML, manifest ghi SHA-256; khi không tải được tệp, checksum là
checksum của raw response/error artifact, không phải checksum tưởng tượng của
nguồn từ xa.

| Trạng thái | Nghĩa vận hành | Không được suy ra |
| --- | --- | --- |
| `RETRIEVED` | Có URL chính thức và artifact cấp tài liệu/metadata đã capture. | Include, độ tin cậy hay kết luận nội dung. |
| `NOT_FOUND` | Đã đạt điều kiện terminal của locator đã khóa nhưng không có URL chính thức phù hợp slot. | Tài liệu hay chính sách không tồn tại. |
| `UNRETRIEVABLE` | Có URL/locator chính thức nhưng ba lần thử không thu được artifact sử dụng được. | Nội dung không tồn tại hoặc không liên quan. |
| `OUT_OF_SCOPE` | URL đã thu hồi nhưng không khớp lớp slot, domain/authority hoặc chỉ là trang kết quả, tin báo chí, fanpage. | Quyết định exclude trong review. |
| `DUPLICATE_ALIAS` | Cùng tài liệu/phiên bản đã có manifestation khác; giữ cả provenance. | Xóa URL hay coi slot đã tự động đủ. |
| `FAIL_CLOSED` | Thiếu raw artifact, manifest/checksum, hoặc terminal evidence. | Nhánh thu hồi hoàn tất. |

`NOT_FOUND`, `UNRETRIEVABLE` và `OUT_OF_SCOPE` là kết quả của một locator hữu
hạn, không phải kết luận phủ định về chính sách hay thực hành ở Việt Nam.

## 3. Quy tắc chung cho mọi slot

1. Chạy locator nội bộ của domain trước, theo query ID đã khóa. Chỉ khi locator
   nội bộ không tạo URL kết quả ngữ nghĩa mới mới dùng `site:` như một công cụ
   định vị; URL chỉ được chấp nhận nếu quay về domain chính thức đã nêu.
2. Mỗi cặp domain × query ID: tối đa 5 trang hoặc 50 URL mới; dừng sớm sau hai
   trang liên tiếp không có URL mới. Độ sâu tối đa 2, và link depth 2 chỉ lấy
   PDF/HTML cùng domain hoặc đường dẫn tài liệu cụ thể từ trang depth 1.
3. Mỗi URL có tối đa 3 lần thử: lần đầu, thử lại sau ít nhất 60 giây, và lần ba
   sau ít nhất 5 phút. HTTP 4xx cố định (trừ 408/429), URL sai cú pháp và DNS
   NXDOMAIN có thể kết thúc sớm nhưng phải lưu raw error. HTTP 408/429/5xx,
   timeout và lỗi kết nối dùng đủ ba lần thử.
4. Một document nhận slot theo thứ tự slot và thứ tự ưu tiên dưới đây. Bản ký,
   PDF chính thức hoặc trang văn bản có metadata được ưu tiên hơn trang tin mô
   tả; bản HTML/PDF của cùng document là alias, không chiếm hai slot.
5. Nếu nhiều document cùng thỏa một locator slot, xếp cố định theo: (a) query
   ID theo thứ tự trong catalogue; (b) channel ưu tiên của slot; (c) ngày ban
   hành mới hơn; (d) normalized URL theo thứ tự chữ cái. Đây là tie-breaker
   thu hồi, không phải phán đoán về chất lượng hay eligibility.
6. Không tìm thêm ngoài locator đã khóa để lấp slot. Nếu slot kết thúc
   `NOT_FOUND`/`UNRETRIEVABLE`, ghi trạng thái đó và tiếp tục readiness audit;
   không thay đổi corpus hay khởi động crawler diện rộng.

## 4. Ma trận 16 slot

### 4.1 Bốn hồ sơ pháp lý quốc gia

Các slot pháp lý đã có seed/quan hệ trực tiếp được xác minh. Chỉ tái thu hồi
để có artifact, manifest và checksum thống nhất; không mở rộng traversal ngoài
điều kiện terminal pháp lý đã khóa.

| Slot | Định danh/locator chính | Domain/cổng ưu tiên | Kết thúc slot |
| --- | --- | --- | --- |
| `VNLAW-01` | `134/2025/QH15` | Cổng văn bản Chính phủ/Công báo | Bản chính thức hoặc `UNRETRIEVABLE` có raw evidence. |
| `VNLAW-02` | `142/2026/NĐ-CP` | Cổng văn bản Chính phủ/Công báo | Như trên. |
| `VNLAW-03` | `05/2026/TT-BKHCN` | Cổng văn bản Chính phủ/Công báo | Như trên. |
| `VNLAW-04` | `55/2025/NĐ-CP` | Cổng văn bản Chính phủ/Công báo | Như trên. |

### 4.2 Bốn slot Bộ Y tế/Bộ Khoa học và Công nghệ

| Slot | Lớp locator | Domain/cổng theo thứ tự | Query ID theo thứ tự | Quy tắc thay thế |
| --- | --- | --- | --- | --- |
| `MINISTRY-01` | Chính sách/kế hoạch AI-y tế cấp Bộ | `moh.gov.vn`, rồi đơn vị trực thuộc Bộ Y tế trong catalogue | `DQ-IMPL-02`, `DQ-IMPL-01`, `DQ-IMPL-04` | Dùng ứng viên kế tiếp theo thứ tự chung; không chuyển sang nguồn ngoài domain. |
| `MINISTRY-02` | Hướng dẫn/triển khai hoặc giám sát AI-y tế cấp Bộ | `moh.gov.vn`, `imda.moh.gov.vn`, `ttyqg.vn`, `kcb.vn` | `DQ-IMPL-04`, `DQ-IMPL-05`, `DQ-EVID-03` | Ưu tiên document khác `MINISTRY-01`; nếu cùng document, ghi alias và chuyển ứng viên kế tiếp. |
| `MINISTRY-03` | Khung/chính sách AI có liên hệ rõ với y tế Việt Nam | `mst.gov.vn` | `DQ-IMPL-03`, `DQ-TOOL-01`, `DQ-TOOL-02` | Không dùng lại `VNLAW-01`–`VNLAW-04`; document trùng chỉ ghi provenance. |
| `MINISTRY-04` | Công cụ, đánh giá tuân thủ/tác động hoặc bằng chứng quản trị AI-y tế | `moh.gov.vn`, rồi `mst.gov.vn` | `DQ-TOOL-01`, `DQ-TOOL-02`, `DQ-EVID-01`, `DQ-EVID-05` | Ứng viên kế tiếp khác ba slot trước; nếu hết, kết thúc trạng thái kỹ thuật phù hợp. |

### 4.3 Ba slot WHO Việt Nam/UNESCO

| Slot | Lớp locator | Domain/cổng theo thứ tự | Query ID theo thứ tự | Quy tắc thay thế |
| --- | --- | --- | --- | --- |
| `INTL-01` | WHO Việt Nam: AI/y tế tại Việt Nam | `who.int/vietnam` | `DQ-IMPL-03`, `DQ-EVID-04` | Ứng viên kế tiếp cùng domain theo thứ tự chung. |
| `INTL-02` | UNESCO: RAM/đạo đức AI gắn Việt Nam | `unesco.org/ethics-ai/en/vietnam`, rồi `unesco.org` | `DQ-IMPL-03`, `DQ-TOOL-01` | Giữ document WHO/UNESCO khác `INTL-01`; không thay bằng báo chí hoặc trang kết quả. |
| `INTL-03` | WHO Việt Nam hoặc UNESCO: quản trị/triển khai AI-y tế có quan hệ Việt Nam | `who.int/vietnam`, rồi `unesco.org/ethics-ai/en/vietnam` | `DQ-IMPL-03`, `DQ-EVID-04`, `DQ-EVID-05` | Ứng viên kế tiếp khác hai slot trước; nếu không có, ghi kết quả kỹ thuật, không mở thêm tổ chức quốc tế. |

### 4.4 Năm slot ví dụ địa phương/bệnh viện

Đây là các ví dụ mô tả; chúng không đại diện cho tỷ lệ áp dụng toàn quốc. Năm
slot dùng một thứ tự đã khóa trong sampling frame nhằm giữ ba miền và tương phản
công/tư. Mỗi slot là **một tài liệu** từ case tương ứng, không phải toàn bộ case.

| Slot | Case chính | Case thay thế theo thứ tự cố định | Domain | Query ID |
| --- | --- | --- | --- | --- |
| `SENTINEL-01` | `DOH-N-01` Sở Y tế Hà Nội | Không có | `soyte.hanoi.gov.vn` | Mười query `DQ-IMPL-01` đến `DQ-EVID-05` trong frame. |
| `SENTINEL-02` | `DOH-C-01` Sở Y tế Đà Nẵng | Không có | `soyte.danang.gov.vn` | Như trên. |
| `SENTINEL-03` | `DOH-S-01` Sở Y tế TP.HCM | Không có | `medinet.gov.vn` | Như trên. |
| `SENTINEL-04` | `HOSP-N-01` Bạch Mai | `HOSP-C-01` Trung ương Huế; `HOSP-S-01` Chợ Rẫy | Domain frozen của case tương ứng | Như trên. |
| `SENTINEL-05` | `HOSP-N-02` Vinmec Times City | `HOSP-S-02` Tâm Anh TP.HCM; `HOSP-S-03` ĐH Y Dược TP.HCM | Domain frozen của case tương ứng | Như trên. |

Một case thay thế chỉ được kích hoạt khi case chính đã đạt `NOT_FOUND` hoặc
`UNRETRIEVABLE` theo đúng locator/terminal rule; không được thay chỉ vì nội
dung nhìn có vẻ mạnh hơn hoặc yếu hơn. Nếu cả chuỗi của slot kết thúc như vậy,
slot giữ trạng thái cuối và lý do theo từng case. Không thay đổi tên, domain,
query set, trần 20 kết quả/query hoặc link depth 2 trong sampling frame frozen.

## 5. Terminal condition của nhánh thu hồi

Nhánh công khai chỉ là `RETRIEVAL_TERMINAL_FOR_READINESS` khi đồng thời có:

1. 16 slot đều có slot ledger với một trạng thái chuẩn và reason cụ thể;
2. mọi query/domain đã kích hoạt đều có terminal evidence (`50 URL`, `5 trang`,
   hoặc `hai trang liên tiếp không có URL mới`), kể cả khi kết quả là rỗng;
3. mọi request có raw artifact, manifest và SHA-256 kiểm chứng được;
4. mỗi document/alias có provenance event; canonicalization/dedup chưa được
   thay bằng việc bỏ alias; và
5. không có `FAIL_CLOSED` chưa được giải quyết bằng việc chạy lại đúng cùng
   locator.

Trạng thái terminal này chỉ xác nhận thao tác thu hồi đã khép kín trong khung
hữu hạn. Nó không phải `DIRECT_SEARCH_COMPLETE`; trạng thái sau chỉ PI mới có
thể xác nhận khi registry, provenance/dedup, calibration và codebook đã qua
readiness audit.

## 6. Kiểm tra trước và sau run

Trước run, kiểm tra checksum của catalogue query, xác minh domain ownership
theo frame, tạo run ID mới và manifest trống. Sau run, kiểm tra checksum,
đếm request/response, tính khép kín terminal của từng slot và đối chiếu event
ledger với schema `record-registry-template.csv`. Audit phải báo riêng các
URL không truy hồi được, redirect khác domain, lỗi parser và case/slot không
có tài liệu; không gộp chúng thành suy luận về khoảng trống chính sách.

Khi tài liệu này được PI chấp thuận để vận hành, ghi ngày/phiên bản trong
`pr07-transition-checklist.md` và run manifest. Bất kỳ thay đổi nào đối với
16 slot, domain, query ID, trần, độ sâu, retry hoặc thứ tự thay thế sau thời
điểm đó đều dừng run và cần được xem xét minh bạch trước khi tiếp tục.
