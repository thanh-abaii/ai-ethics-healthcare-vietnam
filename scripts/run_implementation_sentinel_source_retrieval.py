#!/usr/bin/env python3
"""Auditable, source-level retrieval for the nine preregistered implementation sentinels.

This post-registration runner reads the frozen sampling frame and query catalogue
without altering either.  It captures (1) every portal-search attempt, (2) a
separately labelled Bing ``site:`` locator fallback when an internal portal has
no usable result locator, and (3) the HTTP headers and bodies for every
unscreened official-domain candidate reached to the frozen depth/cap.  It makes
no eligibility, relevance, or implementation judgement.
"""
from __future__ import annotations

import argparse, csv, datetime as dt, hashlib, json, os, re, time
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.error, urllib.parse, urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAME = ROOT / "implementation-case-sampling-frame.csv"
CATALOG = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/nonlegal-portals-2026-07-31/query-catalog.csv"
OUTROOT = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/sentinel-source-runs"

def now(): return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
def safe(x): return re.sub(r"[^a-z0-9_-]+", "-", x.lower()).strip("-")
def long(p: Path):
    s = str(p.resolve()); return "\\\\?\\" + s if os.name == "nt" and not s.startswith("\\\\?\\") else s
def writeb(p: Path, b: bytes):
    os.makedirs(os.path.dirname(long(p)), exist_ok=True)
    with open(long(p), "wb") as f: f.write(b)
def writet(p: Path, s: str): writeb(p, s.encode("utf-8"))
def digest(p: Path):
    h=hashlib.sha256()
    with open(long(p),"rb") as f:
        for c in iter(lambda:f.read(1048576),b""): h.update(c)
    return h.hexdigest().upper()

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.items=[]; self._href=None; self._text=[]
    def handle_starttag(self, tag, attrs):
        if tag.lower()=="a": self._href=dict(attrs).get("href"); self._text=[]
    def handle_data(self, data):
        if self._href: self._text.append(data)
    def handle_endtag(self, tag):
        if tag.lower()=="a" and self._href:
            self.items.append((self._href," ".join(self._text).strip())); self._href=None; self._text=[]

def fetch(url, timeout):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"vi-VN,vi;q=0.9,en;q=0.7"})
    try:
        with urllib.request.urlopen(req,timeout=timeout) as r: return r.status,bytes(str(r.headers),"utf-8"),r.read(),""
    except urllib.error.HTTPError as e: return e.code,bytes(str(e.headers),"utf-8"),e.read(),f"HTTPError: {e.reason}"
    except Exception as e: return None,b"",b"",f"{type(e).__name__}: {e}"

def portal_url(domain, q, page):
    e=urllib.parse.quote(q,safe=""); host=urllib.parse.urlparse(domain).netloc.lower()
    if "soyte.hanoi" in host: return f"https://soyte.hanoi.gov.vn/tim-kiem?query={e}&page={page}"
    if "danang.gov.vn" in host: return f"https://soyte.danang.gov.vn/tim-kiem?query={e}&page={page}"
    if "medinet" in host: return f"https://medinet.gov.vn/tim-kiem?query={e}&page={page}"
    if "bachmai" in host: return f"https://bachmai.gov.vn/?s={e}&paged={page}"
    if "bvtwhue" in host: return f"https://bvtwhue.com.vn/?s={e}&paged={page}"
    if host=="choray.vn": return f"https://bvchoray.vn/?s={e}&paged={page}" # verified operational alias; frozen frame retained
    if "vinmec" in host: return f"https://www.vinmec.com/vie/tim-kiem/?q={e}&page={page}"
    if "tamanh" in host: return f"https://tamanhhospital.vn/?s={e}&paged={page}"
    if "umc" in host: return f"https://www.umc.edu.vn/tim-kiem?q={e}&page={page}"
    return urllib.parse.urljoin(domain,"?s="+e+f"&paged={page}")

def allowed_hosts(domain):
    h=urllib.parse.urlparse(domain).netloc.lower().removeprefix("www.")
    aliases={"choray.vn":{"choray.vn","bvchoray.vn"}}
    return aliases.get(h,{h,"www."+h})
