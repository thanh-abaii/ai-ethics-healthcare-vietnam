# Báo cáo bàn giao session và đề nghị PI xem xét xác nhận `DIRECT_SEARCH_COMPLETE`

**Dự án:** Scoping review “Từ nguyên tắc đến thực hành: khung đạo đức và quản trị AI trong y học, cùng các khoảng trống khi áp dụng tại Việt Nam”  
**OSF registration:** `62b8w`, DOI [10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W)  
**Amendment áp dụng:** `POST_REGISTRATION_AMENDMENT_CONSOLIDATED_V1`, công bố/hiệu lực 2026-08-01  
**Ngày bàn giao:** 2026-08-02  
**Người có thẩm quyền quyết định:** PI Đào Trung Thành

> [!IMPORTANT]
> Báo cáo này là đề nghị để PI xem xét. Nó **không** xác nhận `DIRECT_SEARCH_COMPLETE`, không mở screening và không thay thế quyết định của PI hoặc người rà soát độc lập.

## 1. Kết luận điều hành

Sau remediation và kiểm tra lại độc lập, các điều kiện kỹ thuật trước screening theo Amendment v1 đã đạt mức `ADEQUATE_FOR_PI_REVIEW_WITH_CALIBRATION_EVIDENCE_LIMITATION`.

Đề nghị PI xem xét xác nhận `DIRECT_SEARCH_COMPLETE` cho corpus trực tiếp đã khai báo. Nếu PI xác nhận, bước kế tiếp là tạo hai biểu mẫu screening mới cho 385 `CANON-*` và mở screening tiêu đề/tóm tắt kép độc lập. Không được tái sử dụng worksheet cũ hoặc ghi quyết định thay bất kỳ reviewer nào.

## 2. Tóm tắt công việc của session

| Hạng mục | Kết quả | Trạng thái |
| --- | --- | --- |
| Rà soát registry AGY | Loại 223 tiêu đề ứng viên trong `official-inventory.csv` khỏi corpus; registry đúng phạm vi 445 manifestations. | PASS |
| Sửa provenance PR07 | Compiler chọn body PR07 theo SHA-256 của manifest, thay vì theo thứ tự glob; locator PR07 được chuẩn hóa tương đối với artifact root. | PASS |
| Kiểm tra checksum/locator | 445/445 raw artifact phân giải được và khớp SHA-256. | PASS |
| Canonicalization/dedup | 385 canonical records; 60 cụm định danh cứng được canonicalize; 71 ca `EXACT_TITLE_YEAR` giữ riêng, chờ review theo codebook. | PASS_WITH_PENDING_REVIEW |
| Kiểm tra frozen OSF | 8 tệp lõi và calibration attestation khớp byte-for-byte snapshot khóa. | PASS |
| Kiểm tra screening tiền mở | Event ledger có 0 `SCREENING_DECISION`. Hai legacy worksheet `REC-*` không khớp registry hiện hành đã bị xóa theo yêu cầu trực tiếp của PI ngày 2026-08-02; hash trước xóa được lưu trong audit. | PASS_AFTER_REMEDIATION |
| Calibration/codebook | `SCREENING_EXTRACTION_CODEBOOK_GATE=PASS` theo attestation của PI. | PASS_BY_PI_ATTESTATION_WITH_LIMITATION |

## 3. Corpus trực tiếp hiện hành

| Kênh | Manifestations | Trạng thái chứng cứ |
| --- | ---: | --- |
| PubMed | 88 | Raw export, manifest, provenance trong registry |
| OpenAlex | 347 | Raw API pages, manifest, provenance trong registry |
| Pháp lý quốc gia | 4 | Hồ sơ cấp tài liệu có checksum |
| PR07 nguồn công khai | 6 | Tài liệu chưa screening từ run 12 slot hữu hạn |
| **Tổng** | **445** | **385 canonical records sau dedup cứng** |

PR07 đã kết thúc ở `RETRIEVAL_TERMINAL_FOR_READINESS`: 6 `RETRIEVED`, 4 `OUT_OF_SCOPE`, 2 `UNRETRIEVABLE`. Bốn hồ sơ pháp lý được ghi riêng; cùng 12 slot PR07, khung 16 slot đã có kết quả được ghi nhận. Các trạng thái `OUT_OF_SCOPE` và `UNRETRIEVABLE` là giới hạn truy hồi/phạm vi slot, không phải kết luận rằng chính sách hay thực hành tương ứng không tồn tại.

