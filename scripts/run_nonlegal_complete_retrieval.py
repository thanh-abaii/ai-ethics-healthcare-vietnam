#!/usr/bin/env python3
"""Run the locked non-legal search with auditable source-level retrieval.

This is an execution artifact, not a screening or eligibility tool.  It uses
the locked query catalogue and portal list, records all direct-search attempts,
and uses a separately labelled ``site:`` locator search only if the portal
cannot yield semantic result links.  Every discovered official URL is then
captured at source level and followed once to a narrowly defined second depth.
"""
from __future__ import annotations

import argparse, csv, datetime as dt, hashlib, json, os, re, time
import urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/governance/nonlegal-execution-query-catalogue-pr06.csv"
OUTROOT = ROOT / "artifacts/search-rerun-01-2026-07-31/official-sources/nl-complete-runs"
CHANNELS = {
    "MOH": ("moh.gov.vn", "https://moh.gov.vn/tim-kiem?query={q}&page={page}"),
    "MOH-ASTT": ("asttmoh.vn", "https://asttmoh.vn/?s={q}&paged={page}"),
    "MOH-KCB": ("kcb.vn", "https://kcb.vn/?site=2005611&page=search&keyword={q}&p={page}"),
    "MOH-HTTB": ("imda.moh.gov.vn", "https://imda.moh.gov.vn/?s={q}&paged={page}"),
    "MOH-NHIC": ("ttyqg.vn", "https://ttyqg.vn/?s={q}&paged={page}"),
    "MOH-PC": ("vuphapche.moh.gov.vn", "https://vuphapche.moh.gov.vn/?s={q}&paged={page}"),
    "MOH-HSPI": ("hspi.org.vn", "https://hspi.org.vn/news/find?txtKw={q}&page={page}"),
    "MST": ("most.gov.vn", "https://most.gov.vn/search?q={q}&page={page}"),
    "UNESCO-RAM": ("www.unesco.org", "https://www.unesco.org/ethics-ai/en/search?category=Global%20AI%20Ethics%20and%20Governance%20Observatory&query={q}&page={page}"),
    "WHO-VNM": ("www.who.int", "https://www.who.int/vietnam/search?query={q}&page={page}"),
}
EXPECTED = {"DQ-IMPL-01", "DQ-IMPL-02", "DQ-IMPL-03", "DQ-IMPL-04", "DQ-IMPL-05", "DQ-TOOL-01", "DQ-TOOL-02", "DQ-EVID-01", "DQ-EVID-02", "DQ-EVID-03", "DQ-EVID-04", "DQ-EVID-05"}

def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def digest(b): return hashlib.sha256(b).hexdigest()
def safe(s): return re.sub(r"[^A-Za-z0-9._-]+", "-", s).strip("-")
def local(path):
    text = str(path.resolve())
    return "\\\\?\\" + text if os.name == "nt" and not text.startswith("\\\\?\\") else text
def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(local(path), "wb") as f: f.write(content)
    return len(content), digest(content)
def write_utf8(path, content):
    with open(local(path), "w", encoding="utf-8", newline="") as f: f.write(content)
