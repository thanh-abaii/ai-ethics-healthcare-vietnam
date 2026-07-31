# Codebook registry record

**Trạng thái:** `PASS_CALIBRATED_PRE_REGISTRATION`  
**Phiên bản:** `0.1-draft`  
**Biểu mẫu:** `record-registry-template.csv` — UTF-8, RFC 4180, header-only, `NON_DATA_TEMPLATE`.

Registry này đã được bao gồm trong hiệu chuẩn được ghi nhận ngày 31/07/2026, nhưng chưa có dữ liệu pilot, corpus, PRISMA count hay quyết định đủ điều kiện chính thức. Chỉ ghi quyết định dưới mã Lộc khi chính Lộc thực hiện quyết định đó.

## Mô hình event ledger và đơn vị

CSV là sổ sự kiện append-only. Mỗi dòng có `registry_event_id` duy nhất và một `row_type`:

| `row_type` | Đơn vị dòng | Mục đích |
| --- | --- | --- |
| `MANIFESTATION` | một biểu hiện được phát hiện (`record_id`) | Giữ metadata của từng kết quả/alias đúng như kênh thu hồi. |
| `PROVENANCE` | `record_id × provenance_event_id` | Giữ từng lần phát hiện qua query, portal hoặc citation chasing; một record có thể có nhiều dòng. |
| `CANONICALIZATION` | `record_id → canonical_record_id/document_id` | Ghi quyết định trùng lặp, căn cứ và bản ưu tiên; không xóa alias. |
| `FRAMEWORK_LINK` | `document_id × framework_id` | Biểu diễn quan hệ nhiều–nhiều giữa document và framework; mỗi link một dòng. |
| `SCREENING_DECISION` | `record_id × reviewer × screening_stage` | Giữ quyết định độc lập của từng reviewer ở từng giai đoạn. |
| `ADJUDICATION` | một bất đồng được phân xử | Giữ quyết định cuối, người phân xử, ngày và codebook version. |
| `AUDIT_EVENT` | một thay đổi registry | Bổ sung/sửa/supersede bằng sự kiện mới; không ghi đè dòng cũ. |

`record_id` là một manifestation thu hồi từ một kênh hoặc alias riêng. `canonical_record_id` là manifestation đại diện cho cụm trùng sau canonicalization. `document_id` là toàn văn/nội dung trí tuệ duy nhất; nhiều record và bản định dạng có thể nối đến một document. `framework_id` là khung/chính sách/cơ chế; nhiều document có thể mô tả một framework và một document có thể mô tả nhiều framework qua các dòng `FRAMEWORK_LINK`.

Không dùng `framework_ids` ghép trong một ô. Quan hệ framework luôn là một link event riêng để truy vấn và chống đếm trùng.

## Quy tắc ID và trường

| Trường | Định nghĩa/giá trị kiểm soát |
| --- | --- |
| `registry_event_id` | ID bất biến duy nhất cho từng dòng, ví dụ `REG-E000001`. |
| `row_type` | Một trong bảy loại dòng ở trên. |
| `record_id` | ID manifestation bất biến; bắt buộc trừ audit toàn cục không gắn record. |
| `canonical_record_id` | ID record đại diện; trước canonicalization dùng `PENDING_CANONICALIZATION`. |
| `document_id` | ID nội dung toàn văn canonical; `PENDING_DOCUMENT_LINK` khi chưa xác minh. |
| `framework_id` | Một ID trên dòng `FRAMEWORK_LINK`; `NOT_APPLICABLE` cho nguồn không có framework riêng. |
| `title` | Tiêu đề đúng manifestation; không âm thầm thay bằng tiêu đề normalized. |
| `year` | `YYYY`; `UNKNOWN` nếu chưa xác định. |
| `language` | `VI`, `EN`, `VI_EN`, `OTHER_<ISO_CODE>`, `UNKNOWN`. |
| `doi` | DOI lowercase, bỏ tiền tố URL; `NOT_REPORTED` nếu loại nguồn có thể có nhưng không thấy. |
| `pmid` | PMID dạng số; `NOT_APPLICABLE` hoặc `NOT_REPORTED`. |
| `openalex_id` | ID dạng `W...`; `NOT_APPLICABLE` hoặc `NOT_REPORTED`. |
| `official_document_number` | Số hiệu văn bản chính thức; `NOT_APPLICABLE` hoặc `NOT_REPORTED`. |
| `normalized_url` | HTTPS URL chuẩn hóa bỏ tracking/fragment, giữ đường dẫn định danh; URL gốc nằm trong raw artifact/provenance. |
| `manifestation_type` | `DATABASE_RECORD`, `HTML`, `PDF`, `XML`, `NBIB`, `JSON`, `OFFICIAL_GAZETTE`, `OTHER`. |
| `provenance_event_id` | ID lần phát hiện; bắt buộc với `PROVENANCE`. |
| `discovery_channel` | `PUBMED`, `OPENALEX`, `OFFICIAL_PORTAL`, `LEGAL_DATABASE`, `FORWARD_CITATION`, `BACKWARD_CITATION`, `OTHER_APPROVED`. |
| `query_id` | ID truy vấn/search-log row; `NOT_APPLICABLE` với nguồn không phát hiện qua query. |
| `seed_record_id` | Seed của citation chasing; chỉ dùng với forward/backward, nếu không `NOT_APPLICABLE`. |
| `citation_direction` | `FORWARD`, `BACKWARD`, `NOT_APPLICABLE`. |
| `discovery_date` | ISO 8601 `YYYY-MM-DD`. |
| `raw_artifact_locator` | Đường dẫn/URL đến raw artifact chứa manifestation. |
| `raw_artifact_checksum` | SHA-256 lowercase; `PENDING_CHECKSUM` chỉ trước khi artifact được khóa. |
| `duplicate_status` | `UNASSESSED`, `UNIQUE`, `DUPLICATE_ALIAS`, `VERSION_RELATED`, `NOT_DUPLICATE`. |
| `duplicate_basis` | `DOI`, `PMID`, `OPENALEX_ID`, `OFFICIAL_NUMBER`, `NORMALIZED_URL`, `TITLE_AUTHOR_YEAR`, `CONTENT_MATCH`, hoặc nhiều mã bằng ` | `. |
| `preferred_version` | `YES`, `NO`, `PENDING`; chỉ một manifestation `YES` trong một cụm canonical cho mỗi mục đích phân tích. |
| `preferred_version_reason` | Hiệu lực, độ đầy đủ, bản sửa đổi, định dạng hoặc chất lượng locator; không chọn theo kết quả. |
| `reviewer` | `DAO_TRUNG_THANH`, `LOC_DANG`, hoặc ID reviewer đã xác nhận. |
| `screening_stage` | `TITLE_ABSTRACT`, `FULL_TEXT`, `NOT_APPLICABLE`. |
| `reviewer_decision` | `INCLUDE`, `EXCLUDE`, `UNCERTAIN`, `DUPLICATE_LINKED`, `PENDING_ADJUDICATION`, `NOT_APPLICABLE`. |
| `exclusion_reason` | `EX01`–`EX09` đầy đủ theo screening codebook; chỉ một mã chính khi `EXCLUDE`, nếu không để trống. |
| `decision_date` | ISO 8601; bắt buộc với quyết định reviewer. |
| `final_adjudication` | `INCLUDE`, `EXCLUDE`, `DUPLICATE_LINKED`, `NO_ADJUDICATION_REQUIRED`, `PENDING`. |
| `adjudicator` | ID người/cơ chế phân xử; `NOT_APPLICABLE` nếu không có phân xử. |
| `adjudication_date` | ISO 8601 hoặc `NOT_APPLICABLE`. |
| `screening_codebook_version` | Phiên bản dùng khi quyết định; bắt buộc với screening/adjudication. |
| `registry_version` | Phiên bản schema/ledger áp dụng cho event. |
| `supersedes_event_id` | Event cũ được sửa nghĩa; để trống nếu event mới, không xóa event cũ. |
| `change_type` | `CREATE`, `CORRECT_METADATA`, `ADD_PROVENANCE`, `CANONICALIZE`, `LINK_FRAMEWORK`, `SCREEN`, `ADJUDICATE`, `SUPERSEDE`. |
| `change_reason` | Lý do có locator/bằng chứng; bắt buộc khi sửa hoặc supersede. |
| `notes` | Alias khác, URL gốc, locator quyết định, bất đồng và giới hạn; không chứa dữ liệu nhạy cảm. |

