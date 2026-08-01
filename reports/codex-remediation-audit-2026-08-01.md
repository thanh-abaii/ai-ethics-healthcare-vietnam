# Báo cáo khắc phục và trạng thái gate

**Ngày kiểm tra:** 01/08/2026  
**Trạng thái:** `DIRECT_SEARCH_IN_PROGRESS`; `SCREENING=NOT_OPEN`.

## Kết quả đã khắc phục

- Thu hồi lại ba seed pháp lý từ Cổng Thông tin điện tử Chính phủ: `134/2025/QH15`, `142/2026/NĐ-CP`, `05/2026/TT-BKHCN`. Mỗi seed có landing page, header, PDF first-party và SHA-256 tại `artifacts/search-rerun-01-2026-07-31/official-sources/legal-seed-retrieval-20260801T104813/`.
- Loại 16 PDF trùng mang tiêu đề `Tải về` khỏi đầu vào provenance mới. Inventory raw hiện có 438 manifestation đã kiểm tra checksum: 88 PubMed, 347 OpenAlex, 3 seed pháp lý.
- Tạo `registry-event-ledger.csv` gồm 438 event `MANIFESTATION` và 438 event `PROVENANCE`; chưa có canonicalization, screening hay adjudication.
- Retire script gate cũ vì dùng proxy số lượng bản ghi. Kiểm tra mới tại `docs/audits/g6-g7-contract-audit-2026-08-01.md` giữ G6/G7 `FAIL_CLOSED`.

## Điều chưa đạt và không được suy diễn

- Non-legal source acquisition run `official-nonlegal-source-acquisition-20260801T101500` bị ngắt do timeout và không thể dùng cho count, saturation hoặc gate.
- Legal seed capture không tự hoàn thành relation graph depth 3 và không xác nhận một hội đồng hay tác động thực tế.
- Bản dàn trang mock theo template chính thức mới là kiểm tra kỹ thuật; citation/locator đầy đủ của 16 nguồn và G6 reference budget chưa được xác nhận.

## Quy tắc quyết định

Không phê duyệt `DIRECT_SEARCH_COMPLETE` hoặc mở sàng lọc cho đến khi có một lượt non-legal hoàn chỉnh theo cổng/fallback đã ghi, relation traversal đúng protocol, canonicalization event có căn cứ, và G6/G7 được evidence pack kiểm tra theo Điều 20–21.
