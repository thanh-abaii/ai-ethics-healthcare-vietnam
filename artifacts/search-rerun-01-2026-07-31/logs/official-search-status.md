# Trạng thái tìm kiếm chính thức

| Trường | Giá trị |
| --- | --- |
| Trạng thái hiện hành | `DIRECT_SEARCH_IN_PROGRESS` |
| Ngày ghi nhận trạng thái | 01/08/2026 |
| Protocol thẩm quyền | OSF `62b8w`, DOI `10.17605/OSF.IO/62B8W` |
| Quy tắc bất biến | Không sửa `protocol.md` hoặc `artifacts/protocol-registration-lock-2026-07-31/`. |

| Nhánh | Trạng thái | Bằng chứng | Hệ quả vận hành |
| --- | --- | --- |
| PubMed | `RAW_EXPORT_CAPTURED_NOT_SCREENED` | `pubmed/eutils-run-20260731T203345+0700/manifest.json` | 88 PMID mới; sẵn sàng đưa vào dedup toàn cục khi toàn bộ search hoàn tất. |
| OpenAlex pre-amendment | `FAIL_CLOSED_RAW_EXPORT_INCOMPLETE` | `openalex/openalex-api-20260731T203857+0700/manifest.json` | Bảo lưu để audit; không dùng làm corpus. |
| PR-05 | `POST_REGISTRATION_METHOD_AMENDMENT_APPROVED` | `../../protocol-amendment-pr-05.md` | Chỉ áp dụng prospective cho run OpenAlex mới. |
| OpenAlex theo PR-05 | `RAW_EXPORT_CAPTURED_NOT_SCREENED` | `openalex/openalex-api-20260731T204525+0700/manifest.json` | 347 work/347 ID duy nhất; checksum đã kiểm tra. |
| Nguồn pháp lý/chính thức | `FAIL_CLOSED_INCOMPLETE_LEGAL_PORTAL_SEARCH` | `logs/legal-portal-rerun-2026-08-01.md` | Rerun độc lập ngày 01/08 có 48 dòng ledger: 18 request thực gửi, raw/header hash hợp lệ; 30 dòng `NOT_SENT_AFTER_PORTAL_FAILURE` được ghi rõ. GOV-VB vẫn có lỗi upstream, Công báo chưa xác thực search/pagination và VBPL vẫn lỗi tầng kết nối; không có record pháp lý mới hợp lệ để nạp provenance/dedup. |
| Đồ thị quan hệ pháp lý | `FAIL_CLOSED_INCOMPLETE` | `logs/legal-relation-graph-rerun-20260731T2345.md`; `logs/vbpl-browser-retrieval-deviation-2026-07-31.md`; `logs/vbpl-ipv4-retrieval-deviation-2026-07-31.md` | Đã hash-verify 3 PDF và xác minh một cạnh `05/2026/TT-BKHCN → 134/2025/QH15`. Target depth-1 `55/2025/NĐ-CP` đã có locator VBPL chính thức, nhưng direct capture, trình duyệt và IPv4 đều timeout; không thể tiếp tục depth 2–3 hoặc tuyên bố quan hệ mới. |
| Kiểm toán provenance/dedup chuẩn bị | `PASS_CURRENT_RAW_SOURCES_NOT_FINAL` | `logs/provenance-dedup-audit.json` | 435 manifestation PubMed/OpenAlex đã xác minh hash; 119 candidate cần canonicalization sau khi các kênh còn lại hoàn tất. |
| G6 — khả thi ngân sách 25 nguồn | `NOT_RUN` | Chưa có G6 feasibility record hậu direct search | Phải đạt `PASS` trước sàng lọc chính thức theo protocol §20–21. |
| G7 — bản thử theo hợp đồng tạp chí | `NOT_RUN` | Chưa có G7 mock-manuscript record hậu direct search | Phải đạt `PASS` trước sàng lọc chính thức; `FAIL` buộc dừng trước screening. |
| Sàng lọc kép | `NOT_STARTED` | Không có decision log hậu rerun | Đào Trung Thành và Lộc Đặng chưa đưa ra quyết định eligibility cho run chính thức. |
| Trích xuất/tổng hợp | `NOT_STARTED` | Không có extraction dataset hậu rerun | Chưa tạo kết luận hoặc khoảng trống thực chứng. |

## Điều không được suy diễn ở thời điểm này

- Không có corpus cuối cùng, PRISMA flow diagram hay count PRISMA.
- Không có kết quả G5 hay kết luận về số lượng bằng chứng đủ điều kiện.
- Không diễn giải việc chưa tìm thấy thành “không tồn tại” hoặc “không có tác động”.

## Ranh giới của dashboard pha hiện hành

`DIRECT_SEARCH_IN_PROGRESS` chỉ là pha thu hồi trực tiếp từ PubMed, OpenAlex và các cổng chính thức. Nó không đồng nghĩa với hoàn tất nghiên cứu.

Citation chasing là hoạt động hậu sàng lọc được protocol §9.7 quy định. Nó được theo dõi tại `citation-chasing/citation-chasing-status.md`, không nằm trong dashboard, gate hay mục tiêu đóng direct search hiện tại.

Mốc gần nhất chỉ là `DIRECT_SEARCH_READY_FOR_G6_G7`: hoàn tất các query/cổng trực tiếp còn lại, relation graph, provenance và dedup toàn cục của nguồn direct search. Khi đó nhóm mới kiểm tra G6 (khả thi ngân sách 25 nguồn) và G7 (bản thử theo hợp đồng tạp chí). Chỉ sau khi **cả G6 và G7 đều `PASS`**, cùng các dependency screening còn hiệu lực, mới mở sàng lọc kép. Không được dùng bất kỳ nhãn trung gian nào để tạo PRISMA count cuối, kết luận, hay đóng tìm kiếm toàn bộ.
