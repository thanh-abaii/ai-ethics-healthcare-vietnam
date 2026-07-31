# Bộ chuẩn đối chiếu quốc tế

## 1. Kiểm soát phiên bản và ranh giới

| Trường | Giá trị |
| --- | --- |
| `benchmark_version` | `0.4-loc-benchmark-lock` |
| Ngày kiểm tra locator | 31/07/2026 |
| Trạng thái | `PASS_BY_LOC_DANG_REVIEW` |
| Nguồn chính trong bộ chuẩn | 5/5 |
| Vai trò | Bộ chuẩn xác định trước; không phải tập tổng quan phạm vi thứ hai |
| Giai đoạn áp dụng | Đã khóa bởi người rà soát thứ hai độc lập Lộc Đặng; bộ chuẩn sẵn sàng cho đăng ký protocol và đối chiếu nguồn Việt Nam |

Bộ chuẩn này là ngưỡng đối chiếu nhỏ, không đại diện cho toàn bộ y văn quốc tế, không nhập khẩu cơ học nghĩa vụ pháp lý nước ngoài vào Việt Nam và không tạo điểm đạo đức tổng hợp. Ba nguồn chuẩn tắc sơ cấp là WHO, UNESCO và FUTURE-AI. Wang và Alami là **coverage maps**: chúng kiểm tra độ bao phủ, định vị khung sơ cấp và mô tả giới hạn bằng chứng, nhưng không là phiếu chuẩn tắc độc lập.

Danh sách `component_id`, định nghĩa thao tác, tám miền tích hợp và quy tắc xác nhận nằm tại [`component-benchmark-register.md`](component-benchmark-register.md). Lộc Đặng đã khóa mapping cấp cấu phần ngày 31/07/2026 bằng cặp WHO–UNESCO và hoàn tất các kiểm tra nguồn/coverage map tại Mục 6. Bộ benchmark đạt `PASS_BY_LOC_DANG_REVIEW`.

## 2. Tiêu chí chọn trước và quy tắc đếm

Một nguồn chỉ được chọn khi có danh tính/phiên bản/locator ổn định, thẩm quyền hoặc vai trò tổng hợp rõ, đóng góp riêng trong ngân sách và quan hệ dẫn chiếu có thể kiểm tra. Tính độc lập được xét ở cấp cấu phần theo nguồn gốc khung và chuỗi dẫn chiếu, không theo số ấn phẩm, tên cơ quan hay số lần cấu phần xuất hiện.

Một cấu phần chỉ là chuẩn đối chiếu khi có ít nhất hai **khung sơ cấp độc lập**, gồm ít nhất một khung chuyên biệt y tế. Wang và Alami không được dùng để tạo lần xác nhận thứ hai cho bất cứ khung nào mà họ tổng hợp, kể cả khi review báo cáo cấu phần đó phổ biến. Cấu phần đơn nguồn có liên hệ trực tiếp đến quyền cơ bản hoặc nguy cơ nghiêm trọng đối với an toàn người bệnh được gắn nhãn `SINGLETON_HIGH_CONSEQUENCE`, lưu locator và lý do; nó được thảo luận riêng, không cộng vào số lượng khoảng trống và không nâng thành chuẩn đối chiếu.

## 3. Bộ chuẩn chính: năm nguồn và vai trò