def file_digest(path):
    h=hashlib.sha256()
    with open(local(path), "rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest()
def fetch(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent":"AI-ethics-healthcare-Vietnam-review/1.0 (academic retrieval; contact via registered OSF project)","Accept-Language":"vi,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, dict(r.headers.items()), r.read(), ""
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers.items()) if e.headers else {}, e.read(), "HTTPError: " + str(e)
    except Exception as e:
        return None, {}, b"", type(e).__name__ + ": " + str(e)
class Anchors(HTMLParser):
    def __init__(self): super().__init__(); self.a=[]; self.stack=[]; self.current=None
    def handle_starttag(self, tag, attrs):
        d=dict(attrs); cls=(d.get("class") or "").lower()
        active=any(self.stack) or any(x in cls for x in ("search-result","search_result","entry-title","post-title","article-title","result-item","item-result","news-item"))
        self.stack.append(active)
        if tag.lower()=="a" and active and d.get("href"): self.current=[d["href"],[]]
    def handle_data(self, data):
        if self.current: self.current[1].append(data)
    def handle_endtag(self, tag):
        if tag.lower()=="a" and self.current:
            self.a.append((self.current[0], " ".join(self.current[1]).strip())); self.current=None
        if self.stack: self.stack.pop()
def links(body, base, domain, semantic):
    """Extract only anchors in result/article containers, not navigation.

    BeautifulSoup handles void tags and malformed government-portal markup;
    the previous HTMLParser stack could lose nesting after a ``meta``/``img``
    tag and silently return no result anchors.
    """
    try:
        from bs4 import BeautifulSoup  # supplied by the project Python runtime
        soup=BeautifulSoup(body, "html.parser")
        anchors=soup.select(".search-result a[href], .search_result a[href], .entry-title a[href], .post-title a[href], .article-title a[href], .result-item a[href], .item-result a[href], .news-item a[href]")
    except Exception:
        return []
    out=[]
    for anchor in anchors:
        h=anchor.get("href"); t=anchor.get_text(" ",strip=True)
        if not h or not t: continue
        u=urllib.parse.urljoin(base,h); host=urllib.parse.urlparse(u).netloc.lower()
        if host==domain or host.endswith("."+domain): out.append((u,t))
    return list(dict.fromkeys(out))
def second_depth_links(body, base, domain):
    # This is a retrieval locator rule, intentionally not a relevance classifier.
    text=body.decode("utf-8", "replace")
    found=re.findall(r'''href=["']([^"'#]+)["']''', text, flags=re.I)
    out=[]
    for h in found:
        u=urllib.parse.urljoin(base,h); host=urllib.parse.urlparse(u).netloc.lower(); low=u.lower()
        if (host==domain or host.endswith("."+domain)) and (low.endswith(".pdf") or any(x in low for x in ("/document", "/publication", "/news/", "/tin-", "/van-ban"))): out.append(u)
    return list(dict.fromkeys(out))
def raw_capture(raw, stem, url, timeout):
    status, headers, body, error=fetch(url,timeout)
    bpath=raw/(stem+".body"); hpath=raw/(stem+".headers.json"); epath=raw/(stem+".error.txt")
    bc,bh=write(bpath,body); hc,hh=write(hpath,json.dumps(headers,ensure_ascii=False,indent=2).encode()); write(epath,(error or "NO_TRANSPORT_ERROR").encode())
    return {"requested_url":url,"http_status":"" if status is None else status,"error":error,"response_bytes":bc,"body_file":str(bpath.name),"body_sha256":bh,"headers_file":str(hpath.name),"headers_sha256":hh}, body
def dump_csv(path, rows, fields):
    with open(local(path),"w",encoding="utf-8",newline="") as f: w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--run-id"); ap.add_argument("--timeout-seconds",type=int,default=15); ap.add_argument("--workers",type=int,default=8); ap.add_argument("--max-pages",type=int,default=5); ap.add_argument("--max-sources-per-pair",type=int,default=50); args=ap.parse_args()
    if not 1<=args.max_pages<=5: ap.error("max-pages must be 1..5")
    queries=list(csv.DictReader(CATALOG.open(encoding="utf-8-sig",newline="")))
    if len(queries)!=12 or {x["query_id"] for x in queries}!=EXPECTED: raise SystemExit("Locked query catalogue validation failed")
    rid=args.run_id or "official-nonlegal-complete-"+dt.datetime.now().strftime("%Y%m%dT%H%M%S")
    run=OUTROOT/rid
    if run.exists(): raise SystemExit("Refusing to append to prior run")
    raw=run/"raw"; source_raw=run/"source-raw"
    # Windows legacy MAX_PATH applies to Path.mkdir in this deep audit tree.
    # The extended path is deliberate and applies only to this newly created run.
    os.makedirs(local(raw), exist_ok=False); os.makedirs(local(source_raw), exist_ok=False)
    params={"started_at":now(),"run_id":rid,"catalog":str(CATALOG),"catalog_sha256":digest(CATALOG.read_bytes()),"channels":list(CHANNELS),"queries":[x["query_id"] for x in queries],"direct_stop":"50 results or 5 internal pages; two consecutive pages without new semantic result URL","fallback_stop":"site: locator discovery: 50 results or 5 pages; two consecutive pages without new official URL","depth":2,"scope":"Raw retrieval only; no screening, eligibility, deduplication, extraction, PRISMA count, or substantive inference."}
    write_utf8(run/"run-parameters.json", json.dumps(params,ensure_ascii=False,indent=2)+"\n")
    direct=[]
    def do_direct(j):
        channel,domain,q,page,url=j; stem=f"direct-{safe(channel)}-{q['query_id']}-p{page:02d}"; meta,body=raw_capture(raw,stem,url,args.timeout_seconds); rs=links(body,url,domain,True) if body else []
        return {"channel_id":channel,"domain":domain,"query_id":q["query_id"],"query_family":q["query_family"],"query_verbatim":q["verbatim_query"],"method":"INTERNAL_PORTAL","page_attempt":page,"retrieved_at":now(),**meta,"semantic_result_urls":json.dumps([x[0] for x in rs],ensure_ascii=False),"semantic_result_count":len(rs)},rs
    def do_direct_pair(channel, domain, q, tpl):
        """Execute pages serially within one channel/query, respecting stop."""
        rows=[]; seen=set(); empty=0
        for page in range(1,args.max_pages+1):
            row, _ = do_direct((channel,domain,q,page,tpl.format(q=urllib.parse.quote(q["verbatim_query"],safe=""),page=page)))
            new=[u for u in json.loads(row["semantic_result_urls"]) if u not in seen]
            seen.update(new); empty=empty+1 if not new else 0
            row["new_semantic_urls"]=len(new)
            row["stop_assessment"]="LOCKED_PAGE_CAP" if page==args.max_pages else ("TWO_CONSECUTIVE_NO_NEW" if empty>=2 else "CONTINUE")
            rows.append(row)
            if row["stop_assessment"] != "CONTINUE": break
        return rows, seen
    direct_pairs=[(c,d,q,t) for c,(d,t) in CHANNELS.items() for q in queries]
    accepted={}; fallback_pairs=[]
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures={ex.submit(do_direct_pair,*pair):pair for pair in direct_pairs}
        for fut in as_completed(futures):
            rows, seen=fut.result(); direct.extend(rows); c,_,q,_=futures[fut]
            accepted[(c,q["query_id"])]=seen
            if not seen: fallback_pairs.append((c,CHANNELS[c][0],q))
    direct.sort(key=lambda x:(x["channel_id"],x["query_id"],x["page_attempt"]))
    dump_csv(run/"direct-portal-ledger.csv",direct,list(direct[0].keys()))
    # Fallback is separate raw locator discovery. Bing only locates; resulting URLs are accepted only if official-domain.
    fallback=[]
    def do_fallback(job):
        channel,domain,q,page=job; phrase=f'site:{domain} {q["verbatim_query"]}'; u="https://www.bing.com/search?"+urllib.parse.urlencode({"q":phrase,"first":1+(page-1)*10})
        stem=f"fallback-site-{safe(channel)}-{q['query_id']}-p{page:02d}"; meta,body=raw_capture(raw,stem,u,args.timeout_seconds)
        allurls=re.findall(r'''<a[^>]+href=["'](https?://[^"']+)["']''',body.decode("utf-8","replace"),flags=re.I)
        urls=[]
        for x in allurls:
            host=urllib.parse.urlparse(x).netloc.lower()
            if host==domain or host.endswith("."+domain): urls.append(x)
        return {"channel_id":channel,"domain":domain,"query_id":q["query_id"],"query_verbatim":q["verbatim_query"],"method":"SITE_FALLBACK_LOCATOR","page_attempt":page,"retrieved_at":now(),**meta,"official_urls":json.dumps(list(dict.fromkeys(urls)),ensure_ascii=False),"official_url_count":len(set(urls))}
    def do_fallback_pair(c,d,q):
        rows=[]; seen=set(); empty=0
        for p in range(1,args.max_pages+1):
            r=do_fallback((c,d,q,p)); new=[u for u in json.loads(r["official_urls"]) if u not in seen]
            seen.update(new); empty=empty+1 if not new else 0
            r["new_official_urls"]=len(new); r["stop_assessment"]="LOCKED_PAGE_CAP" if p==args.max_pages else ("TWO_CONSECUTIVE_NO_NEW" if empty>=2 else "CONTINUE")
            rows.append(r)
            if r["stop_assessment"] != "CONTINUE": break
        return rows,seen
    with ThreadPoolExecutor(max_workers=min(args.workers,4)) as ex:
        futures={ex.submit(do_fallback_pair,c,d,q):(c,d,q) for c,d,q in fallback_pairs}
        for fut in as_completed(futures):
            rows, seen=fut.result(); fallback.extend(rows); c,_,q=futures[fut]; accepted[(c,q["query_id"])].update(seen)
    fallback.sort(key=lambda x:(x["channel_id"],x["query_id"],x["page_attempt"]))
    fields=list(fallback[0].keys()) if fallback else ["channel_id","domain","query_id","query_verbatim","method","page_attempt","retrieved_at","requested_url","http_status","error","response_bytes","body_file","body_sha256","headers_file","headers_sha256","official_urls","official_url_count","new_official_urls","stop_assessment"]
    dump_csv(run/"site-fallback-ledger.csv",fallback,fields)
    discovered=[]
    for (c,qid),urls in sorted(accepted.items()):
        for u in sorted(urls)[:args.max_sources_per_pair]: discovered.append({"channel_id":c,"query_id":qid,"source_url":u,"status":"DISCOVERED_UNSCREENED"})
    dump_csv(run/"source-discovery.csv",discovered,["channel_id","query_id","source_url","status"])
    # First-depth acquisition, then one restrictive official same-domain traversal.
    acquisitions=[]
    def acquire(row,depth,parent=""):
        domain=CHANNELS[row["channel_id"]][0]; stem="src-"+hashlib.sha256((row["channel_id"]+"|"+row["query_id"]+"|"+row["source_url"]).encode()).hexdigest()[:22]+f"-d{depth}"; meta,body=raw_capture(source_raw,stem,row["source_url"],args.timeout_seconds)
        return {**row,"depth":depth,"parent_url":parent,"acquired_at":now(),**meta},body,domain
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        fs={ex.submit(acquire,r,1):r for r in discovered}
        for fut in as_completed(fs): acquisitions.append(fut.result()[0])
    depth2=[]
    for a in acquisitions:
        if str(a["http_status"]).startswith("2"):
            with open(local(source_raw/a["body_file"]), "rb") as fh: body=fh.read()
            domain=CHANNELS[a["channel_id"]][0]
            for u in second_depth_links(body,a["source_url"],domain)[:args.max_sources_per_pair]: depth2.append({"channel_id":a["channel_id"],"query_id":a["query_id"],"source_url":u,"status":"DISCOVERED_DEPTH_2_UNSCREENED","parent_url":a["source_url"]})
    unique2=[];seen2=set()
    for r in depth2:
        key=(r["channel_id"],r["query_id"],r["source_url"])
        if key not in seen2: seen2.add(key); unique2.append(r)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        fs={ex.submit(acquire,{k:v for k,v in r.items() if k!="parent_url"},2,r["parent_url"]):r for r in unique2}
        for fut in as_completed(fs): acquisitions.append(fut.result()[0])
    acquisitions.sort(key=lambda x:(x["channel_id"],x["query_id"],x["depth"],x["source_url"]))
    dump_csv(run/"source-acquisition-ledger.csv",acquisitions,list(acquisitions[0].keys()) if acquisitions else ["channel_id","query_id","source_url","status","depth","parent_url","acquired_at","requested_url","http_status","error","response_bytes","body_file","body_sha256","headers_file","headers_sha256"])
    hashes=[]
    for p in sorted(x for x in run.rglob("*") if x.is_file() and x.name!="sha256.csv"): hashes.append({"relative_path":str(p.relative_to(run)).replace("\\","/"),"sha256":file_digest(p),"bytes":p.stat().st_size})
    dump_csv(run/"sha256.csv",hashes,["relative_path","sha256","bytes"])
    has_document_sources = bool(acquisitions)
    status={"completed_at":now(),"expected_channel_query_pairs":len(CHANNELS)*len(queries),"direct_pages_captured":len(direct),"fallback_pairs":len(fallback_pairs),"fallback_pages_captured":len(fallback),"source_acquisition_attempts":len(acquisitions),"depth_2_acquisition_attempts":sum(x["depth"]==2 for x in acquisitions),"status":"RAW_NONLEGAL_PORTAL_FALLBACK_AND_SOURCE_RETRIEVAL_COMPLETE_UNSCREENED" if has_document_sources else "FAIL_CLOSED_NO_DOCUMENT_LEVEL_SOURCE_RETRIEVED","not_permitted_claims":["OFFICIAL_SEARCH_COMPLETE","saturation","absence of evidence","PRISMA identification count","eligibility","implementation/outcome finding"],"required_next_work":["human audit of portal/fallback semantics and coverage","repair or replace the locator parser before claiming source-level retrieval" if not has_document_sources else "global provenance and deduplication","gate review before screening"]}
    write_utf8(run/"completion-status.json", json.dumps(status,ensure_ascii=False,indent=2)+"\n")
    # Rebuild so terminal status is covered; hash manifest cannot cover itself.
    hashes=[]
    for p in sorted(x for x in run.rglob("*") if x.is_file() and x.name!="sha256.csv"): hashes.append({"relative_path":str(p.relative_to(run)).replace("\\","/"),"sha256":file_digest(p),"bytes":p.stat().st_size})
    dump_csv(run/"sha256.csv",hashes,["relative_path","sha256","bytes"])
    print(run)
if __name__=="__main__": main()
