# Thu hồi lượt Firecrawl dùng khóa kế thừa không hợp lệ

**Trạng thái:** `RETRACTED_BEFORE_VALID_SEARCH_EXECUTION`.

Tất cả 120 lệnh search trong lượt này bị Firecrawl từ chối với `Unauthorized:
Invalid token`; stdout rỗng và không có URL nguồn. Nguyên nhân là runner dùng
khóa môi trường kế thừa thay vì ghi đè bằng `FIRECRAWL_API_KEY` mới trong `.env`
của dự án. Lượt này chỉ được giữ để kiểm toán lỗi; không là bằng chứng tìm kiếm.
