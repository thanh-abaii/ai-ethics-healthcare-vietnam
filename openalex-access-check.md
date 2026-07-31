# Kiểm tra truy cập và xuất dữ liệu OpenAlex cho G1

## Mục đích và ranh giới

Đây là kiểm tra truy cập kỹ thuật cho cổng G1, không phải pilot search khoa học. Truy vấn được chọn để kiểm tra đồng thời Boolean, phrase search, filter ngày, field selection và cursor pagination trên một tập nhỏ. Các record trong artifact này không được nhập vào `search-log.csv`, tập nghiên cứu, G4, G5 hoặc dùng làm bằng chứng khoa học.

- `protocol_version`: `PRE_PROTOCOL`
- `search_strategy_version`: `PRE_SEARCH_STRATEGY`
- Người kiểm tra: Codex, dưới sự điều hành của Đào Trung Thành

## Cấu hình tái lập

| Thuộc tính | Giá trị |
| --- | --- |
| Query kỹ thuật | `("artificial intelligence" AND ethics AND medicine AND Vietnam)` |
| Filter | `from_publication_date:2024-01-01,to_publication_date:2024-01-07` |
| API URL template | `https://api.openalex.org/works?search={URL_ENCODED_QUERY}&filter={URL_ENCODED_FILTER}&select={URL_ENCODED_FIELDS}&per-page=25&cursor={URL_ENCODED_CURSOR}` |
| Thời gian chạy | 31/07/2026, 06:10:45–06:10:51, Asia/Saigon (`2026-07-30T23:10:45Z`–`2026-07-30T23:10:51Z`) |
| Phương thức truy cập | HTTPS GET tới OpenAlex API bằng PowerShell `Invoke-WebRequest`, TLS 1.2, anonymous; không tạo tài khoản và không dùng API key |
| `per_page` | `25` |
| Pagination | Cursor bắt đầu bằng `*`; tiếp tục bằng `meta.next_cursor` cho đến khi giá trị này là `null` |
| Trường chọn | `id`, `doi`, `display_name`, `publication_year`, `publication_date`, `type`, `language`, `ids`, `primary_location`, `authorships` |
| Raw format | JSON phản hồi trực tiếp từ API; mỗi page được giữ thành một tệp riêng và không chuyển qua CSV/RIS |
| Script | [`scripts/export-openalex-g1.ps1`](scripts/export-openalex-g1.ps1) |

Mỗi query, filter, danh sách trường và cursor đều được URL-encode. Script phân tích JSON bằng `ConvertFrom-Json -AsHashtable`, phát hiện HTTP lỗi, cursor loop, thay đổi `meta.count`, thiếu OpenAlex ID, ID trùng và sai lệch giữa số thực xuất với `meta.count`. Mỗi lỗi làm tiến trình kết thúc với mã khác 0.

## Kết quả

| Chỉ số | Kết quả |
| --- | ---: |
| Số page | 4 |
| Kết quả theo page | 25, 25, 25, 17 |
| `meta.count` của page đầu | 92 |
| Số record thực xuất | 92 |
| Chênh lệch `actual - meta.count` | 0 |
| Số OpenAlex ID trùng | 0 |
| HTTP status | 200 trên cả 4 page |
| Kết luận G1 | `PASS` |

## Artifact và checksum

Thư mục artifact: [`artifacts/g1-openalex-access/`](artifacts/g1-openalex-access/)

| Tệp | Vai trò | SHA256 |
| --- | --- | --- |
| [`page-001.json`](artifacts/g1-openalex-access/page-001.json) | Raw API page 1, 25 record | `c661c9ea4c249706b15fd5c201f06ef8313244eac2d941c501f2197efaace36c` |
| [`page-002.json`](artifacts/g1-openalex-access/page-002.json) | Raw API page 2, 25 record | `5d356555702f8391842e0797226fe24932189aabd4ad920358ff695184848a01` |
| [`page-003.json`](artifacts/g1-openalex-access/page-003.json) | Raw API page 3, 25 record | `d522b56c07ab78044e8b7eef0d04ebcfbf6e64652aa481b70c24d48b3910b960` |
| [`page-004.json`](artifacts/g1-openalex-access/page-004.json) | Raw API page 4, 17 record | `b24865e497aa21c3012e2a8de6e67e1828cd8ba8259c5fb7db75d9b6a5af49da` |
| [`manifest.csv`](artifacts/g1-openalex-access/manifest.csv) | Page number, requested URL, HTTP status, page/cumulative count, `meta.count`, trạng thái next cursor, filename và SHA256 của raw page | `b6db8e40527baaf699aebd7f67f3bcf0853853ade5ed45e48fa07c195457608d` |
| [`checksums.sha256`](artifacts/g1-openalex-access/checksums.sha256) | Danh sách checksum của 4 raw page và manifest; không tự hash chính tệp checksum | Không áp dụng |

Đối soát độc lập sau lần chạy cuối xác nhận: 4 raw page bằng 4 dòng manifest; tổng `results.Count` là 92 và bằng `meta.count`; không có ID trùng; cả 5 checksum đều khớp; không phát hiện API key, access token hoặc Authorization secret trong script và artifact.

## Kết luận và giới hạn

G1 đạt `PASS`: tại thời điểm kiểm tra, OpenAlex hỗ trợ truy cập anonymous, thực thi được truy vấn kỹ thuật có Boolean và phrase, đi hết cursor, xuất raw JSON có locator và tạo chuỗi checksum tái lập. Checkpoint tổng thể vẫn là `BLOCKED_ACCESS_OR_REVIEWER` vì G2 về xác nhận bằng văn bản của Lộc Đặng còn `PENDING_CONFIRMATION`.

OpenAlex là API sống; dữ liệu, `meta.count`, thứ tự và cursor có thể thay đổi khi OpenAlex cập nhật chỉ mục. Vì vậy, rerun về sau có thể tạo count và checksum khác, cần ghi lại như một snapshot mới. Truy vấn kiểm tra này không đại diện cho câu hỏi nghiên cứu hay chiến lược tìm kiếm khoa học và không được tái sử dụng để kết luận G4–G5.
