# Competitive checkpoint trước khóa protocol

## Kiểm soát

| Trường | Giá trị |
| --- | --- |
| Mốc protocol | Trước khóa protocol |
| Ngày, múi giờ | 31/07/2026, Asia/Saigon (UTC+7) |
| Protocol áp dụng | `0.3-pre-registration` |
| Người thực hiện | Chủ trì, Đào Trung Thành |
| Kết quả | `PASS_WITH_NARROWED_CLAIM` |

Checkpoint này là kiểm tra cạnh tranh, không phải lượt tìm kiếm của tổng quan, không tạo corpus, count PRISMA, quyết định đủ điều kiện hay thay đổi benchmark.

## Đối tượng và đường truy vết đã kiểm tra

| Đối tượng | Đường truy vết | Kết quả |
| --- | --- | --- |
| Wang M et al., *Mapping National Governance of AI for Health* | Tiêu đề chính xác; PMID `42490596`; DOI `10.2196/88970`; tên tác giả; PROSPERO `CRD420251234461` | Tìm thấy protocol đã công bố ngày 23/07/2026 trên *JMIR Research Protocols*; chưa tìm thấy bài kết quả, preprint kết quả, dataset/supplement công khai hay output thứ hai trả lời kết quả Việt Nam. |
| Cited-by/bài kết quả | PubMed record, truy vấn tiêu đề/DOI/PMID và trang bài | Không có kết quả riêng cho Việt Nam được xác minh tại ngày checkpoint. |
| Comparator đã khóa | Wang A 2026, Alami 2026, Hussein 2026, Tran 2022, Vuong 2025, Tun 2025 | Không có output mới được xác minh làm thay đổi đánh giá substantial answer trong `novelty-audit.md`. |

## Quyết định của chủ trì

Protocol Wang M xác nhận rủi ro cạnh tranh phương pháp là hiện hữu: phạm vi toàn cầu của họ bao gồm công cụ chính sách quốc gia và nguồn hỗ trợ theo quốc gia, với bốn chiều ethics, regulation, implementation và operations. Tuy vậy, tại ngày checkpoint, đó vẫn là **protocol**: không có kết quả công bố riêng cho Việt Nam để trả lời phần lớn câu hỏi của nghiên cứu này.

Do đó G3 được giữ ở `PASS_WITH_NARROWED_CLAIM`, chỉ với tuyên bố đóng góp đã khóa trong §4.4 của protocol. Nghiên cứu không được tự nhận đã tạo một schema mới, không được hạ thấp mức overlap phương pháp, và không được suy diễn rằng Wang M không thể có kết quả Việt Nam sau này.

## Điều kiện đặt lại

G3 phải chuyển `FAIL` và kích hoạt `REFRAME` nếu, tại một checkpoint tiếp theo, output của Wang M hoặc comparator khác trả lời phần lớn câu hỏi về Việt Nam hoặc khiến đóng góp còn lại không đủ quan trọng cho một bài riêng. Các checkpoint còn lại giữ nguyên: trước G4–G5, khi đóng tìm kiếm và trước nộp bài.

## Locator công khai

- PubMed: <https://pubmed.ncbi.nlm.nih.gov/42490596/>
- DOI: <https://doi.org/10.2196/88970>
- PROSPERO: `CRD420251234461` (được truy vấn theo mã; không dùng một locator không xác minh để suy tình trạng đăng ký).
