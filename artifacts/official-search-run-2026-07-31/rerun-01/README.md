# Official search rerun 01 — 31/07/2026

## Trạng thái

`IN_PROGRESS` — lượt này được tạo mới sau audit. Thư mục cha `official-search-run-2026-07-31` có artifact trước đó và **không** là corpus/PRISMA của lượt này.

## Ranh giới

1. Không tái dùng count, quyết định sàng lọc, registry hoặc raw export của lượt trước.
2. Chỉ record có raw artifact, checksum, query/portal ID và provenance event mới được nhập registry rerun.
3. Registry dùng schema 42 trường của `record-registry-template.csv`, append-only; canonicalization toàn cục diễn ra trước sàng lọc.
4. Không tạo quyết định sàng lọc hay extraction trong lúc các kênh tìm kiếm, citation chasing, dedup và gate chưa hoàn tất.
5. Đào Trung Thành và Lộc Đặng sẽ sàng lọc độc lập sau khi registry đầu vào chính thức được khóa; khuyến nghị AI chỉ là hỗ trợ, không thay quyết định của hai người.

## Điều kiện hoàn thành official search

- PubMed, OpenAlex, nguồn chính thức/pháp luật và citation chasing có log, raw artifacts và checksum tách biệt.
- Toàn bộ raw/export được canonicalize toàn cục với event ledger truy xuất được.
- Manifest run nêu rõ ngày/giờ, query đã chạy, giới hạn, sự cố và quyết định dừng.
- Chỉ khi mọi điều kiện G4–G5 được kiểm toán lại là `PASS`, lượt này mới được gắn `OFFICIAL_SEARCH_COMPLETE` và mở sàng lọc.

## Cấu trúc dự kiến

- `pubmed/`
- `openalex/`
- `official-sources/`
- `citation-chasing/`
- `logs/`
- `registry/`
