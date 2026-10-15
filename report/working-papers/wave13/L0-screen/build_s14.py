#!/usr/bin/env python3
"""Write Appendix S14 (content/03-appendices/app-s14-solutions-screen.md) from data/solutions_screen.csv.

Run from the repository root after build_screen.py:  python3 working-papers/wave13/L0-screen/build_s14.py
The prose sections are written here; the item tables and counts are generated from the data file.
"""
import csv, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
os.chdir(ROOT)
rows = list(csv.DictReader(open('data/solutions_screen.csv', encoding='utf-8')))
V = ['new candidate play', 'new candidate public good', 'strengthens existing', 'already covered',
     'global frontier, monitor', 'not for Vietnam now', 'out of scope']
SETS = ['GFI Solutions Database', 'The Protein Project (EU)', 'Berkeley Alt:Meat Lab', 'Coefficient Giving grantees']
LINES = {'L1': 'Plant-based', 'L2': 'Fermentation', 'L3': 'Cultivated meat (excluding seafood-specific entries)',
         'L4': 'Alternative seafood', 'L5': 'Capital, markets and business services', 'L6': 'Research system and workforce'}
# what the package did with each new candidate
CAND = {'GFI-111': 'Candidate play T11 (hybrid fish cakes)', 'GFI-045': 'Candidate public good P7 (food strains)'}


def esc(s):
    return (s or '').replace('|', '\\|').strip()


def maps(s):
    s = esc(s).replace(',', ';')
    parts = [p.strip() for p in s.split(';') if p.strip()]
    return ', '.join(parts[:6]) + (' and others' if len(parts) > 6 else '')


n = len(rows)
cnt = {s: Counter(r['verdict'] for r in rows if r['source_set'] == s) for s in SETS}
tot = Counter(r['verdict'] for r in rows)
gfi = [r for r in rows if r['source_set'] == 'GFI Solutions Database']
other = n - len(gfi)

count_table = ['| Verdict | ' + ' | '.join(SETS) + ' | All |', '|---' * (len(SETS) + 2) + '|']
for v in V:
    count_table.append(f'| {v[0].upper() + v[1:]} | ' + ' | '.join(str(cnt[s][v]) for s in SETS) + f' | {tot[v]} |')
count_table.append('| **All** | ' + ' | '.join(str(sum(cnt[s].values())) for s in SETS) + f' | {n} |')

line_table = ['| Line | Entries | Candidate | Strengthens existing | Already covered | Frontier, monitor | Not for Vietnam now | Out of scope |',
              '|---|---|---|---|---|---|---|---|']
for ln, name in LINES.items():
    c = Counter(r['verdict'] for r in gfi if r['line'] == ln)
    line_table.append(f'| {ln} {name} | {sum(c.values())} | {c["new candidate play"] + c["new candidate public good"]} | {c["strengthens existing"]} | '
                      f'{c["already covered"]} | {c["global frontier, monitor"]} | {c["not for Vietnam now"]} | {c["out of scope"]} |')


def item_table(items, with_line=False):
    out = ['| ID | Solution or item | Verdict | Maps to |', '|---|---|---|---|']
    for r in items:
        v = r['verdict']
        if r['item_id'] in CAND:
            v += f' ({CAND[r["item_id"]]})'
        out.append(f'| {r["item_id"]} | {esc(r["title"])} | {esc(v)} | {maps(r["maps_to"])} |')
    return '\n'.join(out)


gfi_sections = []
for ln, name in LINES.items():
    items = sorted([r for r in gfi if r['line'] == ln], key=lambda r: r['item_id'])
    gfi_sections.append(f'### {ln}. {name} ({len(items)})\n\n' + item_table(items))
other_sections = []
for s in SETS[1:]:
    items = [r for r in rows if r['source_set'] == s]
    other_sections.append(f'### {s} ({len(items)})\n\n' + item_table(items))