## Provenance nhiều–nhiều và canonicalization

Mọi manifestation được giữ bằng một dòng `MANIFESTATION`. Mỗi lần cùng manifestation được tìm thấy qua kênh/query/seed khác tạo thêm một dòng `PROVENANCE`; không nhập các kênh vào một ô và không bỏ lần phát hiện trùng. Citation chasing bắt buộc có `seed_record_id`, `citation_direction` và locator. Count “record mới” chỉ tính sau canonicalization toàn cục, còn provenance count báo cáo riêng.

Canonicalization theo thứ tự: DOI/PMID/OpenAlex ID/số hiệu chính thức; normalized URL; rồi tiêu đề–cơ quan/tác giả–năm–version và đối chiếu nội dung. Một ID khớp không đủ khi nguồn là bản sửa đổi hoặc manifestation chứa nội dung khác. Dòng `CANONICALIZATION` ghi status, basis, record đại diện, document link và lý do chọn version. Alias không bị xóa, ID không được tái sử dụng.

Bản hiện hành/đầy đủ thường là `preferred_version=YES`; bản cũ vẫn giữ `VERSION_RELATED` khi cần giải thích thay đổi. Lý do ưu tiên dựa trên hiệu lực, version và khả năng kiểm chứng, không dựa trên việc nội dung ủng hộ kết luận.

## Screening, bất đồng và lịch sử

Hai reviewer tạo hai dòng `SCREENING_DECISION` độc lập trên cùng `record_id × stage`; quyết định của người này không ghi đè người kia. Khi bất đồng, thêm dòng `ADJUDICATION`, giữ nguyên hai dòng gốc. `final_adjudication` là quyết định dùng cho flow, luôn kèm người/ngày/codebook version. Mọi lần sửa metadata, canonicalization hay quyết định tạo `AUDIT_EVENT`/event thay thế có `supersedes_event_id`; dữ liệu trước không bị xóa.

## Missingness và kiểm tra trước sử dụng

- Ô trống chỉ được phép khi trường không áp dụng cho `row_type` và schema nói rõ không bắt buộc.
- `UNKNOWN`: chưa xác định sau kiểm tra hiện tại; `NOT_REPORTED`: loại nguồn có thể báo cáo nhưng không thấy; `NOT_APPLICABLE`: trường không phù hợp cấu trúc; `PENDING_*`: bước hợp lệ chưa hoàn tất vì dependency.
- Không dùng `NOT_FOUND` trong registry để kết luận không tồn tại. Registry chỉ ghi manifestation/provenance/quyết định.
- Trước khi khóa, kiểm tra: ID event duy nhất; mọi record có manifestation; provenance có raw locator/checksum; alias có canonical link; mọi canonical record có document link; framework link không ghép nhiều ID; screening kép có version; adjudication có chuỗi quyết định; không có event bị ghi đè.
