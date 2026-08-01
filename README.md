# Ethical and Responsible AI Implementation in Healthcare in Vietnam: A Systematic Scoping Review Protocol and Audit Trail
## Triển khai AI có đạo đức và trách nhiệm trong Y tế tại Việt Nam: Protocol Tổng quan Phạm vi và Nhật ký Thẩm định Tái lập

[![OSF Registration](https://img.shields.io/badge/OSF%20Registration-62b8w-blue.svg)](https://osf.io/62b8w/)
[![DOI](https://img.shields.io/badge/DOI-10.17605%2FOSF.IO%2F62B8W-green.svg)](https://doi.org/10.17605/OSF.IO/62B8W)
[![Target Journal](https://img.shields.io/badge/Target%20Journal-Ho%20Chi%20Minh%20City%20Journal%20of%20Medicine-104c8f.svg)](https://tapchiyhoctphcm.vn)
[![AI Policy](https://img.shields.io/badge/AI%20Policy-Compliant-brightgreen.svg)](https://tapchiyhoctphcm.vn/su-dung-ai)
[![Feasibility Pilot](https://img.shields.io/badge/Feasibility%20Pilot-PASS%20%28Branch%20A%29-success.svg)](g4-g5-feasibility-pilot-2026-07-31.md)
[![PRISMA-ScR](https://img.shields.io/badge/Standard-PRISMA--ScR-orange.svg)](prisma-scr-checklist.md)

---

## English Summary

### Overview
This repository contains the registered protocol, search strategy, audit trail artifacts, and feasibility pilot results for the research study: **"Ethical and Responsible AI Implementation in Healthcare in Vietnam: A Systematic Scoping Review."**

The project follows a rigorous two-stage Open Science architecture aligned with the **PRISMA-ScR** (Preferred Reporting Items for Systematic Reviews and Meta-Analyses Extension for Scoping Reviews) guidelines and registered on OSF under DOI [10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W).

### Target Journal & AI Policy Compliance
- **Target Publication Venue:** **Ho Chi Minh City Journal of Medicine** (*Tạp chí Y học Thành phố Hồ Chí Minh* — [tapchiyhoctphcm.vn](https://tapchiyhoctphcm.vn)).
- **AI Policy Compliance:** This research strictly adheres to the official **AI Usage Policy** of the *Ho Chi Minh City Journal of Medicine* ([https://tapchiyhoctphcm.vn/su-dung-ai](https://tapchiyhoctphcm.vn/su-dung-ai)):
  1. **Authorship Accountability:** AI tools (LLMs / agent CLI) are **not** credited as authors or co-authors. The human authors (Đào Trung Thành and Lộc Đặng) maintain full accountability for the accuracy, scientific integrity, interpretations, and conclusions of the manuscript.
  2. **Transparent Disclosure:** Artificial Intelligence tools were utilized strictly for automated API data harvesting, JSON/NBIB metadata extraction, syntax verification, and formatting helper scripts. All raw search outputs, execution scripts, and SHA-256 checksums are disclosed transparently in this open repository for auditability.

### Research Status & Gate Decisions
- **OSF Pre-registration:** Locked and public (OSF Identifier: [`62b8w`](https://osf.io/62b8w/)).
- **Feasibility Pilot (Gates G4 & G5):** **`PASS`** (Completed on July 31, 2026).
- **Gate G6 (Reference Budget Feasibility Gate):** **`FAIL_CLOSED`**
- **Gate G7 (Journal Mock Manuscript Gate):** **`FAIL_CLOSED`**
- **Current Research Status:** **`DIRECT_SEARCH_IN_PROGRESS`**
- **Double Screening Status:** **`DEDUP_AND_SCREENING_NOT_OPEN`** (`SCREENING = NOT_OPEN`).

### Single Source of Truth & Repository Layout
- **[INDEX.md](INDEX.md):** **Single Source of Truth (SSOT)** for the entire repository structure, file index, post-registration documents (`docs/`), audit reports (`reports/`), scripts (`scripts/`), and raw artifacts (`artifacts/`).
- **[protocol.md](protocol.md):** Pre-registered research protocol (v0.6-registered).
- **[search-strategy.md](search-strategy.md):** Verbatim search queries (PubMed, OpenAlex, Legal Databases, Citation Chasing).
- **[prisma-scr-checklist.md](prisma-scr-checklist.md):** PRISMA-ScR compliance checklist.
- **[reports/official-sources-harvest-audit-report-2026-08-01.md](reports/official-sources-harvest-audit-report-2026-08-01.md):** Official sources raw harvest & Gate G6/G7 audit report.
- **[docs/audits/g6-g7-evaluation-report-2026-08-01.md](docs/audits/g6-g7-evaluation-report-2026-08-01.md):** Gate G6 & G7 evaluation report.

### API Credentials Setup
To execute automated data harvesting from OpenAlex and PubMed without rate-limiting or WAF abuse blocks, configure a `.env` file at the root of the repository:
```env
# Official email for OpenAlex Polite Pool rate-limit tier
POLITE_EMAIL=your_real_email@domain.com

# Optional OpenAlex API Key (from https://openalex.org/account)
OPENALEX_API_KEY=your_openalex_api_key

# Official NCBI API Key (from https://www.ncbi.nlm.nih.gov/account/settings/)
NCBI_API_KEY=your_ncbi_api_key_36_chars
```

### Research Team & Roles
- **Lead Investigator:** Đào Trung Thành (*AI Ethics Author & Research Lead*).
- **Independent Reviewer:** Lộc Đặng (*Dual Screening & Inductive Coding*).

### OSF Immutability & Audit Trail Policy
- **Fidelity to OSF Registration:** The file [`protocol.md`](protocol.md) and all files in [`artifacts/protocol-registration-lock-2026-07-31/`](artifacts/protocol-registration-lock-2026-07-31/) represent the frozen snapshot pre-registered on OSF. To maintain complete scientific integrity for peer review, these files are immutable and must match the OSF snapshot 100% byte-for-byte.
- **Post-Registration Logging:** All post-registration gate evaluations, pilot execution logs, search logs, and amendments are documented exclusively in separate, transparent log files (such as [`g4-g5-feasibility-pilot-2026-07-31.md`](g4-g5-feasibility-pilot-2026-07-31.md) and [`search-log.csv`](search-log.csv)).

---

## Tóm tắt Tiếng Việt

### Tổng quan dự án
Kho lưu trữ này chứa protocol đăng ký trước, chiến lược tìm kiếm, nhật ký lưu vết thẩm định và kết quả chạy thử nghiệm khả thi (pilot) cho đề tài: **"Triển khai AI có đạo đức và trách nhiệm trong Y tế tại Việt Nam: Tổng quan phạm vi hệ thống."**

Dự án áp dụng kiến trúc Khoa học mở (Open Science) hai tầng tuân thủ nghiêm ngặt chuẩn quốc tế **PRISMA-ScR** và đã được đăng ký chính thức trên OSF tại DOI [10.17605/OSF.IO/62B8W](https://doi.org/10.17605/OSF.IO/62B8W).

### Mục tiêu xuất bản & Tuân thủ quy định sử dụng AI
- **Nơi đăng ký xuất bản mục tiêu:** **Tạp chí Y học Thành phố Hồ Chí Minh** ([tapchiyhoctphcm.vn](https://tapchiyhoctphcm.vn)).
- **Tuân thủ quy định sử dụng AI:** Nghiên cứu tuân thủ 100% **"Quy định công khai về sử dụng Trí tuệ nhân tạo"** của *Tạp chí Y học Thành phố Hồ Chí Minh* ([https://tapchiyhoctphcm.vn/su-dung-ai](https://tapchiyhoctphcm.vn/su-dung-ai)):
  1. **Trách nhiệm tác giả:** AI (các mô hình ngôn ngữ lớn / Agent CLI) **không đứng tên tác giả hoặc đồng tác giả**. Nhóm tác giả con người (Đào Trung Thành và Lộc Đặng) chịu trách nhiệm hoàn toàn về tính chính xác, tính trung thực khoa học, diễn giải và kết luận của bản thảo.
  2. **Khai báo minh bạch:** Công cụ AI chỉ được sử dụng để hỗ trợ thu thập dữ liệu API tự động, xuất metadata JSON/NBIB, kiểm tra cú pháp và viết script hỗ trợ định dạng. Toàn bộ kết quả tìm kiếm thô, script thực thi và mã băm SHA-256 đều được công khai minh bạch trong kho lưu trữ này để phục vụ thẩm định.

### Trạng thái nghiên cứu và Quyết định cổng (Gates)
- **Đăng ký OSF:** Đã khóa bất biến và công khai (Mã OSF: [`62b8w`](https://osf.io/62b8w/)).
- **Thử nghiệm khả thi (Gate G4 & G5):** **`PASS`** (Hoàn tất ngày 31/07/2026).
- **Gate G6 (Khả thi Ngân sách Tham khảo 25 tài liệu):** **`FAIL_CLOSED`**
- **Gate G7 (Bản thảo thử 8 trang Hợp đồng Tạp chí):** **`FAIL_CLOSED`**
- **Trạng thái Tiến độ Nghiên cứu:** **`DIRECT_SEARCH_IN_PROGRESS`**
- **Trạng thái Sàng lọc Kép Vòng 1 / Dedup:** **`DEDUP_AND_SCREENING_NOT_OPEN`** (`SCREENING = NOT_OPEN`).

### Cấu trúc Repository & Single Source of Truth
- **[INDEX.md](INDEX.md):** **Single Source of Truth (SSOT)** quản lý toàn bộ sơ đồ phân mục repository, tài liệu hậu đăng ký (`docs/`), báo cáo kiểm toán (`reports/`), mã nguồn (`scripts/`) và chứng cứ thô (`artifacts/`).
- **[protocol.md](protocol.md):** Protocol nghiên cứu đăng ký trước (phiên bản `0.6-registered`).
- **[search-strategy.md](search-strategy.md):** Chiến lược tìm kiếm nguyên văn (PubMed, OpenAlex, Cổng pháp lý, Citation Chasing).
- **[prisma-scr-checklist.md](prisma-scr-checklist.md):** Bảng kiểm tuân thủ PRISMA-ScR.
- **[reports/official-sources-harvest-audit-report-2026-08-01.md](reports/official-sources-harvest-audit-report-2026-08-01.md):** Báo cáo kiểm toán thu hồi dữ liệu thô 5 nhánh nguồn chính thức.

### Cấu hình API Credentials
Để thực thi thu thập dữ liệu tự động từ OpenAlex và PubMed ổn định mà không bị giới hạn lưu lượng (rate-limit) hoặc bị tường lửa chặn (WAF abuse block), người nghiên cứu cần tạo tệp `.env` tại thư mục gốc repository:
```env
# Email chính thức dùng cho OpenAlex Polite Pool
POLITE_EMAIL=email_that_cua_bac@domain.com

# NCBI API Key chính thức (lấy tại https://www.ncbi.nlm.nih.gov/account/settings/)
NCBI_API_KEY=ncbi_api_key_36_ky_tu
```

### Nhóm nghiên cứu & Vai trò
- **Chủ trì nghiên cứu:** Đào Trung Thành (*Tác giả Đạo đức AI & Chủ trì đề tài*).
- **Người rà soát độc lập:** Lộc Đặng (*Sàng lọc kép & Mã hóa quy nạp*).

### Quy định bảo vệ tính bất biến của tệp đăng ký OSF
- **Bảo toàn tính khớp 100% với OSF:** Tệp [`protocol.md`](protocol.md) và toàn bộ các tệp tại [`artifacts/protocol-registration-lock-2026-07-31/`](artifacts/protocol-registration-lock-2026-07-31/) đại diện cho bản snapshot đóng băng đã đăng ký công khai trên OSF. Để duy trì tính minh bạch khoa học tuyệt đối phục vụ thẩm định (peer-review), các tệp này **bất biến và phải giữ khớp chính xác từng từ** với bản snapshot OSF.
- **Lưu vết hậu đăng ký độc lập:** Mọi cập nhật đánh giá cổng, nhật ký chạy thử nghiệm khả thi, log tìm kiếm và các sửa đổi sau đăng ký chỉ được ghi nhận tại các tệp nhật ký hậu đăng ký riêng biệt (như [`g4-g5-feasibility-pilot-2026-07-31.md`](g4-g5-feasibility-pilot-2026-07-31.md) và [`search-log.csv`](search-log.csv)).

---

## Citation & Contact / Trích dẫn & Liên hệ

If you reference this dataset or protocol in your academic work, please cite:

```bibtex
@misc{dao2026aiethicshealthvn,
  author       = {Thanh, Dao Trung and Dang, Loc},
  title        = {Ethical and Responsible AI Implementation in Healthcare in Vietnam: A Systematic Scoping Review Protocol and Audit Trail},
  year         = {2026},
  publisher    = {Open Science Framework},
  doi          = {10.17605/OSF.IO/62B8W},
  howpublished = {\url{https://osf.io/62b8w/}}
}
```

* **Target Journal:** Ho Chi Minh City Journal of Medicine (*Tạp chí Y học Thành phố Hồ Chí Minh*).
* **License:** Creative Commons Attribution 4.0 International (CC BY 4.0).
* **Repository Maintainer:** Đào Trung Thành (`daotrungthanh2021@gmail.com`).
