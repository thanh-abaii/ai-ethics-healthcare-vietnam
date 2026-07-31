# Codebook trích xuất dữ liệu

**Trạng thái:** `PASS_CALIBRATED_PRE_REGISTRATION`  
**Phiên bản:** `0.1-draft`  
**Biểu mẫu liên kết:** `data-extraction-template.csv` (UTF-8, header-only, `NON_DATA_TEMPLATE`).

Đào Trung Thành là người chủ trì và người trích xuất/mã hóa. Lộc Đặng là reviewer độc lập, G2=`PASS` ngày 31/07/2026. Hiệu chuẩn ba vòng được ghi nhận tại [`calibration-attestation-2026-07-31.md`](calibration-attestation-2026-07-31.md), nên `SCREENING_EXTRACTION_CODEBOOK_GATE=PASS`. Không có pilot G4/G5, mã hóa chính thức, corpus hoặc count PRISMA trong phiên bản này.

## Đơn vị dòng, locator và giá trị chung

Mỗi dòng là một mệnh đề có locator ở đơn vị **`document_id × framework_id × component_id × scope_id`**. Bốn khóa này là các cột riêng, bắt buộc; không giấu khóa tổng hợp trong `principle`, `scope` hoặc `notes`. Một document có thể có nhiều dòng khi nó chứng minh các cấu phần, phạm vi hoặc loại bằng chứng khác nhau. Không tạo dòng lặp chỉ vì cùng một mệnh đề được nhiều reviewer kiểm tra.

`record_id` nối dòng trích xuất với registry tìm kiếm/sàng lọc và provenance của record; nhiều `record_id` có thể quy về một `document_id`, nhưng một document chỉ được trích xuất một lần cho mỗi tổ hợp khóa nội dung. `document_id` định danh một toàn văn; `framework_id` định danh khung/chính sách qua nhiều document/phiên bản; `component_id` định danh cấu phần quản trị; `scope_id` định danh phạm vi dùng để tổng hợp. Bản hiện hành là document chính; bản cũ chỉ giữ khi thay đổi có ảnh hưởng. Mọi phát biểu dương tính có locator (trang/điều/mục/bảng/URL snapshot) trong `notes` hoặc trường nội dung tương ứng. Dùng ` | ` để ngăn nhiều giá trị trong một ô; không dùng dấu phẩy làm delimiter dữ liệu.

Ở cấp source/document, mỗi trường nội dung chỉ chart một trong bốn dạng: giá trị/bằng chứng dương tính có locator; `NO_STATEMENT_IN_SOURCE` khi source đủ đọc nhưng không phát biểu về trường đó; `UNCERTAIN_SOURCE_EVIDENCE` khi có dấu vết nhưng locator/nghĩa/phạm vi chưa đủ chắc; hoặc `NOT_APPLICABLE` khi trường không phù hợp cấu trúc. `NOT_REPORTED` chỉ dùng cho trường báo cáo như tài trợ/COI khi loại nguồn có thể báo cáo nhưng không thấy sau kiểm tra. Tuyệt đối không dùng `NOT_FOUND`, `REPRESENTED`, `PARTIALLY_REPRESENTED` hay `INSUFFICIENT_INFORMATION` làm kết quả của một source/document. Ô trống chỉ dành cho trường không áp dụng với loại dòng và phải được giải thích trong `notes` nếu trường là quyết định.

Các vocab mở (citation, scope chi tiết, ai_type, health_context, principle, actor, control, evidence_record, patient_right, capacity_condition, council fields, monitoring, redress, impact fields, codes, notes) phải ghi nhãn chuẩn hóa ngắn + locator. Vocab đóng dưới đây phải dùng đúng mã. Mọi multi-value giữ thứ tự xuất hiện hoặc thứ tự thời gian và phân tách bằng ` | `.

## Định nghĩa 48 cột

