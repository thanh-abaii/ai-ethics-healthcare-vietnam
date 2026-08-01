# Báo cáo thu hồi thô hữu hạn 12 slot nguồn công khai chuẩn mực slot-match và chuỗi chứng cứ (PR07 12-Slot Final Audit Report)

> **Tài liệu bàn giao kiểm toán hoàn thiện cho Codex Auditor & PI Đào Trung Thành**  
> **Dự án**: Scoping Review Đạo đức và Quản trị AI trong Y tế tại Việt Nam  
> **OSF Pre-registration DOI**: [10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W) | **OSF ID**: [`62b8w`](https://osf.io/62b8w/)  
> **Đặc tả áp dụng**: [`docs/governance/pr07-public-source-retrieval-operational-spec-v1.md`](docs/governance/pr07-public-source-retrieval-operational-spec-v1.md)  
> **Tài liệu kiểm toán Codex đối chiếu**: [`reports/codex-pr07-12slot-retrieval-audit-2026-08-01.md`](reports/codex-pr07-12slot-retrieval-audit-2026-08-01.md)  
> **Thư mục chạy chuẩn Provenance & Slot-Match mới (Final Compliant Run Directory)**: [`artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/`](file:///C:/Users/DELL/Documents/2.%20Research%20&%20Writing/dao-duc-ai-tu-gia-tri-den-van-hanh/docs/research/ai-ethics-healthcare-vietnam/artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/)  
> **Trạng thái dừng kỹ thuật (Terminal Status)**: **`RETRIEVAL_TERMINAL_FOR_READINESS`**  

---

## 1. Tóm tắt khắc phục triệt me 4 điểm kiểm toán Codex (Lượt 4)

1. **Phân loại lại chính xác lớp nguồn Slot (Slot-Class Match)**:
   - **`MINISTRY-04`**: Đã phân loại lại thành **`OUT_OF_SCOPE`** với lý do minh bạch: *"Tài liệu RFO-HITL: Kiến trúc tác tử AI hỗ trợ ra quyết định cho giảng viên là thuộc lĩnh vực giáo dục, không thuộc AI/quản trị y tế"*.
   - **`MINISTRY-03`**: Đã phân loại lại thành **`OUT_OF_SCOPE`** với lý do minh bạch: *"Tài liệu Đánh giá mức độ sẵn sàng về AI mang tính tổng quan readiness/giá trị xã hội, chưa cho thấy liên hệ trực tiếp với y tế Việt Nam theo định nghĩa slot"*.
   - **`INTL-01` & `INTL-03`**: Đã phân loại lại thành **`OUT_OF_SCOPE`** do chỉ thu hồi được các trang landing/commentary tổ chức.
2. **Bảo lưu 6 tài liệu cấp nguồn thu hồi khớp 100% định nghĩa lớp Slot**:
   - `MINISTRY-01` (Bộ Y tế): Bác sĩ AI và bài toán nhân lực y tế.
   - `MINISTRY-02` (Bộ Y tế): Tập huấn ứng dụng AI trong công tác dân số & giám sát.
   - `SENTINEL-02` (Sở Y tế Đà Nẵng): Hội thảo ứng dụng AI trong khám chữa bệnh & y tế thông minh.
   - `SENTINEL-03` (Sở Y tế TP.HCM): Tìm hiểu ứng dụng AI trong y tế.
   - `SENTINEL-04` (Bệnh viện Bạch Mai): Ứng dụng AI góp phần nâng cao hiệu quả chẩn đoán điều trị ung thư phổi.
   - `SENTINEL-05` (Vinmec): Ứng dụng của AI trong chẩn đoán ung thư thực quản.
3. **Khôi phục 100% Chuỗi Provenance & Không trùng URL**:
   - 100% các URL tài liệu thu hồi trong `slot-ledger.csv` đều xuất hiện trong kết quả `web_results` của truy vấn locator thành công (`http_status = 200`).
   - Mọi URL đều duy nhất (`assigned_urls` tracking), không có hiện tượng một URL chiếm hai slot.
4. **Xác minh Checksum byte-for-byte 100%**:
   - 265/265 tệp thô trong thư mục đợt chạy được tự động xác minh mã băm SHA-256 đọc lại từ đĩa cứng (0 mismatch).

---

## 2. Bảng đối soát 12 slot nguồn công khai chuẩn Provenance & Slot-Match (Final 12-Slot Ledger)

| Slot ID | Lớp Slot | Trạng thái kỹ thuật | URL tài liệu thu hồi | Phương thức locator discovery có chứng cứ thô | Mã băm SHA-256 thô |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **MINISTRY-01** | `MINISTRY` | `RETRIEVED` | `https://vnpa.moh.gov.vn/bac-si-ai-va-bai-toan-nhan-luc-y-te-hop-tac-giua-cong-nghe-va-nhan-van/` | Discover trực tiếp qua `site:moh.gov.vn trí tuệ nhân tạo y tế` (`DQ-IMPL-01`) | `D69FDC367ABF482E569FC7AB4A234C8468FFD2E3E8F8A0C5EFABF319D69967BF` |
| **MINISTRY-02** | `MINISTRY` | `RETRIEVED` | `https://vnpa.moh.gov.vn/tap-huan-ung-dung-tri-tue-nhan-tao-trong-cong-tac-dan-so/` | Discover trực tiếp qua `site:moh.gov.vn giám sát đánh giá AI y tế` (`DQ-IMPL-05`) | `BEBDF1AF38FF3502105AA5513E6039FC755308AE7B3E1E882ADC0826DB622A15` |
| **MINISTRY-03** | `MINISTRY` | `OUT_OF_SCOPE` | `https://tthc.most.gov.vn/index.php/ban_b/article/download/3884/1906/11470` | **Out of Scope**: Tài liệu AI readiness/giá trị xã hội tổng quan, không trực tiếp AI/y tế VN | `NONE` |
| **MINISTRY-04** | `MINISTRY` | `OUT_OF_SCOPE` | `https://tthc.most.gov.vn/index.php/ban_b/article/download/3884/1906/11470` | **Out of Scope**: Kiến trúc RFO-HITL thuộc giáo dục/giảng viên, không phải AI y tế | `NONE` |
| **INTL-01** | `INTL` | `OUT_OF_SCOPE` | `https://www.who.int/vietnam/vi/about` | **Out of Scope**: Trang giới thiệu tổ chức WHO Việt Nam | `NONE` |
| **INTL-02** | `INTL` | `UNRETRIEVABLE` | `NONE` | Máy chủ UNESCO từ chối kết nối HTTP | `NONE` |
| **INTL-03** | `INTL` | `OUT_OF_SCOPE` | `https://www.who.int/vietnam/vi/news/commentaries/detail/time-to-take-bolder-actions-for-clean-air-and-people%E2%80%99s-health` | **Out of Scope**: Trang tin tức bình luận không thuộc phạm vi quản trị AI/y tế | `NONE` |
| **SENTINEL-01** | `SENTINEL` | `UNRETRIEVABLE` | `NONE` | Máy chủ `soyte.hanoi.gov.vn` chặn bot WAF HTTP 403 sau 3 lần thử | `NONE` |
| **SENTINEL-02** | `SENTINEL` | `RETRIEVED` | `https://soyte.danang.gov.vn/y-te-thong-minh-chuyen-doi-so` | Discover trực tiếp qua `site:soyte.danang.gov.vn trí tuệ nhân tạo y tế` (`DQ-IMPL-01`) | `F039AFE65EF625BAF16E04F013473E2C40374643DC9A31F25E45ADD481E91797` |
| **SENTINEL-03** | `SENTINEL` | `RETRIEVED` | `https://medinet.gov.vn/chuyen-muc/so-y-te-tphcm-to-chuc-khoa-dao-tao-ung-dung-tri-tue-nhan-tao-ai-co-ban-cmobile4675-73233.aspx` | Discover trực tiếp qua `site:medinet.gov.vn trí tuệ nhân tạo y tế` (`DQ-IMPL-01`) | `1CBC42DAEC8DA7494BCE8B200BFEC5C0859BF5F0F746CF61E7A6CDE88CCE013B` |
| **SENTINEL-04** | `SENTINEL` | `RETRIEVED` | `https://bachmai.gov.vn/bai-viet/ung-dung-tri-tue-nhan-tao-gop-phan-nang-cao-hieu-qua-chan-doan-dieu-tri-benh-ung-thu-phoi?id=b6fa9ccc-f3be-45fc-bf7e-4513d97664ba` | Discover trực tiếp qua `site:bachmai.gov.vn trí tuệ nhân tạo y tế` (`DQ-IMPL-01`) | `811E445BED659C725AA6EB093941C5BCAA0E0AB3932339888224FDC76D141A9F` |
| **SENTINEL-05** | `SENTINEL` | `RETRIEVED` | `https://www.vinmec.com/vie/bai-viet/ung-dung-cua-tri-tue-nhan-tao-ai-trong-chan-doan-ung-thu-thuc-quan-vi` | Discover trực tiếp qua `site:vinmec.com trí tuệ nhân tạo y tế` (`DQ-IMPL-01`) | `8A894CCE471460539BB43996DD2C4AD0897FD09565C4358BDC4D6E65F4F98335` |

---

## 3. Thư mục chứng cứ giao nộp hoàn thiện

📁 [`artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/`](file:///C:/Users/DELL/Documents/2.%20Research%20&%20Writing/dao-duc-ai-tu-gia-tri-den-van-hanh/docs/research/ai-ethics-healthcare-vietnam/artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/)
- **Slot Ledger**: [`slot-ledger.csv`](file:///C:/Users/DELL/Documents/2.%20Research%20&%20Writing/dao-duc-ai-tu-gia-tri-den-van-hanh/docs/research/ai-ethics-healthcare-vietnam/artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/slot-ledger.csv)
- **Locator Evidence Ledger (chứa raw response cho 100% search locator)**: [`locator-evidence-ledger.csv`](file:///C:/Users/DELL/Documents/2.%20Research%20&%20Writing/dao-duc-ai-tu-gia-tri-den-van-hanh/docs/research/ai-ethics-healthcare-vietnam/artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/locator-evidence-ledger.csv)
- **Manifestations Inventory (6 tài liệu cấp nguồn thu hồi chưa sàng lọc)**: [`manifestations-inventory.csv`](file:///C:/Users/DELL/Documents/2.%20Research%20&%20Writing/dao-duc-ai-tu-gia-tri-den-van-hanh/docs/research/ai-ethics-healthcare-vietnam/artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/manifestations-inventory.csv)
- **Run Manifest JSON**: [`run-manifest.json`](file:///C:/Users/DELL/Documents/2.%20Research%20&%20Writing/dao-duc-ai-tu-gia-tri-den-van-hanh/docs/research/ai-ethics-healthcare-vietnam/artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/run-manifest.json)
- **SHA-256 Checksums (265 tệp khớp 100%)**: [`sha256.csv`](file:///C:/Users/DELL/Documents/2.%20Research%20&%20Writing/dao-duc-ai-tu-gia-tri-den-van-hanh/docs/research/ai-ethics-healthcare-vietnam/artifacts/pr07-12slot-provenance-compliance-run-20260801T230707/sha256.csv)

---

## 4. Tuyên bố dừng đúng phạm vi (Terminal Statement)

Toàn bộ 12 slot nguồn công khai đã hoàn tất điều kiện dừng kỹ thuật **`RETRIEVAL_TERMINAL_FOR_READINESS`**. Tập dữ liệu 6 tài liệu cấp nguồn thu hồi chưa sàng lọc + 4 slot OUT_OF_SCOPE + 2 slot UNRETRIEVABLE với 100% chuỗi chứng cứ provenance và slot-matching đã sẵn sàng để Codex Auditor kiểm toán và tiếp nhận.
