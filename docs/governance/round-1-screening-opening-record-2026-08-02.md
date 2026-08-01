# Biên bản mở screening vòng 1: tiêu đề/tóm tắt kép độc lập

**Ngày mở:** 2026-08-02  
**Căn cứ mở:** PI xác nhận `DIRECT_SEARCH_COMPLETE` tại `pi-direct-search-complete-confirmation-2026-08-02.md`  
**Corpus:** 385 `CANON-*` từ Master Input Registry  
**Trạng thái:** `ROUND_1_TITLE_ABSTRACT_SCREENING_OPEN`

## Biểu mẫu đã tạo

| Reviewer | Tệp | Dòng dữ liệu | Quyết định tiền điền | SHA-256 |
| --- | --- | ---: | ---: | --- |
| `DAO_TRUNG_THANH` | `round-1-title-abstract-dao-trung-thanh-2026-08-02.csv` | 385 | 0 | `ddbe4a994ccad9f2dca32e6ffc94ae994cc320094a9afd34f808d69383931a1a` |
| `LOC_DANG` | `round-1-title-abstract-loc-dang-2026-08-02.csv` | 385 | 0 | `39870afe6d66fa3f7e034339d344e4474cf1200d80d551b9ce645d1e77fa4266` |

Mỗi tệp dùng đúng `record_id` `CANON-*`, `stage=TITLE_ABSTRACT`, controlled reviewer ID theo codebook và các ô `inclusion_decision`, `exclusion_reason`, `date` để trống khi mở.

## Quy tắc vận hành

1. PI và Lộc Đặng làm việc độc lập, không xem hoặc sao chép quyết định của nhau.
2. Ở vòng tiêu đề/tóm tắt, chỉ loại khi có căn cứ chắc chắn; record chưa rõ hoặc thiếu thông tin phải ghi `UNCERTAIN` để chuyển toàn văn.
3. Không dùng `EX08_FULL_TEXT_UNAVAILABLE` hay `EX09_WRONG_LANGUAGE` ở vòng này.
4. Khi mỗi reviewer hoàn tất, khóa bản của mình và lưu checksum mới; chỉ sau đó mới tạo bảng đối chiếu bất đồng.

Không có adjudication, screening toàn văn, citation chasing, trích xuất hay tổng hợp nào được tạo khi mở vòng 1.