Danh sách trong plan là mức tối thiểu 39 cột. Protocol/spec còn bắt buộc chín khái niệm thao tác không được nhập chung: `record_id`, `language`, `source_type`, `issuing_body_or_authors`, `component_id`, `scope_id`, `funding_source`, `funder_role`, `conflict_of_interest`. Vì thế template vận hành và danh sách trường chuẩn của Task 7 có **48 cột = 39 cột tối thiểu trong plan + 9 cột protocol/spec**. Bảng này là điểm đồng bộ thao tác cho plan, protocol và spec; mọi lần sửa một trong ba tài liệu phải đối chiếu lại đủ 48 tên cột trước khi khóa phiên bản.

| Trường | Định nghĩa và giá trị kiểm soát |
| --- | --- |
| `document_id` | ID bền của toàn văn, một giá trị, theo registry. |
| `record_id` | ID record từ registry tìm kiếm/sàng lọc; nếu nhiều record quy về cùng document, dùng ID canonical và ghi alias trong audit trail. |
| `framework_id` | ID bền khung/chính sách/cơ chế; `NO_DISTINCT_FRAMEWORK` khi nguồn không mô tả framework riêng. |
| `citation` | Trích dẫn ngắn đủ truy nguyên nguồn. |
| `year` | Năm ban hành/xuất bản `YYYY`; `UNKNOWN` chỉ khi không xác định được. |
| `language` | `VI`, `EN`, `VI_EN`, `OTHER_<ISO_CODE>`; ngôn ngữ toàn văn dùng để trích xuất. |
| `source_type` | `LEGAL_REGULATION`, `OFFICIAL_GUIDANCE_POLICY`, `ACADEMIC_STUDY`, `OFFICIAL_REPORT`, `GREY_REPORT`; phải nhất quán với screening registry. |
| `issuing_body_or_authors` | Tên cơ quan ban hành hoặc tác giả đúng theo nguồn; nhiều tên dùng ` | `. |
| `source_tier` | `T1_LEGAL_REGULATION`, `T2_OFFICIAL_NONBINDING`, `T3_PEER_REVIEWED_ACADEMIC`, `T4_OFFICIAL_REPORT_GREY`. |
| `legal_status` | `IN_FORCE`, `AMENDED_IN_FORCE`, `REPEALED_REPLACED`, `DRAFT`, `NONBINDING`, `NOT_APPLICABLE`, `UNKNOWN`; nêu nguồn kiểm tra trong notes. |
| `effective_date` | `YYYY-MM-DD`, hoặc `NOT_APPLICABLE`/`NOT_REPORTED`. |
| `binding_scope` | `NATIONAL`, `SUBNATIONAL`, `INSTITUTION`, `PROGRAM_PROJECT`, `PROFESSIONAL_GUIDANCE`, `NOT_BINDING`, `UNCLEAR`, kèm đối tượng/phạm vi. |
| `transition_rule` | `TRANSITION_PERIOD_ACTIVE`, `TRANSITION_PERIOD_ENDED`, `NO_TRANSITION_RULE`, `NOT_REPORTED`; ghi điều khoản và ngày kết thúc nếu có. |
| `compliance_deadline` | `YYYY-MM-DD`, `NO_DEADLINE`, `NOT_REPORTED`, hoặc `NOT_APPLICABLE`. |
| `implementation_time_at_search` | Số tháng đủ điều kiện tại ngày tìm (`NN_MONTHS`) + ngày tìm; `NOT_APPLICABLE` nếu không có mốc. |
| `component_id` | ID ổn định của cấu phần chuẩn đối chiếu/registry, dùng trực tiếp cho coverage và gap aggregation. |
| `scope_id` | ID ổn định của phạm vi tổng hợp; một scope hẹp không được gộp vào scope quốc gia nếu chưa có quy tắc đã khóa. |
| `scope` | Mô tả dân số/cơ sở/khu vực/vòng đời tương ứng `scope_id`; không suy rộng scope hẹp thành quốc gia. |
| `ai_type` | `ML`, `GENAI_LLM`, `CLINICAL_DECISION_SUPPORT`, `IMAGING_AI`, `ROBOTICS`, `ADMINISTRATIVE_AI`, `UNSPECIFIED_AI`, hoặc nhãn khác có giải thích. |
| `health_context` | `HOSPITAL`, `PRIMARY_CARE`, `PUBLIC_HEALTH`, `CLINICAL_RESEARCH`, `HEALTH_SYSTEM`, `MULTI_CONTEXT`, `UNSPECIFIED`. |
| `principle` | `component_id` + giá trị: `AUTONOMY`, `SAFETY`, `FAIRNESS`, `TRANSPARENCY`, `ACCOUNTABILITY`, `PRIVACY`, `SUSTAINABILITY`, `OTHER`. |
| `actor` | Chủ thể có trách nhiệm: `REGULATOR`, `HEALTHCARE_ORGANIZATION`, `CLINICIAN`, `DEVELOPER_VENDOR`, `AI_COUNCIL`, `PATIENT_PUBLIC`, `OTHER`. |
| `decision_right` | Quyền phê duyệt/dừng/khiếu nại/xem xét lại; `NO_STATEMENT_IN_SOURCE` nếu source không nêu. |
| `control` | Biện pháp: `IMPACT_ASSESSMENT`, `APPROVAL`, `VALIDATION`, `HUMAN_OVERSIGHT`, `POST_DEPLOYMENT_MONITORING`, `INCIDENT_RESPONSE`, `AUDIT`, `OTHER`, kèm locator. |
| `evidence_record` | Hồ sơ quyết định/nhật ký/chỉ số/báo cáo/audit: `DECISION_RECORD`, `LOG`, `METRIC`, `AUDIT_REPORT`, `COMPLAINT_RECORD`, `NO_STATEMENT_IN_SOURCE`, kèm locator. |
| `patient_right` | `NOTICE`, `CONSENT`, `CHOICE_REFUSAL`, `HUMAN_REVIEW`, `COMPLAINT_REMEDY`, `DATA_RIGHTS`, `NO_STATEMENT_IN_SOURCE`. |
| `capacity_condition` | `WORKFORCE`, `COUNCIL_MECHANISM`, `DATA_INFRASTRUCTURE`, `TRAINING`, `BUDGET`, `INTERSECTORAL_COORDINATION`, `NO_STATEMENT_IN_SOURCE`. |
| `implementation_stage` | Một hay nhiều mã loại bằng chứng ở bảng dưới; không phải điểm trưởng thành. |
| `implementation_scope` | Scope thực tế của bằng chứng triển khai; dùng taxonomy `scope` + locator. |
| `implementation_actor` | Chủ thể thực hiện/giám sát bằng chứng; dùng taxonomy `actor` + locator. |
| `council_establishment_instrument` | Văn bản lập hội đồng/cơ chế tương đương + locator; dùng `NO_STATEMENT_IN_SOURCE` khi source không nêu, không suy không tồn tại. |
| `council_mandate` | Nhiệm vụ, thẩm quyền, thành phần/quy trình hội đồng + locator. |
| `council_activity_evidence` | Họp, thẩm định, đào tạo, rà soát hoặc hoạt động thực tế + locator. |
| `monitoring_output` | Chỉ số, biên bản, audit, báo cáo, sự cố/khiếu nại/khắc phục được công bố + locator. |
| `incident_complaint_redress` | `INCIDENT`, `COMPLAINT`, `REDRESS`, `NO_MECHANISM_STATED`, `NOT_REPORTED`, kèm quy trình/hành động. |
| `impact_domain` | `SAFETY`, `FAIRNESS`, `PRIVACY`, `PATIENT_AUTONOMY`, `ACCOUNTABILITY`, `ACCESS`, `CARE_PROCESS_QUALITY`, `OTHER`; chỉ khi có đo lường. |
| `impact_evaluation_design` | `RCT`, `QUASI_EXPERIMENTAL`, `CONTROLLED_BEFORE_AFTER`, `UNCONTROLLED_BEFORE_AFTER`, `OBSERVATIONAL_ANALYTIC`, `DESCRIPTIVE_SELF_REPORT`, `NO_EVALUATION`, `UNCLEAR`. |
| `impact_comparator` | Nhóm/điều kiện so sánh; `NO_COMPARATOR`, `NOT_REPORTED`, `NOT_APPLICABLE`. |
| `impact_timepoint` | Mốc đo/chuỗi thời gian; `NOT_REPORTED` hoặc `NOT_APPLICABLE`. |
| `impact_attribution_limit` | `CAUSAL_SUPPORTED`, `CAUSAL_LIMITED`, `DESCRIPTIVE_ONLY`, `SELF_REPORT_ONLY`, `NO_OUTCOME_EVIDENCE`, `UNCLEAR`; nêu nguy cơ sai lệch/quy kết. |
| `quality_appraisal` | `LEGAL_AUTHORITY_ASSESSED`, `OFFICIAL_GUIDANCE_AUTHORITY_ASSESSED`, `JBI_<DESIGN>`, `AACODS`, `NOT_APPRAISED`; ghi tên checklist/thiết kế, kết luận và giới hạn, không tạo điểm chung. Thay JBI/AACODS bằng công cụ khác cần amendment trước khi áp dụng. |
| `funding_source` | Nguồn tài trợ tường minh; `NOT_REPORTED` hoặc `NOT_APPLICABLE`. |
| `funder_role` | Vai trò bên tài trợ trong thiết kế/tìm kiếm/lựa chọn/phân tích/viết/công bố; `NOT_REPORTED` hoặc `NOT_APPLICABLE`. |
| `conflict_of_interest` | Khai báo COI tường minh; `NOT_REPORTED` hoặc `NOT_APPLICABLE`. |
| `chapter10_only_code` | Mã chỉ nảy sinh từ Chương 10; chỉ mở sau nhánh quy nạp độc lập. `NONE` khi không dùng. |
| `inductive_code` | Mã mới/ca phủ định từ nguồn ngoài; `NONE` khi không có. |
| `reviewer` | `DAO_TRUNG_THANH`, `LOC_DANG`, `ADJUDICATOR_<ID>`; chỉ ghi mã Lộc cho quyết định thực tế do Lộc thực hiện. |
| `notes` | Locator, trích yếu có kiểm chứng, version, bất đồng/quyết định, giới hạn và liên kết audit trail. |

