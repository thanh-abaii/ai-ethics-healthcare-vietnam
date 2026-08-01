#!/usr/bin/env python3
"""Test actual search form submissions on vanban.chinhphu.vn and congbao.chinhphu.vn."""

from __future__ import annotations

import ssl
import urllib.parse
import urllib.request
import re
from html.parser import HTMLParser

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
}


def test_congbao_search() -> None:
    url = "https://congbao.chinhphu.vn/tim-kiem?keyword=" + urllib.parse.quote('"134/2025/QH15"')
    req = urllib.request.Request(url, headers=HEADERS)
    print("Testing Công báo search:", url)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            print(f"Congbao Status: {resp.status}, HTML bytes: {len(content)}")
            # Extract links
            links = re.findall(r'href=["\']([^"\']+)["\'][^>]*>([^<]*)</a>', content)
            doc_links = [l for l in links if "chi-tiet" in l[0].lower() or "download" in l[0].lower() or ".pdf" in l[0].lower() or "van-ban" in l[0].lower()]
            print(f"Congbao Document links found: {len(doc_links)}")
            for href, txt in doc_links[:10]:
                print("   -", href, "| Text:", txt.strip())
    except Exception as exc:
        print("Congbao Error:", exc)


def test_vanban_aspnet_search() -> None:
    url = "https://vanban.chinhphu.vn/?pageid=27160"
    req = urllib.request.Request(url, headers=HEADERS)
    print("\nTesting Văn bản Chính phủ GET initial page:", url)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            print(f"Vanban Initial Status: {resp.status}, HTML bytes: {len(content)}")
            
            # Extract ASP.NET hidden fields
            vs = re.search(r'id="__VIEWSTATE"\s+value=["\']([^"\']+)["\']', content)
            vsg = re.search(r'id="__VIEWSTATEGENERATOR"\s+value=["\']([^"\']+)["\']', content)
            ev = re.search(r'id="__EVENTVALIDATION"\s+value=["\']([^"\']+)["\']', content)
            
            viewstate = vs.group(1) if vs else ""
            viewstategen = vsg.group(1) if vsg else ""
            eventval = ev.group(1) if ev else ""
            
            print("Extracted ASP.NET ViewState:", bool(viewstate), "Generator:", bool(viewstategen), "Validation:", bool(eventval))

            # Perform POST search
            post_data = {
                "__VIEWSTATE": viewstate,
                "__VIEWSTATEGENERATOR": viewstategen,
                "__EVENTVALIDATION": eventval,
                "ctrl_190927_45$txtSearch": "134/2025/QH15",
                "ctrl_190839_166$hdf_page": "1"
            }
            encoded_post = urllib.parse.urlencode(post_data).encode("utf-8")
            post_headers = dict(HEADERS)
            post_headers["Content-Type"] = "application/x-www-form-urlencoded"

            post_req = urllib.request.Request(url, data=encoded_post, headers=post_headers)
            with urllib.request.urlopen(post_req, context=ctx, timeout=25) as post_resp:
                post_content = post_resp.read().decode("utf-8", errors="replace")
                print(f"Vanban POST Search Status: {post_resp.status}, HTML bytes: {len(post_content)}")
                links = re.findall(r'href=["\']([^"\']+)["\'][^>]*>([^<]*)</a>', post_content)
                doc_links = [l for l in links if "vbid" in l[0].lower() or "chi-tiet" in l[0].lower() or "download" in l[0].lower() or ".pdf" in l[0].lower()]
                print(f"Vanban Document links found: {len(doc_links)}")
                for href, txt in doc_links[:10]:
                    print("   -", href, "| Text:", txt.strip())

    except Exception as exc:
        print("Vanban Error:", exc)


def main() -> int:
    test_congbao_search()
    test_vanban_aspnet_search()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
