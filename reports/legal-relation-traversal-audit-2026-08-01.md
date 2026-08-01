# Kiểm toán lượt truy vết quan hệ pháp lý — 01/08/2026

## Kết luận vận hành

Lượt chạy `legal-relation-traversal-20260801T110354` đã thu hồi lại từ nguồn
chính thức ba seed pháp lý đã đăng ký, cùng header HTTP và SHA-256 cho từng
landing page/PDF. Lượt này **không hoàn tất điều kiện terminal của đồ thị** và
được giữ ở trạng thái:

`FAIL_CLOSED_RELATION_TRAVERSAL_BLOCKED_UNRESOLVED_OFFICIAL_TARGET`

Do đó nó không mở tìm kiếm chính thức, không mở sàng lọc, và không cho phép
khẳng định hiệu lực, phạm vi, triển khai, tác động, hoặc sự tồn tại/hoạt động
của bất kỳ hội đồng nào.

## Bằng chứng đã xác minh

| Nguồn | Tình trạng thu hồi | Quan hệ được ghi |
| --- | --- | --- |
| `134/2025/QH15` | PDF chính thức đã thu hồi; 20 trang nhưng chỉ 19 ký tự lớp chữ | Không ghi quan hệ âm tính hay suy diễn từ PDF quét. |
| `142/2026/NĐ-CP` | PDF chính thức đã thu hồi; 97 trang nhưng chỉ 96 ký tự lớp chữ | Không ghi quan hệ âm tính hay suy diễn từ PDF quét. |
| `05/2026/TT-BKHCN` | PDF chính thức đã thu hồi; 9 trang, 14.129 ký tự lớp chữ | Hai dòng `Căn cứ` có thể kiểm tra trực tiếp. |

Hai cạnh từ `05/2026/TT-BKHCN` là: (i) `CĂN_CỨ → 134/2025/QH15`, đã có seed
đích; (ii) `CĂN_CỨ → 55/2025/NĐ-CP`, là số hiệu mới được phát hiện. Cạnh thứ
hai chưa phải một hồ sơ pháp lý đã xác minh.

## Lý do dừng fail-closed

Theo quy tắc đã đăng ký, đồ thị chỉ dừng hợp lệ khi không còn document ID mới
hoặc đạt trần 50 văn bản liên kết. Sau khi phát hiện `55/2025/NĐ-CP`, runner đã
gửi yêu cầu định vị đến Cổng Văn bản Chính phủ và lưu lại raw HTML/header.
Phản hồi HTTP 200 không chứa số hiệu đích, cũng không trả một locator PDF hoặc
`docid` có thể kiểm tra. Vì vậy không thể chuyển sang độ sâu 1 bằng cách đoán
`docid`, chọn văn bản “tương tự”, hoặc dùng snippet ngoài nguồn chính thức.

## Khả năng kiểm toán

- Run manifest: `artifacts/search-rerun-01-2026-07-31/official-sources/legal-relation-traversal-20260801T110354/run-manifest.json`
- Capture ledger: `.../capture-ledger.csv`
- Node/edge ledger: `.../node-ledger.csv`, `.../edge-ledger.csv`
- Raw HTML/PDF/header và `sha256.csv`: cùng thư mục run.

Đã đối chiếu lại toàn bộ 18 checksum: `0` sai lệch. Script tái lập:
`scripts/run_legal_relation_traversal.py`.

## Điều kiện để chạy tiếp

Chỉ khi có được một locator chính thức xác định được cho `55/2025/NĐ-CP` (hoặc
một cơ chế truy vấn chính thức trả về hồ sơ đó) mới được thu hồi PDF/HTML, kiểm
tra quan hệ ở độ sâu tiếp theo, và tiếp tục đến độ sâu tối đa 3 hoặc điều kiện
terminal/cap. Không được dùng trạng thái fail-closed này để suy ra rằng văn bản
hay bất kỳ cơ chế pháp lý nào không tồn tại.

---

## Cập nhật hậu kiểm: locator chính thức đã được cung cấp và chạy lại

**Run thay thế:** `legal-relation-traversal-20260801T112448`  
**Trạng thái thay thế:** `RAW_RELATION_TRAVERSAL_TERMINAL_NOT_LEGAL_EFFECT_CODED`

Locator chính thức cho `55/2025/NĐ-CP` đã được thu hồi ở cả landing page Cổng
Văn bản Chính phủ (`docid=213020`) và PDF ký số trên `datafiles.chinhphu.vn`.
20/20 checksum của run thay thế đã đối chiếu đúng. PDF có 18 trang nhưng chỉ
17 ký tự lớp chữ có thể trích xuất; vì vậy runner không suy diễn quan hệ âm
tính từ văn bản quét. Không có document ID mới được phát hiện từ các PDF có
lớp chữ đủ để kiểm tra; đồ thị dừng hợp lệ ở 4 node, 2 cạnh, dưới trần 50 và
độ sâu tối đa 3.

Cập nhật này chỉ đóng nhánh **truy vết quan hệ pháp lý**. Nó không mã hóa hiệu
lực/phạm vi, không chứng minh hay bác bỏ bất kỳ hội đồng nào, và không mở G6,
G7 hoặc sàng lọc.