## Ví dụ hiệu chuẩn các trường quyết định khoảng trống

Mỗi nhóm dưới đây bao phủ toàn bộ trường quyết định gap. “Âm tính” nghĩa là bằng chứng không đủ để gán giá trị dương cho nhóm đang xét; nó không tự động cho phép mã `NOT_FOUND`.

| Nhóm và các trường được bao phủ | Ví dụ dương tính | Ví dụ âm tính | Ca biên — cách mã hóa |
| --- | --- | --- | --- |
| Thẩm quyền/pháp lý/phạm vi — `source_tier`, `legal_status`, `effective_date`, `binding_scope`, `transition_rule`, `compliance_deadline`, `implementation_time_at_search`, `component_id`, `scope_id`, `scope`, `quality_appraisal` | Bản Công báo xác nhận luật còn hiệu lực, áp dụng toàn quốc, nêu ngày hiệu lực/hạn chuyển tiếp; locator đủ để gán T1, component và national scope. | Bài blog nói “pháp luật yêu cầu” nhưng không dẫn văn bản/phiên bản: không nâng thành bao phủ pháp lý. | Quy định cấp tỉnh còn hiệu lực: mã dương trong `scope_id` của tỉnh, không gộp thành quốc gia; nếu thời kỳ chuyển tiếp còn chạy, giữ `TRANSITION_PERIOD_ACTIVE` và không suy thất bại. |
| Nguyên tắc/chủ thể/quyền quyết định/kiểm soát/hồ sơ — `principle`, `actor`, `decision_right`, `control`, `evidence_record` | Quy định giao hội đồng bệnh viện quyền phê duyệt và dừng hệ thống, yêu cầu impact assessment và lưu biên bản/audit log. | Nguồn chỉ nói “AI cần trách nhiệm” mà không có actor, quyền, kiểm soát hay hồ sơ: chart `NO_STATEMENT_IN_SOURCE` ở các trường thiếu. | Actor và control nằm ở hai nguồn cùng scope/thẩm quyền tương thích: có thể tổng hợp đủ sau coding kép; nếu phạm vi lệch hoặc xung đột, trạng thái aggregate sau cùng có thể là `PARTIALLY_REPRESENTED`/`INSUFFICIENT_INFORMATION`. |
| Quyền người bệnh/năng lực — `patient_right`, `capacity_condition` | Hướng dẫn nêu quyền được thông báo, từ chối, yêu cầu người xem xét lại và yêu cầu đào tạo/ngân sách/hạ tầng. | Nguồn nhắc “lấy người bệnh làm trung tâm” nhưng không xác định quyền hay điều kiện năng lực: chart `NO_STATEMENT_IN_SOURCE` ở trường cụ thể. | Chỉ có cơ chế phản hồi chung của bệnh viện, chưa rõ áp dụng cho AI: chart `UNCERTAIN_SOURCE_EVIDENCE`, không gán đầy đủ quyền khiếu nại AI. |
| Triển khai/hội đồng/giám sát/khắc phục — `implementation_stage`, `implementation_scope`, `implementation_actor`, `council_establishment_instrument`, `council_mandate`, `council_activity_evidence`, `monitoring_output`, `incident_complaint_redress` | Có quyết định lập hội đồng, nhiệm vụ, biên bản họp, báo cáo audit và hành động khắc phục tại bệnh viện xác định; mã riêng từng lớp bằng chứng. | Chỉ có quyết định thành lập: chứng minh tồn tại pháp lý/thể chế hóa; các trường activity/output/outcome chart `NO_STATEMENT_IN_SOURCE`, không suy không tồn tại. | Tin bệnh viện nói hội đồng “đã hoạt động” nhưng thiếu biên bản/locator: không nâng lên activity/output; chart `UNCERTAIN_SOURCE_EVIDENCE` cho lớp đó. |
| Kết quả và giới hạn quy kết — `impact_domain`, `impact_evaluation_design`, `impact_comparator`, `impact_timepoint`, `impact_attribution_limit` | Thiết kế kiểm soát có comparator, mốc trước–sau, outcome an toàn xác định và phân tích sai lệch đủ hỗ trợ mức quy kết đã ghi. | Báo cáo tự nhận “hiệu quả tăng” không có comparator/timepoint: `DESCRIPTIVE_SELF_REPORT` và `SELF_REPORT_ONLY`, không dùng ngôn ngữ nhân quả. | Quan sát trước–sau không kiểm soát có outcome đo được: có thể là `OUTCOME_EVALUATION`, nhưng `CAUSAL_LIMITED`; nêu nhiễu và không gọi là tác động nhân quả chắc chắn. |
| Nguồn gốc mã Chương 10/quy nạp — `chapter10_only_code`, `inductive_code`, `reviewer`, `notes` | Lộc khóa mã quy nạp cùng locator trước thời điểm mở mã Chương 10; mã sách phát sinh sau được ghi riêng và có audit timestamp. | Mã quy nạp được tạo sau khi reviewer đã xem mã Chương 10 hoặc không có provenance: không được coi là nhánh độc lập. | Khái niệm xuất hiện cả quy nạp và Chương 10: giữ hai provenance, đối chiếu chức năng sau unblinding; không xóa nguồn gốc hay tính hai cấu phần nếu cùng `component_id`. |
| Tài trợ/COI và giới hạn báo cáo — `funding_source`, `funder_role`, `conflict_of_interest` | Bài báo khai rõ nhà tài trợ, vai trò không tham gia phân tích và COI của tác giả. | Loại nguồn có phần khai báo nhưng không nêu thông tin sau kiểm tra toàn văn: dùng `NOT_REPORTED`, không suy “không có”. | Văn bản pháp luật không có cấu trúc tài trợ tác phẩm: dùng `NOT_APPLICABLE`; báo cáo dự án có nhà tài trợ nhưng không nêu vai trò: funding tường minh, `funder_role=NOT_REPORTED`. |
| Trạng thái tổng hợp — `REPRESENTED`, `PARTIALLY_REPRESENTED`, `NOT_FOUND`, `INSUFFICIENT_INFORMATION` tại `component_id × scope_id` | Các dòng nguồn tương thích cùng đáp ứng actor, hành động/control, phạm vi và bằng chứng cốt lõi: `REPRESENTED`. | Một dòng nguồn đơn lẻ không có nội dung cấu phần không đủ để gán `NOT_FOUND`; trạng thái chỉ có sau toàn bộ quy trình. | Nhiều nguồn partial chỉ nâng lên represented khi cùng scope, thẩm quyền tương thích, phủ đủ yếu tố và không xung đột; nếu thiếu locator/xung đột chưa phân xử thì `INSUFFICIENT_INFORMATION`. |

