#!/usr/bin/env python3
"""Fold the wave 13 line registers into the study (lead session, L0).

Run once from the repository root:  python3 working-papers/wave13/L0-screen/fold_registers.py
Standard library only. It refuses to run if any wave 13 source is already registered.

It appends, for every line folder listed in LINES that has the file:
- sources.csv rows to data/sources.csv (then copies it to sources/sources.csv),
  Appendix R4 (one section per prefix, counts table, intro) and sources/bibliography.md;
- open_questions.csv rows to data/open_questions.csv and Appendix R1 (new OQ numbers);
- disagreements.csv rows to data/disagreements.csv and Appendix R2 (new DG numbers).
It writes working-papers/wave13/L0-screen/id_map.csv (line, local row, new OQ or DG id).
"""
import csv, io, os, re, sys
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(ROOT)
W = 'working-papers/wave13'
VERSION = 'v0.10'

# folder, prefix, agent, stream name for R4 and R1/R2 headings
LINES = [
    ('L0-screen', 'GSD', 'SOLUTIONS_SCREEN', 'GFI Solutions Database and ASAP reports'),
    ('L1-plant-based', 'SLP', 'SOLUTIONS_PLANT', 'Solutions screen: plant-based'),
    ('L2-fermentation', 'SLF', 'SOLUTIONS_FERMENTATION', 'Solutions screen: fermentation'),
    ('L3-cultivated', 'SLC', 'SOLUTIONS_CULTIVATED', 'Solutions screen: cultivated meat'),
    ('L4-alt-seafood', 'SLS', 'SOLUTIONS_SEAFOOD', 'Solutions screen: alternative seafood'),
    ('L5-capital-markets', 'SLK', 'SOLUTIONS_CAPITAL', 'Solutions screen: capital, markets and business services'),
    ('L6-research-workforce', 'SLW', 'SOLUTIONS_WORKFORCE', 'Solutions screen: research system and workforce'),
    ('L7-protein-project-eu', 'PPE', 'PROTEIN_PROJECT_EU', 'The Protein Project (EU) publications'),
    ('L8-berkeley-alt-meat-lab', 'AML', 'BERKELEY_ALT_MEAT_LAB', 'Berkeley Alt:Meat Lab'),
    ('L9-coefficient-giving-grantees', 'CGG', 'COEFFICIENT_GIVING', 'Coefficient Giving grantees with published research'),
]
ROUND_COL = 'Solutions screen (wave 13)'
DASH = re.compile('[‒-―]')


def read(path):
    with open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def clean(v):
    v = (v or '').replace('\r', ' ').replace('\n', ' ').strip()
    v = DASH.sub(lambda m: ', ' if m.group(0) in '—―' else ' to ', v)
    return re.sub(r'\s{2,}', ' ', v)


def paper(folder):
    return f'{W}/{folder}/{folder}.md'


def write_csv(path, fields, rows):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, lineterminator='\n')
    w.writeheader()
    w.writerows(rows)
    open(path, 'w', encoding='utf-8', newline='').write(buf.getvalue())


lines = [l for l in LINES if os.path.exists(f'{W}/{l[0]}/sources.csv')]
missing = [l[0] for l in LINES if l not in lines]
if missing:
    print('Line folders without sources.csv (skipped):', ', '.join(missing))

# ---------- 1. sources ----------
src_path = 'data/sources.csv'
src = read(src_path)
fields = list(src[0].keys())
have = {r['source_id'] for r in src}
new_src = []
for folder, pfx, agent, name in lines:
    for r in read(f'{W}/{folder}/sources.csv'):
        sid = r['source_id'].strip()
        if not sid.startswith(pfx + '-'):
            sys.exit(f'{folder}: {sid} does not use prefix {pfx}')
        if sid in have:
            sys.exit(f'{sid} is already registered: the fold has run before. Reset the registers first.')
        row = {k: '' for k in fields}
        for k in ['citation', 'title', 'author_or_publisher', 'date', 'url', 'doi', 'source_type', 'accessed', 'notes']:
            row[k] = clean(r.get(k, ''))
        row.update(source_id=sid, prefix=pfx, agent=agent, wave='wave13', from_note=paper(folder), status_v0_9='active')
        if not row['citation']:
            sys.exit(f'{sid} has no citation')
        new_src.append(row)
write_csv(src_path, fields, src + new_src)
open('sources/sources.csv', 'w', encoding='utf-8', newline='').write(open(src_path, encoding='utf-8').read())
active = [r for r in src + new_src if r['status_v0_9'] == 'active']
n_active = len(active)
print(f'sources: +{len(new_src)}; active total {n_active}')

# ---------- 2. Appendix R4 ----------
r4p = 'content/03-appendices/app-r4-sources.md'
r4 = open(r4p, encoding='utf-8').read()
blocks = []
for folder, pfx, agent, name in lines:
    rows = [r for r in new_src if r['prefix'] == pfx]
    if not rows:
        continue
    blocks.append(f'## {pfx}: {name} (wave 13), {VERSION} ({len(rows)})\n\n' +
                  '\n'.join(f'- <a id="{r["source_id"]}"></a>**{r["source_id"]}.** {r["citation"]}' for r in rows) + '\n')
