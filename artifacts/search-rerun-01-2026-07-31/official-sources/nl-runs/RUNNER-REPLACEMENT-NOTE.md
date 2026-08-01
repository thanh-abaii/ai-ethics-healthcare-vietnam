# Phạm vi các lượt chạy cổng không-pháp lý

**Ngày ghi nhận:** 31/07/2026  
**Trạng thái:** `ACTIVE_REPLACEMENT_RUN_IN_PROGRESS`

Các thư mục `official-sources/nonlegal-portals-2026-07-31/` và
`official-sources/nonlegal-portal-runs/` giữ nguyên như chứng cứ của lượt
partial hoặc các lần khởi động kỹ thuật không thành công. Chúng không phải
nguồn đầu vào cho PRISMA, registry, dedup hay sàng lọc.

Runner thay thế là `scripts/run_nonlegal_official_portals.py`. Các run hợp lệ
do runner này tạo chỉ nằm tại thư mục `nl-runs/`, có `run-parameters.json`,
`query-portal-ledger.csv`, `candidate-url-locators.csv`, `sha256.csv` và
`completion-status.json`. Một run vẫn chưa được dùng để tuyên bố
`OFFICIAL_SEARCH_COMPLETE` nếu `completion-status.json` còn ghi thiếu
source-level acquisition, fallback hoặc độ sâu 2.

Lượt đang hoạt động: `official-nonlegal-20260731T212700+0700`. Nó là capture
trước sàng lọc; không có quyết định eligibility, trích xuất hay citation
chasing trong thư mục này.
