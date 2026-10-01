"""Sync derived metadata after the version 0.8 edits (run from the repository root).

1. site-manifest.json pages: title, short_title, reading_time_min and summary from each page's frontmatter.
2. content/PAGE-IDS.md: page titles in the id lists from frontmatter.
3. data/key-numbers.json: `pages` = pages that embed the tile ({{kn:id}}) or list it in frontmatter key_numbers.
4. charts/chart-specs.json: `placement` = pages that embed the chart ({{chart:id}}) or list it in frontmatter charts.
Prints tiles and charts no page uses.
"""
import glob, json, re
import yaml

pages = {}
for f in sorted(glob.glob('content/*/*.md')):
    text = open(f, encoding='utf-8').read()
    if not text.startswith('---'):
        continue
    fm = yaml.safe_load(text.split('---', 2)[1])
    body = text.split('---', 2)[2]
    pages[fm['id']] = dict(fm=fm, body=body, path=f)

# 1. manifest
m = json.load(open('site-manifest.json', encoding='utf-8'))
for p in m['pages']:
    fm = pages[p['id']]['fm']
    for k in ('title', 'short_title', 'reading_time_min', 'summary'):
        if k in fm:
            p[k] = fm[k]
with open('site-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(m, f, ensure_ascii=False, indent=1)

# 2. PAGE-IDS.md
pid = 'content/PAGE-IDS.md'
lines = open(pid, encoding='utf-8').read().split('\n')
for i, line in enumerate(lines):
    mm = re.match(r'^- ([a-z0-9-]+): (.*)$', line)
    if mm and mm.group(1) in pages:
        title = str(pages[mm.group(1)]['fm']['title'])
        tail = re.search(r' \((uses|normative)[^)]*\)$', mm.group(2))
        lines[i] = f'- {mm.group(1)}: {title}' + (tail.group(0) if tail else '')
open(pid, 'w', encoding='utf-8').write('\n'.join(lines))

# 3 and 4. tile pages and chart placements
kn = json.load(open('data/key-numbers.json', encoding='utf-8'))
cs = json.load(open('charts/chart-specs.json', encoding='utf-8'))
use_kn, use_ch = {}, {}
for pid_, d in pages.items():
    found_kn = set(re.findall(r'\{\{kn:([a-z0-9-]+)\}\}', d['body'])) | set(d['fm'].get('key_numbers') or [])
    found_ch = set(re.findall(r'\{\{chart:([a-z0-9-]+)\}\}', d['body'])) | set(d['fm'].get('charts') or [])
    for k in found_kn:
        use_kn.setdefault(k, set()).add(pid_)
    for c in found_ch:
        use_ch.setdefault(c, set()).add(pid_)
for e in kn:
    used = sorted(use_kn.get(e['id'], []))
    if used:
        e['pages'] = used
    else:
        print('tile not used on any page:', e['id'])
for s in cs['charts']:
    used = use_ch.get(s['id'], set())
    if used:
        prim = [p for p in s.get('placement', []) if p in used]
        s['placement'] = prim + sorted(used - set(prim))
    else:
        print('chart not used on any page:', s['id'])
with open('data/key-numbers.json', 'w', encoding='utf-8') as f:
    json.dump(kn, f, ensure_ascii=False, indent=1)
with open('charts/chart-specs.json', 'w', encoding='utf-8') as f:
    json.dump(cs, f, ensure_ascii=False, indent=1)
print('synced', len(pages), 'pages,', len(kn), 'tiles,', len(cs['charts']), 'charts')
