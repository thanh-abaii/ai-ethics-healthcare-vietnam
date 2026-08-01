# Xác nhận hoàn tất hiệu chuẩn sàng lọc và trích xuất

## Trạng thái

`PASS_BY_PRINCIPAL_INVESTIGATOR_ATTESTATION`

## Thông tin kiểm soát

- Ngày hiệu chuẩn được ghi nhận: **31/07/2026**
- Người rà soát thứ hai: **Lộc Đặng**
- Người chủ trì ghi nhận: **Đào Trung Thành**
- Protocol: `0.3-pre-registration`
- Codebook áp dụng: `screening-codebook.md`, `data-extraction-codebook.md`, `record-registry-codebook.md`
- Nguồn xác nhận: chủ trì xác nhận trong task Codex ngày 31/07/2026 rằng đã có hiệu chuẩn từ Lộc.

## Phạm vi hiệu chuẩn được xác nhận

Theo xác nhận của chủ trì, hiệu chuẩn đã bao phủ đủ ba vòng bắt buộc:

| Vòng | Cỡ mẫu theo protocol | Kết quả được ghi nhận |
| --- | ---: | --- |
| Tiêu đề/tóm tắt | 25 record | Đạt ngưỡng đồng thuận ban đầu tối thiểu 75%; bất đồng đã được thảo luận và ghi nhận. |
| Toàn văn | 8 document đa dạng | Đạt ngưỡng đồng thuận ban đầu tối thiểu 75%; bất đồng đã được xử lý. |
| Trích xuất | 8 document đa dạng | Các trường phân loại không rỗng đạt ngưỡng đồng thuận tối thiểu 75%; locator và bất đồng đã được kiểm tra. |

Không dùng kappa làm hard gate. Không có quyết định hiệu chuẩn nào được nhập vào corpus, count PRISMA, G4–G5 hoặc quyết định đủ điều kiện chính thức.

## Kết luận gate

`SCREENING_EXTRACTION_CODEBOOK_GATE=PASS`

Kết luận dựa trên xác nhận của chủ trì rằng:

1. hai người đã sử dụng cùng phiên bản codebook và biểu mẫu;
2. ba vòng hiệu chuẩn đều đạt ngưỡng protocol;
3. mọi bất đồng đã được xử lý;
4. không còn thay đổi codebook có khả năng ảnh hưởng quyết định mà chưa hiệu chuẩn lại;
5. nhánh quy nạp của Lộc vẫn được giữ tách khỏi mã Chương 10.

## Giới hạn audit

Tại thời điểm lập tài liệu này, hồ sơ chưa có bảng quyết định thô theo từng record/document, phép tính tỷ lệ đồng thuận, random seed của mẫu tiêu đề/tóm tắt hoặc version log của từng vòng. Vì vậy:

- không báo cáo một tỷ lệ cụ thể cao hơn ngưỡng 75%;
- không tuyên bố đã kiểm tra độc lập từng quyết định;
- trước nộp bài hoặc khi có yêu cầu audit, phải bổ sung bảng hiệu chuẩn thô hoặc locator tới bằng chứng gốc;
- nếu bằng chứng gốc sau này cho thấy một vòng không đạt hoặc còn bất đồng chưa xử lý, gate phải được đặt lại `NOT_RUN` và hiệu chuẩn lại.

## Xác nhận của chủ trì

Đào Trung Thành yêu cầu xem hiệu chuẩn của Lộc là đã hoàn tất và đạt yêu cầu protocol ngày **31/07/2026**.
