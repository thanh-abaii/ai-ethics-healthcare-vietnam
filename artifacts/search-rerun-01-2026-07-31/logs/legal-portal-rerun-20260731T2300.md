# Lượt thu hồi cổng pháp lý chính thức — rerun 01

| Trường | Giá trị |
| --- | --- |
| Run ID | `20260731T2300` |
| Trạng thái | `FAIL_CLOSED_INCOMPLETE_LEGAL_PORTAL_SEARCH` |
| Phạm vi | 15 query ID luật/khung/hội đồng của chiến lược đã khóa, cùng một target phát hiện trong đồ thị: `55/2025/NĐ-CP`. |
| Ranh giới | Chỉ thu hồi thô và kiểm tra provenance. Không sàng lọc, quyết định eligibility, mã hóa hiệu lực/quan hệ pháp lý, trích xuất, dedup, citation chasing hoặc đếm PRISMA. |
| Input bất biến | `protocol.md` và snapshot OSF chỉ được đọc; không tệp nào trong chúng bị thay đổi. |

## Artefact kiểm toán

- Runner tái lập: `scripts/run_legal_official_portals.py`.
- Lượt chạy: `official-sources/legal-portals-20260731T2300/`.
- Ledger trang/cổng/query: `query-ledger.csv` (48 dòng).
- Mỗi request đã gửi có raw body và raw response header riêng trong `raw/`; cả hai có SHA-256 trong ledger.
- Kiểm tra độc lập sau run: `HASH_INTEGRITY_FAILURES=0` cho tất cả body/header có trong ledger; `python -m py_compile scripts/run_legal_official_portals.py` thành công.

## Kết quả có thể khẳng định

| Cổng | Dấu vết | Kết quả vận hành | Diễn giải được phép |
| --- | --- | --- | --- |
| GOV-VB | 16 POST tới API mà giao diện GOV-VB gọi: `https://timkiem.chinhphu.vn/Home/search` | HTTP 200, nhưng 16/16 payload có trường `error: "Unable to connect to the remote server"`; từng dòng là `FAIL_CLOSED`. | Không có kết quả tìm kiếm sử dụng được và không đạt rule 10 trang. HTTP 200 không được coi là zero result. |
| Công báo (GAZ) | Một GET công khai được lưu, body có shell giao diện tìm kiếm | Không xác minh được endpoint trả danh mục kết quả hay phân trang server-side; 15 query còn lại được đánh `NOT_ATTEMPTED_AFTER_PORTAL_FAILURE`. | Không đạt truy vấn/cap 100 kết quả hay 10 trang. Không suy ra không có văn bản. |
| VBPL | GET query đầu tiên và lỗi client TLS được lưu | `CLIENT_ERROR`; 15 query còn lại `NOT_ATTEMPTED_AFTER_PORTAL_FAILURE`. | Không có nguồn thay thế nào được tuyên bố. |

## Target của đồ thị: 55/2025/NĐ-CP

Target này phát hiện từ recital trang 1 của `05/2026/TT-BKHCN`, không phải một query ID bổ sung của protocol. Lượt thử tại GOV-VB được lưu ở `query-ledger.csv`, dòng `LGRAPH-TARGET-55-2025-ND-CP`, raw `raw/gov-q16-p01.json` và header tương ứng. API phản hồi HTTP 200 nhưng có lỗi upstream nói trên, hash body `c54306f2380636a70345691b6b563833c5791ebb4f53eb4859e581673e4e0e5a`.

Vì vậy chưa thu hồi được metadata, portal document ID, bản Công báo hay toàn văn chính thức của `55/2025/NĐ-CP`. Đây là **không thu hồi được trong lượt chạy này**, không phải bằng chứng văn bản không tồn tại hoặc không có hiệu lực; cạnh `LRE-002` vẫn giữ trạng thái `DISCOVERED_UNHARVESTED`.

## Hậu quả đối với đồ thị pháp lý

Đồ thị vẫn chỉ có cạnh trực tiếp đã xác minh `05/2026/TT-BKHCN --CĂN_CỨ--> 134/2025/QH15`. Không thể đi đến depth 2 từ target 55; không được khẳng định quan hệ cho hai seed PDF chưa có lớp text. Điều kiện protocol — theo các quan hệ đến depth 3, dừng khi không có document ID mới hoặc 50 tài liệu liên kết — chưa đạt.

## Lượt kỹ thuật không hoàn chỉnh được giữ lại

Hai thử nghiệm trước khi runner xử lý giới hạn đường dẫn/thời hạn request được giữ nguyên trong `official-sources/legal-portals-20260731T213000+0700/`, `...T2145/` và `...T2200/`; mỗi thư mục có `PARTIAL-RUN-STATUS.md`. Chúng không được dùng làm corpus, dedup, screening hay PRISMA.

## Điều còn thiếu để đóng nhánh pháp lý

1. Một client hoặc endpoint có thể thực sự tìm và phân trang GOV-VB, Công báo và VBPL: mỗi query đạt terminal hợp lệ hoặc cap 100 kết quả/10 trang, với raw page/header/checksum.
2. Thu hồi bản chính thức và toàn văn của `55/2025/NĐ-CP`, sau đó tiếp tục mọi target đồ thị mới tới depth 3 hoặc cap 50 liên kết.
3. Lấy text/page-image reviewable cho các seed `134/2025/QH15` và `142/2026/NĐ-CP` trước khi lập cạnh hoặc non-edge từ chúng.
4. Chỉ khi các điều kiện trên có evidentiary record, mới có thể chuyển trạng thái nhánh pháp lý; lượt này không thay đổi trạng thái official search chung.
