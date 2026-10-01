"""Fold wave 11 line sources into the study registers (run from the repository root).

Appends new rows to data/sources.csv (and copies it to sources/sources.csv),
adds one section per prefix to Appendix R4 and a "Food-security round
(version 0.8)" section to sources/bibliography.md. Safe to re-run: rows and
sections already present are rebuilt, not duplicated. Prints duplicate URLs
and DOIs against earlier sources so they can be noted.

Count tables and intro sentences in R4 and the bibliography are updated by
hand after running this script.
"""
import csv, os, re, shutil, sys

LINES = [
    # folder, prefix, agent, stream name for R4 heading
    ('L1-meat-imports', 'MIM', 'MEAT-IMPORTS', 'Imported meat, offal and dairy'),
    ('L2-disease-pandemic', 'PAN', 'DISEASE', 'Animal disease, zoonoses and pandemic risk'),
    ('L3-security-exposures', 'SEC', 'SECURITY', 'Other food-security exposures'),
    ('L4-protein-for-people', 'FBS', 'FOOD-BALANCE', 'Protein for people: food balance sheets'),
]
BASE = 'working-papers/wave11'
TYPE_ORDER = ['gov/statistics', 'law', 'intergovernmental', 'peer-reviewed', 'preprint', 'company',
              'press', 'advocacy', 'market-research', 'database', 'other']
DASHES = re.compile('[–—]')

with open('data/sources.csv', newline='', encoding='utf-8') as f:
    rd = csv.DictReader(f)
    FIELDS = rd.fieldnames
    rows = list(rd)
existing = {r['source_id'] for r in rows}
by_url = {}
for r in rows:
    for key in (r['url'].strip().rstrip('/'), r['doi'].strip().lower()):
        if key:
            by_url.setdefault(key, r['source_id'])

new_rows, sections = [], []
for folder, pfx, agent, stream in LINES:
    path = os.path.join(BASE, folder, 'sources.csv')
    if not os.path.exists(path):
        print('skip (no sources yet):', folder)
        continue
    with open(path, newline='', encoding='utf-8') as f:
        line_rows = list(csv.DictReader(f))
    sec = []
    for s in line_rows:
        sid = s['source_id'].strip()
        if not sid.startswith(pfx + '-'):
            sys.exit(f'unexpected id {sid} in {folder}')
        for k, v in s.items():
            if v and DASHES.search(v):
                s[k] = DASHES.sub(' to ' if k in ('date',) else ', ', v)
        for key in (s.get('url', '').strip().rstrip('/'), s.get('doi', '').strip().lower()):
            if key and key in by_url and by_url[key] != sid:
                print(f'note: {sid} has the same URL or DOI as {by_url[key]}')
        row = {k: '' for k in FIELDS}
        row.update({k: s.get(k, '') for k in FIELDS if k in s})
        row.update(source_id=sid, prefix=pfx, agent=agent, wave='wave11',
                   from_note=f'{BASE}/{folder}/{folder}.md')
        if sid in existing:
            for r in rows:
                if r['source_id'] == sid:
                    r.update(row)
        else:
            new_rows.append(row)
        sec.append(row)
    sections.append((pfx, stream, sec))

rows.extend(new_rows)
with open('data/sources.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
shutil.copyfile('data/sources.csv', 'sources/sources.csv')
print(f'sources.csv: {len(new_rows)} rows added, {len(rows)} in total')


def entry(r, anchor):
    cit = r['citation'].strip()
    typ = r['source_type'].strip()
    acc = r['accessed'].strip()
    tail = f' Accessed {acc}.' if acc and 'ccessed' not in cit else ''
    head = f'- <a id="{r["source_id"]}"></a>**{r["source_id"]}.** ' if anchor else f'- **{r["source_id"]}.** '
    return f'{head}{cit}{tail} Type: {typ}.'


# Appendix R4: one section per prefix, appended at the end (rebuilt on re-run)
r4 = 'content/03-appendices/app-r4-sources.md'
text = open(r4, encoding='utf-8').read()
for pfx, stream, sec in sections:
    text = re.sub(rf'\n## {pfx}: .*?(?=\n## |\Z)', '', text, flags=re.S)
for pfx, stream, sec in sections:
    body = '\n'.join(entry(r, True) for r in sec)
    text = text.rstrip('\n') + f'\n\n## {pfx}: {stream} (wave 11), v0.8 ({len(sec)})\n\n{body}\n'
open(r4, 'w', encoding='utf-8').write(text)

# Bibliography: one round section at the end, grouped by source type
bib = 'sources/bibliography.md'
text = open(bib, encoding='utf-8').read()
text = re.sub(r'\n## Food-security round \(version 0\.8\).*\Z', '', text, flags=re.S)
allrows = [r for _, _, sec in sections for r in sec]
prefixes = '; '.join(f'{p} = {s.lower()}' for p, s, _ in sections)
out = [f'\n\n## Food-security round (version 0.8)\n\nID prefixes: {prefixes}. All wave 11.\n']
types = sorted({r['source_type'] for r in allrows}, key=lambda t: TYPE_ORDER.index(t) if t in TYPE_ORDER else 99)
for t in types:
    grp = [r for r in allrows if r['source_type'] == t]
    out.append(f'\n### {t} ({len(grp)})\n\n' + '\n'.join(entry(r, False) for r in grp) + '\n')
text = text.rstrip('\n') + ''.join(out)
open(bib, 'w', encoding='utf-8').write(text)

from collections import Counter
print('wave 11 by type:', dict(Counter(r['source_type'] for r in allrows)))
print('wave 11 by prefix:', {p: len(s) for p, _, s in sections})
