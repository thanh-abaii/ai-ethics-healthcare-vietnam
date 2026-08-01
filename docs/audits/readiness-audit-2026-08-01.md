# Kiểm toán readiness độc lập trước khi mở sàng lọc

**Ngày kiểm toán:** 2026-08-01  
**Phạm vi:** registry đầu vào, provenance/dedup, calibration/codebook và dấu hiệu mở screening.  
**Thẩm quyền:** đây là đánh giá kỹ thuật fail-closed; không phải xác nhận của PI và không mở sàng lọc.

## Kết luận

`READINESS_AUDIT_ADEQUATE_FOR_PI_REVIEW_WITH_CALIBRATION_EVIDENCE_LIMITATION`

Registry và provenance đạt yêu cầu kỹ thuật. Phiên bản audit ban đầu fail-closed vì có hai legacy worksheet chưa đồng bộ với registry hiện hành. Theo yêu cầu trực tiếp của chủ trì ngày 2026-08-02, hai tệp này đã được xóa. Kiểm tra lại xác nhận không còn worksheet cũ, 445/445 raw artifact vẫn hợp lệ và event ledger không có dòng screening. Audit kỹ thuật vì vậy đủ điều kiện để PI xem xét bước xác nhận tiếp theo, với giới hạn bằng chứng calibration đã nêu; việc này không xác nhận `DIRECT_SEARCH_COMPLETE` và không mở screening.

## Các kiểm tra đã thực hiện

| Điều kiện | Kết quả | Chứng cứ |
| --- | --- | --- |
| Tệp frozen khớp snapshot | PASS | 8 tệp lõi (`protocol`, search strategy, ba codebook, PRISMA-ScR, sampling frame, benchmark) đều khớp SHA-256 với `artifacts/protocol-registration-lock-2026-07-31/files/`; calibration attestation cũng khớp snapshot. |
| Registry đầu vào | PASS | 445 manifestations: 88 PubMed, 347 OpenAlex, 4 pháp lý và 6 PR07; 385 canonical records; 1.335 registry events. |
| Provenance và checksum | PASS | 445/445 locator được phân giải từ `artifacts/search-rerun-01-2026-07-31/registry/` và khớp SHA-256; không có missing hoặc mismatch. |
| Global dedup | PASS_WITH_PENDING_REVIEW | 60 cụm có định danh cứng được canonicalize; 71 trường hợp `EXACT_TITLE_YEAR` được giữ riêng và chờ review, không tự gộp. |
| Calibration và codebook | PASS_BY_PI_ATTESTATION_WITH_LIMITATION | Attestation ghi `SCREENING_EXTRACTION_CODEBOOK_GATE=PASS`; hồ sơ tự nêu chưa có bảng quyết định thô, random seed hay phép tính độc lập để tái kiểm từng vòng. |
| Không có quyết định screening trong event ledger | PASS | 0 dòng `SCREENING_DECISION` trong 1.335 event. |
| Biểu mẫu sàng lọc có thể mở vòng 1 | FAIL | Mỗi CSV reviewer có 391 dòng `PENDING_ADJUDICATION`; toàn bộ 391 `record_id` đều không khớp tập 385 `CANON-*`; reviewer value không theo controlled ID trong codebook. |

## Phát hiện fail-closed: legacy worksheet chưa đồng bộ

Hai tệp dưới đây không phải biểu mẫu trống và không thể được dùng làm biểu mẫu cho corpus hiện hành. Dấu vết cấu trúc cho thấy chúng nhiều khả năng là worksheet của một đợt corpus trước: cùng dải `REC-0001`–`REC-0391`, cùng 16 dòng pháp lý + 375 dòng học thuật, cùng thứ tự title/note và cùng thời điểm tạo/sửa cục bộ ngày 2026-08-01. Đây là suy luận từ cấu trúc tệp, không phải xác nhận về tác giả hay mục đích ban đầu.

- `docs/governance/round-1-screening-reviewer-1-dao-trung-thanh.csv`: 391 dòng, reviewer `Dao Trung Thanh`.
- `docs/governance/round-1-screening-reviewer-2-loc-dang.csv`: 391 dòng, reviewer `Loc Dang`.

`PENDING_ADJUDICATION` là một giá trị quyết định trong codebook, chỉ có nghĩa sau hai quyết định độc lập và một bất đồng. Các record ID `REC-*` của hai tệp không thuộc Master Input Registry hiện hành (`CANON-*`). Không được xóa, sửa, hay quy các dòng này cho bất kỳ người rà soát nào nếu chưa có xác nhận của họ.

## Khắc phục đã thực hiện và điều kiện kiểm tra lại

1. Ngày 2026-08-02, đã xóa hai legacy worksheet theo yêu cầu trực tiếp của chủ trì. Hash trước khi xóa lần lượt là `b5ff2a23bd38886b0ca362bdf31d341fff761fc49ccc83e5606b214567a6f3d2` và `24314191762fc2ef2853d452e94f50ea4fc52420dde17c5166114bd999e38ee0`.
2. Chạy lại kiểm tra rằng registry/event ledger vẫn không có dữ liệu screening và không còn biểu mẫu cũ.
3. Khi PI quyết định mở vòng 1, tạo hai biểu mẫu mới có đúng 385 `CANON-*`, controlled reviewer ID theo codebook và không có quyết định tiền điền.
4. Sau kiểm tra lại, PI tự quyết định có xác nhận `DIRECT_SEARCH_COMPLETE` hay không. Kiểm toán này không thay thế quyết định đó.

## Phụ lục kiểm tra lại sau xóa — 2026-08-02

| Kiểm tra | Kết quả |
| --- | --- |
| Legacy worksheet còn tồn tại | 0/2 |
| Raw artifact không phân giải được hoặc sai SHA-256 | 0/445 |
| Kênh trong registry | 88 PubMed, 347 OpenAlex, 4 pháp lý, 6 PR07 |
| Event ledger | 445 `MANIFESTATION`, 445 `PROVENANCE`, 445 `CANONICALIZATION` |
| Dòng `SCREENING_DECISION` | 0 |

Kết quả này chỉ khôi phục điều kiện kỹ thuật trước khi PI xem xét. Không có quyết định inclusion/exclusion, adjudication, citation chasing hay xác nhận thay PI được tạo ra.

## Giới hạn

Audit không đánh giá inclusion/exclusion, không thực hiện citation chasing, không kiểm tra lâm sàng, không thay đổi tệp frozen và không sửa dữ liệu của reviewer.
