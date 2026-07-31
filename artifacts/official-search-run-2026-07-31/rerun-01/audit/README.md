# Hộ chiếu provenance của 242 raw record

Lượt này không giả định `Direct_Harvest` hay `Indirect_Harvest` là provenance đủ mạnh. Mỗi `raw_record_id` phải được đối chiếu với một dòng evidence map có tối thiểu:

`query_id`, `source_record_id`, `retrieval_date`, `raw_artifact_locator`, `raw_artifact_sha256`, `cursor_or_page`.

Chỉ khi 242/242 dòng có các trường trên và raw artifact/checksum được xác minh thì harvest mới `PASS` về tái lập. Các dòng chưa đối chiếu là `UNRECONCILED_PROVENANCE`, bị chặn khỏi PRISMA, registry chính thức, sàng lọc và extraction.
