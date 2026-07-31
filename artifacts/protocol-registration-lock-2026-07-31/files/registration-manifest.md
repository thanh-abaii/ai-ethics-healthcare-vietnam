# Manifest gói đăng ký protocol

## Trạng thái

`LOCKED_LOCALLY_READY_FOR_OSF`

Các dependency tiền đăng ký đã đạt yêu cầu. Theo [`protocol-amendment-pr-03.md`](protocol-amendment-pr-03.md), hồ sơ được khóa cục bộ ngày 31/07/2026 tại `artifacts/protocol-registration-lock-2026-07-31`, kèm danh mục tệp và checksum SHA-256. Trạng thái nghiên cứu vẫn là `NOT_REGISTERED` cho đến khi locator của bản đăng ký được kiểm tra.

## Các dependency đã hoàn tất

| Dependency | Trạng thái hiện tại | Bằng chứng/việc đã hoàn tất |
| --- | --- | --- |
| Bộ chuẩn quốc tế | `PASS` | Đã được người rà soát thứ hai độc lập Lộc Đặng rà soát và khóa ngày 31/07/2026 (`PASS_BY_LOC_DANG_REVIEW` tại `international-benchmark.md`). |
| Competitive checkpoint trước khóa | `PASS_WITH_NARROWED_CLAIM` | `competitive-checkpoint-2026-07-31.md`. |
| Khai báo tài trợ | `PASS` | `funding-declaration.md`: chủ trì xác nhận không có tài trợ chuyên biệt ngày 31/07/2026; vai trò bên tài trợ `NOT_APPLICABLE`. |
| Ngày khóa cục bộ | `PASS` | 31/07/2026 theo `PR-03`; đây là khóa gói nguồn, không phải xác nhận đã đăng ký. |

## Nội dung gói bất biến khi mọi dependency đạt PASS

1. `protocol.md` bản đã khóa.
2. `prisma-scr-checklist.md`.
3. `search-strategy.md` và artifact `PRE_REGISTRATION_SEARCH_DEVELOPMENT`.
4. `international-benchmark.md` đã được review độc lập.
5. `screening-codebook.md`, `data-extraction-codebook.md`, `record-registry-codebook.md` cùng các template CSV.
6. `competitive-checkpoint-2026-07-31.md` và `funding-declaration.md`.
7. `protocol-amendment-pr-02.md` và `protocol-amendment-pr-03.md`.
8. Xác nhận vai trò, hiệu chuẩn và benchmark của Lộc Đặng.
9. Manifest file-size/SHA-256, version, ngày tạo và quan hệ tệp nguồn.

## Thủ tục đăng ký

Chủ trì tải nguyên gói snapshot bất biến lên OSF bằng mẫu đăng ký phù hợp cho systematic/scoping review, hoàn tất metadata và kiểm tra locator của bản đăng ký. Chỉ sau bước kiểm tra locator mới đổi `NOT_REGISTERED` thành `REGISTERED` trong protocol và mở quyền chạy G4–G5. Mọi thay đổi phương pháp sau đăng ký phải được ghi bằng amendment mới; không sửa ngược gói đã khóa.