r4 = r4.rstrip('\n') + '\n\n' + '\n'.join(blocks)

# counts table: rebuild from sources.csv (active rows), one column per round
ROUNDS = OrderedDict([
    ('Version 0.1 (waves 1 and 2)', ['wave1', 'wave2']),
    ('Futures round (waves 3 to 5)', ['wave3', 'wave4', 'wave5']),
    ('Demand round (wave 6)', ['wave6']),
    ('Actor check and expansion (waves 7 to 9)', ['wave7', 'wave8', 'wave9']),
    ('Prologue (wave 10)', ['wave10']),
    ('Food security (wave 11)', ['wave11']),
    ('Regional deals (wave 12)', ['wave12']),
    (ROUND_COL, ['wave13']),
])
cnt = Counter((r['source_type'], r['wave']) for r in active)
types = Counter(r['source_type'] for r in active)
hdr = '| Source type | ' + ' | '.join(ROUNDS) + ' | Total |'
sep = '|---' * (len(ROUNDS) + 2) + '|'
body = []
for t, tot in sorted(types.items(), key=lambda x: (-x[1], x[0])):
    cells = [str(sum(cnt[(t, w)] for w in ws)) for ws in ROUNDS.values()]
    body.append(f'| {t} | ' + ' | '.join(cells) + f' | {tot} |')
allrow = '| **All** | ' + ' | '.join(str(sum(1 for r in active if r['wave'] in ws)) for ws in ROUNDS.values()) + f' | {n_active} |'
table = '\n'.join([hdr, sep] + body + [allrow])
r4, k = re.subn(r'\| Source type \|.*?\n\| \*\*All\*\*[^\n]*', table, r4, count=1, flags=re.S)
assert k == 1, 'R4 counts table not found'
n13 = sum(1 for r in active if r['wave'] == 'wave13')
r4 = r4.replace('and those of the regional deals round (wave 12) on 15 October 2026.',
                'and those of the regional deals round (wave 12) and the solutions screen (wave 13) on 15 October 2026.')
r4 = re.sub(r'All [\d,]+ sources behind the report \(', f'All {n_active:,} sources behind the report (', r4, count=1)
r4 = r4.replace('and 50 by the regional deals round of v0.9)', f'50 by the regional deals round of v0.9 and {n13} by the solutions screen of v0.10)')
open(r4p, 'w', encoding='utf-8').write(r4)

# ---------- 3. bibliography ----------
bp = 'sources/bibliography.md'
bib = open(bp, encoding='utf-8').read()
pfx_line = '; '.join(f'{pfx} = {name[0].lower() + name[1:]}' for folder, pfx, agent, name in lines if any(r['prefix'] == pfx for r in new_src))
by_type = OrderedDict()
for r in new_src:
    by_type.setdefault(r['source_type'], []).append(r)
sec = [f'## Solutions screen round (version 0.10)\n\nID prefixes: {pfx_line}. All wave 13, accessed 15 October 2026 unless an entry says otherwise.\n']
for t, rows in sorted(by_type.items(), key=lambda x: (-len(x[1]), x[0])):
    sec.append(f'### {t} ({len(rows)})\n\n' + '\n'.join(f'- **{r["source_id"]}.** {r["citation"]}' for r in rows) + '\n')
bib = bib.rstrip('\n') + '\n\n' + '\n'.join(sec)
bib = re.sub(r'^[\d,]+ sources cited in the research', f'{n_active:,} sources cited in the research', bib, count=1, flags=re.M)
bib = bib.replace('version 0.9, October 2026)', 'version 0.9, October 2026, with the version 0.10 additions)', 1)
bib = bib.replace('and 50 from the regional deals round of version 0.9 (wave 12, accessed 15 October 2026); the last five rounds are listed at the end.',
                  f'50 from the regional deals round of version 0.9 (wave 12, accessed 15 October 2026) and {n13} from the solutions screen of version 0.10 (wave 13, accessed 15 October 2026); the last six rounds are listed at the end.')
open(bp, 'w', encoding='utf-8').write(bib)

