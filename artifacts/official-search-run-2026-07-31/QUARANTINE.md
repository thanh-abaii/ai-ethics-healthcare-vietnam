# Quarantine — official-search-run-2026-07-31

**Trạng thái:** `QUARANTINED_LEGACY_NON_PRISMA_ATTEMPT`  
**Ngày:** 31/07/2026  
**Phạm vi:** toàn bộ nội dung trong thư mục này, gồm `rerun-01/` lồng bên trong.

## Quy tắc sử dụng

- Không dùng record, count, kết quả khử trùng lặp, quyết định sàng lọc, bảng extraction hoặc báo cáo trong thư mục này cho PRISMA, corpus hay kết luận.
- Không xóa, ghi đè hoặc “sửa cho hợp lệ” các artifact cũ. Chúng được giữ để kiểm toán quá trình thử nghiệm.
- Raw snapshots có thể được đọc để đối chiếu kỹ thuật, nhưng không tự trở thành input của official rerun.

## Lý do

Lượt cũ không có provenance cấp record đủ tái tạo, query/kênh không khớp hoàn toàn protocol OSF, dedup ledger không liên kết canonical record tin cậy, và workflow sàng lọc/trích xuất đi sai trình tự.

## Thay thế vận hành

Official rerun độc lập được thực hiện tại `artifacts/official-search-rerun-01-2026-07-31/` theo `OFFICIAL-SEARCH-REEXECUTION-RUNBOOK.md` và protocol OSF đã khóa.
