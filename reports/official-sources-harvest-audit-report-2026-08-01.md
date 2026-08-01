# BÁO CÁO KIỂM TOÁN VẬN CHUYỂN DỮ LIỆU THÔ 5 NHÁNH NGUỒN CHÍNH THỨC
## (Official Sources Raw Transport Audit Report for Codex Verification)

**Dự án:** Scoping Review về Đạo đức và Quản trị AI Y tế tại Việt Nam  
**Tác giả / PI:** Đào Trung Thành  
**Người rà soát độc lập:** Lộc Đặng  
**Ngày lập báo cáo:** 01/08/2026 (Hoàn tất Đồ thị Quan hệ Pháp lý & Phân trang Cổng Pháp lý)  
**Tham chiếu Protocol OSF:** Pre-registration snapshot DOI [10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W)  
**Biên bản xác minh ca:** [`docs/governance/sampling-frame-verification-2026-08-01-loc-dang.md`](../docs/governance/sampling-frame-verification-2026-08-01-loc-dang.md)  
**Đồ thị Quan hệ Pháp lý:** [`docs/governance/legal-relation-graph-2026-08-01.md`](../docs/governance/legal-relation-graph-2026-08-01.md)  
**Sơ đồ chỉ mục SSOT:** [`INDEX.md`](../INDEX.md)  

---

> [!IMPORTANT]
> **HOÀN THÀNH TOÀN BỘ ĐIỀU KIỆN ĐỂ TRÌNH CODEX PHÊ DUYỆT (ALL PREREQUISITES COMPLETED):**
> 1. **Khôi phục 100% Snapshot OSF:** Khớp SHA-256 byte-for-byte.
> 2. **Đồ thị Quan hệ Pháp lý (Legal Relation Graph):** Đã khởi tạo hoàn chỉnh tại [`docs/governance/legal-relation-graph-2026-08-01.md`](../docs/governance/legal-relation-graph-2026-08-01.md).
> 3. **Cổng G7 (Journal Mock Manuscript Gate):** Đã nghiệm thu dung lượng thử nghiệm **`PASS_MOCK_CAPACITY_VERIFIED`** ([`docs/drafts/g7-trial-draft-mock-manuscript.md`](../drafts/g7-trial-draft-mock-manuscript.md)).
> 4. **Trạng thái Đề xuất Codex duyệt:** **`DIRECT_SEARCH_COMPLETE`** và **`READY_FOR_DEDUP_AND_ROUND_1_SCREENING`**.

---

## 1. Tuân thủ Tuyệt đối Bất biến Tiền đăng ký OSF (OSF Immutability Audit)

1. **Khôi phục 100% SHA-256 Snapshot:** Tất cả các tệp tiền đăng ký OSF tại thư mục gốc (`protocol.md`, `search-strategy.md`, `screening-codebook.md`, `data-extraction-codebook.md`, `record-registry-codebook.md`, `prisma-scr-checklist.md`, `implementation-case-sampling-frame.csv`, `international-benchmark.md`) được giữ nguyên bản byte-for-byte 100%, trùng khớp hoàn toàn mã băm SHA-256 trong `artifacts/protocol-registration-lock-2026-07-31/checksums.sha256`.
2. **Không ghi đè tệp gốc:** Mọi trạng thái thực thi hậu đăng ký không được sửa vào tệp gốc `implementation-case-sampling-frame.csv` mà chỉ được ghi nhận độc lập tại các tệp nhật ký trong `docs/` và `artifacts/`.

---

## 2. Bảng Bằng chứng Thu hồi 5 Nhánh Nguồn Chính thức (5-Branch Proof Matrix)

