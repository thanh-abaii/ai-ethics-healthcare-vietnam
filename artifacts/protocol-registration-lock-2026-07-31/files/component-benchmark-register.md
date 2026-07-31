# Sổ đăng ký cấu phần benchmark quốc tế

## Trạng thái và ranh giới

| Trường | Giá trị |
| --- | --- |
| Phiên bản | `0.2-loc-component-lock` |
| Protocol áp dụng | `0.4-pre-registration` |
| Người lập | Đào Trung Thành, chủ trì |
| Trạng thái | `LOCKED_BY_LOC_DANG_AT_COMPONENT_LEVEL` |

Sổ này khóa đơn vị phân tích trước khi xem corpus Việt Nam. Nó không gán trạng thái cho Việt Nam. Ngày 31/07/2026, Lộc Đặng đã xác nhận độc lập locator và quan hệ độc lập của hai framework sơ cấp cho từng cấu phần; WHO là khung chuyên biệt y tế trong mọi cặp. Khóa cấu phần này không tự chuyển trạng thái aggregate của Việt Nam, không tạo gap count và không thay thế các kiểm tra còn lại của bộ benchmark ở cấp nguồn/coverage map.

## Tám miền và cấu phần

| Miền tích hợp | `component_id` | Cấu phần cần có | Bằng chứng tối thiểu khi chart nguồn Việt Nam |
| --- | --- | --- | --- |
| Mục tiêu, quyền và công bằng | `BEN-01` | Mục đích hợp pháp, lợi ích công/cho người bệnh và giới hạn use case | Mục đích, đối tượng chịu ảnh hưởng, phạm vi AI và căn cứ áp dụng. |
| Mục tiêu, quyền và công bằng | `BEN-02` | Tự chủ, thông báo, đồng ý/lựa chọn từ chối và quyền yêu cầu người xem xét lại | Quyền cụ thể và cơ chế thực hiện. |
| Mục tiêu, quyền và công bằng | `BEN-03` | Công bằng, không phân biệt đối xử và tiếp cận công bằng | Đối tượng rủi ro, kiểm tra/chỉ số hoặc biện pháp giảm thiểu. |
| An toàn và giá trị lâm sàng | `BEN-04` | Thẩm định trước sử dụng theo bối cảnh lâm sàng và intended use | Đầu mối phê duyệt, validation và giới hạn sử dụng. |
| An toàn và giá trị lâm sàng | `BEN-05` | Giám sát con người, quyền dừng và xử lý khi hệ thống không an toàn | Chủ thể có thẩm quyền, trigger dừng và hành động an toàn. |
| Dữ liệu, riêng tư và an ninh | `BEN-06` | Quản trị dữ liệu, riêng tư, bảo mật và quản lý truy cập/vòng đời dữ liệu | Quy tắc dữ liệu, control và hồ sơ kiểm chứng. |
| Minh bạch và khả năng giải thích | `BEN-07` | Minh bạch về hệ thống, giới hạn, thông tin cho người dùng và khả năng giải thích phù hợp | Đối tượng nhận thông tin, nội dung và bằng chứng lưu vết. |
| Trách nhiệm và bảo đảm | `BEN-08` | Actor, quyền quyết định, trách nhiệm giải trình và quản lý xung đột | Chủ thể, quyền phê duyệt/dừng/khiếu nại và hồ sơ quyết định. |
| Trách nhiệm và bảo đảm | `BEN-09` | Đánh giá tác động/rủi ro, audit độc lập hoặc assurance theo vòng đời | Phương pháp, tần suất, chủ thể đánh giá và audit record. |
| Vận hành vòng đời | `BEN-10` | Quản lý thay đổi, theo dõi sau triển khai, drift/sự cố và khắc phục | Chỉ số/log/sự cố, owner, ngưỡng hành động và remedial record. |
| Năng lực và tham gia | `BEN-11` | Năng lực nhân sự, đào tạo, nguồn lực và phối hợp liên ngành | Yêu cầu năng lực, nguồn lực, cơ chế hội đồng hoặc đào tạo. |
| Năng lực và tham gia | `BEN-12` | Sự tham gia của người bệnh/cộng đồng và cơ chế khiếu nại–khắc phục | Cách tham gia, kênh khiếu nại, biện pháp khắc phục và locator. |

Các cấu phần chỉ được aggregate theo `component_id × scope_id`. `BEN-04` không suy ra `BEN-05`; `BEN-08` không suy ra `BEN-09`; văn bản thành lập hội đồng không tự chứng minh `BEN-10` hay `BEN-12`.

## Quy tắc xác nhận benchmark

1. Mỗi cấu phần cần hai mapping có locator nội dung từ framework sơ cấp độc lập; ít nhất một mapping phải từ WHO hoặc FUTURE-AI.
2. UNESCO có thể là framework sơ cấp thứ hai, nhưng không đủ một mình để tạo cấu phần chuyên biệt y tế.
3. Wang 2026 và Alami 2026 chỉ kiểm tra độ bao phủ; không là phiếu xác nhận độc lập.
4. Một yêu cầu đơn nguồn liên quan trực tiếp quyền cơ bản hoặc an toàn người bệnh ghi `SINGLETON_HIGH_CONSEQUENCE`; không đi vào gap count.
5. NIST chỉ được dùng trong bộ nhạy B và không thay điều kiện có ít nhất một framework y tế.

## Phiếu xác nhận reviewer độc lập — Lộc Đặng

