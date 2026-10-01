#!/usr/bin/env python3
"""Check that the registers stay in sync after direct edits, and print the next free IDs.

Run from the repository root:  python3 tools/check_registers.py
Standard library only. Exit code 0 when no errors.

Checks:
- data/sources.csv and sources/sources.csv are identical copies.
- Every source ID is unique, has an anchor in Appendix R4 and an entry in bibliography.md, and vice versa.
- Open question (OQ-) and disagreement (DG-) IDs are unique and numbered without gaps.
- Every source ID used by key-numbers.json and chart-specs.json resolves.

It also prints the source prefixes already taken and the next free OQ and DG numbers,
so that a new research wave can pick an unused prefix.
"""
import csv, json, os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
errors = []

# 1. Source register copies
a = open('data/sources.csv', 'rb').read()
b = open('sources/sources.csv', 'rb').read()
if a != b:
    errors.append('data/sources.csv and sources/sources.csv differ (copy one onto the other)')

rows = list(csv.DictReader(open('data/sources.csv', encoding='utf-8')))
ids = [r['source_id'] for r in rows]
for i, n in Counter(ids).items():
    if n > 1:
        errors.append(f'sources.csv: duplicate source_id {i}')
idset = set(ids)
for r in rows:
    if r['prefix'] and not r['source_id'].startswith(r['prefix'] + '-'):
        errors.append(f'sources.csv: {r["source_id"]} has prefix column {r["prefix"]}')

# 2. Appendix R4 anchors and bibliography entries
r4 = open('content/03-appendices/app-r4-sources.md', encoding='utf-8').read()
anchors = re.findall(r'<a id="([^"]+)"></a>', r4)
for i, n in Counter(anchors).items():
    if n > 1:
        errors.append(f'app-r4-sources.md: duplicate anchor {i}')
for i in sorted(idset - set(anchors)):
    errors.append(f'app-r4-sources.md: no anchor for {i}')
for i in sorted(set(anchors) - idset):
    errors.append(f'app-r4-sources.md: anchor {i} has no row in sources.csv')

bib = set(re.findall(r'^- \*\*([A-Za-z0-9]+-[A-Za-z0-9]+)\.\*\*', open('sources/bibliography.md', encoding='utf-8').read(), re.M))
for i in sorted(idset - bib):
    errors.append(f'bibliography.md: no entry for {i}')
for i in sorted(bib - idset):
    errors.append(f'bibliography.md: entry {i} has no row in sources.csv')

# 3. Registers numbered without gaps
def check_seq(path, col, pfx):
    ids = [r[col] for r in csv.DictReader(open(path, encoding='utf-8'))]
    nums = []
    for i in ids:
        m = re.fullmatch(pfx + r'-(\d+)', i)
        if not m:
            errors.append(f'{path}: malformed id {i}')
        else:
            nums.append(int(m.group(1)))
    for i, n in Counter(ids).items():
        if n > 1:
            errors.append(f'{path}: duplicate id {i}')
    missing = sorted(set(range(1, max(nums) + 1)) - set(nums)) if nums else []
    if missing:
        errors.append(f'{path}: gaps in numbering, for example {pfx}-{missing[0]:03d}')
    return max(nums) if nums else 0

last_oq = check_seq('data/open_questions.csv', 'oq_id', 'OQ')
last_dg = check_seq('data/disagreements.csv', 'dg_id', 'DG')

# 4. Source IDs in stat tiles and charts
for k in json.load(open('data/key-numbers.json', encoding='utf-8')):
    for s in k.get('source_ids', []):
        if s not in idset:
            errors.append(f'key-numbers.json: {k["id"]} cites unknown source {s}')
for c in json.load(open('charts/chart-specs.json', encoding='utf-8'))['charts']:
    for s in c.get('source_ids', []) or []:
        if s not in idset:
            errors.append(f'chart-specs.json: {c["id"]} cites unknown source {s}')

prefixes = Counter(r['prefix'] for r in rows)
waves = Counter(r['wave'] for r in rows)
print(f'{len(ids)} sources in {len(prefixes)} prefixes; waves: ' + ', '.join(f'{w} ({n})' for w, n in sorted(waves.items(), key=lambda x: int(re.sub(r"\D", "", x[0]) or 0))))
print('Prefixes taken: ' + ' '.join(sorted(prefixes)))
print(f'Next free open question: OQ-{last_oq + 1:03d}; next free disagreement: DG-{last_dg + 1:03d}')
for e in errors:
    print('ERROR', e)
print(f'{len(errors)} errors')
sys.exit(1 if errors else 0)
