# Biên bản hoàn tất Phân xử Bất đồng Vòng 2 (PI Đào Trung Thành)

**Ngày:** 2026-08-02
**Corpus:** 166 record `CANON-*` (sàng lọc toàn văn kép Vòng 2)
**Pi:** Đào Trung Thành (`DAO_TRUNG_THANH`)
**Trạng thái:** 74 dòng bất đồng đã được PI duyệt → danh sách INCLUDE cuối cùng Vòng 2 đã chốt.

---

## 1. Tổng quan phân xử

| Hạng mục | Số dòng |
| --- | ---: |
| Tổng dòng được phân xử (Ma trận) | **74** |
| — `DISAGREEMENT_DECISION` (Thành INCLUDE vs Lộc EXCLUDE) | 55 |
| — `DISAGREEMENT_EXCLUDE_REASON` (cùng EXCLUDE, khác mã) | 19 |
| Quyết định **INCLUDE** (giữ Thành) | **2** |
| Quyết định **EXCLUDE** (đồng thuận Lộc) | **72** |

**Nguyên tắc phân xử:** mọi quyết định dựa trên **rà soát toàn văn/tóm tắt** theo locator (DOI/PMID/arXiv/Frontiers/MDPI/PubMed/journal VN) trong `docs/audits/round-2-full-text-retrieval-ledger-2026-08-02.csv`, theo codebook frozen `0.1-draft`, mã loại `EX01`–`EX09`.

---

## 2. Phân bố mã loại trong 72 dòng EXCLUDE

| Mã | Diễn giải | Số dòng |
| --- | --- | ---: |
| EX04 | Không đạo đức/quản trị AI (thuần kỹ thuật) | 29 |
| EX01 | Không thuộc phạm vi Việt Nam | 22 |
| EX07 | Trùng lắp / không dữ liệu mới (preprint/bản trùng) | 9 |
| EX02 | Không phải lĩnh vực y tế | 7 |
| EX05 | Sai loại nguồn (bài báo/tin/trừu tượng hội nghị) | 4 |
| EX03 | Không có AI | 1 |
| **Tổng** | | **72** |

## 3. Phân bổ theo loại bất đồng

### 3a. DISAGREEMENT_DECISION (55 dòng)
- **INCLUDE (2):** CANON-00281, CANON-00319
- **EXCLUDE (53):** do 53 dòng Thành=INCLUDE / Lộc=EXCLUDE, PI chốt **EXCLUDE** theo toàn văn.

### 3b. DISAGREEMENT_EXCLUDE_REASON (19 dòng)
Cả hai reviewer đồng EXCLUDE, khác mã → PI chốt 1 mã căn cứ chính (tất cả giữ `pi_decision=EXCLUDE`).

---

## 4. Hai dòng INCLUDE được PI duyệt (kèm căn cứ toàn văn)

| ID | Tiêu đề | Căn cứ toàn văn |
| --- | --- | --- |
| **CANON-00281** | Curious but Unprepared: Healthcare Students' Perspectives on AI and Robotics in Care and the Need for Curriculum Reform | Khảo sát **1.221 sinh viên Y–Dược Việt Nam (2023)**; đánh giá nhận thức AI/robot trong chăm sóc, quan ngại riêng tư/phụ thuộc, và **nhu cầu cải cách giảng dạy đạo đức AI**. Thỏa mãn: Việt Nam + công nghệ AI trong y tế + nội dung đạo đức/đào tạo nhân lực. |
| **CANON-00319** | Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification | Khung quản trị trước triển khai (Agent Operational Envelope, Trust Certificate) có **nội dung đạo đức/quản trị rất mạnh** + Việt Nam nằm trong 2 chế độ pháp lý (Việt Nam 2025 AI Law). Thỏa mãn tiêu chí INCLUDE. |

> Lưu ý quản trị: đối với 00281, Lộc Đặng đã gán `EX01_NOT_VIETNAM`, nhưng toàn văn cho thấy **đối tượng là sinh viên Việt Nam** → mã này không phù hợp; PI chốt **INCLUDE**.

---

## 5. Danh sách INCLUDE cuối cùng Vòng 2 (đưa vào trích xuất dữ liệu)

**Tổng cộng: 50 record** = 48 dòng đồng thuận INCLUDE kép + 2 dòng phân xử INCLUDE.

`docs/governance/round-2-final-include-list-2026-08-02.csv` (50 dòng, `round2_final_decision=INCLUDE`)

48 dòng đồng thuận: CANON-00001, 00004, 00005, 00006, 00048, 00068, 00077, 00098, 00101, 00105, 00152, 00166, 00171, 00176, 00180, 00181, 00183, 00185, 00188, 00191, 00196, 00198, 00209, 00210, 00217, 00230, 00232, 00234, 00235, 00236, 00238, 00243, 00247, 00249, 00250, 00251, 00254, 00260, 00262, 00266, 00283, 00290, 00299, 00303, 00335, 00359, 00370, 00374

+ 2 phân xử: **CANON-00281, CANON-00319**

---

## 6. Tính toàn vẹn & đối soát

- Phiếu phân xử `round-2-adjudication-form-2026-08-02.csv`: 74 dòng, mỗi dòng `pi_decision ∈ {INCLUDE, EXCLUDE}` + đúng 1 mã EX (hoặc rỗng khi INCLUDE), `pi_date=2026-08-02`.
- Ma trận `round-2-full-text-adjudication-matrix-2026-08-02.csv`: 74 dòng được điền `adjudicated_decision`, `adjudication_reason`, `adjudicator=DAO_TRUNG_THANH`.
- Đối soát phiếu ↔ ma trận: **0 dòng lệch** (74/74 khớp).
- Không sửa 7 cột cố định của phiếu; không tạo mã mới ngoài EX01–EX09.

---

## 7. Bước tiếp theo

Danh sách **50 INCLUDE cuối cùng Vòng 2** đã sẵn sàng → chuyển sang **trích xuất dữ liệu** (data extraction) theo kế hoạch PRISMA. 116 record còn lại (166 − 50) bị loại và sẽ ghi vào lưu đồ PRISMA Vòng 2.
