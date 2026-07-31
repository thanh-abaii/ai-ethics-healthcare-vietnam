# Novelty audit: đạo đức và quản trị AI y tế tại Việt Nam

## Kết luận go/no-go

**G3: `PASS_WITH_NARROWED_CLAIM`**

Tiêu chí quyết định là **substantial answer**, không phải sự trùng khớp câu chữ hay nhãn mã hóa. G3 phải chuyển thành `FAIL` và kích hoạt `REFRAME` nếu một công trình hiện hữu đã trả lời phần lớn câu hỏi chính về thực trạng quản trị AI y tế tại Việt Nam và khoảng trống vận hành, khiến phần còn lại chỉ là mã hóa lại, đổi thuật ngữ, hoặc không còn đủ quan trọng để thành một bài riêng.

Audit hiện tại chưa tìm thấy công trình đã công bố nào đạt ngưỡng đó. Tuy nhiên, đóng góp chỉ có thể được tuyên bố theo bốn trục chức năng:

| Trục đóng góp | Kết luận audit |
| --- | --- |
| Tổng hợp quốc gia cập nhật và sâu hơn | **Gia tăng:** Tran và cộng sự là snapshot y tế số đến cuối 2020; Vuong và cộng sự tập trung ứng dụng 2018–2024; Tun và cộng sự chỉ đặt Việt Nam trong so sánh ASEAN. Chưa công trình nào tổng hợp sâu tập nguồn trực tiếp về quản trị AI y tế Việt Nam đến 2026. |
| Xác minh nguồn tiếng Việt và cổng chính thức | **Gia tăng một phần:** Tran và cộng sự đã dùng Thư Viện Pháp Luật và trang Bộ Y tế, nên thao tác xác minh nguồn chính thức tự thân không mới. Phần gia tăng nằm ở cập nhật sau 2020, giới hạn vào AI y tế trực tiếp và truy vết tình trạng hiệu lực/phạm vi áp dụng. |
| Phân tích thẩm quyền pháp lý, tầng nguồn và giới hạn nguồn công khai | **Gia tăng:** chưa comparator đã công bố nào dùng tầng hiệu lực/thẩm quyền để giới hạn kết luận về khoảng trống quản trị AI y tế Việt Nam. |
| Schema vận hành chi tiết | **Không mới ở cấp phương pháp chung; gia tăng khi dùng để tổng hợp quốc gia:** Wang A, Alami và Hussein đã phân tích cấu trúc, actor, quy trình, vòng đời, oversight hoặc monitoring. Giá trị còn lại là áp dụng nhất quán các trường `responsible actor/institution`, `decision authority`, `implementation/control/enforcement` và `evidence/monitoring` cho từng nguồn Việt Nam. |

**Tuyên bố đóng góp đã khóa**

> Tổng quan này cập nhật và xác minh tập nguồn công khai trực tiếp về đạo đức và quản trị AI y tế tại Việt Nam, bao gồm nguồn tiếng Việt và cổng chính thức; dùng một schema vận hành làm công cụ tổng hợp quốc gia để truy vết chủ thể, thẩm quyền quyết định, cơ chế thực hiện/kiểm soát/thực thi và bằng chứng/giám sát; đồng thời phân tầng kết luận theo thẩm quyền pháp lý và giới hạn của nguồn công khai.

Schema vận hành không được gọi là khung quản trị mới.

## Phạm vi, truy vấn và quy trình chọn comparator

- Loại hoạt động: audit chuẩn bị, không phải pilot hoặc umbrella review.
- Ngữ cảnh phiên bản: `protocol_version=PRE_PROTOCOL`; `search_strategy_version=PRE_SEARCH_STRATEGY`.
- Ngày truy cập và sàng lọc: 31/07/2026, Asia/Saigon (UTC+7).
- Nguồn: giao diện PubMed của NCBI, OpenAlex API, trang tạp chí/DOI và toàn văn chính thức.
- Không có record hay count nào từ audit được nhập vào tập nghiên cứu hoặc sơ đồ PRISMA.

### Ba truy vấn bắt buộc