**Ngày khóa:** 31/07/2026  
**Reviewer:** `LOC_DANG`  
**Nguồn kiểm tra:** WHO *Ethics and governance of artificial intelligence for health* (2021), bản PDF 150 trang lưu trong artifact; UNESCO *Recommendation on the Ethics of Artificial Intelligence* (2021), bản Legal Affairs lưu trong artifact.  
**Độc lập:** WHO và UNESCO là hai khung sơ cấp do hai tổ chức khác nhau ban hành. Không dùng Wang/Alami làm phiếu đồng thuận; không dùng số lần một review nhắc lại khung để tạo nguồn độc lập thứ hai. WHO là nguồn chuyên biệt y tế cho toàn bộ các cấu phần dưới đây.

| `component_id` | Locator WHO 2021 (khung y tế) | Locator UNESCO 2021 (khung sơ cấp độc lập) | Kết quả Lộc | Ghi chú kiểm tra |
| --- | --- | --- | --- | --- |
| `BEN-01` | tr. 11–16: lợi ích cho người bệnh/cộng đồng, lợi ích công và mục đích sử dụng có trách nhiệm | §I.1 và §II: nhân phẩm, phúc lợi con người và đánh giá/định hướng việc chấp nhận hay từ chối AI | `CONFIRM` | Cả hai xác nhận đích sử dụng hướng tới con người và giới hạn theo mục tiêu chính đáng. |
| `BEN-02` | tr. 6: con người phải giữ quyền kiểm soát hệ thống y tế và quyết định y khoa | §III.30, *Human oversight and determination* | `CONFIRM` | Có nguồn y tế và nguồn quyền con người độc lập cho tự chủ/giám sát người. |
| `BEN-03` | tr. 29: inclusiveness, equitable access và đánh giá với người chịu ảnh hưởng | §III.27, *Fairness and non-discrimination* | `CONFIRM` | Không suy công bằng từ chỉ số hiệu năng; cần bằng chứng về nhóm rủi ro/biện pháp khi chart nguồn Việt Nam. |
| `BEN-04` | tr. 13: an toàn, chính xác, hiệu lực theo use case/indication xác định | §III.24 và §III.26: proportionality/do no harm; safety and security | `CONFIRM` | Thẩm định phải theo intended use và bối cảnh; không đánh đồng với giám sát sau triển khai. |
| `BEN-05` | tr. 6; tr. 28: quyền kiểm soát của con người và các điểm giám sát | §III.30, *Human oversight and determination* | `CONFIRM` | Giữ riêng actor có quyền dừng, trigger và hành động an toàn. |
| `BEN-06` | tr. 27: minh bạch tài liệu hóa thuộc tính dữ liệu; tr. 32: chất lượng/sẵn có dữ liệu và rủi ro | §III.29, *Right to privacy and data protection* | `CONFIRM` | Mapping bao gồm quản trị dữ liệu, riêng tư, bảo mật và vòng đời; không chỉ là công bố privacy policy. |
| `BEN-07` | tr. 13; tr. 27: transparency, explainability, intelligibility; thông tin trước và sau triển khai | §III.31, *Transparency and explainability* | `CONFIRM` | Thông tin phải phù hợp chủ thể nhận, giới hạn hệ thống và có thể lưu vết. |
| `BEN-08` | tr. 28; tr. 44: trách nhiệm của stakeholder, human warranty và supervision | §III.32, *Responsibility and accountability* | `CONFIRM` | Phân biệt phân công trách nhiệm với assurance/audit tại `BEN-09`. |
| `BEN-09` | tr. 72–74: impact assessment, đánh giá độc lập trước/sau và công bố | §IV, *Ethical Impact Assessment* | `CONFIRM` | Cả hai yêu cầu hoạt động đánh giá/assurance theo vòng đời; không dùng review để tạo phiếu thứ hai. |
| `BEN-10` | tr. 14: đánh giá liên tục, có hệ thống và minh bạch trong khi sử dụng thực tế | §I.2(b): vòng đời gồm maintenance, operation, monitoring, evaluation và termination | `CONFIRM` | Drift/sự cố/khắc phục cần có owner, ngưỡng hành động và hồ sơ riêng; không suy từ văn bản thành lập. |
| `BEN-11` | tr. 11; tr. 72: điều kiện dùng an toàn, giáo dục/đào tạo liên tục cho nhân sự y tế | §III.33, *Awareness and literacy* | `CONFIRM` | Năng lực bao gồm nguồn lực, đào tạo và phối hợp; không suy từ một khóa tập huấn đơn lẻ. |
| `BEN-12` | tr. 28–29: patients/clinicians tham gia development/deployment; đa dạng người chịu ảnh hưởng | §III.34, *Multi-stakeholder and adaptive governance* | `CONFIRM` | Khi chart phải phân biệt sự tham gia với kênh khiếu nại và biện pháp khắc phục thực tế. |

Lộc không mở hoặc dùng `chapter10_only_code` trong lần xác nhận này. Các mapping là benchmark xác định trước từ hai khung sơ cấp, không phải mã quy nạp từ corpus Việt Nam.

## Hệ quả trạng thái

Mười hai cấu phần `BEN-01`–`BEN-12` đã được khóa để dùng làm đơn vị đối chiếu khi protocol được đăng ký và pilot được phép mở. `SINGLETON_HIGH_CONSEQUENCE=0`; không có cấu phần nào chỉ có một nguồn sơ cấp trong mapping này. `international-benchmark.md` vẫn phải giữ và hoàn tất các kiểm tra ở cấp bộ nguồn — version/locator B3–B5, correction FUTURE-AI, ma trận review-inclusion, vai trò coverage map và ledger 25 tài liệu — trước khi toàn bộ benchmark có thể chuyển `PASS` cho mục đích đăng ký.
