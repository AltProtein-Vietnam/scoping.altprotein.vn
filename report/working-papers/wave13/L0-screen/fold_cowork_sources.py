#!/usr/bin/env python3
"""Register the sources from the Coefficient Giving browser check (wave 13, L9 reconciliation).

Run once from the repository root:  python3 working-papers/wave13/L0-screen/fold_cowork_sources.py
Appends CGG-19 to CGG-24 to data/sources.csv (and its copy), Appendix R4 (CGG section, counts table,
summary) and sources/bibliography.md (solutions screen round). Refuses to run twice.
"""
import csv, io, os, re, sys
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(ROOT)
NOTE = 'working-papers/wave13/L9-coefficient-giving-grantees/cowork/RECONCILIATION.md'
NEW = [
    ('CGG-19', 'Coefficient Giving. Grants list for the focus area "Alternatives to Animal Products", Farm Animal Welfare Fund: 61 grants, September 2016 to July 2026. https://coefficientgiving.org/funds/farm-animal-welfare/#grants-alternatives-to-animal-products . Read in a separate browser session (Claude Cowork) on 15 October 2026, because the site refused automated access from the research environment (HTTP 403); grantee, title, amount and month as shown on the site; files in working-papers/wave13/L9-coefficient-giving-grantees/cowork/. Type: database.',
     'Grants list: Alternatives to Animal Products', 'Coefficient Giving', '2026-10', 'https://coefficientgiving.org/funds/farm-animal-welfare/#grants-alternatives-to-animal-products', '', 'database',
     'Site count "Found 61 grants" matches the rows read; total USD 49,310,121 (our sum); grant types are the browser session\'s classification from titles, not the funder\'s.'),
    ('CGG-20', 'Caputo, V., Lusk, J.L. and Blaustein-Rejto, D. "Plant-Based versus Conventional Meat: Substitution, Complementarity, and Market Impacts." Working paper, Breakthrough Institute, 2023 (survey August 2023). https://static1.squarespace.com/static/502c267524aca01df475f9ec/t/6526c7450f0d7e4a89d8c158/1697040198414/Manuscript+-+PBMAs+-FINAL.pdf . Accessed 2026-10-15. "This work was partly funded by Open Philanthropy and Breakthrough Institute." Type: preprint.',
     'Plant-Based versus Conventional Meat: Substitution, Complementarity, and Market Impacts', 'Breakthrough Institute; Michigan State University; Oklahoma State University', '2023', 'https://static1.squarespace.com/static/502c267524aca01df475f9ec/t/6526c7450f0d7e4a89d8c158/1697040198414/Manuscript+-+PBMAs+-FINAL.pdf', '', 'preprint',
     'US basket-based choice experiment (1,011 food shoppers at home) and an equilibrium displacement model; output of Coefficient Giving grant CG-G019 (USD 50,000, June 2022).'),
    ('CGG-21', 'Caputo, V., Lusk, J.L. and Blaustein-Rejto, D. (2025). Plant-Based versus Conventional Meat in Food Away From Home Settings: Substitution, Complementarity, and Market Impacts. Agricultural Economics 56(4): 587 to 603. https://doi.org/10.1111/agec.70002 . Crossref metadata read 2026-10-15; full text and funding statement not read. Type: peer-reviewed.',
     'Plant-Based versus Conventional Meat in Food Away From Home Settings: Substitution, Complementarity, and Market Impacts', 'Agricultural Economics (Wiley)', '2025-03-23', 'https://doi.org/10.1111/agec.70002', '10.1111/agec.70002', 'peer-reviewed',
     'Peer-reviewed version of CGG-20 for restaurant settings; metadata only (Low).'),
    ('CGG-22', 'Food Frontier, with research by Mintel and Te Puna Whakaaronui. "Alternative Proteins and Asia." 2023. https://www.foodfrontier.org/resource/alternative-proteins-and-asia/ . Accessed 2026-10-15. Report page: 11 Asian markets assessed (not named on the page), top five China, Singapore, South Korea, Thailand and Japan; 5,000 consumers; no funder named; Vietnam not mentioned. Type: advocacy.',
     'Alternative Proteins and Asia', 'Food Frontier', '2023', 'https://www.foodfrontier.org/resource/alternative-proteins-and-asia/', '', 'advocacy',
     'Grantee output in the period of Coefficient Giving grant CG-G020 (USD 500,000, August 2022, "Promoting Plant-Based Meat Alternatives in Asia"); the report does not name the funder. Whether Vietnam was among the 11 markets is not shown (OQ-524).'),
    ('CGG-23', 'Mendez, S. and McAuliffe, W. "Technical feasibility of egg ingredient reduction/replacement in US foods." Rethink Priorities, 14 December 2025. https://rethinkpriorities.org/research-area/egg-ingredient-reduction-us-foods/ . Accessed 2026-10-15. "This report was commissioned by Coefficient Giving (formerly Open Philanthropy)." Type: other.',
     'Technical feasibility of egg ingredient reduction/replacement in US foods', 'Rethink Priorities', '2025-12-14', 'https://rethinkpriorities.org/research-area/egg-ingredient-reduction-us-foods/', '', 'other',
     'About 80% of sampled US products moderately difficult and about 20% difficult to replace (low confidence, as stated); about 8% of global egg production is processed; cites an IMPROVE (2023) test of 10 plant protein ingredients in which potato protein came closest to egg white.'),
    ('CGG-24', 'Thomas, A.T., Hope, J.E. and Mathur, M.B. (2025). Documentary films can increase public interest in plant-based diets in the USA. Nature Food 6: 837 to 842. https://doi.org/10.1038/s43016-025-01227-7 . Crossref metadata read 2026-10-15 (funder listed: National Science Foundation); the browser session reports that the acknowledgements cite a gift from Open Philanthropy. Type: peer-reviewed.',
     'Documentary films can increase public interest in plant-based diets in the USA', 'Nature Food', '2025-09-19', 'https://doi.org/10.1038/s43016-025-01227-7', '10.1038/s43016-025-01227-7', 'peer-reviewed',
     'Consumer-interest study; out of scope for the study (diet change). Linked to grant CG-G044 (Stanford, USD 300,000, June 2025) by grantee and period only.'),
]

