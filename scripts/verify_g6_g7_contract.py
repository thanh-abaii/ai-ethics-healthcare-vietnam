#!/usr/bin/env python3
"""Fail-closed verification of the pre-registered G6 and G7 contracts.

This checker records evidence gaps; it never upgrades a gate and never opens
screening.  A PASS remains a human PI decision after the complete evidence pack
has been independently inspected.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/governance/reference-budget-ledger.md"
MOCK = ROOT / "docs/drafts/g7-trial-draft-mock-manuscript.md"
REPORT = ROOT / "docs/audits/g6-g7-contract-audit-2026-08-01.md"


def main() -> int:
    ledger = LEDGER.read_text(encoding="utf-8")
    mock = MOCK.read_text(encoding="utf-8")
    g6 = []
    if "Cần khóa bản trích dẫn NLM" in ledger:
        g6.append("M-01/M-02 vẫn chưa có citation NLM đã khóa.")
    if "Chưa sàng lọc" in ledger:
        g6.append("16 slot Việt Nam vẫn là sức chứa dự kiến, chưa có nguồn đủ điều kiện và quyết định final-reserve/include/exclude.")
    if not re.search(r"COUNT\(DISTINCT reference_id\)=25", ledger):
        g6.append("Không có chứng cứ tính toán 25 reference_id đã được kiểm chứng.")
    g7 = []
    for phrase, explanation in (
        ("PENDING_HUMAN_LAYOUT_AND_CITATION_CHECK", "Bản mock tự ghi nhận còn chờ kiểm tra citation và layout."),
        ("locator chính thức cần xác minh", "Có locator pháp lý chưa được xác nhận trong bảng mock."),
        ("layout trên template tạp chí", "Chưa có artifact dàn trang/template và đo số trang."),
        ("citation NLM", "Danh mục tham khảo chưa là citation NLM hoàn chỉnh."),
    ):
        if phrase in mock:
            g7.append(explanation)
    report = """# Kiểm tra hợp đồng G6–G7 sau đăng ký

**Thời điểm chạy:** {time}  
**Tính chất:** kiểm tra fail-closed bằng tệp hiện hành; không phải quyết định của PI và không mở screening.

## G6 — `FAIL_CLOSED`

{g6}

## G7 — `FAIL_CLOSED`

{g7}

## Quyết định vận hành

`DIRECT_SEARCH_IN_PROGRESS`; `SCREENING=NOT_OPEN`. Không dùng số record, sự tồn tại của registry, hay số từ markdown làm proxy cho G6/G7. Chỉ xem xét lại khi toàn bộ điều kiện Điều 20–21 của protocol đã có evidence pack kiểm chứng được và PI xác nhận.
""".format(
        time=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        g6="\n".join(f"- {item}" for item in g6) or "- Không có bằng chứng PASS tự động.",
        g7="\n".join(f"- {item}" for item in g7) or "- Không có bằng chứng PASS tự động.",
    )
    REPORT.write_text(report, encoding="utf-8")
    print(f"G6=FAIL_CLOSED G7=FAIL_CLOSED report={REPORT}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
