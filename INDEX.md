# SƠ ĐỒ CẤU TRÚC REPOSITORY VÀ CHỈ MỤC TỆP TIN (REPOSITORY INDEX)

**Dự án:** Scoping Review về Đạo đức và Quản trị AI Y tế tại Việt Nam  
**Mã tiền đăng ký OSF:** DOI [10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W) (OSF ID [`62b8w`](https://osf.io/62b8w/))  
**PI / Tác giả chính:** Đào Trung Thành  
**Người rà soát độc lập:** Lộc Đặng  
**Ngày cập nhật chỉ mục:** 02/08/2026  
**Trạng thái Nghiên cứu:** **`DIRECT_SEARCH_COMPLETE_PI_CONFIRMED_2026-08-02`** *(PI đã xác nhận; chưa có quyết định screening)*  
**Trạng thái Cổng:** **`READINESS_CHECK = COMPLETE_FOR_SCREENING_SETUP`**; kiểm tra trình bày chỉ thực hiện sau screening toàn văn theo Amendment v1.  
**Trạng thái Sàng lọc Kép Vòng 1:** **`SCREENING = OPEN_TITLE_ABSTRACT_DUAL_INDEPENDENT_2026-08-02`** *(385 `CANON-*`; biểu mẫu riêng đã tạo, chưa có quyết định nào)*

---

## 📌 1. Thư mục Gốc & Hồ sơ Tiền đăng ký OSF Đã khóa (OSF Frozen Pre-Registration Core)
> [!IMPORTANT]
> Theo quy tắc bất biến trong `AGENTS.md`, các tệp thuộc nhóm này và trong thư mục `artifacts/protocol-registration-lock-2026-07-31/` đại diện cho bản frozen pre-registration snapshot trên OSF. **100% khớp mã băm SHA-256 byte-for-byte. KHÔNG ĐƯỢC CHỈNH SỬA HOẶC DI CHUYỂN CÁC TỆP NÀY.**

- [`protocol.md`](protocol.md): Bản Protocol tiền đăng ký OSF chính thức (DOI 10.17605/OSF.IO/62B8W).
- [`search-strategy.md`](search-strategy.md): Chiến lược tìm kiếm chi tiết 5 nhánh nguồn.
- [`screening-codebook.md`](screening-codebook.md): Sổ tay mã hóa quy trình sàng lọc 2 vòng độc lập.
- [`data-extraction-codebook.md`](data-extraction-codebook.md): Sổ tay mã hóa trích xuất dữ liệu.
- [`record-registry-codebook.md`](record-registry-codebook.md): Sổ tay xây dựng sổ cái bản ghi và dedup.
- [`prisma-scr-checklist.md`](prisma-scr-checklist.md): Bảng kiểm tiêu chuẩn PRISMA-ScR.
- [`implementation-case-sampling-frame.csv`](implementation-case-sampling-frame.csv): Khung lấy mẫu 9 ca địa phương & bệnh viện sentinel (Khôi phục chuẩn 100% mã băm OSF snapshot).
- [`international-benchmark.md`](international-benchmark.md): Khung đối chiếu chuẩn quốc tế.
- [`artifacts/protocol-registration-lock-2026-07-31/`](artifacts/protocol-registration-lock-2026-07-31/): Thư mục khóa snapshot đăng ký OSF.

---

## 📜 2. Thư mục Tài liệu Hậu đăng ký & Kiểm toán (`docs/`)

### 📁 `docs/drafts/` (Bản thảo thử nghiệm Feasibility Trial Drafts / Gate G7)
- [`docs/drafts/g7-trial-draft-mock-manuscript.md`](docs/drafts/g7-trial-draft-mock-manuscript.md): Bản thử G7 có cấu trúc đủ thành phần, còn chờ kiểm tra citation, locator nguồn, template và số trang; **không phải G7 PASS**.

### 📁 `docs/amendments/` (Biên bản sửa đổi bổ sung)
- [`docs/amendments/post-registration-amendment-consolidated-v1.md`](docs/amendments/post-registration-amendment-consolidated-v1.md): **Tài liệu duy nhất dự kiến tải lên OSF**; hợp nhất thay đổi hậu đăng ký về OpenAlex, catalogue thực thi và corpus/gate.
- [`docs/governance/amendment-v1-effectiveness-record.md`](docs/governance/amendment-v1-effectiveness-record.md): Biên bản URL, ngày hiệu lực và trạng thái chuyển tiếp sau khi amendment được công bố.

### 📁 `docs/governance/` (Biên bản xác minh độc lập, Biểu mẫu Sàng lọc & Đồ thị Quan hệ Pháp lý)
- [`docs/governance/legal-relation-graph-2026-08-01.md`](docs/governance/legal-relation-graph-2026-08-01.md): **[MỚI]** Đồ thị Quan hệ Pháp lý cho 6 văn bản neo thể chế AI Y tế Việt Nam.
- [`docs/governance/OFFICIAL-SEARCH-REEXECUTION-RUNBOOK.md`](docs/governance/OFFICIAL-SEARCH-REEXECUTION-RUNBOOK.md): Sổ tay quy trình chạy lại thu hồi nguồn chính thức.
- [`docs/governance/pr07-public-source-retrieval-operational-spec-v1.md`](docs/governance/pr07-public-source-retrieval-operational-spec-v1.md): Đặc tả hữu hạn domain, locator, retry, thay thế và điều kiện terminal cho 16 slot Amendment v1; chưa phải kết quả retrieval hay screening.
- [`docs/governance/pi-direct-search-complete-confirmation-2026-08-02.md`](docs/governance/pi-direct-search-complete-confirmation-2026-08-02.md): Biên bản PI xác nhận `DIRECT_SEARCH_COMPLETE`, là căn cứ mở vòng 1.
- [`docs/governance/round-1-screening-opening-record-2026-08-02.md`](docs/governance/round-1-screening-opening-record-2026-08-02.md): Biên bản mở vòng 1 và checksum biểu mẫu quyết định trống.
- [`docs/governance/session-handoff-screening-round-1-2026-08-02.md`](docs/governance/session-handoff-screening-round-1-2026-08-02.md): Bàn giao session cho Agents hỗ trợ PI/Lộc ở screening vòng 1, với ranh giới thẩm quyền và điểm kiểm soát sau khóa.
- [`docs/governance/round-1-title-abstract-dao-trung-thanh-2026-08-02.csv`](docs/governance/round-1-title-abstract-dao-trung-thanh-2026-08-02.csv): Biểu mẫu vòng 1 của `DAO_TRUNG_THANH`, 385 record, chưa có quyết định.
- [`docs/governance/round-1-title-abstract-loc-dang-2026-08-02.csv`](docs/governance/round-1-title-abstract-loc-dang-2026-08-02.csv): Biểu mẫu vòng 1 của `LOC_DANG`, 385 record, chưa có quyết định.
- [`docs/governance/round-1-title-abstract-screening-guide-2026-08-02.md`](docs/governance/round-1-title-abstract-screening-guide-2026-08-02.md): Hướng dẫn PI và Lộc Đặng điền biểu mẫu vòng 1 độc lập.
- [`docs/governance/sampling-frame-verification-2026-08-01-loc-dang.md`](docs/governance/sampling-frame-verification-2026-08-01-loc-dang.md): Biên bản xác minh độc lập 9 ca tiêu biểu do Lộc Đặng ký.
- [`docs/governance/loc-dang-reviewer-confirmation.md`](docs/governance/loc-dang-reviewer-confirmation.md): Giấy xác nhận độc lập của người rà soát thứ hai.
- [`docs/governance/calibration-attestation-2026-07-31.md`](docs/governance/calibration-attestation-2026-07-31.md): Biên bản chuẩn hóa đánh giá sàng lọc kép.
- [`docs/governance/competitive-checkpoint-2026-07-31.md`](docs/governance/competitive-checkpoint-2026-07-31.md): Điểm kiểm soát cạnh tranh.
- [`docs/governance/funding-declaration.md`](docs/governance/funding-declaration.md): Tuyên bố kinh phí và xung đột lợi ích.
- [`docs/governance/reference-budget-ledger.md`](docs/governance/reference-budget-ledger.md): Ngân sách trích dẫn mục tiêu.
- [`docs/governance/registration-manifest.md`](docs/governance/registration-manifest.md): Manifest đăng ký OSF.

### 📁 `docs/audits/` (Đánh giá Gate G6/G7, Benchmark & Thử nghiệm cũ)
- [`docs/audits/g6-g7-contract-audit-2026-08-01.md`](docs/audits/g6-g7-contract-audit-2026-08-01.md): Kiểm tra fail-closed theo đúng Điều 20–21: G6/G7 đều chưa đạt.
- [`docs/audits/ROUND-1-EXECUTION-AND-AUDIT-PROTOCOL.md`](docs/audits/ROUND-1-EXECUTION-AND-AUDIT-PROTOCOL.md): **[FROZEN LEGACY]** Nhật ký thử nghiệm quy trình Vòng 1 cũ đã đóng băng (không dùng cho PRISMA).
- [`docs/audits/novelty-audit.md`](docs/audits/novelty-audit.md): Đánh giá khoảng trống và tính độc đáo của đề tài.
- [`docs/audits/novelty-comparator-log.csv`](docs/audits/novelty-comparator-log.csv): Sổ nhật ký đối chiếu khoảng trống nghiên cứu.
- [`docs/audits/component-benchmark-register.md`](docs/audits/component-benchmark-register.md): Đánh giá thành phần chuẩn quốc tế.
- [`docs/audits/openalex-access-check.md`](docs/audits/openalex-access-check.md): Nhật ký kiểm tra kết nối API OpenAlex.
- [`docs/audits/g4-g5-feasibility-pilot-2026-07-31.md`](docs/audits/g4-g5-feasibility-pilot-2026-07-31.md): Nhật ký thử nghiệm khả thi G4-G5.
- [`docs/audits/readiness-audit-2026-08-01.md`](docs/audits/readiness-audit-2026-08-01.md): Kiểm toán readiness độc lập; fail-closed vì biểu mẫu screening có dữ liệu tiền điền không khớp registry hiện hành.

---

## 📊 3. Thư mục Báo cáo Kiểm toán (`reports/`)

- [`reports/master-input-registry-and-deduplication-report-2026-08-01.md`](reports/master-input-registry-and-deduplication-report-2026-08-01.md): Báo cáo bàn giao kết quả dựng Master Input Registry & Khử trùng lặp toàn cục cho Codex Audit & PI Đào Trung Thành.
- [`reports/pr07-12slot-isolated-retrieval-report-2026-08-01.md`](reports/pr07-12slot-isolated-retrieval-report-2026-08-01.md): Báo cáo bàn giao Antigravity cho run PR07 12 slot.
- [`reports/codex-pr07-12slot-retrieval-audit-2026-08-01.md`](reports/codex-pr07-12slot-retrieval-audit-2026-08-01.md): Hậu kiểm độc lập Codex cho run PR07 12 slot.
- [`reports/retrieval-execution-audit-report-2026-08-01.md`](reports/retrieval-execution-audit-report-2026-08-01.md): Báo cáo kiểm toán và tổng kết quy trình thu hồi nguồn thô 5 nhánh cho Codex audit và hội đồng đánh giá.
- [`reports/official-sources-harvest-audit-report-2026-08-01.md`](reports/official-sources-harvest-audit-report-2026-08-01.md): Báo cáo thu hồi thô cần được đọc cùng dashboard trạng thái.
- [`reports/codex-remediation-audit-2026-08-01.md`](reports/codex-remediation-audit-2026-08-01.md): Báo cáo hậu kiểm thay thế cho quyết định gate hiện hành.
- [`reports/pi-direct-search-completion-review-2026-08-02.md`](reports/pi-direct-search-completion-review-2026-08-02.md): Báo cáo bàn giao session và đề nghị PI xem xét xác nhận `DIRECT_SEARCH_COMPLETE`; không phải xác nhận thay PI.


---

## 🛠️ 4. Thư mục Công cụ & Script (`scripts/`)

- [`scripts/compile_master_input_registry.py`](scripts/compile_master_input_registry.py): Script tổng hợp Master Input Registry, canonicalization & khử trùng lặp toàn cục 664 manifestations.
- [`scripts/build_official_inventory.py`](scripts/build_official_inventory.py): Trích xuất 223 biểu hiện tiêu đề văn bản ứng viên từ các trang HTML kết quả tìm kiếm nguồn chính thức.
- [`scripts/run_legal_official_portals.py`](scripts/run_legal_official_portals.py): Runner thu hồi văn bản pháp lý cổng chính phủ.
- [`scripts/fix_reviewer_csv_schema.py`](scripts/fix_reviewer_csv_schema.py): Kịch bản chuẩn hóa schema biểu mẫu sàng lọc theo `screening-codebook.md`.
- [`scripts/execute_gates_g6_g7.py`](scripts/execute_gates_g6_g7.py): Script legacy đã retire fail-closed; không được chạy để tạo registry hoặc mở screening.
- [`scripts/verify_g6_g7_contract.py`](scripts/verify_g6_g7_contract.py): Kiểm tra fail-closed hợp đồng G6/G7.
- [`scripts/build_event_registry_from_inventory.py`](scripts/build_event_registry_from_inventory.py): Dựng event ledger `MANIFESTATION`/`PROVENANCE` từ inventory raw đã xác minh.
- [`scripts/run_legal_seed_retrieval.py`](scripts/run_legal_seed_retrieval.py): Thu hồi seed pháp lý từ Cổng Thông tin điện tử Chính phủ.
- [`scripts/audit_official_provenance_and_dedup.py`](scripts/audit_official_provenance_and_dedup.py): Kịch bản kiểm toán sổ cái toàn cục và lọc trùng.
- [`scripts/run_g4_g5.py`](scripts/run_g4_g5.py): Runner thu hồi PubMed E-utilities và OpenAlex API.
- [`scripts/run_nonlegal_official_portals.py`](scripts/run_nonlegal_official_portals.py): Runner thu hồi cổng Bộ Y tế (7 kênh), Bộ KH&CN, UNESCO RAM, WHO Việt Nam.
- [`scripts/run_implementation_sentinels.py`](scripts/run_implementation_sentinels.py): Runner thu hồi 9 ca địa phương & bệnh viện sentinel.

---

## 📦 5. Thư mục Chứng cứ Dữ liệu Thô & Artifacts (`artifacts/search-rerun-01-2026-07-31/`)

- [`artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/`](artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/): Đợt thu hồi PR07 12 slot chính thức đã phê duyệt (`RETRIEVAL_TERMINAL_FOR_READINESS`, 6 unscreened RETRIEVED documents).
- [`artifacts/pr07-12slot-isolated-run-20260801T164606/`](artifacts/pr07-12slot-isolated-run-20260801T164606/): Đợt thu hồi PR07 thử nghiệm cũ giữ lại làm audit trail cho báo cáo kiểm toán Codex.
- [`artifacts/archive/pr07-runs-2026-08-01/`](artifacts/archive/pr07-runs-2026-08-01/): Thư mục lưu trữ 11 đợt chạy thử nghiệm PR07 trung gian cũ để giữ repository gọn gàng.
- [`artifacts/search-rerun-01-2026-07-31/official-inventory.csv`](artifacts/search-rerun-01-2026-07-31/official-inventory.csv): Danh mục 223 biểu hiện tiêu đề/locator ứng viên từ nguồn chính thức (được giữ làm candidate inventory thô, không đưa vào Master Input Registry khi chưa xác minh).
- [`artifacts/search-rerun-01-2026-07-31/official-sources/legal-portals-20260801T095241/`](artifacts/search-rerun-01-2026-07-31/official-sources/legal-portals-20260801T095241/): Chứng cứ thô Cổng Pháp lý (`RAW_LEGAL_PORTAL_CAPTURE_COMPLETE_UNSCREENED` 32 raw page captures).
- [`artifacts/search-rerun-01-2026-07-31/registry/raw-manifestation-inventory.csv`](artifacts/search-rerun-01-2026-07-31/registry/raw-manifestation-inventory.csv): Danh mục đúng 445 biểu hiện thô đã xác minh (88 PubMed, 347 OpenAlex, 4 Legal, 6 PR07 Approved Run).
- [`artifacts/search-rerun-01-2026-07-31/registry/registry-event-ledger.csv`](artifacts/search-rerun-01-2026-07-31/registry/registry-event-ledger.csv): Event ledger 1.335 dòng (MANIFESTATION, PROVENANCE, CANONICALIZATION) tuân thủ `record-registry-codebook.md`.
- [`artifacts/search-rerun-01-2026-07-31/registry/master-record-registry.csv`](artifacts/search-rerun-01-2026-07-31/registry/master-record-registry.csv): Master Input Registry đại diện cho 385 cụm canonical (screening status: PENDING_SCREENING).
- [`artifacts/search-rerun-01-2026-07-31/registry/global-dedup-candidates.csv`](artifacts/search-rerun-01-2026-07-31/registry/global-dedup-candidates.csv): Danh mục 131 cụm ứng viên trùng lặp xác định theo DOI/PMID/OpenAlex ID và Title+Year candidate review.
- [`artifacts/search-rerun-01-2026-07-31/pubmed/`](artifacts/search-rerun-01-2026-07-31/pubmed/): Phản hồi thô PubMed E-utilities API.
- [`artifacts/search-rerun-01-2026-07-31/openalex/`](artifacts/search-rerun-01-2026-07-31/openalex/): Phản hồi thô OpenAlex Polite Pool API (14 trang / 347 works).
- [`artifacts/search-rerun-01-2026-07-31/official-sources/nl-runs/official-nonlegal-20260801T065552/`](artifacts/search-rerun-01-2026-07-31/official-sources/nl-runs/official-nonlegal-20260801T065552/): Chứng cứ thô 7 kênh Bộ Y tế.
- [`artifacts/search-rerun-01-2026-07-31/official-sources/nl-runs/official-nonlegal-20260801T061911/`](artifacts/search-rerun-01-2026-07-31/official-sources/nl-runs/official-nonlegal-20260801T061911/): Chứng cứ thô Bộ KH&CN, UNESCO RAM, WHO Việt Nam.
- [`artifacts/search-rerun-01-2026-07-31/official-sources/sentinel-runs/sentinel-capture-20260801T063425/`](artifacts/search-rerun-01-2026-07-31/official-sources/sentinel-runs/sentinel-capture-20260801T063425/): Chứng cứ thô 9 ca địa phương & bệnh viện sentinel (544 tệp thô).

---

## 🔒 6. Tệp Cấu hình & Môi trường

- [`.env`](.env): Lưu biến môi trường cục bộ (`POLITE_EMAIL`, `NCBI_API_KEY`, `OPENALEX_API_KEY`) — *Đã đưa vào `.gitignore`*.
- [`.gitignore`](.gitignore): Loại bỏ `.env` và tệp tạm khỏi theo dõi git.
- [`AGENTS.md`](AGENTS.md): Quy tắc ứng xử và kỷ luật bảo vệ tệp tiền đăng ký OSF dành cho AI Agent.
- [`README.md`](README.md): Hướng dẫn thiết lập và tổng quan đề tài.