## 4. Căn cứ cho PI xem xét

1. Amendment v1 yêu cầu trước screening: registry có provenance/dedup đã kiểm toán, mỗi slot nguồn công khai có kết quả truy hồi được ghi nhận, và calibration/codebook còn hiệu lực.
2. Những điều kiện trên đã được đối soát bằng registry, manifest PR07, run legal, event ledger và readiness audit.
3. Không có quyết định inclusion/exclusion, adjudication, citation chasing, trích xuất hay tổng hợp nào được tạo trong session này.
4. G6/G7 và giới hạn 8 trang/25 tài liệu tham khảo không phải gate mở screening; chúng không được dùng để thay đổi corpus trực tiếp.

## 5. Giới hạn cần được PI ghi nhận

- 71 cặp `EXACT_TITLE_YEAR` chưa được gộp tự động. Chúng vẫn được giữ auditably và không phải lý do dừng screening.
- Calibration hiện được chấp nhận theo attestation của PI. Hồ sơ chưa có bảng quyết định thô, random seed hoặc phép tính tỷ lệ đồng thuận để tái kiểm từng vòng; đây là giới hạn bằng chứng, không phải quyết định inclusion/exclusion.
- `DIRECT_SEARCH_COMPLETE` xác nhận sự hoàn tất theo phạm vi tìm kiếm trực tiếp đã công bố. Nó không khẳng định search saturation, không kết luận eligibility, và không cho phép suy diễn quốc gia từ trạng thái không thu hồi được.

## 6. Đề nghị quyết định của PI

Sau khi xem xét các chứng cứ nêu trên, PI có thể lựa chọn một trong hai phương án dưới đây:

### Phương án A — xác nhận

> Tôi, Đào Trung Thành, đã xem xét báo cáo readiness và các giới hạn được nêu. Tôi xác nhận `DIRECT_SEARCH_COMPLETE` cho corpus trực tiếp theo Amendment v1 kể từ ngày ____ / ____ / 2026. Xác nhận này không phải quyết định screening, không xác nhận inclusion/exclusion và không thay thế screening kép độc lập.

Ký/tên hoặc ghi nhận trong nhật ký quyết định PI: ____________________

### Phương án B — chưa xác nhận

> Tôi chưa xác nhận `DIRECT_SEARCH_COMPLETE` và yêu cầu hoàn thiện/giải thích thêm: ________________________________________________

Ký/tên hoặc ghi nhận trong nhật ký quyết định PI: ____________________

## 7. Hành động ngay sau xác nhận của PI

1. Lập biên bản xác nhận PI độc lập, có ngày và locator tới báo cáo này.
2. Tạo hai biểu mẫu vòng 1 mới, cùng 385 `CANON-*`, controlled reviewer ID và không có quyết định tiền điền.
3. Mở screening tiêu đề/tóm tắt kép độc lập cho Đào Trung Thành và Lộc Đặng.

Không tạo biểu mẫu có quyết định sẵn, không gán quyết định cho reviewer, và không thực hiện citation chasing trước khi các nguồn Việt Nam được chọn qua screening kép.

## 8. Chứng cứ liên quan

- [Amendment v1](../docs/amendments/post-registration-amendment-consolidated-v1.md)
- [Biên bản hiệu lực amendment](../docs/governance/amendment-v1-effectiveness-record.md)
- [Đặc tả retrieval PR07](../docs/governance/pr07-public-source-retrieval-operational-spec-v1.md)
- [Báo cáo PR07 12 slot](pr07-12slot-isolated-retrieval-report-2026-08-01.md)
- [Báo cáo Master Input Registry](master-input-registry-and-deduplication-report-2026-08-01.md)
- [Readiness audit độc lập](../docs/audits/readiness-audit-2026-08-01.md)
- [Calibration attestation](../docs/governance/calibration-attestation-2026-07-31.md)
- [Audit JSON provenance/dedup](../artifacts/search-rerun-01-2026-07-31/logs/provenance-dedup-audit.json)
