# Chiến lược tìm kiếm

## 1. Kiểm soát phiên bản và ranh giới

| Trường | Giá trị |
| --- | --- |
| `strategy_version` | `0.2-pre-registration-search-development` |
| Ngày kiểm tra | 31/07/2026 |
| Trạng thái | `PASS_PRE_REGISTRATION_SEARCH_VALIDATION` |
| Giai đoạn | `PRE_REGISTRATION_SEARCH_DEVELOPMENT` |
| `seed_retrieval_test` | `PASS_PRELIMINARY` |
| Corpus/PRISMA | `NOT_CREATED` |
| G4–G5 | `NOT_RUN` |
| Citation chasing | `NOT_RUN` |

Chiến lược đã qua một lượt rà soát đặc tả và một lượt rà soát khoa học độc lập ngày 31/07/2026. Các lượt chạy ngày 31/07/2026 chỉ kiểm tra cú pháp, bản dịch nền tảng, khả năng xuất dữ liệu, độ nhạy đối với seed và độ nhiễu sơ bộ. Chúng không tạo corpus, count PRISMA, quyết định đủ điều kiện hay kết luận khoảng trống. Việc `PASS` ở đây không thay thế xác nhận vai trò của Lộc Đặng, không mở G4–G5 và không xác nhận tính đầy đủ của tập bằng chứng.

Tìm kiếm chính thức sẽ dùng **ngày đóng tìm kiếm thực tế** làm mốc trên bao hàm. Nếu ngày này khác 31/07/2026, mốc ngày phải được cập nhật trước lần chạy chính thức và ghi trong một amendment có dấu thời gian; không dùng một năm giả định ở tương lai. Sau đăng ký, mọi thay đổi thực chất về nguồn, trường hoặc từ khóa cũng phải theo thủ tục amendment.

## 2. Logic PCC và ba cụm

### Cụm A — AI

- MeSH: `Artificial Intelligence`, `Machine Learning`.
- Từ tự do: `artificial intelligence`, `machine learning`, `generative AI`, `large language model(s)`, `LLM(s)`.
- Cổng Việt Nam: `trí tuệ nhân tạo`, `học máy`, `AI tạo sinh`, `mô hình ngôn ngữ lớn`.

### Cụm B — đạo đức, quản trị, quyền và kiểm soát

Ngoài nhóm nguyên tắc chung, cụm này bao phủ các thuật ngữ có tính vận hành:

- đạo đức/quản trị: `ethic*`, `govern*`, `accountab*`, `responsib*`, `transparen*`, `fair*`, `bias`, `privacy`, `oversight`;
- chính sách/pháp lý: `policy`, `policies`, `regulat*`, `legal`, `law`, `laws`;
- quyền và tự quyết: `patient rights`, `human rights`, `consent`, `autonomy`;
- an toàn/rủi ro: `risk*`, `safety`, `harm*`;
- khả năng hiểu và kiểm soát: `explainab*`, `interpretab*`, `audit*`, `monitor*`;
- phản hồi và khắc phục: `incident*`, `complaint*`, `redress`, `incident reporting`, `quality management`, `post-implementation monitoring`, `post-market surveillance`, `effectiveness evaluation`, `audit*`;
- dữ liệu và công bằng: `data protection`, `confidential*`, `equity`, `justice`, `discriminat*`;
- chuẩn hóa: `standard*`, `guideline*`.

Các MeSH được dùng khi PubMed nhận diện: `Ethics`, `Ethics, Medical`, `Government Regulation`, `Patient Rights`, `Informed Consent`, `Health Equity`. Không dùng `"Data Protection"[mh]` vì PubMed cảnh báo cụm MeSH này không có trong phrase index tại ngày kiểm tra; khái niệm vẫn được giữ bằng từ tự do.

### Cụm C — Việt Nam kết hợp y tế

Địa lý và y tế phải cùng xuất hiện:

- địa lý: `Vietnam`, `Viet Nam`, `Vietnamese`, `Việt Nam`;
- y tế: `health*`, `healthcare`, `health care`, `medic*`, `clinical`, `hospital*`, `y tế`, `chăm sóc sức khỏe`, `khám bệnh`, `chữa bệnh`, `bệnh viện`, `lâm sàng`.

Mốc dưới là 01/01/2019 cho nghiên cứu, báo cáo và hướng dẫn. Văn bản pháp luật hoặc công cụ chính thức đang có hiệu lực được kiểm tra bất kể năm ban hành. Ngôn ngữ đủ điều kiện là tiếng Việt hoặc tiếng Anh.

## 3. Phát triển ba bước theo JBI

### Bước 1 — limited search

1. Chạy ứng viên trên PubMed và một trang đầu OpenAlex.
2. Kiểm tra seed trực tiếp Việt Nam theo các lớp chính sách/pháp lý, tiếp nhận lâm sàng, quyền–an toàn–giám sát.
3. Kiểm tra cổng, locator và quan hệ văn bản.
4. Chỉ phân loại sơ bộ liên quan/nhiễu để phát triển truy vấn; không sàng lọc đủ điều kiện.

Kết quả vòng 0.2: PubMed 88 record và xuất đủ 88 record NBIB; OpenAlex `meta.count=347`, xuất giới hạn 25 record trang đầu. Hai count là dữ liệu phát triển truy vấn.