| Mã | Truy vấn nguyên văn | PubMed | OpenAlex |
| --- | --- | ---: | ---: |
| Q1 | `("artificial intelligence" OR AI) AND (ethics OR governance) AND (healthcare OR medicine) AND (review OR framework)` | 15.100 ([truy vấn](https://pubmed.ncbi.nlm.nih.gov/?term=%28%22artificial%20intelligence%22%20OR%20AI%29%20AND%20%28ethics%20OR%20governance%29%20AND%20%28healthcare%20OR%20medicine%29%20AND%20%28review%20OR%20framework%29)) | 468.271 ([API](https://api.openalex.org/works?search=%28%22artificial%20intelligence%22%20OR%20AI%29%20AND%20%28ethics%20OR%20governance%29%20AND%20%28healthcare%20OR%20medicine%29%20AND%20%28review%20OR%20framework%29&per-page=1&select=id)) |
| Q2 | `("artificial intelligence" OR AI) AND (ethics OR governance) AND (Vietnam OR "Viet Nam") AND (health OR healthcare OR medicine)` | 204 ([truy vấn](https://pubmed.ncbi.nlm.nih.gov/?term=%28%22artificial%20intelligence%22%20OR%20AI%29%20AND%20%28ethics%20OR%20governance%29%20AND%20%28Vietnam%20OR%20%22Viet%20Nam%22%29%20AND%20%28health%20OR%20healthcare%20OR%20medicine%29)) | 26.720 ([API](https://api.openalex.org/works?search=%28%22artificial%20intelligence%22%20OR%20AI%29%20AND%20%28ethics%20OR%20governance%29%20AND%20%28Vietnam%20OR%20%22Viet%20Nam%22%29%20AND%20%28health%20OR%20healthcare%20OR%20medicine%29&per-page=1&select=id)) |
| Q3 | `("AI governance" OR "responsible AI") AND healthcare AND ("scoping review" OR "systematic review")` | 44 ([truy vấn](https://pubmed.ncbi.nlm.nih.gov/?term=%28%22AI%20governance%22%20OR%20%22responsible%20AI%22%29%20AND%20healthcare%20AND%20%28%22scoping%20review%22%20OR%20%22systematic%20review%22%29)) | 11.646 ([API](https://api.openalex.org/works?search=%28%22AI%20governance%22%20OR%20%22responsible%20AI%22%29%20AND%20healthcare%20AND%20%28%22scoping%20review%22%20OR%20%22systematic%20review%22%29&per-page=1&select=id)) |

Không có filter ngày, ngôn ngữ hoặc loại ấn phẩm cho ba truy vấn này. Count rộng, đặc biệt OpenAlex tìm cả tiêu đề, tóm tắt và toàn văn và token `AI` mơ hồ, chỉ mô tả truy vấn; chúng không phải bằng chứng tính mới và không được sàng lọc toàn bộ.

### Focused candidate scan và điểm dừng

Hai tập định vị được chạy trên `title_and_abstract.search`, giới hạn 01/01/2019–31/07/2026:

- **FS2:** `("artificial intelligence") AND (ethics OR governance) AND (Vietnam OR "Viet Nam") AND (health OR healthcare OR medicine) AND (review OR framework)`. Sàng lọc toàn bộ 33/33 record.
- **FS3:** `("AI governance" OR "responsible AI") AND healthcare AND ("scoping review" OR "systematic review")`. Trước khi xem kết quả, điểm dừng được đặt ở **top 20/151 theo `relevance_score:desc`**.
- Bổ sung bốn nguồn bắt buộc được xác minh theo tiêu đề/DOI/toàn văn: Alami 2026, Tran 2022, Vuong 2025 và protocol Wang M 2026. Wang A, Hussein và Tun đã có trong FS2/FS3 nên không nhập lặp.

Nhật ký đầy đủ: [`novelty-comparator-log.csv`](novelty-comparator-log.csv).

| Chỉ số | Số lượng |
| --- | ---: |
| Record đã xem | 57 |
| Duplicate manifestation được gắn cờ | 8 |
| Record duy nhất sau khử trùng lặp | 49 |
| `INCLUDE_COMPARATOR` | 7 |
| Loại sau khử trùng lặp | 42 |

Khử trùng lặp ưu tiên DOI; khi DOI khác nhưng tiêu đề không chung chung và nội dung thể hiện cùng preprint/version/dataset, giữ một manifestation và ghi liên kết duplicate. Các tiêu đề chung như “Index” không được tự động gộp nếu DOI khác. Audit này là focused scan có điểm dừng, không tuyên bố exhaustive.

## Bảng đối chiếu chức năng

| Comparator | Geography/corpus | Search/method | Unit | Responsible actor/institution | Decision authority | Implementation/control/enforcement | Evidence/monitoring | Source authority/tiering | Country-level output | Residual contribution Vietnam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Wang A, Freeman, Magrabi. 2026.** *Governance for safe and responsible AI in healthcare organisations*. [doi:10.1038/s41746-026-02679-2](https://doi.org/10.1038/s41746-026-02679-2) | Quốc tế; framework cho tổ chức y tế cấp tính, mục tiêu ứng dụng Australia. | MEDLINE, Embase, Scopus; 4/2024, cập nhật 3/2025; scoping review. | 77 framework. | Có oversight mechanism và nhóm quản trị AI. | Có assessment/approval theo framework nhưng không lập authority map quốc gia. | Nguyên tắc, assessment method, lifecycle, oversight; 10/77 có đủ bốn. | Có monitoring như thành phần vòng đời; không tổng hợp evidence trail quốc gia. | Không phân tầng hiệu lực nguồn quốc gia. | Không. | Tổng hợp nguồn Việt Nam, thẩm quyền nguồn và evidence trail theo từng yêu cầu. |
| **Alami et al. 2026.** *Artificial Intelligence Governance in Health Systems*. [doi:10.2196/87448](https://doi.org/10.2196/87448) | Quốc tế; framework ở cấp quốc tế, quốc gia, địa phương và tổ chức. | Tám database, nguồn xám/cổng tổ chức; 10/2024, cập nhật 7/2025 và 3/2026; systematic review. | 19 framework. | Mã hóa actor, role, accountability và cấu trúc đa ngành. | Nêu phân bổ decision-making authority và trách nhiệm. | Sáu process và bốn relational mechanisms; có data governance, risk, validation, integration. | Maintenance/monitoring là process cốt lõi; framework quality được đánh giá. | Đánh giá chất lượng framework, không tier hiệu lực văn bản theo quốc gia. | Mô hình tích hợp toàn cầu, không country profile Việt Nam. | Không mới ở schema actor/process; còn giá trị ở áp dụng schema cho nguồn Việt Nam và tầng thẩm quyền. |
| **Hussein et al. 2026.** *Advancing healthcare AI governance through a comprehensive maturity model*. [doi:10.1038/s41746-026-02418-7](https://doi.org/10.1038/s41746-026-02418-7) | Quốc tế; tổ chức y tế có mức nguồn lực khác nhau. | PubMed, giới hạn 26 tạp chí, 2019–2024; thêm nguồn xám/ngoài chỉ mục. | 35 framework từ 29 tài liệu. | Organizational structure, leadership và team. | Maturity levels gắn năng lực ra quyết định, không authority map quốc gia. | Bảy miền từ problem formulation đến deployment/integration. | Monitoring/maintenance và benchmark HAIRA năm mức. | Không phân tầng pháp lý/quyền lực nguồn. | Không. | Chỉ còn đóng góp khi schema được dùng để kiểm tra nguồn và nghĩa vụ Việt Nam, không phải để đề xuất maturity model mới. |
| **Tran et al. 2022.** *Digital Health Policy and Programs for Hospital Care in Vietnam*. [doi:10.2196/32392](https://doi.org/10.2196/32392) | Việt Nam; nghiên cứu và chính sách y tế số bệnh viện. | PubMed, Web of Science, Thư Viện Pháp Luật, trang Bộ Y tế; Google snowball; snapshot cuối 2020. | 11 nghiên cứu và 20 văn bản chính phủ. | Có ministry ban hành và đối tượng hệ thống y tế số. | Có quy định/mandate theo văn bản nhưng không lập bản đồ authority cho AI. | HIS, EHR/EMR, liên thông, an ninh mạng, tiêu chuẩn và mức sẵn sàng. | Charting chính sách/chương trình, không evidence schema cho vòng đời AI. | Tách nghiên cứu và chính sách; chưa phân tầng hiệu lực để gán gap AI. | Bản đồ quốc gia y tế số. | Cập nhật sau 2020, chỉ lấy AI y tế trực tiếp, kiểm chứng hiệu lực và phân tích controls/evidence AI. |
| **Vuong et al. 2025.** *Application of Artificial Intelligence in Healthcare in Vietnam*. [doi:10.25073/2588-1132/vnumps.4799](https://doi.org/10.25073/2588-1132/vnumps.4799) | Việt Nam; nghiên cứu ứng dụng AI 2018–2024. | PubMed, Google Scholar, ScienceDirect và tám tạp chí Việt Nam; ngày tìm không báo cáo. | 37 nghiên cứu ứng dụng. | Chủ thể quản trị không phải trường trích xuất. | Không. | Sáu nhóm ứng dụng; không phân tích control/enforcement. | Hiệu năng/ứng dụng, không monitoring governance. | Không. | Bản đồ ứng dụng và hướng AI đa phương thức. | Toàn bộ câu hỏi quản trị, nguồn chính thức, authority và operational evidence còn bỏ ngỏ. |
| **Tun et al. 2025.** *Navigating ASEAN region AI governance readiness in healthcare*. [doi:10.1016/j.hlpt.2025.100981](https://doi.org/10.1016/j.hlpt.2025.100981) | 11 nước ASEAN, có Việt Nam; index và chính sách/hướng dẫn. | Oxford Insights 2020–2023; rà soát chính sách, trang bộ y tế và web. | Điểm readiness quốc gia và policy/guidance. | Nêu cơ quan/chính phủ ở cấp cao, không actor map theo yêu cầu. | Không mã hóa decision authority. | So sánh policy readiness, nhân lực và hạ tầng; không control/enforcement matrix. | Dùng chỉ số tổng hợp và nguồn công khai; không evidence trail theo yêu cầu. | Không phân tầng hiệu lực pháp lý. | Country comparison ASEAN, Việt Nam là một điểm dữ liệu. | Cần tổng hợp sâu trong quốc gia, xác minh nguồn Việt Nam và phân loại gap theo authority/control/evidence. |
| **Wang M et al. 2026 protocol.** *Mapping National Governance of AI for Health*. [doi:10.2196/88970](https://doi.org/10.2196/88970) | Toàn cầu; national policy instruments, nguồn hỗ trợ country-specific; Việt Nam đủ khả năng thuộc phạm vi. | Sáu database, 972 nguồn xám; 1/2015–4/2025; 149 nguồn đủ điều kiện; protocol/kết quả chưa hoàn tất công bố. | National policy instrument; empirical/policy analysis dùng để xác minh/bối cảnh hóa. | Trường “responsible institutions”; văn bản do national government/ministry/authority/regulator ban hành hoặc endorse. | Mã hóa responsible actors và operational details; authority nằm trong institutional arrangements/regulatory mechanisms. | Bốn chiều ethics, regulation, implementation, operations; operational detail gồm implementation mechanisms, regulatory requirements và enforcement arrangements. | Mã hóa monitoring procedures; barriers/enablers và gap; thừa nhận documented policy có thể không phản ánh thực tế. | Phân tích theo policy type và official national instrument; có nguồn hỗ trợ, nhưng chưa biết cách tier hiệu lực trong kết quả. | Dự kiến profile/phân nhóm quốc gia; **methodological overlap: strong; Vietnam result overlap: unknown**. | Chỉ còn nếu bài Việt Nam sâu hơn về nguồn bản địa, hiệu lực/tầng nguồn và country-specific evidence; không được hạ overlap phương pháp vì protocol chưa công bố kết quả Việt Nam. |

## Đánh giá substantial answer

Ba comparator quốc tế 2026 đã trả lời phần lớn câu hỏi phương pháp về chuyển nguyên tắc thành cấu trúc, quy trình, oversight và monitoring. Vì vậy, schema vận hành của bài không phải novelty tự thân.

Ba comparator có liên quan Việt Nam chưa trả lời phần lớn câu hỏi chính:

- Tran 2022 rộng về y tế số và dừng ở snapshot cuối 2020;
- Vuong 2025 lập bản đồ ứng dụng, không lập bản đồ quản trị;
- Tun 2025 so sánh readiness ASEAN ở mức quốc gia tổng hợp.

Phần còn lại vẫn đủ quan trọng cho một bài riêng vì cần xác định nguồn quản trị AI y tế trực tiếp nào đang có hiệu lực hoặc được công bố tại Việt Nam, yêu cầu nào xác định actor/authority/control/evidence, và mức suy luận nào được nguồn cho phép. Đây là căn cứ giữ `PASS_WITH_NARROWED_CLAIM`.

## Competitive checkpoints

Protocol Wang M có **overlap phương pháp mạnh** và là rủi ro cạnh tranh lớn nhất. Tại mỗi mốc dưới đây phải tìm theo tiêu đề, DOI, PMID 42490596, PROSPERO CRD420251234461 và tên tác giả; kiểm tra trang journal/preprint, dataset/supplement, cited-by và bài kết quả:

1. trước khóa protocol;
2. trước pilot;
3. khi đóng tìm kiếm;
4. trước nộp bài.

Bất kỳ output mới nào trả lời thực chất phần lớn câu hỏi chính, hoặc làm bốn trục đóng góp còn lại không đủ quan trọng cho một bài riêng, đều chuyển G3 thành `FAIL` và kích hoạt `REFRAME`, dù không dùng cùng ba nhãn hay cùng thuật ngữ.

## Giới hạn

- Đây là focused comparator scan có điểm dừng, không phải systematic review của reviews.
- PubMed không bao phủ đầy đủ luật/chính sách và tạp chí Việt Nam; OpenAlex có metadata và chỉ mục động.
- Broad counts không được dùng làm bằng chứng tính mới.
- FS3 chỉ sàng lọc top 20/151 theo relevance; những record ngoài điểm dừng có thể chứa comparator khác.
- Kết luận cần được kiểm tra lại tại cả bốn competitive checkpoints.