## Tầng bằng chứng, chuyển tiếp và hội đồng

| `implementation_stage` | Điều kiện tối thiểu |
| --- | --- |
| `NORMATIVE_LEGAL_ONLY` | Có văn bản/khung ban hành, nhưng chính document không có bằng chứng triển khai. |
| `INSTITUTIONALIZATION` | Có quyết định lập, nhiệm vụ, thành viên/chủ thể, quy trình, nguồn lực hoặc công cụ có locator. |
| `ADOPTION_ACTIVITY` | Có hoạt động xác định: thí điểm, sử dụng, đào tạo, tự đánh giá, kiểm tra hoặc họp. |
| `MONITORING_OUTPUT` | Có chỉ số, audit, báo cáo, sự cố, khiếu nại, khắc phục hoặc đầu ra giám sát được công bố. |
| `OUTCOME_EVALUATION` | Có đo thay đổi về an toàn, công bằng, quyền, tiếp cận hoặc quy trình/chất lượng chăm sóc. |

Các mã có thể cùng tồn tại cho một framework, nhưng luôn gắn document, scope, thời gian và locator riêng; không cộng thành thang tuyến tính. `OUTCOME_EVALUATION` chỉ dùng ngôn ngữ nhân quả khi `impact_evaluation_design` và `impact_attribution_limit=CAUSAL_SUPPORTED` thực sự cho phép. Báo cáo mô tả/tự báo cáo chỉ là hoạt động hoặc kết quả được công bố.

