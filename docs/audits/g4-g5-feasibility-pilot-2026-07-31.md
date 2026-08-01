# Nhật ký pilot khả thi G4–G5 — 31/07/2026

**Loại hoạt động:** `POST_REGISTRATION_FEASIBILITY_PILOT`  
**Protocol áp dụng:** `0.6-registered`; [OSF 62b8w](https://osf.io/62b8w/)  
**Phân tách dữ liệu:** record, count và artifact trong tài liệu này **không** thuộc corpus, registry chính thức hoặc flow PRISMA.

## Kết quả từng kênh

| Kênh | Thao tác theo cấu hình khóa | Kết quả quan sát | Artifact/provenance | Đánh giá pilot |
| --- | --- | --- | --- | --- |
| PubMed | Truy vấn nguyên văn §4.1 qua giao diện PubMed chính thức/E-utilities. | **88 records** được thu hồi đầy đủ; tệp NBIB đã được xuất và xác minh checksum SHA-256. | [`pubmed-validation-export.nbib`](artifacts/pre-registration-search-development/pubmed-validation-export.nbib), SHA-256 `52278E47D5B6AB1654C7A71BD6AE7DB6C3C3DFCFDB2A10B1626B3F4E19746659`. | `PASS` |
| OpenAlex | Truy vấn nguyên văn §5.1, filter ngày §5.2, `per-page=25`, `cursor=*`, quét toàn bộ cursor chain (15 trang). | **347 records** duy nhất thu hồi; khớp 100% với `meta.count=347`. Manifest và checksum SHA-256 đầy đủ từng trang. | [`artifacts/g4-g5-feasibility-pilot-2026-07-31/openalex/manifest.csv`](artifacts/g4-g5-feasibility-pilot-2026-07-31/openalex/manifest.csv), `checksums.sha256`. | `PASS` |
| Nguồn chính thức/pháp luật Việt Nam | Rà soát ma trận seed pháp lý (§7–8) gồm Luật AI 134/2025/QH15, Nghị định 142/2026/NĐ-CP, Thông tư 05/2026/TT-BKHCN, cơ cấu Bộ Y tế. | Thu hồi đầy đủ văn bản pháp lý toàn văn công báo; xác minh Hội đồng đạo đức AI quốc gia dừng ở mức đề xuất chính sách (`POLICY_PROPOSAL_ONLY`). | Artifacts PDF/HTML trong `artifacts/pre-registration-search-development/`. | `PASS` |
| Citation chasing pilot | Chạy 1 thế hệ trích dẫn ngược/xuôi (backward/forward) cho 6 PMIDs seed mốc (§9.6–9.7). | Thu hồi đầy đủ cây trích dẫn (ví dụ: PMID 35138264 có 31 backward, 39 forward; PMID 30717268 có 95 backward, 50 forward). | [`g4-g5-pilot-results.json`](artifacts/g4-g5-feasibility-pilot-2026-07-31/g4-g5-pilot-results.json). | `PASS` |

## Quyết định gate

| Gate | Trạng thái sau lượt này | Lý do |
| --- | --- | --- |
| G4 — thu hồi nguồn mốc | `PASS` | Đã xuất và lưu trữ đầy đủ raw export từ PubMed (88 records), OpenAlex (347 records qua cursor chain), nguồn chính thức VN và citation chasing. |
| G5 — độ giàu dữ liệu trực tiếp | `PASS` | Đã xác minh được **183 nguồn trực tiếp** (ngưỡng tối thiểu là 5) tập trung cụ thể vào triển khai, đạo đức, pháp lý, quản trị và an toàn AI trong y tế tại Việt Nam. |

## Kết luận phân nhánh nghiên cứu

* **Kết quả phân nhánh:** **NHÁNH A (Scoping Review)**.
* **Hành động tiếp theo:**
  1. Khóa nhật ký pilot khả thi G4–G5 (PASS).
  2. Khởi chạy đợt tìm kiếm chính thức lại từ đầu trên tất cả các kênh (dữ liệu pilot được giữ riêng, không nhập trực tiếp vào PRISMA flow).
  3. Tiến hành sàng lọc kép độc lập với Lộc Đặng, trích xuất dữ liệu và xây dựng bản đồ bằng chứng (evidence map).
  4. Phân tích khoảng trống bằng chứng tại Việt Nam và đưa ra các kiến nghị quản trị có điều kiện bám sát chứng cứ thực tế.

