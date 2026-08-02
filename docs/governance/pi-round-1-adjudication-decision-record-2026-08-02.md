# Biên bản quyết định phân xử bất đồng vòng 1 của chủ trì nghiên cứu (PI Adjudication Decision Record)

**Ngày tạo:** 2026-08-02
**Chủ trì nghiên cứu (PI):** Đào Trung Thành
**Người rà soát độc lập thứ hai:** Lộc Đặng
**Phạm vi:** Phân xử 76 bản ghi bất đồng (`PENDING_ADJUDICATION`) sau khi hai tác giả hoàn tất và khóa độc lập Vòng 1 sàng lọc tiêu đề/tóm tắt cho 385 `CANON-*`.

---

## 📌 1. Tuyên bố ranh giới thẩm quyền và trách nhiệm khoa học

1. **Thẩm quyền phân xử độc nhất:** Toàn bộ quyết định phân xử đối với 76 bản ghi bất đồng trong biên bản này thuộc về thẩm quyền cá nhân của **Chủ trì nghiên cứu (PI Đào Trung Thành)**, tuân thủ đúng quy trình đã đăng ký tại `protocol.md` và `screening-codebook.md`.
2. **Tính chính danh của bằng chứng:** Quyết định phê duyệt ngày 02/08/2026 của PI là căn cứ pháp lý và khoa học duy nhất để chốt trạng thái phân xử của Vòng 1.

---

## 📊 2. Quyết định phân xử chi tiết cho 76 bản ghi bất đồng

PI Đào Trung Thành đã xem xét toàn bộ 76 bản ghi bất đồng và đưa ra quyết định phân xử chính thức theo 3 cụm như sau:

### 2.1 Cụm 1: Các nghiên cứu ngoài phạm vi y tế (6 bản ghi) -> Quyết định: LOẠI (`EXCLUDE`)

* **Lý do phân xử:** Các bản ghi này thuộc lĩnh vực dự báo thiên tai (sạt lở, hạn hán), địa chất/xây dựng (sụt lún công trình), hóa sinh thực vật (cây gừng), nhận dạng thực thể hành chính (`PAP_NER`), hoặc đánh giá "sức khỏe kinh tế tư nhân" (sử dụng từ *"health"* như một ẩn dụ kinh tế). Các bản ghi này vi phạm tiêu chí phạm vi y tế theo mã **`EX02_NOT_HEALTHCARE`**.
* **Danh sách 6 bản ghi bị loại:**
  1. `CANON-00192`: *Drought risk assessment in Quang Tri Province, Vietnam using Landsat multi-temporal remote sensing data and machine learning algorithm*
  2. `CANON-00193`: *Developing machine learning models for vegetation health index forecasting in the Srepok basin, Vietnam*
  3. `CANON-00205`: *PAP_NER: A large-scale vietnamese administrative named entity recognition corpus and hybrid deep learning architecture.*
  4. `CANON-00295`: *Prediction of building subsidence in Vietnam using machine learning techniques based on leveling results*
  5. `CANON-00351`: *Molecular characterization of a distinct ginger chemotype from Thua Thien Hue, Vietnam, and the application of PCR-based markers for identifying unknown ginger populations in the region using machine learning*
  6. `CANON-00363`: *Applying Machine Learning in assessing the health of the private economy in Vietnamese localities*

---

### 2.2 Cụm 2: Các nghiên cứu ứng dụng ML dự báo lâm sàng / dịch tễ học (10 bản ghi) -> Quyết định: CHUYỂN VÒNG 2 (`ADVANCE_TO_FULL_TEXT`)

* **Lý do phân xử:** Tuy các tóm tắt ban đầu chủ yếu tập trung vào chỉ số mô hình dự báo (COVID-19, sốc xuất huyết, loãng xương, sán lá gan, bỏ điều trị HIV, trẻ sinh nhẹ cân), nhưng theo đúng nguyên tắc bộ lọc mở rộng ở Vòng 1 (`inclusive filter`), PI quyết định **chuyển toàn văn sang Vòng 2** để rà soát chi tiết xem bài có phần thảo luận về quy trình vận hành, quản trị dữ liệu bệnh nhân, hoặc an toàn lâm sàng hay không.
* **Danh sách 10 bản ghi được chuyển toàn văn:**
  `CANON-00081`, `CANON-00092`, `CANON-00187`, `CANON-00221`, `CANON-00228`, `CANON-00231`, `CANON-00241`, `CANON-00322`, `CANON-00382`, `CANON-00383`.