fm = f'''---
id: app-s14-solutions-screen
title: "S14. Solutions screen: published solutions checked for Vietnam"
short_title: "S14. Solutions screen"
section: appendix
part: null
order: 34
summary: "We checked {n} published solutions for Vietnam: the {len(gfi)} entries of the Good Food Institute's Solutions Database and {other} publications, research outputs and grants from The Protein Project, the Berkeley Alt:Meat Lab and Coefficient Giving's grantees. For each we ask whether Vietnam should make it, buy it or leave it. Most are covered already or are frontier work Vietnam would buy. None displaces the leading plays; three candidates and more than thirty changes to existing plays, moves and rules came out of it."
audiences: [investors, startups, manufacturers, research, policy, international]
reading_time_min: 25
key_numbers: [kn-solutions-screened]
related_data: [solutions_screen.csv, coefficient_giving_grants.csv, plays.csv, robust_moves.csv, open_questions.csv]
related_pages: [ch26-plays, ch28-robust-moves, ch10-technology-fit, ch07-rules, ch08-capital, ch06-knowledge-talent, app-m1-method, app-m5-changelog, app-r4-sources]
charts: [chart-solutions-screen]
---
'''

body = f'''# S14. Solutions screen: published solutions checked for Vietnam

**In brief.**

- We screened {n} published solutions in October 2026. These were the {len(gfi)} entries of the Good Food Institute's (GFI) Solutions Database and {other} items from three other sources: The Protein Project in Brussels, the Berkeley Alt:Meat Lab and the grantees of Coefficient Giving (formerly Open Philanthropy).
- The question for each was not "is this a good idea?" but **should Vietnam make it, buy it from abroad, or leave it?** A solution earns a place in the study only if Vietnam has a specific reason to act: an asset, a buyer, a rule, or a gap no foreign supplier fills.
- Most solutions are already covered by the study ({tot["already covered"]}), or are frontier research Vietnam would buy rather than make ({tot["global frontier, monitor"]}). {tot["not for Vietnam now"]} are not for Vietnam now and {tot["out of scope"]} are out of scope.
- {tot["strengthens existing"]} strengthen an existing play, public good, move or rule. They change the T1 financing advice, add a raw-material condition to T10 and extend the protein-quality laboratory (P4) to protein function. They also correct the route for licences to use Vietnamese microbial strains and add two routes to the "do not recommend" list.
- None displaces T1, T4 or T5. Three candidates are listed in [[ch26-plays]] (section 26.8) but not yet ranked: hybrid fish cakes and fish balls (T11), domestic food-grade soybean and mung bean (T12) and a characterised set of Vietnamese food strains (P7).

{{{{kn:kn-solutions-screened}}}}

## S14.1 What we screened

- **GFI Solutions Database.** {len(gfi)} entries, read through the site's public listing on 15 October 2026 [@GSD-01] {{general|High}}.
  - **Age.** 89 were published in 2021, 12 in 2022, 2 in 2023 and 9 in 2024; none was added after April 2024.
  - **Tags.** GFI tags each as Research, Commercial or Ecosystem, often more than one.
  - **Origin.** They come from GFI's Advancing Solutions for Alternative Proteins project. Its report (dated July 2020) drew on 39 interviews, 41 online surveys and three online ideation sessions. It counts more than 120 experts; the landing page now says more than 150 [@GSD-02; @GSD-03; @GSD-04] {{general|High}}. The project did not study demand.
  - **Status.** GFI is an advocacy organisation, so we treat its claims about impact as claims.
- **The Protein Project.** Eight publications from May 2025 to October 2026, plus six methods inside them [@PPE-01; @PPE-03; @PPE-05] {{general|Medium}}. It is a Brussels advocacy group, paid for by "two large philanthropic foundations" it does not name [@PPE-02] {{general|Medium}}. One is identified: Coefficient Giving granted it USD 353,764 in September 2025 for EU fermentation technology advocacy [@CGG-19] {{general|High}}.
- **The Berkeley Alt:Meat Lab.** 16 items: classes, blog posts, partners, alumni startups and research by affiliated authors [@AML-01; @AML-02] {{general|Medium}}.
- **Coefficient Giving grantees.** 28 grantees and research outputs linked to the focus area "Alternatives to Animal Products" [@CGG-01; @CGG-02; @CGG-19] {{general|Medium}}.
  - **How we found them.** The funder's website refused automated access from our research environment. We first traced grantees through funding statements in Crossref and OpenAlex (484 and 2,411 works), grantee announcements and the press. A separate browser session then read the grant list itself on 15 October 2026 [@CGG-19] {{general|High}}.
  - **The focus area.** It lists 61 grants worth USD 49.3 million from September 2016 to July 2026 (our sum). The Good Food Institute received USD 22.5 million of it (46%), and the Berkeley Alt:Meat Lab USD 3.4 million in five grants [@CGG-19] {{general|High}}.
  - **What it funds.** By title, 9 grants are research or R&D, worth about USD 2.1 million (about 4%). The rest fund policy, advocacy, field-building and general support (our classification from grant titles). None names Vietnam or Southeast Asia [@CGG-19] {{general|Medium}}.
  - **Research funded elsewhere.** Several outputs that thank Open Philanthropy came from its other programmes or from contracts, not this focus area. Examples are the resilient-food work at Pennsylvania State University and the cultured-meat cost model the study uses [@CGG-19; @COST-47] {{general|Medium}}.

## S14.2 How we judged each solution

Nine research lines did the screen, six on the GFI database (one per cluster) and one per other source. Each followed the study's evidence rules ([[app-m1-method]]). For each item, a line asked four questions:
1. Is it in scope? The study covers protein for people, not feed or insects, and offers no marketing plans or market-size forecasts.
2. Does the study already cover it?
3. Is there a Vietnam-specific reason to act, backed by retrieved evidence?
4. What follows?

The answer is one of seven verdicts:

| Verdict | What it means |
|---|---|
| New candidate play or public good | A Vietnam-specific case strong enough to score against the existing plays ([[ch26-plays]]) |
| Strengthens existing | Adds a component, partner, condition, kill test or correction to an existing play, public good, move or rule |
| Already covered | The study already holds it; we name where |
| Global frontier, monitor | Vietnam would buy the result, not make it; we name the signal to watch |
| Not for Vietnam now | Relevant, but premature or the wrong fit; we say why |
| Out of scope | Feed, insects, consumer marketing, market forecasts or diet-change campaigns |

## S14.3 Results

{chr(10).join(count_table)}

Source: AltProtein Vietnam screen, research wave 13 (`solutions_screen.csv`) {{VN-direct\\|Medium}}.

{{{{chart:chart-solutions-screen}}}}

The GFI database by research line:

{chr(10).join(line_table)}

**Reading.**
- **Cultivated meat.** The GFI entries on cultivated meat are almost all frontier research: 28 of 34 in line L3.
- **Business and workforce.** The ecosystem entries split between "strengthens existing" and "not for Vietnam now". Many assume a large domestic industry to serve (investor platforms, brokers, directories), which Vietnam does not yet have.

## S14.4 What the screen changed

The main changes, with the pages that now carry them:

- **T1 financing ([[ch26-plays]], [[ch08-capital]], [[app-s11-capital]]).** "Trade finance" now has a concrete form under Vietnamese law:
  - receivables finance and factoring against an anchor buyer (Circular 20/2024/TT-NHNN);
  - finance leases, including sale and leaseback (Circular 26/2024/TT-NHNN);
  - SME credit guarantees, such as the Ho Chi Minh City fund, capped at about USD 1.3 million per customer [@SLK-01; @SLK-05; @SLK-19; @SLK-20] {{VN-direct|High}}.

  Pooled offtake by chay makers should take a form that avoids price-fixing between competitors [@SLK-08] {{VN-direct|Medium}}.
- **T10 raw material ([[ch26-plays]], [[ch25-demand-to-frontier]]).** Mung beans alone cost USD 3.0 to 4.9 per kg of isolate at 2023 to 2025 import prices, above Chinese pea protein (our calculation) [@SLP-14] {{VN-direct|Medium}}. So T10 needs a paid starch co-product or a higher-priced job such as egg-white replacement.
- **P4 extended to function.** No Vietnamese laboratory sells functional testing of protein ingredients, which buyers specify [@SLP-17; @SLP-10] {{VN-direct|Low}}.
- **Genetic-resources licence corrected ([[ch07-rules]], [[app-s9-regulation]]).** Decree 43/2026 moved the licence for using Vietnamese strains to the provincial chairman, in about 19 working days (our calculation). Benefit sharing of at least 1% of product revenue still applies [@SLF-02] {{VN-direct|High}}.
- **Idle ethanol plants are no longer spare ([[app-s5-facilities]]).** Since the E10 mandate of June 2026, Vietnam imports about 75,000 m3 of ethanol a month [@SLF-13] {{VN-direct|Medium}}. The ethanol-plant retrofit that GFI cites was paused in 2024 [@SLF-12] {{general|Medium}}. Contract capacity and used equipment (RM-15) are the better routes.
- **Two routes added to "what we do not recommend" ([[ch26-plays]], section 26.6).**
  - Bulk fats made by fermentation, which cost more than palm and coconut oil even in an ideal plant [@SLF-08; @FM-01] {{general|Medium}}.
  - Cultivated or fermentation-made surimi, which would cost more than Vietnamese surimi sells for [@SLS-05] {{VN-direct|Medium}}.
- **Cultivated meat ([[ch09-economics]], [[ch10-technology-fit]], T8).** The cost model the study uses (funded by Open Philanthropy) sets its own affordability test: about USD 25 per kg of cells, or about USD 50 at the shelf. Both base cases exceed it [@COST-47] {{general|High}}. Amino acids, not growth factors, are the larger medium cost, so T8 now includes cheap hydrolysate media. Grouper and Asian seabass are candidate target species (metadata only) [@SLS-14; @SLS-15] {{general|Low}}.
- **Skills and research money ([[ch06-knowledge-talent]], [[ch28-robust-moves]]).**
  - **RM-09 splits into two tracks.** A senior-engineer track and an operator track, plus a buyer-set product challenge lab on the Berkeley model [@SLW-07; @AML-32] {{VN-direct|Medium}}.
  - **A scale check for the protein fund.** NAFOSTED approved VND 278.3 billion for 284 new projects in 2023 [@SLW-01] {{VN-direct|High}}. The proposed protein fund of USD 5 to 15 million a year (RM-11) would equal 47% to 140% of that (our calculation).
  - **No Vietnamese authors.** None of 270 works funded by GFI's research grants has a Vietnamese author [@SLW-02] {{general|Medium}}.
- **Soy import dependency ([[ch22-protein-balance-2050]]).** The Protein Project's back-casting method, run on the study's own data, confirms chapter 22. A 20% cut in imported soy protein by 2035 would need about 1.74 Mt of protein against the trend, and the in-scope levers reach about 9% to 16% of it (our calculation) [@PPE-03; @PPE-04] {{VN-direct|Low}}.

Every change, with its evidence and strength, is listed in `working-papers/wave13/L0-screen/changes_all.csv` and in [[app-m5-changelog]].

## S14.5 The GFI Solutions Database, entry by entry

Each row of `solutions_screen.csv` also gives the scope note, the Vietnam angle and evidence, the verdict note, the signal to watch and the sources. GFI numbers (GFI-001 to GFI-112) follow publication date. "Maps to" lists the study items that already cover the entry or that it changes. All rows rest on [@GSD-01] and the line's own sources {{general|Medium}}.

{chr(10).join(s + chr(10) for s in gfi_sections)}
## S14.6 Other sources, item by item

{chr(10).join(s + chr(10) for s in other_sections)}
## S14.7 Limits

- The GFI database is mostly from 2021. Lines checked whether each gap had been filled since, but some entries describe a field that has moved on.
- The verdicts are our judgement on desk evidence. Most open points now need calls, quotes or trials, not more reading: 47 new open questions (OQ-477 to OQ-523) say what to ask and whom ([[app-r1-open-questions]]).
- The Coefficient Giving grant list was read in a separate browser session, because the funder's site refused automated access from our research environment. It gives grantee, title, amount and month but no purpose text, and old grant pages no longer load, so grant types are our classification from titles. Its 2026 call page now returns "Page not found", and no awards had been announced by 15 October 2026 (OQ-519).
- Several Vietnam-direct facts rest on one press report or a search summary, and are tagged Low in the data file.
'''

open('content/03-appendices/app-s14-solutions-screen.md', 'w', encoding='utf-8').write(fm + '\n' + body)
print('written', n, 'items')
