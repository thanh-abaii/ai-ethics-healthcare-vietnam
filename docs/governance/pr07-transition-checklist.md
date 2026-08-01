# Checklist chuyển trạng thái theo sửa đổi hậu đăng ký hợp nhất v1

- [x] Đào Trung Thành phê duyệt `post-registration-amendment-consolidated-v1.md`.
- [x] Bản hợp nhất được tải lên/công bố tại OSF `62b8w`; URL `https://osf.io/4qzxn/files/2cakm`, hiệu lực 2026-08-01.
- [x] Lập đặc tả vận hành hữu hạn cho 16 slot: `pr07-public-source-retrieval-operational-spec-v1.md`; chờ PI rà soát trước retrieval.
- [ ] Tạo tối đa 16 record theo `pr07-authoritative-public-source-frame.csv`, mỗi record có provenance và locator chính thức.
- [ ] Chạy canonicalization/dedup toàn cục với 88 PubMed, 347 OpenAlex, hồ sơ pháp lý và khung 16 nguồn; không dùng run partial.
- [ ] Audit registry: mỗi record giữ alias/provenance và checksum khi có raw file.
- [ ] Xác minh calibration/codebook còn hiệu lực.
- [ ] PI xác nhận `DIRECT_SEARCH_COMPLETE` theo sửa đổi hợp nhất v1.
- [ ] Mở sàng lọc tiêu đề/tóm tắt kép độc lập cho Đào Trung Thành và Lộc Đặng.

G6/G7 không bị bỏ: theo bản hợp nhất v1 chúng là điều kiện trước trích xuất/tổng hợp cuối,
dùng pool đã qua screening toàn văn thay vì suy đoán nguồn đủ điều kiện từ trước.