### Bước 2 — text words và index terms

| Nguồn phát triển | Từ/khái niệm bổ sung | Quyết định |
| --- | --- | --- |
| Tran và cs., 2022, PMID `35138264` | policy, adoption, hospital, government requirements, regulations | Giữ policy/regulation và địa lý AND y tế. |
| Vuong và cs., 2019, PMID `30717268` | readiness, socio-political commitment, information system | Giữ governance/readiness nhưng không mở nhánh y tế số chung. |
| Yang và cs., 2024, PMID `38858466` | bias, fairness, generalizability, LMIC | Giữ bias/fairness/equity. |
| Van và cs., 2024, PMID `39430352` | clinical/community screening, effectiveness, safety context | Giữ clinical/hospital và nhánh tiếp nhận độc lập với tên Thông tư. |
| Chanh và cs., 2023, PMID `37397176` | clinical monitoring, implementation, digital health | Tầng `implementation`; giữ monitor/implementation và biến thể theo dõi sau triển khai, quản lý chất lượng, báo cáo sự cố, hậu kiểm; phân loại cuối vẫn qua sàng lọc kép. |
| Nguyen và cs., 2025, PMID `41329943` | challenges, medical education, Vietnam | Tầng `education/challenges`; dùng như seed độ nhạy bối cảnh, có thể là nhiễu đối với câu hỏi quản trị lâm sàng. |
| WHO 2021; UNESCO 2021 | autonomy, rights, safety, transparency, responsibility, oversight | Giữ cụm chuẩn tắc và kênh tổ chức quốc tế. |
| Luật AI `134/2025/QH15`, Nghị định `142/2026/NĐ-CP`, Thông tư `05/2026/TT-BKHCN` | đạo đức, quyền, dữ liệu, an toàn người bệnh, đánh giá tác động, giám sát, báo cáo sự cố | Khóa nhánh pháp lý và truy quan hệ Luật → Nghị định → khung/hướng dẫn. Không suy hiệu lực thành triển khai. |

### Bước 3 — dịch cú pháp

| Nền tảng | Cách dịch |
| --- | --- |
| PubMed | MeSH OR `[tiab]`; ba cụm nối `AND`; địa lý AND y tế nằm trong cụm C; lọc ngày/ngôn ngữ. |
| OpenAlex | Không MeSH/wildcard; liệt kê biến thể; Boolean nguyên văn trong `title_and_abstract.search`; lọc hai đầu ngày. |
| Cổng chính thức | Truy vấn Việt/Anh phân rã thành query ID; tìm nội bộ trước, `site:` chỉ là fallback định vị; truy số hiệu/tên và quan hệ văn bản. |

## 4. PubMed

PubMed bao gồm record MEDLINE và PubMed ngoài MEDLINE; không gọi kết quả là “MEDLINE-only”.

### 4.1. Truy vấn nguyên văn

```text
("Artificial Intelligence"[mh] OR "Machine Learning"[mh] OR "artificial intelligence"[tiab] OR "machine learning"[tiab] OR "generative AI"[tiab] OR "large language model"[tiab] OR "large language models"[tiab] OR LLM[tiab] OR LLMs[tiab]) AND ("Ethics"[mh] OR "Ethics, Medical"[mh] OR "Government Regulation"[mh] OR "Patient Rights"[mh] OR "Informed Consent"[mh] OR "Health Equity"[mh] OR ethic*[tiab] OR accountab*[tiab] OR responsib*[tiab] OR transparen*[tiab] OR fair*[tiab] OR bias[tiab] OR biases[tiab] OR privacy[tiab] OR oversight[tiab] OR govern*[tiab] OR policy[tiab] OR policies[tiab] OR regulat*[tiab] OR legal[tiab] OR law[tiab] OR laws[tiab] OR risk*[tiab] OR safety[tiab] OR harm*[tiab] OR "patient rights"[tiab] OR "human rights"[tiab] OR consent[tiab] OR autonomy[tiab] OR explainab*[tiab] OR interpretab*[tiab] OR audit*[tiab] OR monitor*[tiab] OR incident*[tiab] OR complaint*[tiab] OR redress[tiab] OR "data protection"[tiab] OR confidential*[tiab] OR equity[tiab] OR justice[tiab] OR discriminat*[tiab] OR standard*[tiab] OR guideline*[tiab]) AND (("Vietnam"[mh] OR Vietnam[tiab] OR "Viet Nam"[tiab] OR Vietnamese[tiab]) AND ("Delivery of Health Care"[mh] OR "Medicine"[mh] OR health*[tiab] OR healthcare[tiab] OR "health care"[tiab] OR medic*[tiab] OR clinical[tiab] OR hospital*[tiab])) AND ("2019/01/01"[dp] : "2026/07/31"[dp]) AND (english[la] OR vietnamese[la])
```

Không thêm filter loại bài hoặc full text.

### 4.2. Query translation do PubMed hiển thị

