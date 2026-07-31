# Official search rerun 01 — 31/07/2026

**Trạng thái:** `IN_PROGRESS`  
**Protocol thẩm quyền:** [OSF 62b8w](https://osf.io/62b8w/) — không sửa protocol hay snapshot OSF.

## Ranh giới input

Run này khởi đầu rỗng. Không dùng record, count, quyết định hoặc raw artifact từ `official-search-run-2026-07-31/`, kể cả thư mục `rerun-01` lồng bên trong. Mọi record phải được thu hồi mới qua kênh và truy vấn đã khóa, có provenance/checksum trong chính thư mục này.

## Cấu trúc

- `pubmed/` — raw export, query translation và checksum
- `openalex/` — raw JSON, cursor manifest, discrepancy log và checksum
- `official-sources/` — raw HTML/PDF, query log và checksum
- `citation-chasing/` — seed/direction/locator/count/dedup log
- `logs/` — search log và gate evidence
- `registry/` — event ledger append-only đúng schema

Không tạo screening hoặc extraction trước khi G4–G7 đạt theo protocol.