def candidate_links(body, origin, domain):
    p=Links()
    try: p.feed(body.decode("utf-8",errors="replace"))
    except Exception: return []
    out=[]; seen=set(); hosts=allowed_hosts(domain)
    for href,text in p.items:
        u=urllib.parse.urljoin(origin,href); x=urllib.parse.urlparse(u)
        canonical=urllib.parse.urlunparse((x.scheme,x.netloc,x.path,"",x.query,""))
        path=x.path.lower()
        if x.scheme not in {"http","https"} or x.netloc.lower().removeprefix("www.") not in {z.removeprefix("www.") for z in hosts}: continue
        if path in {"","/"} or any(z in path for z in ("/tim-kiem","/search","/tag/","/category/","/wp-json","/feed")): continue
        if re.search(r"\.(css|js|png|jpg|jpeg|gif|svg|ico|woff2?)$",path): continue
        if canonical not in seen: seen.add(canonical); out.append((canonical,text))
    return out
def bing_url(domain,q,first):
    return "https://www.bing.com/search?"+urllib.parse.urlencode({"q":f"site:{urllib.parse.urlparse(domain).netloc} {q}","first":first,"count":10})

def save_capture(raw, stem, url, timeout):
    started=now(); status,headers,body,error=fetch(url,timeout)
    writeb(raw/(stem+".headers"),headers); writeb(raw/(stem+".body"),body); writet(raw/(stem+".error.txt"),(error or "NO_TRANSPORT_ERROR")+"\n")
    return {"requested_url":url,"started_at":started,"http_status":"" if status is None else status,"response_bytes":len(body),"transport_error":error,"headers_file":f"raw/{stem}.headers","body_file":f"raw/{stem}.body","body_sha256":digest(raw/(stem+".body"))},body

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--timeout",type=int,default=20); ap.add_argument("--pause",type=float,default=.15); ap.add_argument("--workers",type=int,default=8); ap.add_argument("--run-id")
    a=ap.parse_args(); runid=a.run_id or "sentinel-source-retrieval-"+dt.datetime.now().strftime("%Y%m%dT%H%M%S")
    run=OUTROOT/runid; raw=run/"raw"; raw.mkdir(parents=True,exist_ok=False)
    cases=list(csv.DictReader(FRAME.open(encoding="utf-8-sig",newline=""))); queries={r["query_id"]:r for r in csv.DictReader(CATALOG.open(encoding="utf-8-sig",newline=""))}
    search=[]; locators=[]; sources=[]; acquisition=[]
    for case in cases:
      qids=case["query_set"].split("|"); domain=case["official_domain"]
      for qid in qids:
        q=queries[qid]["verbatim_query"]; found=[]; zero_pages=0
        # Portal search: max two pages, or two terminal pages with no new usable URLs.
        for page in (1,2):
          stem=f"search-{safe(case['case_id'])}-{safe(qid)}-p{page:02d}"; row,body=save_capture(raw,stem,portal_url(domain,q,page),a.timeout)
          links=candidate_links(body,row["requested_url"],domain); new=[z for z in links if z[0] not in {x[0] for x in found}]; found.extend(new)
          row.update({"case_id":case["case_id"],"query_id":qid,"query_verbatim":q,"interface":"official_portal","page":page,"candidate_count":len(links),"new_candidate_count":len(new),"status":"RAW_SEARCH_PAGE_CAPTURED" if row["http_status"]==200 else "SEARCH_TRANSPORT_ATTEMPTED"}); search.append(row); time.sleep(a.pause)
          if not new: zero_pages+=1
          if zero_pages>=2: break
        # Preregistered query retained verbatim; fallback only locates official-domain URLs.
        if not found:
          for page,first in ((1,1),(2,11)):
            stem=f"fallback-{safe(case['case_id'])}-{safe(qid)}-p{page:02d}"; row,body=save_capture(raw,stem,bing_url(domain,q,first),a.timeout)
            links=candidate_links(body,row["requested_url"],domain); new=[z for z in links if z[0] not in {x[0] for x in found}]; found.extend(new)
            row.update({"case_id":case["case_id"],"query_id":qid,"query_verbatim":q,"interface":"bing_site_fallback_locator_only","page":page,"candidate_count":len(links),"new_candidate_count":len(new),"status":"RAW_FALLBACK_PAGE_CAPTURED" if row["http_status"]==200 else "FALLBACK_TRANSPORT_ATTEMPTED"}); search.append(row); time.sleep(a.pause)
            if not new and page==2: break
        # Capture sources to the frozen cap (20).  Depth 1 result URLs, then depth 2 links.
        queue=[(u,t,1) for u,t in found]; seen=set(); captured=0
        while queue and captured<int(case["result_cap_per_query"]):
          batch=[]
          while queue and len(batch)<min(a.workers,int(case["result_cap_per_query"])-captured):
            url,text,depth=queue.pop(0)
            if url not in seen: seen.add(url); captured+=1; batch.append((url,text,depth,captured))
          def retrieve(item):
            url,text,depth,ordinal=item; stem=f"source-{safe(case['case_id'])}-{safe(qid)}-d{depth}-{ordinal:02d}"
            row,body=save_capture(raw,stem,url,a.timeout); return item,row,body
          with ThreadPoolExecutor(max_workers=a.workers) as pool:
            futures=[pool.submit(retrieve,item) for item in batch]
            for future in as_completed(futures):
              (url,text,depth,_),row,body=future.result()
              row.update({"case_id":case["case_id"],"query_id":qid,"query_verbatim":q,"source_url":url,"anchor_text":text,"link_depth":depth,"status":"RAW_SOURCE_CAPTURED" if row["http_status"]==200 else "SOURCE_TRANSPORT_ATTEMPTED"}); sources.append(row)
              locators.append({"case_id":case["case_id"],"query_id":qid,"candidate_url":url,"anchor_text":text,"link_depth":depth,"status":"UNSCREENED_OFFICIAL_DOMAIN_LOCATOR"})
              if depth < int(case["link_depth"]) and body:
                for child,ctext in candidate_links(body,url,domain):
                  if child not in seen and all(child!=x[0] for x in queue): queue.append((child,ctext,depth+1))
          time.sleep(a.pause)
        acquisition.append({"case_id":case["case_id"],"query_id":qid,"frozen_result_cap":case["result_cap_per_query"],"frozen_link_depth":case["link_depth"],"unique_source_urls_attempted":captured,"source_level_records_200":sum(1 for x in sources if x["case_id"]==case["case_id"] and x["query_id"]==qid and x["http_status"]==200),"terminal_reason":"QUEUE_EXHAUSTED" if not queue else "FROZEN_RESULT_CAP_REACHED"})
    def dump(name,rows):
      keys=sorted({k for r in rows for k in r})
      with (run/name).open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=keys); w.writeheader(); w.writerows(rows)
    dump("search-attempt-ledger.csv",search); dump("source-locator-ledger.csv",locators); dump("source-acquisition-ledger.csv",sources); dump("query-terminal-ledger.csv",acquisition)
    n200=sum(1 for r in sources if r["http_status"]==200); expected=len(cases)*10
    status="SENTINEL_SOURCE_RETRIEVAL_COMPLETE_NOT_SCREENED" if n200 else "FAIL_CLOSED_NO_SOURCE_LEVEL_SENTINEL_DOCUMENT_RETRIEVED"
    manifest={"run_id":runid,"completed_at_utc":now(),"frozen_case_count":len(cases),"expected_query_case_pairs":expected,"search_attempts":len(search),"source_attempts":len(sources),"source_level_http_200":n200,"status":status,"interpretation":"Transport capture only. No eligibility, screening, implementation inference, or reviewer decision was performed."}
    writet(run/"manifest.json",json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    writet(run/"README.md",f"# Sentinel source retrieval — {runid}\n\nStatus: `{status}`\n\nThis run reads the frozen sampling frame and query catalogue. It contains raw search/fallback/source responses, headers, ledgers, and SHA-256 inventory. It is not screening.\n")
    hashes=[]
    for base,_,files in os.walk(long(run)):
      for fn in sorted(files):
        if fn=="sha256.csv": continue
        p=Path(base)/fn; hashes.append({"relative_path":str(p.relative_to(long(run))).replace("\\","/"),"sha256":digest(p),"bytes":p.stat().st_size})
    dump("sha256.csv",hashes)
    print(json.dumps(manifest,ensure_ascii=False))
if __name__=="__main__": main()
