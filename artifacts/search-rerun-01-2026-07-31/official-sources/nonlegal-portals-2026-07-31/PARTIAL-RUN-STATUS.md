# Trạng thái lượt capture cổng không-pháp lý

**Trạng thái:** `FAIL_CLOSED_PARTIAL_RUN_NOT_FOR_COMPLETION`  
**Ngày:** 31/07/2026  
**Phạm vi dự kiến:** 12 query ID `DQ-IMPL-*`, `DQ-TOOL-*`, `DQ-EVID-*` qua MOH, các đơn vị MOH, UNESCO-RAM và WHO-VNM.

## Bằng chứng được giữ lại

- `query-catalog.csv` giữ 12 query ID và chuỗi nguyên văn.
- `raw/` chứa các response/header/stderr/status đã capture trước khi lượt chạy bị gián đoạn.
- `sha256.csv` giữ hash cho các artefact đã ghi.
- `run-nonlegal-official-portals.ps1` giữ logic prospective đã dùng.

## Giới hạn bắt buộc

Lượt này bị dừng trước khi tạo `query-provenance.csv`, chưa bao phủ toàn bộ cổng/query, chưa xác minh phân trang/điểm dừng và chưa có result-level acquisition. Vì vậy không dùng raw trong thư mục này làm bằng chứng search complete, count PRISMA, eligibility, absence, implementation hay outcome.

Một run mới có ledger theo query/cổng, raw locator/checksum, trạng thái truy cập, số trang/kết quả và rule dừng phải hoàn tất trước khi nhánh không-pháp lý có thể đóng.
