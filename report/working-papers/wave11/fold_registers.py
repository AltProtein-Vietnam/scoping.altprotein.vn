"""Fold wave 11 open questions and disagreements into the registers (run from the repository root).

Appends rows to data/open_questions.csv (from OQ-447) and data/disagreements.csv
(from DG-353), and rebuilds a "Food security, v0.8" section at the end of
Appendix R1 and R2. Safe to re-run: earlier wave 11 rows are removed and
rebuilt in line order, so IDs stay stable as long as the line files do not
change order. Updates to existing rows (closes_oq) are made by hand.

Do not re-run after consolidation: DG-373 and the status changes to OQ-004, OQ-009
and OQ-164 were added by hand and a re-run would drop DG-373.
"""
import csv, re

LINES = [
    # L1 last: it finished last, so the IDs of the other lines stay stable when it is added
    ('L2-disease-pandemic', 'Animal disease, zoonoses and pandemic risk'),
    ('L3-security-exposures', 'Other food-security exposures'),
    ('L4-protein-for-people', 'Protein for people: food balance sheets'),
    ('L1-meat-imports', 'Imported meat, offal and dairy'),
]
BASE = 'working-papers/wave11'
FIRST_OQ, FIRST_DG = 447, 353


def read(path):
    with open(path, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        return rd.fieldnames, list(rd)


def write(path, fields, rows, crlf):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\r\n' if crlf else '\n')
        w.writeheader()
        w.writerows(rows)


def is_crlf(path):
    with open(path, 'rb') as f:
        return b'\r\n' in f.readline()


def cell(s):
    return (s or '').replace('|', '/').replace('\n', ' ').strip()


oq_f, oqs = read('data/open_questions.csv')
dg_f, dgs = read('data/disagreements.csv')
oqs = [r for r in oqs if int(r['oq_id'][3:]) < FIRST_OQ]
dgs = [r for r in dgs if int(r['dg_id'][3:]) < FIRST_DG]
n_oq, n_dg = FIRST_OQ, FIRST_DG
r1_parts, r2_parts = [], []
for folder, name in LINES:
    note = f'{BASE}/{folder}/{folder}.md'
    try:
        _, loq = read(f'{BASE}/{folder}/open_questions.csv')
        _, ldg = read(f'{BASE}/{folder}/disagreements.csv')
    except FileNotFoundError:
        print('skip (not ready):', folder)
        continue
    r1_rows, r2_rows = [], []
    for q in loq:
        if not q.get('question', '').strip():
            continue
        oid = f'OQ-{n_oq}'; n_oq += 1
        pr = (q.get('priority') or '').strip().capitalize()
        closes = (q.get('closes_oq') or '').strip()
        notes = f'Added in v0.8 (wave 11, {folder}). Line priority: {pr or "not set"}.'
        if closes:
            notes += f' Partly answers or follows {closes}.'
        row = {k: '' for k in oq_f}
        row.update(oq_id=oid, topic=f'wave 11 {name.lower()}', question=q['question'].strip(),
                   why_it_matters=q.get('why_it_matters', '').strip(),
                   cheapest_way_to_close=q.get('cheapest_way_to_close', '').strip(),
                   owner_org_to_ask=q.get('owner_org_to_ask', '').strip(), from_note=note,
                   status='open', notes=notes)
        oqs.append(row)
        r1_rows.append(f"| {oid} | {pr} | {cell(row['question'])} | {cell(row['why_it_matters'])} | "
                       f"{cell(row['cheapest_way_to_close'])} | {cell(row['owner_org_to_ask'])} | open |")
    for d in ldg:
        if not d.get('topic', '').strip():
            continue
        did = f'DG-{n_dg}'; n_dg += 1
        row = {k: '' for k in dg_f}
        row.update(dg_id=did, topic=d['topic'].strip(), claim_a=d.get('claim_a', '').strip(),
                   claim_b=d.get('claim_b', '').strip(), position_taken=d.get('position_taken', '').strip(),
                   from_note=note, notes=('Version 0.8 (wave 11). ' + d.get('notes', '').strip()).strip())
        dgs.append(row)
        r2_rows.append(f"| {did} | {cell(row['topic'])} | {cell(row['claim_a'])} | {cell(row['claim_b'])} | "
                       f"{cell(row['position_taken'])} |")
    if r1_rows:
        r1_parts.append(f'### {name} ({len(r1_rows)})\n\n| ID | Priority | Question | Why it matters | '
                        f'Cheapest way to close it | Who to ask | Status |\n|---|---|---|---|---|---|---|\n'
                        + '\n'.join(r1_rows) + '\n')
    if r2_rows:
        r2_parts.append(f'### {name} (wave 11) ({len(r2_rows)})\n\n| ID | Topic | Claim A | Claim B | '
                        f'Position taken |\n|---|---|---|---|---|\n' + '\n'.join(r2_rows) + '\n')

write('data/open_questions.csv', oq_f, oqs, is_crlf('data/open_questions.csv'))
write('data/disagreements.csv', dg_f, dgs, is_crlf('data/disagreements.csv'))

for page, parts, total, title in (
        ('content/03-appendices/app-r1-open-questions.md', r1_parts, n_oq - FIRST_OQ, 'Food security, v0.8'),
        ('content/03-appendices/app-r2-disagreements.md', r2_parts, n_dg - FIRST_DG, 'Food security (wave 11), v0.8')):
    text = open(page, encoding='utf-8').read()
    text = re.sub(r'\n## Food security.*\Z', '', text, flags=re.S)
    if parts:
        text = text.rstrip('\n') + f'\n\n## {title} ({total})\n\n' + '\n'.join(parts)
    open(page, 'w', encoding='utf-8').write(text)

print(f'open questions: OQ-{FIRST_OQ} to OQ-{n_oq - 1} ({n_oq - FIRST_OQ}); '
      f'disagreements: DG-{FIRST_DG} to DG-{n_dg - 1} ({n_dg - FIRST_DG})')