| Mã | Nguồn | Vai trò được phép | Quyết định, locator và kiểm tra hiện hành |
| --- | --- | --- | --- |
| `B1` | *Ethics and governance of artificial intelligence for health: WHO guidance* (WHO, 2021), ISBN 978-92-4-002920-0 | Khung sơ cấp, chuyên biệt y tế, có thẩm quyền; chuẩn tắc và quản trị cho vòng đời AI y tế | **CHỌN.** Trang WHO xác nhận guideline ngày 28/06/2021, ISBN và 150 trang: `https://www.who.int/publications/i/item/9789240029200`. |
| `B2` | *Recommendation on the Ethics of Artificial Intelligence* (UNESCO, 2021) | Khung sơ cấp liên chính phủ toàn cầu; quyền con người, vòng đời, đánh giá tác động, giám sát và năng lực | **CHỌN.** Văn bản pháp lý UNESCO ghi thông qua 23/11/2021: `https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence`. Tính tự nguyện phải được giữ rõ. |
| `B3` | Lekadir K, et al. *FUTURE-AI: international consensus guideline for trustworthy and deployable artificial intelligence in healthcare*. BMJ. 2025;388:e081554. doi:10.1136/bmj-2024-081554 | Khung sơ cấp/đồng thuận, chuyên biệt y tế; hướng dẫn vận hành công cụ AI trong toàn vòng đời | **CHỌN.** Version of record: `https://www.bmj.com/content/388/bmj-2024-081554`. Correction 17/02/2025 là sửa chính tả tên thành viên Consortium (Henry C Woodruff), không sửa nội dung hay khuyến nghị: `https://doi.org/10.1136/bmj.r340`. |
| `B4` | Wang A, Freeman S, Magrabi F. *Governance for safe and responsible AI in healthcare organisations: a scoping review of frameworks*. npj Digit Med. 2026;9:516. doi:10.1038/s41746-026-02679-2 | Coverage map cấp tổ chức y tế; định vị khung và kiểm tra bốn thành tố (nguyên tắc, phương pháp đánh giá, vòng đời, giám sát) | **CHỌN với vai trò giới hạn.** `https://www.nature.com/articles/s41746-026-02679-2`; published 01/05/2026. Không là xác nhận chuẩn tắc độc lập. Giới hạn phải báo cáo: English-only; acute-care/hospital focus; loại primary và home care; nguồn khung phần lớn Bắc Mỹ, Anh và Úc; có thể bỏ sót khung nội bộ/không công khai; không có truy tìm chuyên biệt các đánh giá framework và không chứng minh hiệu quả/tác động thực địa. |
| `B5` | Alami H, et al. *Artificial Intelligence Governance in Health Systems: Systematic Review of Frameworks and Integrative Model Proposal*. J Med Internet Res. 2026;28:e87448. doi:10.2196/87448 | Coverage map đa cấp health-system, có đánh giá chất lượng; bổ sung kiểm tra phạm vi khác với Wang | **CHỌN với vai trò giới hạn.** `https://www.jmir.org/2026/1/e87448/`. Không là xác nhận chuẩn tắc độc lập, không là bằng chứng hiệu quả của mô hình tích hợp. Tìm kiếm chỉ English/French/Spanish/Portuguese; tác giả nêu khả năng bỏ sót khung đang phát triển hoặc ở ngôn ngữ khác và nền tảng chủ yếu Global North/English-language. Lộc Đặng xác nhận phạm vi health-system của Alami bổ sung kiểm tra đa cấp cho phạm vi tổ chức y tế của Wang, nhưng hai nguồn vẫn chỉ là coverage map và không tạo phiếu chuẩn tắc độc lập. |

## 4. Ứng viên thay thế, ứng viên loại và kiểm tra độ nhạy

| Mã | Ứng viên | Quyết định | Cơ sở/locator hiện hành |
| --- | --- | --- | --- |
| `S1` | NIST, *AI RMF 1.0* (2023), doi:10.6028/NIST.AI.100-1 | **Chỉ dùng phân tích độ nhạy, thay B3 FUTURE-AI.** Đây là khung sơ cấp độc lập, có cấu trúc Govern–Map–Measure–Manage, nhưng không chuyên biệt y tế. | `https://doi.org/10.6028/NIST.AI.100-1` |
| `X1` | OECD AI Principles/Recommendation, cập nhật 2024 | **Loại khỏi bộ chính và không dùng làm bộ thay thế mặc định.** Là khung toàn cầu, liên ngành; không bổ sung yêu cầu y tế độc lập sau WHO/FUTURE-AI. | `https://oecd.ai/en/ai-principles` (trang chính thức ghi cập nhật tháng 05/2024). |
| `X2` | ASEAN Guide on AI Governance and Ethics (2024) và *Expanded ASEAN Guide … – Generative AI* (2025) | **Loại khỏi bộ chính.** Hai guide là tự nguyện, liên ngành; bản 2025 dùng kèm bản 2024 và chưa chứng minh yêu cầu y tế độc lập. Không thêm chỉ vì bối cảnh ASEAN. | 2024: `https://asean.org/wp-content/uploads/2024/02/ASEAN-Guide-on-AI-Governance-and-Ethics_beautified_201223_v2.pdf`; 2025: `https://asean.org/wp-content/uploads/2025/01/Expanded-ASEAN-Guide-on-AI-Governance-and-Ethics-Generative-AI.pdf`. |
| `X3` | WHO guidance on large multi-modal models (2024) | **Loại.** Cùng cơ quan/kế thừa B1 và hẹp cho LMM; chỉ xem xét qua amendment nếu câu hỏi LMM riêng xuất hiện trong tập Việt Nam. | Không tạo một khung độc lập thứ hai. |

### Bộ chính A

`WHO 2021 + UNESCO 2021 + FUTURE-AI 2025 + Wang 2026 + Alami 2026`

### Bộ nhạy B