```text
("Artificial Intelligence"[MeSH Terms] OR "Machine Learning"[MeSH Terms] OR "Artificial Intelligence"[Title/Abstract] OR "Machine Learning"[Title/Abstract] OR "generative AI"[Title/Abstract] OR "large language model"[Title/Abstract] OR "large language models"[Title/Abstract] OR "LLM"[Title/Abstract] OR "LLMs"[Title/Abstract]) AND ("Ethics"[MeSH Terms] OR "ethics, medical"[MeSH Terms] OR "Government Regulation"[MeSH Terms] OR "Patient Rights"[MeSH Terms] OR "Informed Consent"[MeSH Terms] OR "Health Equity"[MeSH Terms] OR "ethic*"[Title/Abstract] OR "accountab*"[Title/Abstract] OR "responsib*"[Title/Abstract] OR "transparen*"[Title/Abstract] OR "fair*"[Title/Abstract] OR "bias"[Title/Abstract] OR "biases"[Title/Abstract] OR "privacy"[Title/Abstract] OR "oversight"[Title/Abstract] OR "govern*"[Title/Abstract] OR "policy"[Title/Abstract] OR "policies"[Title/Abstract] OR "regulat*"[Title/Abstract] OR "legal"[Title/Abstract] OR "law"[Title/Abstract] OR "laws"[Title/Abstract] OR "risk*"[Title/Abstract] OR "safety"[Title/Abstract] OR "harm*"[Title/Abstract] OR "Patient Rights"[Title/Abstract] OR "human rights"[Title/Abstract] OR "consent"[Title/Abstract] OR "autonomy"[Title/Abstract] OR "explainab*"[Title/Abstract] OR "interpretab*"[Title/Abstract] OR "audit*"[Title/Abstract] OR "monitor*"[Title/Abstract] OR "incident*"[Title/Abstract] OR "complaint*"[Title/Abstract] OR "redress"[Title/Abstract] OR "data protection"[Title/Abstract] OR "confidential*"[Title/Abstract] OR "equity"[Title/Abstract] OR "justice"[Title/Abstract] OR "discriminat*"[Title/Abstract] OR "standard*"[Title/Abstract] OR "guideline*"[Title/Abstract]) AND (("Vietnam"[MeSH Terms] OR "Vietnam"[Title/Abstract] OR "Viet Nam"[Title/Abstract] OR "Vietnamese"[Title/Abstract]) AND ("Delivery of Health Care"[MeSH Terms] OR "Medicine"[MeSH Terms] OR "health*"[Title/Abstract] OR "healthcare"[Title/Abstract] OR "health care"[Title/Abstract] OR "medic*"[Title/Abstract] OR "clinical"[Title/Abstract] OR "hospital*"[Title/Abstract])) AND 2019/01/01:2026/07/31[Date - Publication] AND ("english"[Language] OR "Vietnamese"[Language])
```

### 4.3. Validation

- Giao diện PubMed chính thức ngày 31/07/2026: 88 record.
- Sáu PMID trực tiếp Việt Nam trong Mục 3 đều được thu hồi.
- Toàn bộ 88 record ở định dạng PubMed/NBIB:
  `artifacts/pre-registration-search-development/pubmed-validation-export.nbib`.
- SHA-256: `52278E47D5B6AB1654C7A71BD6AE7DB6C3C3DFCFDB2A10B1626B3F4E19746659`.
- E-utilities từ địa chỉ mạng dùng chung bị chặn; validation hoàn tất qua giao diện chính thức. Lần chạy chính thức thử E-utilities lại; giao diện NCBI và xuất NBIB là đường dự phòng.

Nhận xét phát triển truy vấn: độ nhạy tăng từ 21 lên 88, đồng thời có nhiễu rõ (ASEAN chỉ nhắc Việt Nam, tiếng Việt như ngôn ngữ dịch, môi trường/NER ngoài y tế). Đây là lý do cần sàng lọc kép, không phải lý do thu hẹp truy vấn sau khi đã thấy kết quả.

## 5. OpenAlex

OpenAlex là nguồn bổ sung mở, không tương đương tuyệt đối với Scopus.

### 5.1. Verbatim Boolean query string

```text
("artificial intelligence" OR "machine learning" OR "generative AI" OR "generative artificial intelligence" OR "large language model" OR "large language models" OR LLM OR LLMs) AND (ethics OR ethical OR governance OR govern OR government OR governing OR accountability OR accountable OR responsibility OR responsible OR transparency OR transparent OR fairness OR fair OR bias OR biases OR policy OR policies OR regulation OR regulations OR regulatory OR legal OR law OR laws OR risk OR risks OR safety OR harm OR harms OR "patient rights" OR "human rights" OR consent OR autonomy OR explainability OR explainable OR interpretability OR interpretable OR audit OR auditing OR monitoring OR monitor OR incident OR incidents OR complaint OR complaints OR redress OR "data protection" OR confidentiality OR confidential OR equity OR justice OR discrimination OR discriminatory OR standard OR standards OR guideline OR guidelines OR oversight OR privacy) AND ((Vietnam OR "Viet Nam" OR Vietnamese) AND (health OR healthcare OR "health care" OR medicine OR medical OR clinical OR hospital OR hospitals))
```

Đây là chuỗi Boolean nguyên văn, không gọi là “exact search”: OpenAlex có stemming/matching riêng nên chuỗi không bảo đảm đối sánh ký tự tuyệt đối. Các biến thể số ít/số nhiều và họ từ quan trọng được liệt kê thay cho wildcard.

