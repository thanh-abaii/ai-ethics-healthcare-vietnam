# Deviation truy hồi VBPL qua IPv4

**Trạng thái:** `RETRIEVAL_TIMEOUT_NO_RAW_RESPONSE`  
**Ngày:** 31/07/2026  
**Locator:** `https://vbpl.vn/TW/Pages/vbpq-van-ban-goc.aspx?ItemID=175587`

Sau direct HTTP/curl mặc định và truy hồi dự phòng qua trình duyệt, một lượt truy hồi mới dùng `curl --ipv4 --http1.1 --tlsv1.2` cũng timeout (exit 28) trước khi nhận body hoặc header.

Artefact: `official-sources/legal-relation-55-2025-ndcp-ipv4-20260731T213800+0700/` gồm request, body/header rỗng, stderr, checksum và capture manifest. Kiểm tra script parse thành công; checksum của mỗi artifact được ghi trong manifest.

Sự kiện chỉ củng cố kết luận kỹ thuật rằng chưa thu hồi được raw source từ locator VBPL trong môi trường này. Nó không xác nhận nội dung, hiệu lực, quan hệ văn bản hoặc sự vắng mặt của nguồn.
