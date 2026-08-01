# Lượt chạy hủy ở bước gọi CLI

**Trạng thái:** `ABORTED_BEFORE_ANY_SEARCH_REQUEST`.

Python runtime cô lập không có npm shim Firecrawl trên `PATH`. Lượt này dừng trước khi gửi truy vấn đầu tiên và không chứa dữ liệu nguồn. Runner được hiệu chỉnh để gọi shim Windows theo đường dẫn tuyệt đối ở các lượt sau.
