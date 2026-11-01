#!/usr/bin/env python3
"""Dependency-free portfolio smoke checks; intentionally conservative."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
PAGES=list(ROOT.glob("*.html"))
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.links=[];self.images=[];self.headings=[];self.lang=False;self.main=0
    def handle_starttag(self,t,a):
        a=dict(a)
        if "id" in a:self.ids.append(a["id"])
        if t=="a" and "href" in a:self.links.append(a["href"])
        if t=="img":self.images.append(a)
        if t=="h1":self.headings.append("h1")
        if t=="html" and a.get("lang"):self.lang=True
        if t=="main":self.main+=1
issues=[]
if not PAGES:issues.append("No site pages found")
parsed={}
for p in PAGES:
    parser=Page()
    try:parser.feed(p.read_text(encoding="utf-8"))
    except Exception as e:issues.append(f"{p.name}: invalid input: {e}")
    parsed[p.name]=parser
    if not parser.lang:issues.append(f"{p.name}: missing html lang")
    if parser.main!=1:issues.append(f"{p.name}: expected one main landmark, got {parser.main}")
    if parser.headings.count("h1")!=1:issues.append(f"{p.name}: expected one h1")
    for id,count in Counter(parser.ids).items():
        if count>1:issues.append(f"{p.name}: duplicated id {id}")
    for img in parser.images:
        if "alt" not in img:issues.append(f"{p.name}: image missing alt")
for p in PAGES:
    for link in parsed[p.name].links:
        u=urlsplit(link)
        if u.scheme or u.netloc or link.startswith(("mailto:","tel:","javascript:")):continue
        target=(ROOT/unquote(u.path)) if u.path else p
        if target.is_dir():target=target/"index.html"
        if not target.exists():issues.append(f"{p.name}: missing target {link}")
        if u.fragment and target.suffix==".html" and target.exists():
            a=parsed.get(target.name)
            if a and u.fragment not in a.ids:issues.append(f"{p.name}: missing anchor {link}")
if issues:
    print("\n".join("ERROR: "+s for s in issues))
    raise SystemExit(1)
print(f"Validated {len(PAGES)} HTML pages: local links, anchors, landmarks, h1, lang and image alt attributes.")