Hội đồng/cơ chế tương đương được tách: sự tồn tại pháp lý (`council_establishment_instrument`), nhiệm vụ (`council_mandate`), hoạt động (`council_activity_evidence`), đầu ra giám sát (`monitoring_output`) và kết quả (`impact_*`). Không suy hoạt động từ văn bản thành lập, không suy kết quả từ biên bản hoạt động.

Nếu `transition_rule=TRANSITION_PERIOD_ACTIVE`, bắt buộc có `compliance_deadline` và `implementation_time_at_search`. Thiếu hoạt động/đầu ra trong thời gian này chỉ là khoảng trống bằng chứng triển khai sớm; tuyệt đối không suy thành thất bại thực thi/chính sách.

## Bốn trạng thái đối chiếu chỉ ở tầng tổng hợp

`REPRESENTED`, `PARTIALLY_REPRESENTED`, `NOT_FOUND` và `INSUFFICIENT_INFORMATION` chỉ được gán **một lần cho mỗi `component_id × scope_id`** sau khi: tìm kiếm chính thức và các kênh bắt buộc đã hoàn tất; toàn bộ nguồn đủ điều kiện trong scope đã được chart; kiểm tra version/dẫn chiếu hoàn tất; các trường quyết định được coding kép; và hai reviewer đã đồng thuận hoặc phân xử. Chúng không phải nhãn source-level và không được điền vào `data-extraction-template.csv`.

