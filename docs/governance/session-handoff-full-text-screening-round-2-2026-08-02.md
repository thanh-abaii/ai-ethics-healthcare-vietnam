# Bàn giao session: hỗ trợ sàng lọc toàn văn vòng 2

**Ngày bàn giao:** 2026-08-02
**Dự án:** Scoping review Đạo đức và Quản trị AI trong Y tế tại Việt Nam
**Trạng thái xuất phát:** `SCREENING = ROUND_1_ADJUDICATION_COMPLETE_2026-08-02`

## 1. Điểm xuất phát đã khóa

- Vòng 1 (tiêu đề/tóm tắt) đã hoàn tất cho toàn bộ 385 `CANON-*` trong Master Input Registry.
- Kết quả chốt Vòng 1: **219** record loại tại vòng 1 và **166** record chuyển sang Vòng 2 sàng lọc toàn văn kép độc lập.
- Hai reviewer đã khóa tệp Vòng 1; 76 bất đồng đã được PI Đào Trung Thành phân xử. Không mở lại Vòng 1, không thay đổi quyết định gốc, quyết định phân xử hoặc provenance.
- Ma trận quyết định cuối: `docs/governance/round-1-adjudication-matrix-2026-08-02.csv`.
- Biên bản phân xử của PI: `docs/governance/pi-round-1-adjudication-decision-record-2026-08-02.md`.

## 2. Ranh giới thẩm quyền của Agents

Agents chỉ hỗ trợ vận hành, truy hồi và kiểm toán. Agents **không được**:

- tự quyết định `INCLUDE`/`EXCLUDE`, suy đoán quyết định, điền lý do loại hoặc thay đổi quyết định thay PI hay Lộc Đặng;
- đọc tệp quyết định Vòng 2 của reviewer này để gợi ý, tiết lộ hoặc làm ảnh hưởng đến reviewer kia trước khi cả hai khóa;
- tự phân xử bất đồng, tự xác nhận thay PI, hoặc mở citation chasing trước điều kiện hợp lệ;
- sửa `protocol.md`, `screening-codebook.md`, `record-registry-codebook.md`, các codebook/tài liệu OSF frozen khác, hoặc bất kỳ tệp nào trong `artifacts/protocol-registration-lock-2026-07-31/`;
- xóa record, alias, manifest, raw artifact hoặc provenance của 219 record đã loại Vòng 1.

Agents được phép:

- giải thích tiêu chí toàn văn và mã `EX01`–`EX09` trong `screening-codebook.md` khi reviewer hỏi;
- hỗ trợ truy hồi toàn văn cho record thuộc danh sách 166 record sau Vòng 1, lưu locator, ngày truy hồi và checksum tại artifact hậu đăng ký;
- kiểm tra schema, ID, checksum, trạng thái hoàn tất/khóa của **tệp đúng reviewer đang yêu cầu hỗ trợ**;
- sau khi cả hai reviewer xác nhận khóa Vòng 2, lập báo cáo cơ học, ma trận bất đồng và thống kê đồng thuận; không tự phân xử.

## 3. Chuẩn bị Vòng 2

1. Tạo hai biểu mẫu Vòng 2 tách biệt, cùng tập 166 `CANON-*`, một cho `DAO_TRUNG_THANH`, một cho `LOC_DANG`.
2. Biểu mẫu phải có các trường tối thiểu: `record_id`, `stage=FULL_TEXT`, `reviewer`, `inclusion_decision`, `exclusion_reason`, `notes`, `date`.
3. Mỗi reviewer chỉ xem tệp của mình. Tất cả quyết định mới phải bắt đầu trống; không sao chép quyết định Vòng 1 vào cột quyết định Vòng 2.
4. Trước khi reviewer bắt đầu, lưu checksum, số record và tập ID của cả hai biểu mẫu trống.
5. Chỉ truy hồi toàn văn cho 166 record đã chuyển Vòng 2. Nếu toàn văn chưa có, ghi nhận nỗ lực theo protocol; chỉ dùng `EX08_FULL_TEXT_UNAVAILABLE` sau khi quy trình truy hồi đã hoàn tất.

## 4. Quy tắc quyết định Vòng 2

- Vòng 2 là screening kép độc lập trên **toàn văn**.
- `EX01`–`EX09` chỉ được dùng tại Vòng 2, với một lý do loại chuẩn hóa cho mỗi quyết định `EXCLUDE`.
- Record thiếu thông tin, toàn văn chưa đủ hoặc ca biên phải được giữ để xử lý theo quy trình; không suy diễn nội dung không có trong nguồn.
- `INCLUDE` chỉ dành cho record đáp ứng đầy đủ PCC và có nội dung đạo đức/quản trị AI trong y tế Việt Nam có thể kiểm chứng.
- Không dùng giới hạn 8 trang/25 tài liệu tham khảo, G6/G7 hoặc mục tiêu trình bày để tác động quyết định screening.

## 5. Điểm kiểm soát sau khi hai reviewer khóa Vòng 2

Chỉ sau hai xác nhận khóa độc lập, Agent được thực hiện kiểm tra cơ học:

| Kiểm tra | Điều kiện đạt |
| --- | --- |
| Tính toàn vẹn tập | Mỗi tệp có đúng 166 `CANON-*`, không trùng ID và tập ID khớp danh sách chuyển Vòng 2. |
| Phân tách reviewer | Reviewer ID đúng, tệp không bị ghi đè và provenance đầy đủ. |
| Giá trị quyết định | Mỗi record có một `INCLUDE` hoặc `EXCLUDE`; không tự bổ sung giá trị thiếu. |
| Mã loại | Mỗi `EXCLUDE` có đúng một mã `EX01`–`EX09`; `INCLUDE` để trống lý do loại. |
| Toàn văn & provenance | Có locator toàn văn/nỗ lực truy hồi, SHA-256 khi có tệp, ngày và nguồn. |
| Khóa | Lưu SHA-256, ngày/giờ nếu biên bản có ghi, và locator của từng tệp reviewer. |

Sau kiểm tra:

- Đồng thuận `INCLUDE`: chuyển sang bước trích xuất dữ liệu theo codebook.
- Đồng thuận `EXCLUDE`: giữ record/provenance và lý do loại; không xóa dữ liệu.
- Bất đồng: giữ nguyên hai quyết định gốc, ghi `PENDING_ADJUDICATION`; chỉ PI/cơ chế phân xử đã đăng ký mới ra quyết định cuối cùng.

## 6. Tệp cần đọc đầu session Vòng 2

1. `AGENTS.md` và `INDEX.md`.
2. Tệp bàn giao này.
3. `screening-codebook.md` và `record-registry-codebook.md` (frozen, chỉ đọc).
4. `docs/governance/pi-round-1-adjudication-decision-record-2026-08-02.md`.
5. `docs/governance/round-1-adjudication-matrix-2026-08-02.csv`.
6. `docs/audits/round-1-dual-screening-mechanical-audit-2026-08-02.md`.

## 7. Điều kiện kết thúc session Vòng 2

Không tuyên bố Vòng 2 hoàn tất cho đến khi:

1. PI và Lộc Đặng đều xác nhận đã khóa tệp Vòng 2 riêng;
2. kiểm tra cơ học ở Mục 5 đạt;
3. có ma trận bất đồng, checksum và báo cáo audit; và
4. mọi quyết định cuối cùng cùng lý do loại/provenance được lưu auditably mà không xóa lịch sử.
