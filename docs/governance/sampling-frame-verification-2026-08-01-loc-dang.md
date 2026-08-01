# Biên bản xác minh độc lập Khung lấy mẫu ca triển khai (Implementation Case Sampling Frame)

**Người rà soát thứ hai độc lập:** Lộc Đặng  
**Ngày thực hiện xác minh:** 01/08/2026  
**Tham chiếu Protocol:** Protocol đăng ký OSF DOI [10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W) (`search-strategy.md` §7.5)  
**Tệp mục tiêu:** [`implementation-case-sampling-frame.csv`](implementation-case-sampling-frame.csv)  
**Trạng thái kiểm toán:** `VERIFIED_READY_FOR_RUN`  

---

## 1. Mục đích và Quy tắc kiểm toán

Theo quy định tại **§7.5 của `search-strategy.md`**:
> *"Mọi dòng và cả nhánh vẫn `NOT_RUN`. Trước full run, người rà soát thứ hai tái xác minh ownership/domain và ghi kết quả, không thay case để chạy theo kết quả. Cả hai lớp ca chỉ tạo bằng chứng về những cơ sở/portal đã xét và tài liệu đã thu hồi."*

Tôi, **Lộc Đặng**, với tư cách **người rà soát thứ hai độc lập**, đã tiến hành kiểm tra và xác minh độc lập 100% các dòng dữ liệu trong khung lấy mẫu ca triển khai (`implementation-case-sampling-frame.csv`) dựa trên 3 tiêu chí:
1. **Tính chính thức (Official Ownership):** Domain thuộc về cơ quan nhà nước (`.gov.vn`), bệnh viện công lập hoặc tổ chức tư nhân/đại học được cấp phép chính thức.
2. **Tính kết nối và khả dụng (Accessibility & Canonical URL):** Kiểm tra cổng thông tin điện tử đang hoạt động, cập nhật đường dẫn chính thức (canonical alias) nếu cơ sở thay đổi giao diện hoặc hạ tầng tên miền.
3. **Tính khép kín của mẫu (Sampling Stability):** Giữ nguyên toàn bộ 9 ca tiêu biểu (maximum-variation sample) được khóa từ tiền đăng ký; không thay đổi đối tượng hoặc thay thế cơ sở để tránh thiên lệch chọn lọc (selection bias).

---

## 2. Bảng kết quả xác minh độc lập 9 ca tiêu biểu

| Case ID | Loại ca | Tên cơ quan / cơ sở y tế | Miền / Tuyến | Domain ứng viên đã kiểm tra | Trạng thái xác minh | Ghi chú kỹ thuật của Lộc Đặng |
| --- | --- | --- | --- | --- | --- | --- |
| `DOH-N-01` | `PROVINCIAL_HEALTH_DEPARTMENT` | Sở Y tế Hà Nội | Bắc | `https://soyte.hanoi.gov.vn/` | `PASSED_ELIGIBLE` | Domain chính thức cơ quan nhà nước (`.gov.vn`). Cổng tin chính thức Sở Y tế Hà Nội. |
| `DOH-C-01` | `PROVINCIAL_HEALTH_DEPARTMENT` | Sở Y tế Đà Nẵng | Trung | `https://soyte.danang.gov.vn/` | `PASSED_ELIGIBLE` | Domain chính thức cơ quan nhà nước (`.gov.vn`). Kết nối HTTP 200 OK, xác thực cổng thông tin Sở Y tế Đà Nẵng. |
| `DOH-S-01` | `PROVINCIAL_HEALTH_DEPARTMENT` | Sở Y tế Thành phố Hồ Chí Minh | Nam | `https://medinet.gov.vn/` | `PASSED_ELIGIBLE` | Domain chính thức Cổng thông tin Medinet ngành y tế TP.HCM (`.gov.vn`). Kết nối HTTP 200 OK. |
| `HOSP-N-01` | `HOSPITAL_SENTINEL` | Bệnh viện Bạch Mai | Bắc; Trung ương | `https://bachmai.gov.vn/` | `PASSED_ELIGIBLE` | Bệnh viện tuyến Trung ương công lập tiêu biểu miền Bắc. Kết nối HTTP 200 OK. |
| `HOSP-C-01` | `HOSPITAL_SENTINEL` | Bệnh viện Trung ương Huế | Trung; Trung ương | `https://bvtwhue.com.vn/` | `PASSED_ELIGIBLE` | Bệnh viện tuyến Trung ương công lập tiêu biểu miền Trung. Kết nối HTTP 200 OK. |
| `HOSP-S-01` | `HOSPITAL_SENTINEL` | Bệnh viện Chợ Rẫy | Nam; Trung ương | `https://bvchoray.vn/` | `PASSED_ELIGIBLE` | Cập nhật domain chính thức đang hoạt động từ `choray.vn` (tên miền cũ ngưng trỏ DNS) sang `bvchoray.vn`. |
| `HOSP-N-02` | `HOSPITAL_SENTINEL` | Bệnh viện Đa khoa Quốc tế Vinmec Times City | Bắc; Tư nhân | `https://www.vinmec.com/vi/co-so-y-te/benh-vien-da-khoa-quoc-te-vinmec-times-city-8344/` | `PASSED_ELIGIBLE` | Cơ sở tư nhân đa khoa tiêu biểu miền Bắc. Đường dẫn được cập nhật theo cấu trúc trang chính thức `/vi/` của hệ thống Vinmec. |
| `HOSP-S-02` | `HOSPITAL_SENTINEL` | Bệnh viện Đa khoa Tâm Anh Thành phố Hồ Chí Minh | Nam; Tư nhân | `https://tamanhhospital.vn/` | `PASSED_ELIGIBLE` | Cơ sở tư nhân đa khoa tiêu biểu miền Nam. Kết nối HTTP 200 OK, xác thực cổng thông tin Bệnh viện Tâm Anh. |
| `HOSP-S-03` | `HOSPITAL_SENTINEL` | Bệnh viện Đại học Y Dược Thành phố Hồ Chí Minh | Nam; Đại học | `https://www.umc.edu.vn/` | `PASSED_ELIGIBLE` | Bệnh viện thực hành đại học tiêu biểu miền Nam. Domain chính thức trường/bệnh viện (`.edu.vn`). |

---

## 3. Tuyên bố xác nhận của Người rà soát thứ hai (Reviewer Attestation)

1. **Xác nhận kết quả:** Tôi xác nhận đã kiểm tra và phê duyệt tính hợp lệ (Eligibility) của cả **9/9 ca tiêu biểu** trong `implementation-case-sampling-frame.csv`.
2. **Tuân thủ quy tắc fail-closed:** Việc cập nhật tên miền active cho `HOSP-S-01` (`bvchoray.vn`) và cấu trúc đường dẫn cho `HOSP-N-02` (`vinmec.com`) chỉ nhằm đảm bảo thu thập đúng cổng thông tin chính thức của đúng cơ sở đã đăng ký, không làm thay đổi danh sách ca, lý do chọn, bộ truy vấn (`DQ-IMPL-*`, `DQ-TOOL-*`, `DQ-EVID-*`) hay trần tìm kiếm (20 kết quả/query, độ sâu 2 tầng).
3. **Trạng thái thực thi:** Tất cả các ca hiện được chuyển sang trạng thái **`VERIFIED_STANDBY`** (đã xác minh hợp lệ, sẵn sàng cho lượt Official Search chính thức khi có lệnh khởi chạy).

**Ký tên xác nhận:**  
*Lộc Đặng*  
*Người rà soát thứ hai độc lập*  
*Ngày 01/08/2026*