| Mã | Định nghĩa | Ví dụ dương tính | Ví dụ âm tính | Ca biên |
| --- | --- | --- | --- | --- |
| `REPRESENTED` | Tập nguồn đủ điều kiện của đúng scope, xét theo thẩm quyền và tổng hợp đồng thuận, đáp ứng đủ chủ thể–hành động/kiểm soát–bằng chứng cốt lõi. | Tổng hợp cho thấy quy định còn hiệu lực và bằng chứng tương thích cùng xác định phê duyệt/audit AI lâm sàng trong scope bệnh viện. | Một bài quốc tế hoặc một source đơn lẻ không đủ để gán trạng thái tổng hợp Việt Nam. | Nhiều source chỉ nâng được khi cùng scope, thẩm quyền tương thích, đủ toàn bộ yếu tố và không xung đột. |
| `PARTIALLY_REPRESENTED` | Tổng hợp toàn bộ nguồn đủ điều kiện trong scope có phần tương ứng nhưng còn thiếu actor, hành động, scope, kiểm soát hoặc bằng chứng cốt lõi. | Sau tổng hợp, có yêu cầu minh bạch nhưng không source tương thích nào xác định người chịu trách nhiệm hay hồ sơ chứng minh. | Một source riêng không nêu actor chỉ được chart `NO_STATEMENT_IN_SOURCE`, chưa tạo trạng thái aggregate. | Một quy định cấp tỉnh đủ chi tiết: represented tại scope tỉnh, không đại diện quốc gia. |
| `NOT_FOUND` | Sau mọi kênh bắt buộc, truy vết sửa đổi/dẫn chiếu và kiểm tra chéo, không tìm thấy nguồn công khai đáp ứng. | Nhật ký hoàn tất không có cơ chế khắc phục khiếu nại AI trong scope đã khóa. | Chưa chạy xong tìm kiếm nhưng không thấy kết quả ban đầu. | Văn bản có dấu vết nhưng chưa truy được toàn văn: `INSUFFICIENT_INFORMATION`, không phải `NOT_FOUND`. |
| `INSUFFICIENT_INFORMATION` | Sau tổng hợp đầy đủ, tập nguồn có dấu vết liên quan nhưng thiếu locator, thẩm quyền, phiên bản hoặc phạm vi để phân loại aggregate chắc chắn. | Các source đủ điều kiện nhắc “hội đồng AI” nhưng bằng chứng tổng hợp không xác định được văn bản lập/nhiệm vụ. | Một tài liệu riêng có dấu vết mơ hồ chỉ chart `UNCERTAIN_SOURCE_EVIDENCE`; chưa tự tạo trạng thái aggregate. | Hai nguồn xung đột cùng tầng/phạm vi không quy đổi được sau phân xử: aggregate giữ `INSUFFICIENT_INFORMATION` hoặc trình bày phân tầng. |