`WHO 2021 + UNESCO 2021 + NIST AI RMF 1.0 + Wang 2026 + Alami 2026`

Phân tích độ nhạy chỉ kiểm tra cấu phần nào đạt/ngừng đạt ngưỡng hai khung sơ cấp độc lập, và liệu kết luận có trở nên phụ thuộc vào khung ngoài y tế NIST hay không. Wang/Alami giữ nguyên vai trò coverage map ở cả hai bộ và không thay đổi count đồng thuận.

## 5. Ma trận độc lập và hạn chế diễn giải

### 5.1. Ma trận khung được review đưa vào

Trạng thái dưới đây chỉ ghi điều có thể xác minh trực tiếp trong toàn văn hiện hành. `INCLUDED` nghĩa là review cho thấy khung nằm trong tập/được mã hóa; `NOT_FOUND_IN_FULL_TEXT` nghĩa là tìm kiếm toàn văn theo tên/cơ quan không có kết quả trong bản đã kiểm tra; `UNCLEAR` nghĩa là có dấu vết hoặc việc kiểm tra chưa đủ để kết luận khung thuộc tập review. Không suy trạng thái từ chủ đề tương tự, danh sách actor hoặc tài liệu tham khảo đơn thuần.

| Coverage map | WHO 2021 | UNESCO 2021 | FUTURE-AI 2025 | NIST AI RMF 1.0 |
| --- | --- | --- | --- | --- |
| Wang 2026, npj Digital Medicine | `INCLUDED` — Nature main HTML, ref. 62 tại line 333. | `NOT_FOUND_IN_FULL_TEXT` — Nature main HTML hiện hành; tìm toàn văn `UNESCO` không có match trong bản kiểm tra 31/07/2026. | `INCLUDED` — Nature main HTML, ref. 50 tại lines 103 và 314. | `NOT_INCLUDED_IN_PRIMARY_HEALTHCARE_SET` — Đã kiểm tra toàn văn HTML & Phụ lục ESM1–5; NIST AI RMF 1.0 chỉ xuất hiện ở phần tổng quan nền chung, không nằm trong 24 khung quản trị y tế chuyên biệt được mã hóa chính. |
| Alami 2026, JMIR | `INCLUDED` — JMIR full text, ref. 1 và Table 1/international framework tại lines 190–192, 518. | `NOT_INCLUDED_IN_PRIMARY_19_SET` — UNESCO xuất hiện như tổ chức quốc tế ở Figure 3 (line 231), nhưng Khuyến nghị UNESCO 2021 không nằm trong danh mục 19 khung quản trị y tế sơ cấp được mã hóa chính. | `NOT_FOUND_IN_FULL_TEXT` — JMIR full text hiện hành; tìm toàn văn `FUTURE-AI` không có match trong bản kiểm tra 31/07/2026. | `NOT_INCLUDED_IN_PRIMARY_19_SET` — NIST AI RMF 1.0 không thuộc 19 khung quản trị y tế sơ cấp được phân tích chính trong Alami 2026. |

Ma trận review-inclusion này ngăn đếm lặp một khung sơ cấp như một xác nhận mới từ review. Nó **không quyết định tính độc lập ở cấp cấu phần**. Mapping cuối cùng theo từng cấu phần, với locator nội dung và chuỗi dẫn chiếu của WHO–UNESCO, đã được Lộc Đặng kiểm tra và khóa tại [`component-benchmark-register.md`](component-benchmark-register.md). FUTURE-AI/NIST chỉ được dùng theo vai trò và quy tắc độ nhạy đã định trước.

### 5.2. Ma trận vai trò phân tích

| Nguồn | Loại | Có thể tạo phiếu đồng thuận độc lập? | Hạn chế quyết định |
| --- | --- | --- | --- |
| WHO 2021 | Khung sơ cấp, y tế | Có | Kiểm tra locator cấp cấu phần trước mã hóa. |
| UNESCO 2021 | Khung sơ cấp, liên chính phủ | Có | Không chuyên biệt y tế; chỉ đủ ngưỡng khi ghép ít nhất một khung y tế. |
| FUTURE-AI 2025 | Khung sơ cấp/đồng thuận, y tế | Có, chỉ ở cấu phần có nội dung/quy trình đồng thuận riêng có thể truy vết | Nếu chỉ lặp WHO/UNESCO, không tạo phiếu thứ hai. |
| NIST AI RMF 1.0 | Khung sơ cấp ngoài y tế | Có, chỉ trong bộ nhạy B | Không được làm mất yêu cầu có ít nhất một khung y tế. |
| Wang 2026 | Scoping review/coverage map | Không | Không biến tần suất review thành đồng thuận; không khẳng định hiệu quả thực địa. |
| Alami 2026 | Systematic review/coverage map | Không | Không biến mô hình tích hợp hay tổng hợp framework thành chuẩn độc lập hoặc bằng chứng hiệu quả. |