# ---------- 4. open questions ----------
oqp = 'data/open_questions.csv'
oq = read(oqp)
oqf = list(oq[0].keys())
nxt = max(int(r['oq_id'][3:]) for r in oq) + 1
first_oq = nxt
idmap = []
r1_groups = []
for folder, pfx, agent, name in lines:
    p = f'{W}/{folder}/open_questions.csv'
    if not os.path.exists(p):
        continue
    rows = [r for r in read(p) if clean(r.get('question'))]
    grp = []
    for i, r in enumerate(rows, 1):
        oid = f'OQ-{nxt:03d}'
        nxt += 1
        note = f'Added in {VERSION} (solutions screen, wave 13, {folder.split("-")[0]}).'
        if clean(r.get('priority')):
            note += f' Line priority: {clean(r["priority"]).lower()}.'
        if clean(r.get('closes_oq')):
            note += f' Follows on from {clean(r["closes_oq"])}.'
        row = {k: '' for k in oqf}
        row.update(oq_id=oid, topic=f'{name[0].lower() + name[1:]} (wave 13)', question=clean(r['question']),
                   why_it_matters=clean(r.get('why_it_matters')), cheapest_way_to_close=clean(r.get('cheapest_way_to_close')),
                   owner_org_to_ask=clean(r.get('owner_org_to_ask')), from_note=paper(folder).replace('working-papers/', ''),
                   status='open', notes=note, status_v0_9='active')
        oq.append(row)
        grp.append(row)
        idmap.append((folder, 'open_questions.csv', i, oid))
    if grp:
        esc = lambda s: s.replace('|', '\\|')
        r1_groups.append(f'## {name} (wave 13), {VERSION} ({len(grp)})\n\n| ID | Priority | Question | Why it matters | Cheapest way to close it | Who to ask | Status |\n|---|---|---|---|---|---|---|\n' +
                         '\n'.join(f'| {g["oq_id"]} |  | {esc(g["question"])} | {esc(g["why_it_matters"])} | {esc(g["cheapest_way_to_close"])} | {esc(g["owner_org_to_ask"])} | open |' for g in grp) + '\n')
write_csv(oqp, oqf, oq)
last_oq = nxt - 1
r1p = 'content/03-appendices/app-r1-open-questions.md'
r1 = open(r1p, encoding='utf-8').read().rstrip('\n') + '\n\n' + '\n'.join(r1_groups)
act = [r for r in oq if r['status_v0_9'] == 'active']
st = Counter(r['status'] for r in act)
r1 = re.sub(r'All [\d,]+ open questions left by the research', f'All {len(act)} open questions left by the research', r1, count=1)
r1 = re.sub(r'Status: \d+ open; \d+ partly closed; \d+ closed\.', f'Status: {st["open"]} open; {st["partly closed"]} partly closed; {st["closed"]} closed.', r1, count=1)
open(r1p, 'w', encoding='utf-8').write(r1)
print(f'open questions: OQ-{first_oq:03d} to OQ-{last_oq:03d}; active {len(act)}; {dict(st)}')

# ---------- 5. disagreements ----------
dgp = 'data/disagreements.csv'
dg = read(dgp)
dgf = list(dg[0].keys())
nxt = max(int(r['dg_id'][3:]) for r in dg) + 1
first_dg = nxt
r2_groups = []
for folder, pfx, agent, name in lines:
    p = f'{W}/{folder}/disagreements.csv'
    if not os.path.exists(p):
        continue
    rows = [r for r in read(p) if clean(r.get('topic'))]
    grp = []
    for i, r in enumerate(rows, 1):
        did = f'DG-{nxt:03d}'
        nxt += 1
        row = {k: '' for k in dgf}
        notes = clean(r.get('notes'))
        row.update(dg_id=did, topic=clean(r['topic']), claim_a=clean(r['claim_a']), claim_b=clean(r['claim_b']),
                   position_taken=clean(r['position_taken']), from_note=paper(folder).replace('working-papers/', ''),
                   notes=(notes + ' ' if notes else '') + f'Added in {VERSION} (solutions screen, wave 13, {folder.split("-")[0]}).',
                   status_v0_9='active')
        dg.append(row)
        grp.append(row)
        idmap.append((folder, 'disagreements.csv', i, did))
    if grp:
        esc = lambda s: s.replace('|', '\\|')
        r2_groups.append(f'## {name} (wave 13), {VERSION} ({len(grp)})\n\n| ID | Topic | Claim A | Claim B | Position taken |\n|---|---|---|---|---|\n' +
                         '\n'.join(f'| {g["dg_id"]} | {esc(g["topic"])} | {esc(g["claim_a"])} | {esc(g["claim_b"])} | {esc(g["position_taken"])} |' for g in grp) + '\n')
write_csv(dgp, dgf, dg)
last_dg = nxt - 1
r2p = 'content/03-appendices/app-r2-disagreements.md'
r2 = open(r2p, encoding='utf-8').read().rstrip('\n') + '\n\n' + '\n'.join(r2_groups)
n_dg = sum(1 for r in dg if r['status_v0_9'] == 'active')
r2 = re.sub(r'All [\d,]+ cases where sources disagree', f'All {n_dg} cases where sources disagree', r2, count=1)
open(r2p, 'w', encoding='utf-8').write(r2)
print(f'disagreements: DG-{first_dg:03d} to DG-{last_dg:03d}; active {n_dg}')

write_csv(f'{W}/L0-screen/id_map.csv', ['line', 'file', 'row', 'new_id'],
          [dict(line=a, file=b, row=c, new_id=d) for a, b, c, d in idmap])
