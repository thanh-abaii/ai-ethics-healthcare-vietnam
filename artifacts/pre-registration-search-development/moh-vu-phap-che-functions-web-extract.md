# Vụ Pháp chế Bộ Y tế — snapshot dẫn xuất để xác minh chức năng

- Ngày truy cập: 31/07/2026
- Trang chức năng chính thức: https://vuphapche.moh.gov.vn/pages/news/16411/Chuc-nang-nhiem-vu.html
- Tài liệu gốc được trang trên dẫn chiếu: Quyết định số 3628/QĐ-BYT ngày 24/11/2025, *Quy định chức năng, nhiệm vụ, quyền hạn và cơ cấu tổ chức của Vụ Pháp chế thuộc Bộ Y tế*
- Locator tài liệu trên hệ thống Bộ Y tế: https://emohbackup.moh.gov.vn/publish/attach/getfile/413436
- Trạng thái snapshot: `DERIVED_WEB_EXTRACT_WITH_DIRECT_ACCESS_ERROR`

## Đoạn xác minh

Trang chính thức mô tả Vụ Pháp chế là đơn vị thuộc Bộ Y tế, có chức năng tham mưu, giúp Bộ trưởng thực hiện quản lý nhà nước bằng pháp luật đối với các lĩnh vực thuộc phạm vi quản lý nhà nước của Bộ Y tế và tổ chức thực hiện công tác pháp chế theo quy định của pháp luật.

Kết quả trích xuất tài liệu được bộ máy tìm kiếm ghi nhận cho thấy Quyết định 3628/QĐ-BYT bao gồm nhiệm vụ xây dựng pháp luật, hướng dẫn lập và điều chỉnh chương trình xây dựng văn bản quy phạm pháp luật, tổng hợp trình ban hành, và đôn đốc việc thực hiện chương trình sau khi được cấp có thẩm quyền thông qua.

## Giới hạn kỹ thuật

Trong lần lưu ngày 31/07/2026, trang chức năng trả lỗi máy chủ do transaction log của cơ sở dữ liệu đầy; endpoint tài liệu dự phòng có lỗi chứng thư TLS và không trả được PDF hợp lệ khi thử lại. Vì vậy đây là snapshot văn bản dẫn xuất từ nội dung trang/tài liệu chính thức đã được công cụ tìm kiếm lập chỉ mục, không phải bản PDF gốc. Vị trí của Vụ Pháp chế trong cơ cấu Bộ Y tế được đối chiếu độc lập bằng bản Công báo Nghị định 42/2025/NĐ-CP lưu cùng thư mục. Full run phải thử tải lại tài liệu gốc và thay snapshot dẫn xuất bằng raw PDF qua amendment/log nếu thành công.
