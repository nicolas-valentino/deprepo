#!/usr/bin/env python3
"""Check curated external URLs without treating access restrictions as dead links."""
import argparse
import concurrent.futures
import json
import urllib.error
import urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def check(item):
    id, source = item
    url = source['url']
    result = {'source':id,'url':url}
    for method in ('HEAD','GET'):
        try:
            request = urllib.request.Request(url,method=method,headers={'User-Agent':'Deprepo-LinkCheck/1.0'})
            with urllib.request.urlopen(request,timeout=12) as response:
                return dict(result,status='reachable',http=response.status,final_url=response.url)
        except urllib.error.HTTPError as error:
            if method=='HEAD' and error.code in (403,405):
                continue
            return dict(result,status='broken' if error.code in (404,410) else 'inaccessible',http=error.code)
        except (OSError,ValueError) as error:
            return dict(result,status='inaccessible',error=type(error).__name__)
    return dict(result,status='inaccessible')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    output=args.output.resolve()
    if output==ROOT or ROOT in output.parents:
        p.error('Store runtime link reports outside the checkout; redact before publishing')
    sources=json.loads((ROOT/'resources/sources.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results=list(pool.map(check,[(k,v) for k,v in sources.items() if 'url' in v]))
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    counts={status:sum(r['status']==status for r in results) for status in ('reachable','broken','inaccessible')}
    print(json.dumps(counts))
    return int(bool(counts['broken']))
if __name__=='__main__':
    raise SystemExit(main())
