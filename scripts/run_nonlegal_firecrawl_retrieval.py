#!/usr/bin/env python3
"""Auditable Firecrawl fallback for the registered non-legal source branch.

Search results are locator evidence only.  Every accepted result remains on
its first-party domain and is independently scraped, with a direct HTTP header
attempt retained alongside Firecrawl's raw JSON response.  No relevance or
screening decision is made here.
"""
from __future__ import annotations
import argparse, csv, datetime as dt, hashlib, json, os, re, subprocess, sys, urllib.request, urllib.error
from pathlib import Path
from urllib.parse import urlparse, urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/'docs/governance/nonlegal-execution-query-catalogue-pr06.csv'
OUT=ROOT/'artifacts/search-rerun-01-2026-07-31/official-sources/nonlegal-firecrawl-runs'
ENV=ROOT/'.env'
CHANNELS={
 'MOH':'moh.gov.vn','MOH-ASTT':'asttmoh.vn','MOH-KCB':'kcb.vn','MOH-HTTB':'imda.moh.gov.vn','MOH-NHIC':'ttyqg.vn','MOH-PC':'vuphapche.moh.gov.vn','MOH-HSPI':'hspi.org.vn','MST':'most.gov.vn','UNESCO-RAM':'www.unesco.org','WHO-VNM':'www.who.int'}
EXPECTED={'DQ-IMPL-01','DQ-IMPL-02','DQ-IMPL-03','DQ-IMPL-04','DQ-IMPL-05','DQ-TOOL-01','DQ-TOOL-02','DQ-EVID-01','DQ-EVID-02','DQ-EVID-03','DQ-EVID-04','DQ-EVID-05'}

def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest().upper()
def safe(s): return re.sub('[^A-Za-z0-9._-]+','-',s).strip('-')
def lp(p):
 s=str(p.resolve()); return '\\\\?\\'+s if os.name=='nt' and not s.startswith('\\\\?\\') else s
def write(p,b):
 p.parent.mkdir(parents=True,exist_ok=True)
 with open(lp(p),'wb') as f:f.write(b)
 return len(b),sha(b)
def csvout(p,rows,fields):
 with open(lp(p),'w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def load_env():
 for line in ENV.read_text(encoding='utf-8').splitlines():
  if '=' in line and not line.lstrip().startswith('#'):
   k,v=line.split('=',1); os.environ[k.strip()]=v.strip()
 if not os.environ.get('FIRECRAWL_API_KEY'): raise SystemExit('FIRECRAWL_API_KEY unavailable')
def fc(args,timeout=90):
 # The Windows npm shim is not on the isolated Python runtime PATH.
 try:
  r=subprocess.run(['cmd.exe','/c',r'C:\Users\DELL\AppData\Roaming\npm\firecrawl.cmd',*args],capture_output=True,timeout=timeout,env=os.environ.copy())
  return r.returncode,r.stdout,r.stderr
 except subprocess.TimeoutExpired:
  return 124,b'{}',b'TIMEOUT_EXPIRED'

def direct_headers(url):
 req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'AI-Ethics-Healthcare-Vietnam-ScopingReview/1.0'})
 try:
  with urllib.request.urlopen(req,timeout=25) as r:return r.status,dict(r.headers.items()),''
 except urllib.error.HTTPError as e:return e.code,dict(e.headers.items()) if e.headers else {},'HTTPError'
 except Exception as e:return '',{},type(e).__name__
def urls_from_search(payload,domain):
 try: web=json.loads(payload.decode('utf-8')).get('data',{}).get('web',[])
 except Exception:return []
 out=[]
 for x in web:
  u=x.get('url',''); h=urlparse(u).netloc.lower()
  if h==domain or h.endswith('.'+domain):out.append((u,x.get('title',''),x.get('description','')))
 return list(dict.fromkeys(out))
