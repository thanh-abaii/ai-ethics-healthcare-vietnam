# Trạng thái citation chasing chính thức

| Trường | Giá trị |
| --- | --- |
| Trạng thái hiện hành | `NOT_STARTED_PENDING_DUAL_SCREENING_AND_SEQUENCE_RESOLUTION` |
| Ngày ghi nhận trạng thái | 31/07/2026 |
| Phạm vi | Đợt tìm kiếm chính thức `search-rerun-01-2026-07-31`; chỉ tập Việt Nam. |
| Protocol thẩm quyền | OSF `62b8w`, DOI `10.17605/OSF.IO/62B8W`, §9.6–9.7. |
| Hành động trong lượt này | Không gọi nền tảng trích dẫn, không tạo record/provenance hay count mới. |

## Kết luận vận hành

Citation chasing **không được phép bắt đầu** cho đợt tìm kiếm chính thức hiện tại.

Theo protocol §9.7, seed của tìm kiếm chính thức chỉ có thể là nguồn “đã đủ điều kiện sau sàng lọc kép”. Registry của rerun hiện chỉ có header; trạng thái chính thức cũng ghi rõ PubMed và OpenAlex là `RAW_EXPORT_CAPTURED_NOT_SCREENED`, sàng lọc kép là `NOT_STARTED`. Vì vậy hiện không có `document_id` hoặc `record_id` nào đáp ứng điều kiện seed, và không có seed nào được nêu hoặc suy diễn từ export thô.

Sáu PMID ở `artifacts/g4-g5-feasibility-pilot-2026-07-31/g4-g5-pilot-results.json` chỉ là seed của **pilot khả thi**. Protocol §9.6 quy định record pilot không tự động đi vào corpus chính thức; chúng không thể được tái dùng làm seed cho rerun này.

## Đối chiếu điều kiện

| Điều kiện | Bằng chứng kiểm tra | Trạng thái | Hệ quả |
| --- | --- | --- | --- |
| Protocol đã đăng ký | OSF `62b8w`; protocol §9.6–9.7 | `PASS` | Điều kiện cần, chưa đủ để chạy. |
| G2 | `loc-dang-reviewer-confirmation.md` ghi `G2=PASS` | `PASS` | Thỏa điều kiện áp dụng cho pilot; không tạo seed chính thức. |
| `SCREENING_EXTRACTION_CODEBOOK_GATE` | `calibration-attestation-2026-07-31.md` ghi `PASS` | `PASS` | Sàng lọc kép có thể được tổ chức khi đúng trình tự. |
| Seed chính thức đủ điều kiện sau sàng lọc kép | `registry/record-registry.csv` header-only; `logs/official-search-status.md` ghi dual screening `NOT_STARTED` | `FAIL / NOT_AVAILABLE` | Chặn toàn bộ backward và forward citation chasing chính thức. |
| Điều kiện dừng tại cấp hướng | Chỉ đánh giá sau khi có seed và dedup toàn cục | `NOT_RUN` | Không được ghi “bão hòa” hay zero record. |

## Quy trình đã khóa khi blocker được tháo gỡ

Đối với **mỗi** seed chính thức đã có hai quyết định sàng lọc hợp lệ và kết quả đủ điều kiện:

1. Chỉ chạy một thế hệ `BACKWARD` và một thế hệ `FORWARD` trong tập Việt Nam.
2. Mỗi lượt phải lưu seed/document ID, hướng, nền tảng/cách truy, ngày, số record đã xem, raw locator/checksum, số record mới sau khử trùng lặp toàn cục, điểm đến/quyết định và điểm dừng.
3. Dừng sớm riêng cho một hướng khi hướng đó không tạo record mới sau khử trùng lặp toàn cục.
4. Giữ mọi manifestation và provenance trong event ledger; không xóa alias và không dùng count citation làm count PRISMA trước khi toàn bộ ledger được kiểm toán.

## Xung đột trình tự cần giải quyết trước khi chạy

`logs/official-search-status.md` đặt citation chasing là một điều kiện để chuyển `OFFICIAL_SEARCH_COMPLETE`, rồi mới mở sàng lọc. Cách sắp thứ tự đó mâu thuẫn với protocol §9.7, vì §9.7 yêu cầu seed chính thức phải có **sàng lọc kép trước**. Không thể vừa chờ `OFFICIAL_SEARCH_COMPLETE` để mở screening, vừa cần screening để có seed citation chasing.

Nhật ký này không diễn giải lại protocol và không tự mở sàng lọc. Chủ trì cần ghi một quyết định hậu đăng ký có locator kiểm tra được về trình tự thực thi; nếu quyết định đó làm thay đổi quy tắc đã đăng ký, phải công bố amendment trước khi chạy. Chỉ sau đó mới lập runbook thực thi và thu hồi citation chính thức.

## Evidence locators

- `../../../protocol.md` — §9.6–9.7; §8 về registry/provenance và khử trùng lặp.
- `../registry/record-registry.csv` — ledger chính thức hiện header-only.
- `../logs/official-search-status.md` — trạng thái export, dedup và sàng lọc của rerun.
- `../../../g4-g5-feasibility-pilot-2026-07-31.md` — tách riêng pilot khỏi corpus chính thức.
- `../../g4-g5-feasibility-pilot-2026-07-31/g4-g5-pilot-results.json` — sáu seed chỉ thuộc pilot.