### 5.2. API mapping và trạng thái kỹ thuật

```text
Endpoint: https://api.openalex.org/works
filter: from_publication_date:2019-01-01,to_publication_date:2026-07-31,title_and_abstract.search:<verbatim Boolean query string>
select: id,doi,display_name,publication_year,publication_date,type,language,ids,primary_location,authorships,abstract_inverted_index
per-page: 25
cursor: *
```

Mẫu URL tái lập, percent-encoded và không mang secret, được giữ trong artifact recall: `https://api.openalex.org/works?filter={FILTER_PERCENT_ENCODED}&select=id%2Cdoi&per-page=25&cursor=%2A`. `{FILTER_PERCENT_ENCODED}` là toàn bộ filter sau khi UTF-8 percent-encode; không chèn `api_key`, `mailto`, token hay biến môi trường vào manifest, URL, log hoặc artifact. Với kiểm tra DOI, filter ứng viên được giữ nguyên rồi thêm `,doi:https://doi.org/{DOI}` trước khi encode; mẫu URL đầy đủ và kết quả nằm tại `artifacts/pre-registration-search-development/openalex-candidate-doi-recall-validation.json`.

Tại 31/07/2026, tài liệu OpenAlex đánh dấu các `.search` filter, gồm `title_and_abstract.search`, là deprecated và khuyến nghị tham số `search`. Validation 0.2 vẫn dùng mapping đã định trước và còn hoạt động. Chuyển sang `search=` chỉ được thực hiện bằng prospective amendment, kiểm tra tương đương/độ nhiễu và chạy lại seed test trước tìm kiếm chính thức.

OpenAlex hiện yêu cầu API key miễn phí; tài khoản miễn phí có hạn mức $1/ngày. Nghiên cứu không giả định mua gói trả phí. Key phải đọc từ biến môi trường/secret store, không ghi vào URL lưu trữ, log, script hay artifact. Lượt validation giới hạn nhận HTTP 200 không kèm key trong artifact; hành vi này không được coi là bảo đảm truy cập anonymous cho full run.

### 5.3. Validation và quy tắc full run

- Trang đầu ngày 31/07/2026: `meta.count=347`, 25 record, `next_cursor` khác null.
- Raw JSON: `openalex-validation-page-001.json`, SHA-256 `5212FEECBC83994BA10BC95C8DEF20618F9FA8F44E87247CB5F16F4636127281`.
- Artifact dẫn xuất để QA abstract: `openalex-validation-derived-abstract.csv`, 25 dòng, 22 abstract không rỗng, SHA-256 `DF1642F53366503B23DE0ECFA789EA20378A9FE63FF6A27B027DE026DBA4371B`.
- Artifact dẫn xuất không thay raw JSON.

Full run bắt đầu `cursor=*`, giữ toàn bộ cursor chain theo đúng thứ tự, từng raw page và checksum; mỗi page phải ghi `cursor_in`, `next_cursor`, `meta.count`, `meta.per_page`, số `results`, HTTP status, thời điểm nhận và SHA-256 vào manifest. Lặp lại **cho đến khi** phản hồi có đồng thời `next_cursor=null` **và** `results` rỗng, đúng hướng dẫn OpenAlex. Một trang `next_cursor=null` nhưng còn `results` không phải điểm kết thúc và không được tính là full export: lưu nó, ghi điều kiện chưa đạt; vì không còn cursor hợp lệ để tiếp tục thì đánh dấu `PAGING_PROTOCOL_ERROR`, dừng lỗi và tạo amendment, không tự suy trang cuối.

Khử trùng lặp xuất dùng OpenAlex `id` đã chuẩn hóa làm khóa duy nhất; DOI hoặc tiêu đề chỉ dùng để điều tra, không thay thế khóa này. `meta.count` có thể trôi trong lúc chụp dữ liệu, nên manifest phải lưu chuỗi `meta.count` theo page và một `count_discrepancy_log`: `first_meta_count`, `last_meta_count`, `unique_openalex_ids`, `raw_results_seen`, duplicate IDs, cursor lặp, page thiếu/HTTP lỗi và chênh lệch. Không yêu cầu một ảnh chụp động có `unique IDs = meta.count`; nếu có drift hay chênh lệch, ghi rõ và không tuyên bố tập đầy đủ cho đến khi rerun sạch hoặc amendment quyết định cách xử lý. Validation một trang không phải corpus.

## 6. Nguồn chính thức và kiểm tra cơ cấu Bộ Y tế