def read(p):
    with open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def write_csv(p, fields, rows):
    buf = io.StringIO(); w = csv.DictWriter(buf, fieldnames=fields, lineterminator='\n'); w.writeheader(); w.writerows(rows)
    open(p, 'w', encoding='utf-8', newline='').write(buf.getvalue())

src = read('data/sources.csv'); F = list(src[0].keys())
have = {r['source_id'] for r in src}
if any(n[0] in have for n in NEW):
    sys.exit('Already registered.')
new = []
for sid, cit, title, auth, date, url, doi, typ, notes in NEW:
    r = {k: '' for k in F}
    r.update(source_id=sid, prefix='CGG', agent='COEFFICIENT_GIVING', citation=cit, title=title, author_or_publisher=auth, date=date,
             url=url, doi=doi, source_type=typ, accessed='2026-10-15', notes=notes, wave='wave13', from_note=NOTE, status_v0_9='active')
    new.append(r)
write_csv('data/sources.csv', F, src + new)
open('sources/sources.csv', 'w', encoding='utf-8', newline='').write(open('data/sources.csv', encoding='utf-8').read())
active = [r for r in src + new if r['status_v0_9'] == 'active']
N = len(active); n13 = sum(1 for r in active if r['wave'] == 'wave13'); ncgg = sum(1 for r in active if r['prefix'] == 'CGG')

# R4: append to the CGG section, fix its count, rebuild the counts table and summary
p = 'content/03-appendices/app-r4-sources.md'; s = open(p, encoding='utf-8').read()
m = re.search(r'## CGG: (.*?) \(wave 13\), v0\.10 \((\d+)\)\n\n(.*?)(?=\n## |\Z)', s, re.S)
assert m, 'CGG section not found'
block = m.group(0).rstrip('\n')
block2 = re.sub(r'v0\.10 \(\d+\)', f'v0.10 ({ncgg})', block, count=1) + '\n' + '\n'.join(f'- <a id="{r["source_id"]}"></a>**{r["source_id"]}.** {r["citation"]}' for r in new)
s = s.replace(block, block2)
ROUNDS = OrderedDict([('Version 0.1 (waves 1 and 2)', ['wave1', 'wave2']), ('Futures round (waves 3 to 5)', ['wave3', 'wave4', 'wave5']),
                      ('Demand round (wave 6)', ['wave6']), ('Actor check and expansion (waves 7 to 9)', ['wave7', 'wave8', 'wave9']),
                      ('Prologue (wave 10)', ['wave10']), ('Food security (wave 11)', ['wave11']), ('Regional deals (wave 12)', ['wave12']),
                      ('Solutions screen (wave 13)', ['wave13'])])
cnt = Counter((r['source_type'], r['wave']) for r in active); types = Counter(r['source_type'] for r in active)
rows = ['| Source type | ' + ' | '.join(ROUNDS) + ' | Total |', '|---' * (len(ROUNDS) + 2) + '|']
for t, tot in sorted(types.items(), key=lambda x: (-x[1], x[0])):
    rows.append(f'| {t} | ' + ' | '.join(str(sum(cnt[(t, w)] for w in ws)) for ws in ROUNDS.values()) + f' | {tot} |')
rows.append('| **All** | ' + ' | '.join(str(sum(1 for r in active if r['wave'] in ws)) for ws in ROUNDS.values()) + f' | {N} |')
s, k = re.subn(r'\| Source type \|.*?\n\| \*\*All\*\*[^\n]*', '\n'.join(rows), s, count=1, flags=re.S); assert k == 1
s = re.sub(r'All [\d,]+ sources behind the report \(', f'All {N:,} sources behind the report (', s, count=1)
s = re.sub(r'and \d+ by the solutions screen of v0\.10\)', f'and {n13} by the solutions screen of v0.10)', s, count=1)
open(p, 'w', encoding='utf-8').write(s)

# bibliography: add to the solutions screen round, by type
p = 'sources/bibliography.md'; b = open(p, encoding='utf-8').read()
head, sep, rnd = b.partition('## Solutions screen round (version 0.10)')
assert sep
for r in new:
    t = r['source_type']
    mm = re.search(r'### ' + re.escape(t) + r' \((\d+)\)\n\n(.*?)(?=\n### |\Z)', rnd, re.S)
    entry = f'- **{r["source_id"]}.** {r["citation"]}'
    if mm:
        old = mm.group(0).rstrip('\n')
        newb = old.replace(f'### {t} ({mm.group(1)})', f'### {t} ({int(mm.group(1)) + 1})', 1) + '\n' + entry
        rnd = rnd.replace(old, newb, 1)
    else:
        rnd = rnd.rstrip('\n') + f'\n\n### {t} (1)\n\n{entry}\n'
b = head + sep + rnd
b = re.sub(r'^[\d,]+ sources cited in the research', f'{N:,} sources cited in the research', b, count=1, flags=re.M)
b = re.sub(r'and \d+ from the solutions screen of version 0\.10', f'and {n13} from the solutions screen of version 0.10', b, count=1)
open(p, 'w', encoding='utf-8').write(b.rstrip('\n') + '\n')
print(f'+{len(new)} sources; active {N}; wave 13 {n13}; CGG {ncgg}')