---

### 2.3 Cụm 3: Các nghiên cứu AI y tế và giáo dục y khoa tại Việt Nam (60 bản ghi) -> Quyết định: CHUYỂN VÒNG 2 (`ADVANCE_TO_FULL_TEXT`)

* **Lý do phân xử:** Các nghiên cứu này đề cập trực tiếp đến ứng dụng AI trong chẩn đoán/điều trị (sàng lọc bệnh võng mạc tiểu đường ở Bình Định, PhoBERT phân loại bệnh, GenAI trong ung thư, X-quang ngực), kiến thức/thái độ/thực hành (KAP) của sinh viên y dược về AI, ChatGPT trong học tập y khoa, VietCheckMed kiểm tra quảng cáo y tế. Cả hai tác giả ĐỀU ĐỒNG Ý ĐƯA VÀO VÒNG 2 (PI đánh `INCLUDE`, Lộc Đặng đánh `UNCERTAIN` để xác minh toàn văn). PI chính thức chốt chuyển toàn bộ sang Vòng 2.

---

## 📈 3. Tổng kết số liệu PRISMA-ScR Vòng 1 sau phân xử

| Trạng thái quyết định Vòng 1                        | Đồng thuận ban đầu | Phân xử của PI | Tổng số cuối cùng | Tỷ lệ / Ghi chú                                   |
| :-------------------------------------------------------- | :---------------------: | :---------------: | :--------------------: | :--------------------------------------------------- |
| **Loại tại Vòng 1 (Title/Abstract Excluded)**    |           213           |    +6 (Cụm 1)    | **219 bản ghi** | 56.88% (Không xóa record/provenance)               |
| **Chuyển sang Vòng 2 (Full-Text Dual Screening)** |           96           | +70 (Cụm 2 & 3) | **166 bản ghi** | 43.12% (Chuyển sàng lọc toàn văn kép)          |
| **Chờ phân xử (Pending Adjudication)**           |           76           |        -76        |  **0 bản ghi**  | **100% bất đồng đã được giải quyết** |
| **TỔNG CỘNG**                                     |      **385**      |    **0**    | **385 bản ghi** | **Khớp 100% Master Input Registry**           |

---

## 🔒 4. Xác minh tính toàn vẹn dữ liệu & Mã băm SHA-256

- **Tệp ma trận đối soát & phân xử Vòng 1:** [`docs/governance/round-1-adjudication-matrix-2026-08-02.csv`](round-1-adjudication-matrix-2026-08-02.csv)
  - **Mã băm SHA-256:** `178e3ce4f577a9fa4b9370369141ba2c6ba0e8780ea9f1bf6f59a5fef3e9d044`
- **Tệp sàng lọc gốc Vòng 1 - PI Đào Trung Thành:** [`docs/governance/round-1-title-abstract-dao-trung-thanh-2026-08-02.csv`](round-1-title-abstract-dao-trung-thanh-2026-08-02.csv)
  - **Mã băm SHA-256:** `adb127e9fac328946d9cac5a2479f17f0ecab0b03b6d0dbcab7e6d0f398252a3`
- **Tệp sàng lọc gốc Vòng 1 - Lộc Đặng:** [`docs/governance/round-1-title-abstract-loc-dang-2026-08-02.csv`](round-1-title-abstract-loc-dang-2026-08-02.csv)
  - **Mã băm SHA-256:** `3252babc45529bffff1c4562e453cd03455838dae1cbdecd79a409b451c69430`

Biên bản này được khóa và lưu trữ trong audit trail của repository làm bằng chứng độc lập cho quyết định của Chủ trì nghiên cứu.