| Mã | Cổng/đơn vị | URL gốc | Vai trò |
| --- | --- | --- | --- |
| GOV/GAZ/GOV-VB/VBPL | Chính phủ, Công báo, văn bản Chính phủ, CSDL pháp luật | `chinhphu.vn`; `congbao.chinhphu.vn`; `vanban.chinhphu.vn`; `vbpl.vn` | Văn bản, hiệu lực, quan hệ pháp lý. |
| MOH | Bộ Y tế | `https://moh.gov.vn/` | Chính sách/kế hoạch ngành. |
| MOH-ASTT | Cục Khoa học công nghệ và Đào tạo | `https://asttmoh.vn/` | Khoa học, công nghệ, đổi mới sáng tạo và đầu mối liên quan được xác minh theo chức năng hiện hành. |
| MOH-KCB | Cục Quản lý Khám, chữa bệnh | `https://kcb.vn/` | Chất lượng, an toàn, cơ sở khám chữa bệnh. |
| MOH-HTTB | Cục Hạ tầng và Thiết bị y tế | `https://imda.moh.gov.vn/` | Hạ tầng, thiết bị và an toàn liên quan công nghệ y tế. |
| MOH-NHIC | Trung tâm Thông tin Y tế Quốc gia | `https://ttyqg.vn/` | Hệ thống thông tin, dữ liệu, chuyển đổi số y tế. |
| MOH-PC | Vụ Pháp chế | `https://vuphapche.moh.gov.vn/` | Xây dựng, rà soát và theo dõi thi hành pháp luật y tế. |
| MOH-HSPI | Viện Chiến lược và Chính sách y tế | `https://hspi.org.vn/` | Nghiên cứu, bằng chứng và hoạch định chính sách y tế. |
| MST | Bộ Khoa học và Công nghệ | `https://mst.gov.vn/` | Luật/chính sách/khung AI. |
| UNESCO-RAM | UNESCO RAM Việt Nam | `https://www.unesco.org/ethics-ai/en/vietnam` | Đánh giá mức sẵn sàng và cập nhật chính thức. |
| WHO-VNM | WHO Việt Nam | `https://www.who.int/vietnam` | Nguồn WHO gắn Việt Nam và y tế. |

Nghị định `42/2025/NĐ-CP` được dùng làm snapshot cơ cấu cấp Bộ; file Công báo có SHA-256 `224724CE39E507A6EA594E6C0B24E3A207EE3312521E7D9BF3934369033B217F`. Snapshot trang Cục HTTB có SHA-256 `AF20D401D5DEEA7CE61AFD784FB42C97A009112931819A4048F02AC38535CCFB`; trang Viện HSPI `926BF727A8C5ADB6DBD9C58E2DAF5DFA2E3170044AE7AC63AAB6F43941A3BA25`; snapshot dẫn xuất chức năng Vụ Pháp chế `C741CF6AA29B78EBFF2CC0EF080AE8DA7F7423DFBF9A5E26478835B02704616E`.

Vụ Pháp chế được **bao gồm**, không loại trừ: chức năng pháp chế và theo dõi thi hành pháp luật liên quan trực tiếp việc phân biệt quy định với bằng chứng thực thi. Trang chức năng của Vụ trả lỗi máy chủ khi snapshot trực tiếp ngày 31/07/2026; vị trí trong cơ cấu được xác minh bằng Nghị định 42 và locator trang chức năng chính thức được giữ trong log. Lỗi truy cập phải được thử lại ở full run.

## 7. Truy vấn cổng chính thức đã phân rã

Mỗi dòng là một query ID độc lập. Nếu cổng không hỗ trợ Boolean, chạy từng cụm trong ngoặc kép như một query con `-a`, `-b` và ghi chuỗi thực tế.

### 7.1. Luật/khung và quan hệ

```text
DQ-LAW-01: "134/2025/QH15"
DQ-LAW-02: "Luật Trí tuệ nhân tạo" AND (y tế OR "người bệnh" OR bệnh viện)
DQ-DEC-01: "142/2026/NĐ-CP"
DQ-FRAME-01: "05/2026/TT-BKHCN"
DQ-FRAME-02: "Khung đạo đức trí tuệ nhân tạo quốc gia" AND (y tế OR bệnh viện OR "khám chữa bệnh")
DQ-REL-01: ("134/2025/QH15" OR "142/2026/NĐ-CP" OR "05/2026/TT-BKHCN") AND (sửa đổi OR thay thế OR hướng dẫn OR triển khai)
```

### 7.2. Hội đồng: thành lập tách khỏi hoạt động

```text
DQ-COUNCIL-NAME-01: "Hội đồng đạo đức AI quốc gia"
DQ-COUNCIL-NAME-02: "Hội đồng đạo đức trí tuệ nhân tạo quốc gia"
DQ-COUNCIL-NAME-03: "Ủy ban đạo đức AI quốc gia"
DQ-COUNCIL-NAME-04: "National AI Ethics Council" Vietnam
DQ-COUNCIL-NAME-05: "National Council on AI Ethics" Vietnam
DQ-COUNCIL-NAME-06: "AI ethics committee" Vietnam
DQ-COUNCIL-EST-01: ("hội đồng đạo đức AI" OR "hội đồng đạo đức trí tuệ nhân tạo") AND ("quyết định thành lập" OR "quy chế" OR "chức năng nhiệm vụ" OR "thành viên")
DQ-COUNCIL-ACT-01: ("hội đồng đạo đức AI" OR "hội đồng đạo đức trí tuệ nhân tạo") AND ("phiên họp" OR "biên bản" OR "báo cáo hoạt động")
DQ-COUNCIL-ACT-02: ("National AI Ethics Council" OR "National Council on AI Ethics") AND (decision OR regulation OR mandate OR members OR meeting OR minutes OR "activity report")
```