## Chống đếm trùng, coding kép và audit trail

Registry giữ mọi `record_id` và provenance/kênh phát hiện; sau khử trùng lặp toàn cục, các record trùng được ánh xạ vào một `document_id` canonical thay vì xóa dấu vết. Trích xuất không nhân dòng theo số record alias hay số reviewer. Coverage/status chỉ đếm một lần mỗi aggregate `component_id × scope_id`. Gap chỉ được gán sau trạng thái aggregate đã đồng thuận và đếm một lần mỗi `component_id × gap_type × scope_id`, bất kể số record/document cùng hỗ trợ; không tạo gap count từ `NO_STATEMENT_IN_SOURCE` của một source. Số record, document và framework báo cáo riêng bằng đúng ID. Nhiều document của một framework không nhân số cấu phần; version chỉ được tách nếu thay đổi kết quả và phải liên kết cùng `framework_id`. Nguồn cấp thấp không ghi đè nghĩa vụ cấp cao trong scope chồng lấp; nguồn phạm vi hẹp không suy rộng.

Các trường quyết định gap phải coding kép: `source_tier`, `legal_status`, `binding_scope`, `scope`, `principle`, `actor`, `decision_right`, `control`, `evidence_record`, `patient_right`, `capacity_condition`, `implementation_stage`, các trường council/monitoring/redress, `impact_*`, `quality_appraisal`, `chapter10_only_code`, `inductive_code`. Trường mô tả có thể một người trích xuất, người thứ hai kiểm tra. Cùng một mẫu 8 document đa dạng (hoặc toàn bộ nếu dưới 8) được hai người trích độc lập; cần ≥75% đồng thuận ban đầu trên từng trường phân loại không rỗng. Sửa định nghĩa/aggregation/gap ảnh hưởng kết quả buộc lặp mẫu mới. Mọi vòng ghi version, ngày, sampling basis/seed, reviewer, locator, quyết định gốc, bất đồng, adjudication và lý do; không xóa bản cũ.

Nhánh `inductive_code` của Lộc Đặng phải hoàn tất và khóa trước khi `chapter10_only_code` được mở hoặc hiển thị cho Lộc Đặng. Sau đó mới đối chiếu hai nhánh, công bố mã/ca phủ định/kết luận thay đổi do lăng kính Chương 10 và chạy phân tích độ nhạy.