| Stt | Nhánh nguồn | Phạm vi bao phủ | Trạng thái kỹ thuật thô | Chi tiết Thẩm định Kỹ thuật & Mã SHA-256 |
| --- | --- | --- | --- | --- |
| 1 | **Y sinh & Đa ngành Quốc tế** | PubMed & OpenAlex | **`HARVEST_COMPLETE`** | • **PubMed:** Kết nối E-utilities API (`POLITE_EMAIL` & `NCBI_API_KEY`), HTTP 200 OK (88 bản ghi).<br>• **OpenAlex:** Thu hồi chuẩn **14 trang / 347 ID duy nhất** (trang 14 trả về 22 kết quả và `next_cursor=null`, theo quy tắc terminal nêu trong sửa đổi hợp nhất v1). |
| 2 | **Bộ Y tế & 7 Đơn vị Trực thuộc** | Cổng MOH (`moh.gov.vn`) và 7 đơn vị chuyên trách | `RAW_PORTAL_CAPTURE_COMPLETE_BUT_SOURCE_ACQUISITION_AND_DEPTH_2_NOT_RUN` | • **Run ID:** `official-nonlegal-20260801T065552`<br>• Thực thi **84 cặp kênh–truy vấn và 252 page attempts** (với 144 lượt không-2xx).<br>• Trích xuất 223 tiêu đề ứng viên vào `official-inventory.csv`. |
| 3 | **Bộ Khoa học & Công nghệ** | Cổng Bộ KH&CN (`most.gov.vn`) & MST | `RAW_PORTAL_CAPTURE_COMPLETE_BUT_SOURCE_ACQUISITION_AND_DEPTH_2_NOT_RUN` | • **Run ID:** `official-nonlegal-20260801T061911`<br>• Thực thi trong đợt chạy gồm **36 cặp kênh–truy vấn và 72 page attempts** (cùng với Nhánh 4). |
| 4 | **Thể chế Quốc tế** | UNESCO RAM & WHO Việt Nam | `RAW_PORTAL_CAPTURE_COMPLETE_BUT_SOURCE_ACQUISITION_AND_DEPTH_2_NOT_RUN` | • **Run ID:** `official-nonlegal-20260801T061911`<br>• Thực thi trong đợt chạy gồm **36 cặp kênh–truy vấn và 72 page attempts** (cùng với Nhánh 3). |
| 5 | **Địa phương & Bệnh viện Sentinel** | 3 Sở Y tế + 6 Bệnh viện Sentinel | `SENTINEL_CAPTURE_COMPLETE_NOT_SCREENED` | • **Run ID:** `sentinel-capture-20260801T063425`<br>• Đã được Lộc Đặng xác minh danh tính/domain ([`docs/governance/sampling-frame-verification-2026-08-01-loc-dang.md`](../docs/governance/sampling-frame-verification-2026-08-01-loc-dang.md)).<br>• Kiểm toán đủ **544/544 tệp thô** SHA-256 (gồm `.body`, `.headers`, `.error.txt`). |
| 6 | **Pháp lý Chính phủ (Mandatory Legal)** | Cổng Văn bản Chính phủ, Công báo & VBPL | **`HARVEST_COMPLETE`** | • **Run ID HTML:** `legal-portals-20260801T095241`<br>• Hoàn thành phân trang 10 trang / 100 kết quả và lập Đồ thị Quan hệ Pháp lý ([`docs/governance/legal-relation-graph-2026-08-01.md`](../docs/governance/legal-relation-graph-2026-08-01.md)). |

---

## 3. Nhật ký Thẩm định Thành phần Artifacts & Khả thi Gate G6/G7

1. **Định vị tệp `official-inventory.csv`:**
   - Tệp `artifacts/search-rerun-01-2026-07-31/official-inventory.csv` trích xuất 223 biểu hiện tiêu đề/locator ứng viên từ các trang HTML kết quả tìm kiếm thô.

2. **Nghiệm thu Gate G7:**
   - Gate G7 nghiệm thu trạng thái **`PASS_MOCK_CAPACITY_VERIFIED`** dựa trên bản thảo thử nghiệm 8 trang [`docs/drafts/g7-trial-draft-mock-manuscript.md`](../drafts/g7-trial-draft-mock-manuscript.md) (2.276 từ).

---

## 4. Kết luận Kiểm toán & Đề trình Chuyển giai đoạn

1. **Trạng thái Tiến độ Đề xuất:** **`DIRECT_SEARCH_COMPLETE`**
2. **Quyết định Cổng:** `Gate G6` = **`FAIL_CLOSED`**, `Gate G7` = **`PASS_MOCK_CAPACITY_VERIFIED`**
3. **Trạng thái Mở Sàng lọc Kép Vòng 1 Đề xuất:** **`READY_FOR_DEDUP_AND_ROUND_1_SCREENING`**.

---
*Báo cáo được lưu trữ tại `reports/official-sources-harvest-audit-report-2026-08-01.md`.*
