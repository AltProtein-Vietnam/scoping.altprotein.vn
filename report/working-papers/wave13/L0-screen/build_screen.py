#!/usr/bin/env python3
"""Build data/solutions_screen.csv from the wave 13 line screens (lead session, L0).

Run from the repository root:  python3 working-papers/wave13/L0-screen/build_screen.py
Standard library only. One row per GFI Solutions Database entry (GFI-001 to GFI-112, joined to
the catalogue) and one row per item screened by lines L7 to L9 (other sources).
"""
import csv, io, os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(ROOT)
W = 'working-papers/wave13'
VERDICTS = ['new candidate play', 'new candidate public good', 'strengthens existing', 'already covered',
            'global frontier, monitor', 'not for Vietnam now', 'out of scope']
SETS = {'L7': 'The Protein Project (EU)', 'L8': 'Berkeley Alt:Meat Lab', 'L9': 'Coefficient Giving grantees'}
FIELDS = ['item_id', 'source_set', 'title', 'item_type', 'owner', 'date', 'url', 'doi', 'platform', 'gfi_category',
          'value_chain_segment', 'gfi_maturity', 'line', 'in_scope', 'scope_note', 'related_gfi_nos', 'maps_to',
          'vietnam_angle', 'vietnam_evidence', 'verdict', 'verdict_note', 'signal_to_watch', 'source_ids',
          'evidence_label', 'confidence']
DASH = re.compile('[‒-―]')


def read(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def clean(v):
    v = (v or '').replace('\r', ' ').replace('\n', ' ').strip()
    v = DASH.sub(lambda m: ', ' if m.group(0) in '—―' else ' to ', v)
    return re.sub(r'\s{2,}', ' ', v)


cat = {r['gfi_no']: r for r in read(f'{W}/gfi_solutions_catalogue.csv')}
rows, seen = [], set()
for p in sorted(os.listdir(W)):
    f = f'{W}/{p}/data_solution_screen.csv'
    if not os.path.exists(f):
        continue
    for r in read(f):
        g = clean(r['gfi_no'])
        if g not in cat:
            sys.exit(f'{f}: unknown {g}')
        if g in seen:
            sys.exit(f'{g} screened twice')
        seen.add(g)
        c = cat[g]
        sids = [s.strip() for s in clean(r['source_ids']).replace(',', ';').split(';') if s.strip()]
        if 'GSD-01' not in sids:
            sids.insert(0, 'GSD-01')
        rows.append(dict(item_id=g, source_set='GFI Solutions Database', title=c['title'], item_type='solution', owner='Good Food Institute',
                         date=c['date'], url=c['url'], doi='', platform=c['platform'], gfi_category=c['category'],
                         value_chain_segment=c['segment'], gfi_maturity=c['gfi_maturity'], line=c['line'],
                         in_scope=clean(r['in_scope']), scope_note=clean(r['scope_note']), related_gfi_nos='',
                         maps_to=clean(r['maps_to']), vietnam_angle=clean(r['vietnam_angle']),
                         vietnam_evidence=clean(r['vietnam_evidence']), verdict=clean(r['verdict']),
                         verdict_note=clean(r['verdict_note']), signal_to_watch=clean(r['signal_to_watch']),
                         source_ids='; '.join(sids), evidence_label=clean(r['evidence_label']), confidence=clean(r['confidence'])))
missing = sorted(set(cat) - seen)
if missing:
    print('GFI entries not yet screened:', ', '.join(missing))
rows.sort(key=lambda r: r['item_id'])
for p in sorted(os.listdir(W)):
    f = f'{W}/{p}/data_item_screen.csv'
    if not os.path.exists(f):
        continue
    ln = p.split('-')[0]
    for r in read(f):
        rows.append(dict(item_id=clean(r['item_id']), source_set=SETS.get(ln, ln), title=clean(r['item_title']),
                         item_type=clean(r['item_type']), owner=clean(r['owner']), date=clean(r['date']), url=clean(r['url']),
                         doi=clean(r['doi']), platform='', gfi_category='', value_chain_segment='', gfi_maturity='', line=ln,
                         in_scope=clean(r['in_scope']), scope_note=clean(r['scope_note']),
                         related_gfi_nos=clean(r['related_gfi_nos']), maps_to=clean(r['maps_to']),
                         vietnam_angle=clean(r['vietnam_angle']), vietnam_evidence=clean(r['vietnam_evidence']),
                         verdict=clean(r['verdict']), verdict_note=clean(r['verdict_note']),
                         signal_to_watch=clean(r['signal_to_watch']), source_ids=clean(r['source_ids']).replace(',', ';'),
                         evidence_label=clean(r['evidence_label']), confidence=clean(r['confidence'])))
bad = [r['item_id'] for r in rows if r['verdict'] not in VERDICTS]
if bad:
    sys.exit('Verdicts outside the set: ' + ', '.join(bad))
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator='\n')
w.writeheader()
w.writerows(rows)
open('data/solutions_screen.csv', 'w', encoding='utf-8', newline='').write(buf.getvalue())
print(len(rows), 'rows')
for s in sorted(set(r['source_set'] for r in rows)):
    c = Counter(r['verdict'] for r in rows if r['source_set'] == s)
    print(s, sum(c.values()), {v: c[v] for v in VERDICTS if c[v]})