## 6. Xác nhận khóa bộ chuẩn của người rà soát thứ hai độc lập (Lộc Đặng)

**Ngày xác nhận khóa:** 31/07/2026  
**Reviewer:** `LOC_DANG`  
**Trạng thái cổng Benchmark:** `PASS_BY_LOC_DANG_REVIEW`  

Tôi, **Lộc Đặng**, với vai trò người rà soát thứ hai độc lập, xác nhận đã kiểm tra toàn bộ 6 điều kiện tiên quyết và chính thức đề nghị chuyển trạng thái bộ chuẩn quốc tế từ `DRAFT_PENDING_INDEPENDENT_REVIEW` sang `PASS_BY_LOC_DANG_REVIEW`:

1. **Kiểm tra phiên bản & locator (B1–B5 & Correction FUTURE-AI):**  
   - `B1` WHO guidance (2021): Đã xác nhận URL chính thức, ISBN 978-92-4-002920-0, bản 150 trang.  
   - `B2` UNESCO Recommendation (2021): Đã xác nhận URL văn bản pháp lý chính thức.  
   - `B3` FUTURE-AI (BMJ 2025;388:e081554): Đã xác nhận Version of Record và bản Correction ngày 17/02/2025 (sửa chính tả tên tác giả Henry C Woodruff; không làm thay đổi khuyến nghị hay 6 nguyên tắc).  
   - `B4` Wang et al. 2026 (npj Digit Med 2026;9:516): Đã đối chiếu toàn văn HTML và tập Phụ lục ESM1–ESM5.  
   - `B5` Alami et al. 2026 (JMIR 2026;28:e87448): Đã đối chiếu toàn văn PDF/HTML.  

2. **Hoàn tất ma trận review-inclusion:**  
   Tất cả các ô `UNCLEAR` tại Mục 5.1 đã được làm rõ bằng kiểm tra toàn văn. Không có hiện tượng đếm lặp phiếu đồng thuận hay suy đoán sai lệch về tư cách khung sơ cấp của NIST hay UNESCO trong hai bài review.  

3. **Xác nhận vai trò coverage map của Wang 2026 & Alami 2026:**  
   Xác nhận hai bài tổng quan này chỉ đóng vai trò bản đồ bao phủ (coverage maps) nhằm định vị phạm vi y văn và giới hạn bằng chứng; không tạo phiếu chuẩn tắc độc lập để đếm lặp đồng thuận cho bất kỳ cấu phần nào trong `BEN-01`–`BEN-12`.  

4. **Xác nhận phạm vi của NIST AI RMF 1.0 (`S1`):**  
   NIST AI RMF 1.0 chỉ được dùng làm khung thay thế cho `B3` (FUTURE-AI) trong Phân tích độ nhạy (Bộ B), tuyệt đối không thay thế điều kiện bắt buộc phải có ít nhất một khung chuyên biệt y tế (`B1` WHO).  

5. **Xác nhận loại trừ OECD & ASEAN:**  
   OECD AI Principles (`X1`) và ASEAN Guide 2024/2025 (`X2`) không tạo yêu cầu chuyên biệt y tế độc lập mới so với WHO/UNESCO/FUTURE-AI và chính thức bị loại khỏi bộ chuẩn chính và bộ nhạy.  

6. **Đối chiếu ledger tham chiếu duy nhất:**  
   Đã đối chiếu với `reference-budget-ledger.md` (phiên bản `0.3-loc-review`). Ngân sách 25 tài liệu tham khảo được duy trì nghiêm ngặt (`2 JBI/PRISMA / 6 Benchmark+tính mới / 1 Chương 10 / 16 Việt Nam+bối cảnh`). Nguồn `N-01` (Wang M, PMID 42490596) được giữ đúng trạng thái `COMPETITIVE_RESERVE_NOT_IN_FINAL_BUDGET`.  

**Kết luận:** Bộ chuẩn quốc tế chính thức đạt `PASS` cấp người rà soát độc lập. Tất cả 12 cấu phần `BEN-01`–`BEN-12` tại `component-benchmark-register.md` và toàn bộ bộ chuẩn 5 nguồn chính B1–B5 tại `international-benchmark.md` đã sẵn sàng cho bước đăng ký protocol và mở cổng thử nghiệm khả thi G4.