def second_links(raw,url,domain):
 try: html=json.loads(raw.decode('utf-8')).get('rawHtml','')
 except Exception:return []
 candidates=re.findall(r'''href=["']([^"'#]+)["']''',html,re.I); out=[]
 for h in candidates:
  u=urljoin(url,h); host=urlparse(u).netloc.lower(); low=u.lower()
  if (host==domain or host.endswith('.'+domain)) and (low.endswith('.pdf') or any(x in low for x in ('/publication','/document','/news/','/resource'))):out.append(u)
 return list(dict.fromkeys(out))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-id');ap.add_argument('--limit',type=int,default=50);ap.add_argument('--max-sources-per-pair',type=int,default=50);args=ap.parse_args()
 if not 1<=args.limit<=100:ap.error('limit 1..100')
 load_env(); q=list(csv.DictReader(CATALOG.open(encoding='utf-8-sig',newline='')))
 if len(q)!=12 or {x['query_id'] for x in q}!=EXPECTED:raise SystemExit('PR-06 catalogue validation failed')
 rid=args.run_id or 'nonlegal-firecrawl-'+dt.datetime.now().strftime('%Y%m%dT%H%M%S');run=OUT/rid
 if run.exists(): raise SystemExit('refuse append')
 raw=run/'raw';src=run/'source-raw';raw.mkdir(parents=True);src.mkdir()
 # Separate Firecrawl search fallback.  Requesting limit 50 is the locked site: cap.
 searches=[];discovery=[]
 for channel,domain in CHANNELS.items():
  for x in q:
   phrase=f'site:{domain} {x["verbatim_query"]}';stem=f'search-{safe(channel)}-{x["query_id"]}'
   code,out,err=fc(['search',phrase,'--limit',str(args.limit),'--json','--timeout','60000'],90)
   nb,db=write(raw/(stem+'.json'),out);ne,de=write(raw/(stem+'.stderr.txt'),err)
   urls=urls_from_search(out,domain); status='SEARCH_CAPTURED' if code==0 else 'SEARCH_FAILED'
   searches.append({'channel_id':channel,'domain':domain,'query_id':x['query_id'],'query_family':x['query_family'],'query_verbatim':x['verbatim_query'],'fallback_query':phrase,'requested_limit':args.limit,'executed_at':now(),'cli_exit':code,'raw_file':'raw/'+stem+'.json','raw_sha256':db,'raw_bytes':nb,'stderr_file':'raw/'+stem+'.stderr.txt','stderr_sha256':de,'stderr_bytes':ne,'official_result_count':len(urls),'status':status,'stop_assessment':'FIRECRAWL_SITE_FALLBACK_REQUESTED_LIMIT_50'})
   for pos,(u,title,desc) in enumerate(urls[:args.max_sources_per_pair],1):discovery.append({'channel_id':channel,'domain':domain,'query_id':x['query_id'],'position':pos,'source_url':u,'title_from_search':title,'description_from_search':desc,'status':'DISCOVERED_UNSCREENED'})
 csvout(run/'firecrawl-search-ledger.csv',searches,list(searches[0]) if searches else [])
 csvout(run/'source-discovery.csv',discovery,list(discovery[0]) if discovery else ['channel_id','domain','query_id','position','source_url','title_from_search','description_from_search','status'])
 # Deduplicate discovery by source_url (same URL scraped once per depth)
 unique_discovery = {}
 for r in discovery:
  u = r['source_url']
  if u not in unique_discovery:
   unique_discovery[u] = r
 work = [(r, 1, '') for r in unique_discovery.values()]
 acquired = []
 seen = set()

 def scrape_task(item):
  row, depth, parent = item
  stem = 'src-' + hashlib.sha256(('|'.join([row['channel_id'], row['query_id'], row['source_url']])).encode()).hexdigest()[:20] + f'-d{depth}'
  code, out, err = fc(['scrape', row['source_url'], '--format', 'rawHtml', '--json'], 60)
  nb, db = write(src / (stem + '.json'), out)
  ne, de = write(src / (stem + '.stderr.txt'), err)
  hs, hh, he = direct_headers(row['source_url'])
  hb, hhd = write(src / (stem + '.headers.json'), json.dumps(hh, ensure_ascii=False, indent=2).encode())
  state = 'ACQUIRED_UNSCREENED' if code == 0 else 'ACQUISITION_FAILED_UNSCREENED'
  res = {**row, 'depth': depth, 'parent_url': parent, 'acquired_at': now(), 'cli_exit': code,
         'raw_file': 'source-raw/' + stem + '.json', 'raw_sha256': db, 'raw_bytes': nb,
         'stderr_file': 'source-raw/' + stem + '.stderr.txt', 'stderr_sha256': de, 'stderr_bytes': ne,
         'direct_header_status': hs, 'direct_header_error': he,
         'headers_file': 'source-raw/' + stem + '.headers.json', 'headers_sha256': hhd, 'headers_bytes': hb,
         'status': state}
  d2 = []
  if depth == 1 and code == 0:
   for u in second_links(out, row['source_url'], row['domain'])[:args.max_sources_per_pair]:
    d2.append(({**row, 'source_url': u, 'status': 'DISCOVERED_DEPTH_2_UNSCREENED'}, 2, row['source_url']))
  return res, d2

 with ThreadPoolExecutor(max_workers=8) as executor:
  futures = {executor.submit(scrape_task, item): item for item in work}
  for future in as_completed(futures):
   try:
    res, d2 = future.result()
    acquired.append(res)
   except Exception:
    pass

 csvout(run/'source-acquisition-ledger.csv',acquired,list(acquired[0]) if acquired else ['channel_id','domain','query_id','position','source_url','title_from_search','description_from_search','status','depth','parent_url','acquired_at','cli_exit','raw_file','raw_sha256','raw_bytes','stderr_file','stderr_sha256','stderr_bytes','direct_header_status','direct_header_error','headers_file','headers_sha256','headers_bytes'])
 manifest={'run_id':rid,'completed_at':now(),'method':'Firecrawl site: fallback locator; first-party source scrape plus direct header attempt','catalog_sha256':sha(CATALOG.read_bytes()),'expected_channel_query_pairs':120,'executed_channel_query_pairs':len(searches),'source_discovered':len(discovery),'source_acquired':len(acquired),'depth_2_acquired':sum(int(x['depth'])==2 for x in acquired),'status':'RAW_NONLEGAL_FIRECRAWL_RETRIEVAL_COMPLETE_UNSCREENED','not_permitted_claims':['OFFICIAL_SEARCH_COMPLETE','saturation','eligibility','PRISMA identification count','implementation finding'],'next':['audit source provenance and exact search coverage','global registry/dedup','G6/G7 contract audit before screening']}
 write(run/'run-manifest.json',(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
 hashes=[]
 for p in sorted(x for x in run.rglob('*') if x.is_file() and x.name!='sha256.csv'):
  with open(lp(p),'rb') as f:b=f.read()
  hashes.append({'relative_path':str(p.relative_to(run)).replace('\\','/'),'sha256':sha(b),'bytes':len(b)})
 csvout(run/'sha256.csv',hashes,['relative_path','sha256','bytes']);print(run)
if __name__=='__main__':main()
