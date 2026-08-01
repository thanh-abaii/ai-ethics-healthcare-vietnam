#!/usr/bin/env python3
"""Inspect captured legal HTML search result pages to identify distinct document links and structure."""

from __future__ import annotations

import re
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/legal-portals-20260801T092029/raw"


class LegalLinkInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.current_href: str | None = None
        self.current_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) -> None:
        if tag.lower() == "a":
            attr_dict = dict(attrs)
            self.current_href = attr_dict.get("href")
            self.current_text = []

    def handle_data(self, data: str) -> None:
        if self.current_href and data.strip():
            self.current_text.append(data.strip())

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.current_href:
            text = " ".join(self.current_text)
            self.links.append((self.current_href, text))
            self.current_href = None
            self.current_text = []


def main() -> int:
    html_files = sorted(RAW_DIR.glob("*.html"))
    print(f"Inspecting {len(html_files)} raw HTML search result pages...")

    found_links: set[tuple[str, str, str]] = set()

    for html_file in html_files:
        content = html_file.read_bytes().decode("utf-8", errors="replace")
        parser = LegalLinkInspector()
        parser.feed(content)

        for href, text in parser.links:
            if any(k in href.lower() for k in ["pageid=", "vbid=", "chi-tiet", "vbpq", "download", ".pdf"]):
                found_links.add((html_file.name, href, text[:100]))

    print(f"\nExtracted {len(found_links)} candidate links across raw HTML files.\nSample links:")
    for src, href, txt in sorted(found_links)[:25]:
        print(f"[{src}] {href} | Text: {txt}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
