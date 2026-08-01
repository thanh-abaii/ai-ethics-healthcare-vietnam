# Kiểm toán Codex: đợt thu hồi độc lập PR07 12 slot

| Trường | Giá trị |
| --- | --- |
| Artifact được kiểm toán | `artifacts/pr07-12slot-isolated-run-20260801T164606/` |
| Báo cáo bàn giao | `reports/pr07-12slot-isolated-retrieval-report-2026-08-01.md` |
| Đặc tả đối chiếu | `docs/governance/pr07-public-source-retrieval-operational-spec-v1.md` |
| Kết luận kiểm toán | `FAIL_CLOSED_NOT_READY_FOR_MASTER_REGISTRY` |
| Phạm vi | Tính đầy đủ retrieval/provenance/checksum; không đánh giá eligibility hay screening |

## Kết luận

Đợt chạy có 12 dòng slot ledger và 186 dòng checksum, nhưng không đạt điều
kiện `RETRIEVAL_TERMINAL_FOR_READINESS` trong đặc tả PR07 v1. Không dùng
manifestation inventory của run này để dựng Master Input Registry hoặc chạy
global dedup của corpus chính thức. Giữ nguyên toàn bộ run và báo cáo bàn giao
như audit trail; không xóa hay sửa artifact.

## Bằng chứng fail-closed

1. **Checksum không khớp.** Kiểm tra lại toàn bộ 186 dòng `sha256.csv` cho
   thấy 31 mismatch, đều là raw header artifacts. Vì manifest/checksum là điều
   kiện bắt buộc của terminal readiness, chỉ riêng lỗi này đã chặn nhận run.
2. **Không có artifact cấp tài liệu cho các slot được ghi `RETRIEVED`.** Sáu
   trong tám slot `RETRIEVED` trỏ đúng homepage domain (`asttmoh.vn`,
   `imda.moh.gov.vn`, `soyte.danang.gov.vn`, `medinet.gov.vn`, `bachmai.gov.vn`,
   `vinmec.com`). Hai URL WHO còn lại cũng là landing page `www.who.int/vietnam/`.
   Homepage/landing page không phải PDF, HTML bài viết hay metadata cấp tài liệu
   theo định nghĩa `RETRIEVED` của PR07 v1.
3. **Hai slot dùng cùng một manifestation.** `INTL-01` và `INTL-03` cùng trỏ
   `https://www.who.int/vietnam/` và cùng raw body SHA-256
   `2F093E9AD117BDEDAFAE7D77225361DDFFD6DD5B69FD2D0262A88CFEE9D900E6`.
   PR07 v1 quy định alias giữ provenance nhưng không chiếm hai slot.
4. **Locator không phản ánh truy vấn.** Locator evidence ledger ghi target URL
   là root homepage cho từng domain/query, thay vì URL search/locator có query
   hoặc URL tài liệu phát hiện từ locator. HTTP 200 của homepage chỉ chứng minh
   transport đến homepage, không chứng minh đã thực hiện locator cho slot.

## Hệ quả vận hành

- Không ghi `DIRECT_SEARCH_COMPLETE`, không mở screening và không gọi readiness
  audit là đạt.
- Không gộp 8 manifestation của run này vào registry chính thức.
- Có thể tái sử dụng run này làm bằng chứng lỗi transport/WAF và làm bản mẫu để
  sửa runner, nhưng không dùng kết quả `RETRIEVED` của nó làm corpus.

## Điều kiện cho một run thay thế có thể được audit

1. URL request cho từng query phải là search/locator thực tế hoặc URL tài liệu
   phát hiện từ locator, không phải homepage mặc định.
2. Mỗi `RETRIEVED` phải có artifact cấp tài liệu/metadata và locator/provenance
   liên kết được tới query ID/slot.
3. Document trùng giữa các slot chỉ là alias/provenance; slot sau đi theo quy
   tắc thay thế hoặc nhận trạng thái kỹ thuật thích hợp.
4. Tái tạo `sha256.csv` sau khi mọi raw body/header/error đã được ghi, rồi kiểm
   tra 100% dòng manifest khớp byte-for-byte trước khi tuyên bố terminal.

Không yêu cầu mở rộng domain, query, số slot, crawler hay thay đổi Amendment v1
để khắc phục các lỗi này.
