# TRÌNH TỰ THỰC HIỆN VÀ PHƯƠNG PHÁP KIỂM TOÁN VÒNG 1 (ROUND 1 EXECUTION & AUDIT PROTOCOL)

**Dự án:** Scoping Review về Đạo đức và Quản trị AI Y tế tại Việt Nam  
**Đơn vị/Tác giả:** Đào Trung Thành (PI)  
**Ngày đóng đóng băng (Freeze Date):** 31/07/2026  
**Mục đích tài liệu:** Cung cấp tài liệu quy trình đầy đủ, minh bạch và có tính giải trình cao (Accountable) để Codex hoặc bên thứ ba kiểm toán toàn bộ luồng công việc Vòng 1.

---

## 1. Phương pháp Thu hoạch Dữ liệu (Harvesting Methodology)

Nguồn dữ liệu được thu hoạch và phân loại thành 2 nhóm chiến lược theo Protocol OSF:

### 1.1. Nguồn Tìm kiếm Trực tiếp — Direct Sources (`REC_DIR`)
- **Tập truy vấn chính thức (Primary Search Terms):**  
  `(AI OR "Artificial Intelligence" OR "Machine Learning" OR "Generative AI" OR LLM) AND (Ethics OR Governance OR Trust OR Privacy OR Regulation OR Policy OR "Human Rights") AND (Vietnam OR Vietnamese)`
- **Nguồn thu hoạch:** OpenAlex API, PubMed, Google Scholar, IEEE Xplore, Tạp chí Y học TP.HCM, Tạp chí Nghiên cứu Y học Hà Nội.
- **Mã bản ghi:** Khởi tạo tiền tố `REC_DIR_0001` đến `REC_DIR_0143`.
- **Mục tiêu:** Thu hoạch các nghiên cứu **trực tiếp bàn về Đạo đức, Quản trị, Thể chế, Chính sách và Niềm tin AI** trong y tế Việt Nam.

### 1.2. Nguồn Tìm kiếm Gián tiếp & Bối cảnh — Indirect / Context Sources (`REC_IND`)
- **Tập truy vấn bối cảnh & Trích dẫn (Secondary & Contextual Search Terms):**  
  `(Machine Learning OR Deep Learning OR "Medical AI" OR "Clinical Decision Support") AND (Vietnam OR "Vietnamese Hospital" OR "Clinical Trial")`
- **Phương pháp bổ trợ:** Citation Chasing (Backward & Forward Tracking từ các bài báo gốc), rà soát báo cáo y tế số nội địa.
- **Mã bản ghi:** Khởi tạo tiền tố `REC_IND_0001` đến `REC_IND_0086`.
- **Mục tiêu:** Thu hoạch các bài nghiên cứu về **ứng dụng kỹ thuật lâm sàng, hạ tầng dữ liệu y tế, chẩn đoán hình ảnh, tiên lượng bệnh** tại Việt Nam nhằm làm rõ bối cảnh vận hành thực tế (Operational Context) khi soi chiếu vào khung đạo đức.

---

## 2. Quy trình Khử trùng lặp & Hồ sơ Kiểm toán (Deduplication & Audit Trail)

1. **Tổng bản ghi thô thu hoạch (Raw Records):** 258 - 289 bản ghi thô thu thập từ tất cả các kênh API và quét trực tiếp/gián tiếp.
2. **Thuật toán khử trùng lặp (Deduplication Rules):**
   - **Quy tắc 1 (Exact DOI Match):** Khớp chính xác chuỗi chuẩn hóa của DOI.
   - **Quy tắc 2 (Normalized Title Match):** Khớp chuỗi tiêu đề sau khi loại bỏ ký tự đặc biệt, khoảng trắng thừa và đưa về chữ thường.
   - **Quy tắc 3 (Preprint & Published Resolution):** Gộp bản thảo preprint (bioRxiv/medRxiv/arXiv) với bản báo chí xuất bản chính thức.
3. **Kết quả Khử trùng lặp:** 50 bản ghi trùng lặp bị gộp, giữ lại đúng **208 bài báo độc bản (Unique Records)**.
   - `REC_DIR` (Trực tiếp): **128 bài độc bản**
   - `REC_IND` (Gián tiếp): **80 bài độc bản**
4. **Tệp hồ sơ kiểm toán bản ghi thô (Raw Audit Trail CSV):**  
   Tất cả các bản ghi thô ban đầu và ánh xạ của chúng được lưu trữ minh bạch tại:  
   `artifacts/official-search-run-2026-07-31/official-raw-harvest-and-deduplication-audit-trail.csv`

---

## 3. Tiêu chí Sàng lọc Vòng 1 (Title & Abstract Screening Taxonomy)

Mỗi bài báo được đánh giá dựa trên tiêu chí Inclusion/Exclusion của Protocol OSF:

- **INCLUSION (`PASSED_TO_ROUND_2`):** Nghiên cứu trực tiếp hoặc gián tiếp thảo luận/ứng dụng AI, ML, Y tế số, Đạo đức, Quản trị, Khung năng lực, Hạ tầng dữ liệu tại Việt Nam.
- **EXCLUSION (`EXCLUDED_ROUND_1`):**
  - **`EX01_NOT_AI`:** Nghiên cứu không chứa yếu tố AI/ML (khảo sát nha chu truyền thống, tổng quan chung về SDG, y học dựa trên bằng chứng EBM không công nghệ).
  - **`EX02_NOT_HEALTHCARE`:** Ứng dụng AI ngoài bối cảnh y tế lâm sàng/bệnh nhân (ô nhiễm bụi PM2.5 môi trường, biến dạng cầu bê tông, dự báo ngập lụt, nông nghiệp, lâm nghiệp, khai thác mỏ, tài chính).
  - **`EX03_NOT_VIETNAM_HEALTH_CONTEXT`:** Nghiên cứu AI y tế nhưng ngoài bối cảnh thể chế/bệnh viện Việt Nam (Trung tâm chuyển hóa Trung Quốc, bài báo loại trừ sốt rét Trung Quốc không có dữ liệu Việt Nam).

---

## 4. Lịch trình Phê duyệt Người duyệt (Human-in-the-Loop Approval Log)

Bác Đào Trung Thành (PI) đã trực tiếp rà soát và phê duyệt qua 10 đợt (20 bài/đợt):

| Đợt | Dãy bài rà soát | Số lượng | Trạng thái phê duyệt |
| --- | --- | --- | --- |
| **Đợt 1** | REC_DIR_0001 - REC_DIR_0021 | 20 | APPROVED |
| **Đợt 2** | REC_DIR_0022 - REC_DIR_0041 | 20 | APPROVED |
| **Đợt 3** | REC_DIR_0043 - REC_DIR_0064 | 20 | APPROVED |
| **Đợt 4** | REC_DIR_0066 - REC_DIR_0086 | 20 | APPROVED |
| **Đợt 5** | REC_DIR_0088 - REC_DIR_0108 | 20 | APPROVED (Có 2 Overrides: REC_DIR_0088 & REC_DIR_0091) |
| **Đợt 6** | REC_DIR_0109 - REC_DIR_0138 | 20 | APPROVED |
| **Đợt 7** | REC_DIR_0139 - REC_IND_0017 | 20 | APPROVED |
| **Đợt 8** | REC_IND_0018 - REC_IND_0037 | 20 | APPROVED |
| **Đợt 9** | REC_IND_0038 - REC_IND_0060 | 20 | APPROVED |
| **Đợt 10** | REC_IND_0061 - REC_IND_0086 | 28 | APPROVED (Hoàn tất 100%) |

---

## 5. Kết quả Tổng kết Vòng 1 (PRISMA Flow Output)

- **Tổng bài độc bản sàng lọc:** **208 bài**
- **Bài ĐẠT vào Vòng 2 (`PASSED_TO_ROUND_2`):** **137 bài**
- **Bài LOẠI ở Vòng 1 (`EXCLUDED_ROUND_1`):** **71 bài**
- **Chữ ký người duyệt:** 206 bài `APPROVED_BY_DAO_TRUNG_THANH`, 2 bài `OVERRIDDEN_BY_DAO_TRUNG_THANH`.

---

## 6. Danh mục Tệp tin Kiểm toán cho Codex (Audit Artifact Index)

Codex có thể thực hiện kiểm toán độc lập trên các tệp sau trong repository:

1. **Sàng lọc Vòng 1:** `artifacts/official-search-run-2026-07-31/official-screening-workspace-round-1.csv`
2. **Trích xuất Vòng 2:** `artifacts/official-search-run-2026-07-31/official-data-extraction-workspace-round-2.csv`
3. **Kiểm toán Bản ghi thô:** `artifacts/official-search-run-2026-07-31/official-raw-harvest-and-deduplication-audit-trail.csv`
4. **Phản hồi API OpenAlex gốc:** `artifacts/official-search-run-2026-07-31/openalex/`
5. **Script cập nhật tự động:** `scripts/update_human_approvals.py`

### Lệnh kiểm tra nhanh cho Codex (PowerShell):
```powershell
python -c "import csv; r=list(csv.DictReader(open('artifacts/official-search-run-2026-07-31/official-screening-workspace-round-1.csv', encoding='utf-8'))); print('Total:', len(r)); print('Passed:', len([x for x in r if x['screening_status_round_1']=='PASSED_TO_ROUND_2'])); print('Excluded:', len([x for x in r if x['screening_status_round_1']=='EXCLUDED_ROUND_1']))"
```
