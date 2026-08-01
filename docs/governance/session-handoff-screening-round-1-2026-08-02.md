# Bàn giao session: hỗ trợ screening vòng 1

**Ngày bàn giao:** 2026-08-02  
**Dự án:** Scoping review Đạo đức và Quản trị AI trong Y tế tại Việt Nam  
**Trạng thái tại thời điểm bàn giao:** `SCREENING = OPEN_TITLE_ABSTRACT_DUAL_INDEPENDENT_2026-08-02`

## 1. Điểm xuất phát đã khóa

- PI Đào Trung Thành đã xác nhận `DIRECT_SEARCH_COMPLETE` ngày 2026-08-02. Xem `pi-direct-search-complete-confirmation-2026-08-02.md`.
- Tìm kiếm trực tiếp và readiness đã hoàn tất về mặt kỹ thuật; không tiếp tục retrieval diện rộng, không dùng các run partial cũ.
- Master Input Registry có **445 manifestations** và **385 canonical records** (`CANON-*`).
- Hai biểu mẫu screening tiêu đề/tóm tắt độc lập đã được tạo, mỗi biểu mẫu có đúng 385 dòng và **0 quyết định tiền điền**:
  - `round-1-title-abstract-dao-trung-thanh-2026-08-02.csv`
  - `round-1-title-abstract-loc-dang-2026-08-02.csv`
- Hai tệp legacy `REC-*` 391 dòng đã bị xóa theo yêu cầu PI; không tái tạo, không tham chiếu như dữ liệu screening.

## 2. Vai trò của Agents trong session sau

Agents chỉ hỗ trợ vận hành và kiểm toán. Agents **không được**:

- ghi, suy đoán, gợi ý hoặc thay đổi quyết định `INCLUDE`/`EXCLUDE`/`UNCERTAIN` thay PI hoặc Lộc Đặng;
- đọc tệp quyết định của reviewer này để gợi ý hay tiết lộ cho reviewer kia trước khi cả hai khóa vòng;
- adjudicate bất đồng, xác nhận thay PI, hoặc mở screening toàn văn/citation chasing trước thời điểm hợp lệ;
- sửa `protocol.md`, các codebook frozen, search strategy, snapshot tại `artifacts/protocol-registration-lock-2026-07-31/`, hay các raw artifact;
- dùng giới hạn 8 trang/25 tài liệu tham khảo để tác động quyết định screening.

Agents được phép:

- giải thích tiêu chí và mã loại trong `screening-codebook.md` khi PI/Lộc hỏi;
- kiểm tra schema, ID, checksum, trạng thái trống/đã khóa của **tệp của đúng reviewer đang yêu cầu hỗ trợ**;
- tạo báo cáo kiểm toán, bảng đối chiếu bất đồng **chỉ sau khi cả hai reviewer xác nhận đã khóa**;
- hỗ trợ truy hồi toàn văn cho các record đã chuyển sang vòng toàn văn, theo quy trình và không tự ra quyết định.

## 3. Cách PI và Lộc thực hiện vòng 1

1. Mỗi reviewer chỉ mở tệp của mình; không chia sẻ cột `inclusion_decision` trước khi khóa.
2. Với từng `CANON-*`, ghi một trong `INCLUDE`, `EXCLUDE`, `UNCERTAIN` vào `inclusion_decision`.
3. Ở vòng tiêu đề/tóm tắt, chỉ dùng `EXCLUDE` khi căn cứ chắc chắn. Record không đủ thông tin hoặc có ca biên phải là `UNCERTAIN` để chuyển vòng toàn văn.
4. Để trống `exclusion_reason` ở vòng này. Không dùng `EX08_FULL_TEXT_UNAVAILABLE` hoặc `EX09_WRONG_LANGUAGE` tại tiêu đề/tóm tắt.
5. Khi hoàn tất, reviewer tự xác nhận “đã khóa vòng 1”; Agent ghi checksum của tệp đã khóa và không sửa tệp đó.

## 4. Điểm kiểm soát sau khi cả hai khóa

Chỉ sau hai xác nhận khóa độc lập, Agent thực hiện kiểm tra cơ học sau:

| Kiểm tra | Điều kiện đạt |
| --- | --- |
| Tính toàn vẹn tập | Mỗi tệp có đúng 385 `CANON-*`, không trùng ID, tập ID khớp Master Input Registry. |
| Phân tách reviewer | Reviewer ID đúng `DAO_TRUNG_THANH`/`LOC_DANG`; không có dấu hiệu tệp bị ghi đè. |
| Giá trị quyết định | Mỗi record có đúng một giá trị `INCLUDE`, `EXCLUDE` hoặc `UNCERTAIN`; không tự đổi giá trị thiếu. |
| Cấm lý do loại sớm | `exclusion_reason` vẫn trống ở vòng tiêu đề/tóm tắt. |
| Khóa và provenance | Lưu SHA-256, thời gian khóa và locator của từng tệp. |

Sau đó mới tạo bảng đối chiếu theo record:

- Đồng thuận `INCLUDE` hoặc `UNCERTAIN`: chuyển sang tìm/sàng lọc toàn văn.
- Đồng thuận `EXCLUDE`: ghi nhận là loại ở vòng tiêu đề/tóm tắt theo codebook, không xóa record hay provenance.
- Bất đồng: giữ nguyên hai quyết định, đặt trạng thái đối chiếu `PENDING_ADJUDICATION`; chỉ PI/cơ chế phân xử được đăng ký mới xử lý nội dung bất đồng.

## 5. Sau vòng 1

- Screening toàn văn vẫn là screening kép độc lập; lý do loại chuẩn hóa `EX01`–`EX09` chỉ chốt ở vòng này.
- Citation chasing chỉ bắt đầu sau khi nguồn Việt Nam được chọn qua screening kép theo Amendment v1.
- Global dedup đã hoàn tất định danh cứng. Có 71 ca `EXACT_TITLE_YEAR` giữ riêng chờ review theo codebook; không tự gộp chúng để thay đổi quyết định screening.
- G6/G7 chỉ kiểm tra khả năng trình bày sau screening toàn văn; không phải cổng `PASS/FAIL` và không điều khiển corpus.

## 6. Tệp cần đọc đầu session sau

1. `AGENTS.md` và `INDEX.md` của dự án.
2. `docs/governance/session-handoff-screening-round-1-2026-08-02.md` (tệp này).
3. `screening-codebook.md` và `record-registry-codebook.md` (frozen, chỉ đọc).
4. `docs/governance/round-1-screening-opening-record-2026-08-02.md`.
5. Chỉ khi cần audit: `docs/audits/readiness-audit-2026-08-01.md` và `reports/pi-direct-search-completion-review-2026-08-02.md`.

## 7. Điều kiện kết thúc session screening tiếp theo

Không tuyên bố vòng 1 hoàn tất cho đến khi:

1. PI và Lộc đều xác nhận đã khóa tệp riêng;
2. kiểm tra cơ học ở Mục 4 đạt;
3. có bảng đối chiếu, checksum và ghi nhận bất đồng; và
4. trạng thái mọi record được lưu auditably mà không xóa alias/provenance.