Trang MST ngày 26/11/2025 về một người tham gia **đề xuất** lập hội đồng độc lập là `POLICY_PROPOSAL`/negative control; không phải bằng chứng thành lập hay hoạt động.

### 7.3. Triển khai và tiếp nhận y tế độc lập với tên Thông tư

```text
DQ-IMPL-01: ("đạo đức AI" OR "AI có trách nhiệm" OR "quản trị AI") AND (kế hoạch OR triển khai OR áp dụng OR thí điểm)
DQ-IMPL-02: ("đạo đức AI" OR "AI có trách nhiệm" OR "quản trị AI") AND ("Bộ Y tế" OR bệnh viện OR "cơ sở khám bệnh, chữa bệnh")
DQ-IMPL-03: ("responsible AI" OR "AI governance" OR "AI ethics") AND (implementation OR adoption OR uptake OR plan OR pilot) AND (Vietnam OR "Viet Nam") AND (health OR hospital OR clinical)
DQ-TOOL-01: ("đánh giá tuân thủ" OR "tự đánh giá") AND ("đạo đức AI" OR "AI có trách nhiệm")
DQ-TOOL-02: (nền tảng OR công cụ) AND ("đánh giá tuân thủ" OR "đánh giá tác động") AND ("AI" OR "trí tuệ nhân tạo")
DQ-IMPL-04: ("trí tuệ nhân tạo" OR AI) AND ("theo dõi sau triển khai" OR hậu kiểm OR "giám sát sau triển khai" OR "đánh giá hiệu quả") AND (y tế OR bệnh viện OR "Sở Y tế")
DQ-IMPL-05: ("trí tuệ nhân tạo" OR AI) AND ("báo cáo sự cố" OR "quản lý chất lượng" OR kiểm toán OR thanh tra) AND (y tế OR bệnh viện OR "Sở Y tế")
```

### 7.4. Giám sát, khắc phục và kết quả

```text
DQ-EVID-01: ("đạo đức AI" OR "quản trị AI") AND (kiểm toán OR thanh tra OR giám sát)
DQ-EVID-02: ("AI" OR "trí tuệ nhân tạo") AND (sự cố OR khiếu nại OR khắc phục) AND (y tế OR bệnh viện)
DQ-EVID-03: ("AI" OR "trí tuệ nhân tạo") AND ("đánh giá tác động" OR kết quả) AND (y tế OR bệnh viện)
DQ-EVID-04: ("AI ethics" OR "AI governance") AND (audit OR inspection OR monitoring OR incident OR complaint OR redress OR "impact assessment" OR outcome OR result) AND (Vietnam OR "Viet Nam") AND (health OR hospital)
DQ-EVID-05: ("artificial intelligence" OR AI) AND ("post-implementation monitoring" OR "post-market surveillance" OR "incident reporting" OR "quality management" OR "effectiveness evaluation" OR audit) AND (Vietnam OR "Viet Nam") AND (health OR hospital OR "provincial health department")
```

Mỗi query ID có quy tắc dừng riêng; không gộp kết quả của nhiều query để tuyên bố một query đã bão hòa.

## 7.5. Khung tìm ca hữu hạn cho bằng chứng triển khai cấp Sở Y tế/bệnh viện

Nhánh này là **case-finding có chủ đích, maximum-variation** để tìm bằng chứng công khai về triển khai; nó không phải lấy mẫu xác suất, không đo prevalence và không đại diện cho toàn quốc. Khung hữu hạn được khóa để khả thi với bài 8 trang:

| Lớp ca | Khung lấy mẫu khóa trước | Domain chính thức bắt buộc | Query set | Trần và điểm dừng |
| --- | --- | --- | --- | --- |
| Sở Y tế | Ba Sở Y tế đã liệt kê trong frame: Hà Nội, Đà Nẵng, TP.HCM — một ca/miền Bắc/Trung/Nam. Tiêu chí đã khóa: domain cơ quan chính thức, không trùng cấp ca và cho phép kiểm tra thông tin chuyển đổi số/y tế số hoặc quản lý chất lượng. | Domain trong `implementation-case-sampling-frame.csv`; chỉ dùng PDF/HTML trên domain chính thức, không dùng fanpage hay báo chí làm bằng chứng. | `DQ-IMPL-01`, `DQ-IMPL-04`, `DQ-IMPL-05`, `DQ-TOOL-01`, `DQ-TOOL-02`, `DQ-EVID-01`, `DQ-EVID-02`, `DQ-EVID-03`, `DQ-EVID-04`, `DQ-EVID-05` | 3 Sở × 10 query ID × 20 kết quả/query; đọc tối đa 2 tầng. Dừng một Sở khi hết 20 kết quả hoặc hai trang liên tiếp không có URL mới; dừng toàn nhánh khi đủ 3 Sở. |
| Bệnh viện | Sáu sentinel đã liệt kê trong frame: Bạch Mai, Trung ương Huế, Chợ Rẫy, Vinmec Times City, Tâm Anh TP.HCM, Đại học Y Dược TP.HCM. Maximum-variation theo miền, tuyến trung ương, công/tư và đại học; mỗi cơ sở có domain chính thức được tái xác minh trước run. Danh sách không đổi sau khi bắt đầu nếu không có amendment. | Website chính thức của bệnh viện hoặc trang hệ thống/cơ quan chủ quản trong frame; PDF/HTML chính thức ưu tiên. | `DQ-IMPL-01`, `DQ-IMPL-04`, `DQ-IMPL-05`, `DQ-TOOL-01`, `DQ-TOOL-02`, `DQ-EVID-01`, `DQ-EVID-02`, `DQ-EVID-03`, `DQ-EVID-04`, `DQ-EVID-05` | 6 bệnh viện × 10 query ID × 20 kết quả/query; đọc tối đa 2 tầng. Dừng theo query như trên; dừng nhánh khi đủ 6 bệnh viện. |

