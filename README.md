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
- **Execution Branch:** **`BRANCH A (Scoping Review)`** — 183 direct/contextual sources identified across PubMed, OpenAlex, official legal/governmental channels, and citation chasing (exceeding the threshold of 5 direct sources).

### Key Repository Artifacts
- **[protocol.md](protocol.md):** Pre-registered research protocol (v0.6-registered).
- **[search-strategy.md](search-strategy.md):** Verbatim search queries (PubMed, OpenAlex, Legal Databases, Citation Chasing).
- **[g4-g5-feasibility-pilot-2026-07-31.md](g4-g5-feasibility-pilot-2026-07-31.md):** Locked feasibility pilot execution log and gate evaluation report.
- **[prisma-scr-checklist.md](prisma-scr-checklist.md):** PRISMA-ScR compliance checklist.
- **[artifacts/g4-g5-feasibility-pilot-2026-07-31/](artifacts/g4-g5-feasibility-pilot-2026-07-31/):** OpenAlex cursor API JSON dumps, PubMed NBIB exports, `manifest.csv`, and `checksums.sha256`.

### Research Team & Roles
- **Lead Investigator:** Đào Trung Thành (*AI Ethics Author & Research Lead*).
- **Independent Reviewer:** Lộc Đặng (*Dual Screening & Inductive Coding*).

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
- **Phân nhánh nghiên cứu:** **`NHÁNH A (Scoping Review)`** — Đã xác minh 183 nguồn trực tiếp/bối cảnh trên PubMed, OpenAlex, cổng chính thức/pháp luật VN và citation chasing (vượt xa ngưỡng 5 nguồn tối thiểu).

### Các tài liệu cốt lõi
- **[protocol.md](protocol.md):** Protocol nghiên cứu đăng ký trước (phiên bản `0.6-registered`).
- **[search-strategy.md](search-strategy.md):** Chiến lược tìm kiếm nguyên văn (PubMed, OpenAlex, Cổng pháp lý, Citation Chasing).
- **[g4-g5-feasibility-pilot-2026-07-31.md](g4-g5-feasibility-pilot-2026-07-31.md):** Nhật ký khả thi G4–G5 và báo cáo đánh giá gate đã khóa.
- **[prisma-scr-checklist.md](prisma-scr-checklist.md):** Bảng kiểm tuân thủ PRISMA-ScR.
- **[artifacts/g4-g5-feasibility-pilot-2026-07-31/](artifacts/g4-g5-feasibility-pilot-2026-07-31/):** Thư mục lưu vết raw JSON OpenAlex API, raw NBIB PubMed, `manifest.csv` và băm SHA-256 `checksums.sha256`.

### Nhóm nghiên cứu & Vai trò
- **Chủ trì nghiên cứu:** Đào Trung Thành (*Tác giả Đạo đức AI & Chủ trì đề tài*).
- **Người rà soát độc lập:** Lộc Đặng (*Sàng lọc kép & Mã hóa quy nạp*).

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
