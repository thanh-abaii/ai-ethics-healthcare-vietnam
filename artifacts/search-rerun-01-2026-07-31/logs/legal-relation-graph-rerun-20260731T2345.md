# Cập nhật đồ thị quan hệ pháp lý — target 55/2025/NĐ-CP

| Trường | Giá trị |
| --- | --- |
| Trạng thái | `FAIL_CLOSED_OFFICIAL_LOCATOR_IDENTIFIED_RAW_RETRIEVAL_FAILED` |
| Phạm vi | Một target đã phát hiện tại depth 1; không có sàng lọc, mã hóa pháp lý, trích xuất, deduplication, citation chasing hoặc sự kiện PRISMA. |
| Locator được cung cấp để kiểm tra | `https://vbpl.vn/TW/Pages/vbpq-van-ban-goc.aspx?ItemID=175587` |
| Định danh được gắn với locator | `55/2025/NĐ-CP` |
| Nguồn quan hệ depth 1 | `05/2026/TT-BKHCN`, recital p. 1: căn cứ Nghị định số `55/2025/NĐ-CP`. |

## Bằng chứng thu hồi và kiểm toán

Lượt truy hồi trực tiếp dùng URL chính thức nói trên được lưu tại `official-sources/legal-relation-55-2025-ndcp-20260731T2345/`.

| Artefact | SHA-256 | Kết quả |
| --- | --- | --- |
| `request.json` | `eabce12bcbafc68d293a6613a3572f66e4891bd9288967f7c7159da2f5d6a3fb` | Lưu URL, ItemID, thời điểm, phương thức GET và user-agent. |
| `response-body.html` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Rỗng: không nhận được response body. |
| `response-headers.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Rỗng: không có HTTP response header trước khi timeout. |
| `transport-stderr.txt` | `fd28073aa2fee7cf83137b8a84efed8dd2284bf46091a89f10082db62c399595` | `curl: (28) Connection timed out after 10010 milliseconds`. |

`checksums.csv` và `capture-manifest.json` nằm cùng thư mục. Kiểm tra lại sau run có `HASH_INTEGRITY_FAILURES=0`. Script tái lập là `scripts/capture_vbpl_official_document.ps1`.

## Cập nhật register cạnh

| Edge ID | Source | Quan hệ | Target | Trạng thái trước | Trạng thái sau |
| --- | --- | --- | --- | --- | --- |
| `LRE-002` | `GOV-VB-05-2026-TT-BKHCN` | `CĂN_CỨ` | `55/2025/NĐ-CP` | `DISCOVERED_UNHARVESTED` | `OFFICIAL_LOCATOR_IDENTIFIED_RAW_RETRIEVAL_FAILED` |

Trạng thái sau chỉ nói rằng một locator VBPL chính thức đã được định danh để thử thu hồi và request trực tiếp đã thất bại ở tầng vận chuyển. Nó **không** xác nhận nội dung toàn văn, cơ quan ban hành, ngày, hiệu lực, sửa đổi/thay thế/bãi bỏ, hoặc bất kỳ cạnh mới nào phát sinh từ Nghị định 55.

## Hệ quả đối với traversal

Không thể đọc target để phát hiện quan hệ depth 2. Đồ thị chưa đạt depth 3 và không thỏa điều kiện dừng protocol. Cần một client/kết nối khác thu hồi được HTML/PDF gốc từ VBPL hoặc nguồn pháp lý chính thức tương đương, kèm raw/header/checksum, trước khi tiếp tục traversal.
