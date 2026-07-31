# Ledger tham chiếu duy nhất và ngân sách 25 nguồn

## 1. Kiểm soát

| Trường | Giá trị |
| --- | --- |
| `ledger_version` | `0.3-loc-review` |
| Ngày lập | 31/07/2026 |
| Trạng thái | `PASS_BY_LOC_DANG_REVIEW` |
| Quy tắc đơn vị | Một `reference_id` chỉ chiếm một slot, dù được dùng tại nhiều phần của bài. |

Ledger này là nguồn kiểm soát chung cho G6. Nó không chứng minh nguồn Việt Nam cuối cùng đã đủ điều kiện; các slot `VN-01`–`VN-16` chỉ là sức chứa đã khóa trước sàng lọc. Không dùng nguồn nền hoặc loại nguồn hậu nghiệm để lấp/giảm slot.

## 2. Ngân sách và tham chiếu đã định danh

| Nhóm chính | Slot | `reference_id` | Nguồn/ vai trò | Trạng thái |
| --- | ---: | --- | --- | --- |
| Phương pháp JBI/PRISMA-ScR | 1/2 | `M-01` | JBI methodology cho scoping review | Cần khóa bản trích dẫn NLM trước G6 |
| Phương pháp JBI/PRISMA-ScR | 2/2 | `M-02` | PRISMA-ScR statement | Cần khóa bản trích dẫn NLM trước G6 |
| Benchmark+tính mới | 1/6 | `B1` | WHO 2021 | Chọn, locator đã kiểm tra |
| Benchmark+tính mới | 2/6 | `B2` | UNESCO 2021 | Chọn, locator đã kiểm tra |
| Benchmark+tính mới | 3/6 | `B3` | FUTURE-AI 2025 | Chọn, locator/correction đã kiểm tra |
| Benchmark+tính mới | 4/6 | `B4` | Wang, Freeman, Magrabi 2026 npj Digital Medicine; coverage map | Chọn, locator đã kiểm tra |
| Benchmark+tính mới | 5/6 | `B5` | Alami et al. 2026 JMIR; coverage map | Chọn, locator đã kiểm tra |
| Benchmark+tính mới | 6/6 | `S1` | NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*; sensitivity thay FUTURE-AI | Chọn cho phân tích độ nhạy; cần citation riêng dù không thuộc bộ chính A |
| Chương 10 | 1/1 | `C10-01` | Đào Trung Thành, *Đạo đức AI: Nguyên tắc và Thực hành*, Chương 10 | Chọn; chỉ là lăng kính khái niệm, không tự xác nhận kết quả |
| Việt Nam/bối cảnh trực tiếp | 1–16/16 | `VN-01` … `VN-16` | Các nguồn Việt Nam đủ điều kiện và nguồn bối cảnh trực tiếp theo protocol | Chưa sàng lọc; không được vượt 16 mà không RESCOPE/phụ lục/đổi tạp chí |
| **Tổng** | **25/25** |  |  |  |

## 3. Quy tắc dùng và kiểm tra G6

1. B1–B5 là năm nguồn chính duy nhất của benchmark. NIST có citation slot thứ sáu vì phân tích độ nhạy phải dẫn chính nguồn NIST, dù NIST chỉ thay B3 trong bộ nhạy và không làm bộ chính A vượt năm nguồn. OECD và ASEAN không có slot.
2. Wang và Alami có một slot mỗi nguồn vì vai trò coverage map/tính mới; không được nhân đôi dưới “benchmark” và “novelty”, cũng không tạo phiếu đồng thuận độc lập.
3. Wang M et al., *Mapping National Governance of AI for Health* (PMID 42490596), mang mã `N-01`, là `COMPETITIVE_RESERVE_NOT_IN_FINAL_BUDGET`; nguồn này nằm ngoài count 25 ở phiên bản hiện hành. Nếu cần dẫn trong bản cuối, nó phải thay một slot benchmark/tính mới khác hoặc kích hoạt `RESCOPE`, không được trở thành nguồn thứ 26.
4. Nếu output kết quả của `N-01` làm đóng góp còn lại không đủ quan trọng, G3=`FAIL`/`REFRAME`, thay vì thay comparator hậu nghiệm.
5. Trước G6=`PASS`, reviewer phải thêm citation NLM chuẩn, locator, ngày kiểm tra và quyết định `include/final-reserve/exclude` cho mọi `reference_id` được tính, rồi kiểm tra `COUNT(DISTINCT reference_id)=25` và tổng từng nhóm là `2/6/1/16`.

## 4. Competitive reserve ngoài ngân sách cuối

| `reference_id` | Nguồn | Trạng thái ngân sách | Quy tắc kích hoạt |
| --- | --- | --- | --- |
| `N-01` | Wang M et al., *Mapping National Governance of AI for Health*, PMID 42490596 | `COMPETITIVE_RESERVE_NOT_IN_FINAL_BUDGET` | Nếu cần trích dẫn trong bản cuối: thay một slot benchmark/tính mới hiện có hoặc `RESCOPE`; vẫn phải giữ tổng tối đa 25. |
