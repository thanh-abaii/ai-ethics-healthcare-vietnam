# Runbook thực thi lại official search

**Trạng thái:** `OPERATIONAL_RUNBOOK_NOT_A_PROTOCOL`  
**Nguồn thẩm quyền duy nhất:** [protocol đã đăng ký OSF](https://osf.io/62b8w/), `protocol.md` v0.6-registered, `search-strategy.md` và các codebook đã khóa.

## Phạm vi

Runbook này chỉ ghi thứ tự thao tác, tên artifact, checksum và điều kiện dừng để thực thi lại đúng protocol đã đăng ký. Nó không sửa câu hỏi, PCC, nguồn, truy vấn, tiêu chí, vai trò reviewer, quy tắc citation chasing, gate hoặc lịch đã đăng ký. Mọi thay đổi như vậy chỉ có thể thực hiện qua amendment công khai sau OSF.

## Trình tự vận hành

1. Giữ `ROUND-1-EXECUTION-AND-AUDIT-PROTOCOL.md` và artifact Antigravity nguyên trạng, chỉ như thử nghiệm không hoàn chỉnh.
2. Chạy lại từng kênh đã khóa, lưu raw export/HTML/PDF, query ID, ngày-giờ, manifest và SHA-256 trong `artifacts/official-search-rerun-01-2026-07-31/`.
3. Tạo event ledger đúng `record-registry-template.csv`; canonicalize toàn cục mà không xóa alias hoặc gộp preprint–published thiếu căn cứ.
4. Kiểm tra G4–G5 theo protocol. Khi chưa có `PASS`, không mở official screening.
5. Khi protocol cho phép, Đào Trung Thành và Lộc Đặng sàng lọc độc lập; sau full-text kép và phân xử mới mở extraction.

## Quy tắc fail-closed

Raw provenance/checksum thiếu, query sai, kênh bị thiếu, count không khép kín, hoặc thiếu quyết định độc lập của một reviewer đều dừng run. Không script nào được phép tự gán include/exclude, tự ghi `PASS`, hoặc tạo extraction.
