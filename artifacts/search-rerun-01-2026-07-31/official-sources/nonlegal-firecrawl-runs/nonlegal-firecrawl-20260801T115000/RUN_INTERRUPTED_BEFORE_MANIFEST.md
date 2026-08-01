# Lượt Firecrawl bị ngắt trước manifest terminal

**Trạng thái:** `INTERRUPTED_NOT_A_COMPLETE_SEARCH_RUN`.

Lượt này bị hủy bởi giới hạn thời gian của môi trường trong khi đang scrape các
URL nguồn. Vì chưa có manifest, ledger tổng và checksum inventory, mọi raw file
trong thư mục chỉ được giữ để kiểm toán lỗi; không được dùng cho corpus, G6,
G7 hay screening.
