# Kiểm chứng phản biện script legacy `run_g4_g5.py` — 31/07/2026

**Đối tượng kiểm chứng:** commit `01b3f39` trên `origin/main`, script `scripts/run_g4_g5.py`.  
**Kết luận:** `NOT_APPROVED_FOR_OFFICIAL_SEARCH_OR_PRISMA`.

## Điều đã xác nhận

- Commit và script tồn tại trên remote hiện hành.
- Script thêm retry/backoff cho một số lỗi HTTP, khoảng nghỉ 0,5 giây cho OpenAlex và nhánh fallback local cache.
- Những đặc tính đó có thể giúp một chương trình không crash. Chúng không tự xác nhận một lượt tìm kiếm mới, đầy đủ, đúng protocol hay độc lập với dữ liệu cũ.

## Các điểm không đạt

| Hạng mục | Bằng chứng trong script | Hệ quả khoa học |
| --- | --- | --- |
| Truy vấn PubMed | Chuỗi trong script là bản rút gọn; thiếu nhiều thuật ngữ, điều kiện ngôn ngữ và không bằng chuỗi §4.1 đã khóa. | Không phải truy vấn chính thức đã đăng ký. |
| Fallback PubMed | Khi API lỗi, script dùng cache local hoặc tự gán `pm_count = 88`. | Có thể `exit 0` dù không thu hồi được PMID/raw API; không được tạo count PRISMA. |
| Fallback OpenAlex | Đọc các trang `openalex-pilot-page-*.json` trong `artifacts/search-run-2026-07-31/`, là nhánh đã quarantine. | Tái dùng dữ liệu legacy thay vì một run mới. |
| API key và nhận diện | Địa chỉ `daotrungthanh@domain.com` là placeholder; không phải contact đã xác minh hay secret/API key hợp lệ. | Không chứng minh quyền truy cập Polite Pool hoặc tuân thủ truy cập. |
| Cursor/provenance | `requested_url` bị rút thành `https://api.openalex.org/works?...`; dừng ở `page < 25`; không kiểm tra điều kiện terminal cursor đã khóa. | Không tái tạo chuỗi trang, không chứng minh full export. |
| Sàng lọc | Phân loại bằng từ khóa heuristic ngay trong script. | Không thay thế double independent screening theo codebook; không dùng để quyết định eligibility. |
| Nguồn pháp lý | Script không thu hồi, không ghi log hay kiểm tra hiệu lực/quan hệ của các portal pháp lý/MOH/MST/WHO/UNESCO. | Không thể tuyên bố đã chạy nhánh thông tin pháp lý. |

## Quyết định vận hành

Không chạy script này: nó ghi vào `artifacts/search-run-2026-07-31/`, tức thư mục legacy đã quarantine, và có nguy cơ làm lẫn lịch sử thử nghiệm với official rerun sạch.

Lượt official chỉ được công nhận khi từng nguồn được thu hồi mới theo query đã khóa, có raw response, URL/cursor hoặc history handle, thời điểm, checksum, record-level provenance và không có fallback thay count hay thay raw record. Trạng thái hiện tại của rerun sạch vẫn là: pháp lý `RETRIEVED_SEED_ONLY`; PubMed và OpenAlex `FAIL_CLOSED`.