`implementation-case-sampling-frame.csv` đã khóa tên, domain ứng viên, lý do chọn, query set, trần và độ sâu; mọi dòng và cả nhánh vẫn `NOT_RUN`. Trước full run, người rà soát thứ hai tái xác minh ownership/domain và ghi kết quả, không thay case để chạy theo kết quả. Cả hai lớp ca chỉ tạo bằng chứng về những cơ sở/portal đã xét và tài liệu đã thu hồi. Không suy prevalence, mức độ áp dụng quốc gia, hay hiệu quả toàn hệ thống; kết luận chỉ dùng ngôn ngữ “trong frame công khai đã tìm theo protocol”.

## 8. Quy tắc chạy, bão hòa và diễn giải

| Nhóm | Giới hạn cho từng query ID | Độ sâu | Điểm dừng |
| --- | ---: | ---: | --- |
| GOV, MOH và đơn vị, MST, UNESCO, WHO | 50 kết quả hoặc 5 trang nội bộ; fallback `site:` 50 | 2 tầng | Đạt trần hoặc hai trang liên tiếp không tạo URL mới. |
| GOV-VB, GAZ, VBPL | 100 kết quả hoặc 10 trang | 3 tầng trong đồ thị văn bản | Với mỗi seed, theo quan hệ căn cứ/dẫn chiếu/sửa đổi/thay thế/bãi bỏ/hướng dẫn đến khi không có document ID mới hoặc đạt 50 văn bản liên kết. |

Với mỗi văn bản, mã hóa riêng: hiệu lực; phạm vi; hướng dẫn triển khai; cơ quan/cơ chế được thành lập; bằng chứng hoạt động; tiếp nhận y tế; kiểm toán/giám sát/sự cố/khiếu nại/khắc phục; đánh giá kết quả. Một trường dương tính không làm các trường khác dương tính.

Tổng quan đánh giá **mức độ và chất lượng của bằng chứng công khai** về triển khai và hệ quả. Thiết kế này không ước tính trực tiếp tác động nhân quả của luật/khung lên kết quả y tế. Khi không thu hồi được bằng chứng sau quy trình đã định, viết: **“chưa tìm thấy trong nguồn công khai đã tìm theo protocol”**; không viết cơ chế “không tồn tại”, “không hoạt động” hoặc “không có tác động”.

Mỗi nguồn lưu URL, ngày truy cập, PDF/HTML, số hiệu/phiên bản, trạng thái, quan hệ văn bản và SHA-256. Ưu tiên bản ký/đăng Công báo. Nếu attachment một cổng mang dấu hiệu dự thảo nhưng Công báo có bản hoàn chỉnh, ghi discrepancy và dùng bản Công báo làm bản pháp lý chính.

## 9. Seed retrieval test

### 9.1. Ma trận seed Việt Nam phân tầng và provenance

| Tầng seed | Seed | Provenance/kênh | Thu hồi | Vai trò phát triển truy vấn |
| --- | --- | --- | --- |
| Policy/governance | Tran và cs., 2022 | PubMed PMID `35138264`; DOI `10.2196/32392`; pre-specified from JBI text-word development | Có | `DIRECT_POLICY_GOVERNANCE` |
| Policy/governance | Vuong và cs., 2019 | PubMed PMID `30717268`; DOI `10.3390/jcm8020168`; pre-specified from JBI text-word development | Có | `DIRECT_READINESS_GOVERNANCE` |
| Rights/safety/bias | Yang và cs., 2024 | PubMed PMID `38858466`; DOI `10.1038/s41598-024-64210-5`; pre-specified for bias/fairness vocabulary | Có | `DIRECT_EQUITY_BIAS` |
| Implementation | Van và cs., 2024 | PubMed PMID `39430352`; DOI `10.4103/tjo.TJO-D-23-00101`; pre-specified for clinical adoption vocabulary | Có | `DIRECT_CLINICAL_ADOPTION` |
| Implementation | Chanh và cs., 2023 | PubMed PMID `37397176`; DOI `10.2471/BLT.22.289423`; pre-specified for monitoring/implementation vocabulary | Có | `DIRECT_IMPLEMENTATION_MONITORING_CONTEXT` |
| Education/challenges | Nguyen và cs., 2025 | PubMed PMID `41329943`; DOI `10.2196/77817`; pre-specified as contextual sensitivity/noise check | Có | `CONTEXT_MEDICAL_EDUCATION_POSSIBLE_NOISE` |
| Luật AI | Công báo; `134/2025/QH15`; ban hành 10/12/2025, hiệu lực 01/03/2026 | Có | `LEGAL_RIGHTS_SAFETY_TRANSITION` |
| Nghị định thi hành | Công báo; `142/2026/NĐ-CP`; ban hành 30/04/2026, hiệu lực 01/05/2026 | Có | `LEGAL_IMPACT_MONITORING_INCIDENT` |
| Khung đạo đức AI | Công báo/Cổng văn bản; `05/2026/TT-BKHCN`; hiệu lực 10/03/2026 | Có | `LEGAL_ETHICS_FRAMEWORK` |

Các nhãn trên chỉ đánh giá độ bao phủ query. Không phải quyết định eligibility. Exact full-text check của Luật và Nghị định không tìm thấy điều khoản thành lập Hội đồng đạo đức AI quốc gia; đây là kết quả seed validation, không phải kết luận cuối về mọi nguồn công khai.

### 9.2. Seed chuẩn tắc/benchmark

WHO 2021, UNESCO 2021 và Wang–Freeman–Magrabi 2026 được thu hồi qua kênh phù hợp, nhưng không bị buộc phải xuất hiện trong corpus Việt Nam.

### 9.3. Artifact pháp lý và snapshot

| Artifact | SHA-256 |
| --- | --- |
| `vn-ai-law-134-2025-qh15.pdf` | `181B8687613093EAF42D09AF506999A22C7B13453EDE8EF574AC48DE2E1FDD1B` |
| `vn-ai-decree-142-2026-nd-cp.pdf` | `B2F71E9B86A878E4E91E0F59478B893F98A7DB853112DE66F3A7C58CBF392E18` |
| `05-2026-TT-BKHCN-signed-gazette.pdf` | `B7E83E1924FAFC2D94D008F20167CA9B5F8E6238EE7C274AA3BF6BD9C5CB4800` |
| `moh-structure-nd42-2025.pdf` | `224724CE39E507A6EA594E6C0B24E3A207EE3312521E7D9BF3934369033B217F` |
| `who-2021-ai-ethics-health-validation.pdf` | `DC5697AB8BA83B0AB42232DA6E85F1DD41EB4FAB9D112DEAEDFA97458A8CDFB1` |
| `unesco-2021-ai-ethics-recommendation-validation.html` | `7F57E5D885A7A35BEA0F18F863A35CB218F7CD3029BB1BE9C3DDFFE819DC57FB` |

PubMed kiểm tra sáu seed bằng PMID trong NBIB; OpenAlex kiểm tra từng DOI bằng candidate filter giữ nguyên cộng filter DOI, xem artifact `openalex-candidate-doi-recall-validation.json` (6/6 `RECALLED`). Không có independent gold standard; đặc biệt nhánh monitoring/outcome có thể không có seed đã biết. Vì vậy `seed_retrieval_test=PASS_PRELIMINARY` chỉ xác nhận độ nhạy tối thiểu đối với ma trận seed này, không xác nhận đủ điều kiện, tính đầy đủ, triển khai trong ngành y tế, hoạt động của hội đồng hay tác động.

## 10. Citation chasing

Chưa chạy. Sau G4–G5, mỗi nguồn Việt Nam đủ điều kiện có một thế hệ backward và một thế hệ forward; giữ `seed_id`, hướng, locator, kênh và điểm dừng. Record mới chỉ tính sau khử trùng lặp toàn cục.

## 11. Lịch sử thay đổi

| Phiên bản | Thay đổi | Tác động |
| --- | --- | --- |
| `dev-1` | MeSH/từ tự do cơ bản, địa lý AND y tế | 21 PubMed record. |
| `dev-2-PM` | Mở cụm chính sách, pháp lý, quyền, an toàn, explainability, audit/monitoring, sự cố/khiếu nại/khắc phục, dữ liệu, công bằng và chuẩn hóa; mốc trên 31/07/2026 | 88 PubMed record; tăng độ nhạy và nhiễu có thể quản lý bằng sàng lọc kép. |
| `dev-2-OA` | Liệt kê biến thể, thêm mốc trên, abstract inverted index; ghi trạng thái deprecated/API key | `meta.count=347`; 25 raw record validation. |
| `dev-2-official` | Phân rã council establishment/activity, implementation/adoption, audit/incident/redress/outcome; thêm Luật/Nghị định và cơ cấu MOH | Giảm nguy cơ suy pháp lý thành triển khai/tác động. |
| `dev-3-science-repair` | Khóa finite case-finding frame Sở Y tế/bệnh viện, thêm biến thể hậu triển khai/sự cố/chất lượng/hiệu quả, cursor-chain/count-discrepancy và DOI recall OpenAlex theo ma trận seed | Giới hạn suy luận và tăng khả năng tái lập; vẫn chỉ là `SEARCH_DEVELOPMENT`. |

## 12. Điều kiện chuyển trạng thái

Chỉ chuyển sang `PASS` khi Lộc Đặng kiểm tra độc lập:

- query và translation PubMed;
- mapping OpenAlex, key hygiene và terminal cursor rule;
- danh mục đơn vị/cổng và query ID/rule dừng;
- seed/channel và hash/path;
- CSV đọc đúng RFC 4180 UTF-8;
- phân biệt pháp lý, thành lập, hoạt động, tiếp nhận, giám sát và kết quả;
- không đưa count/artifact validation vào corpus hoặc PRISMA.
