# Wave 13: solutions from GFI's database, screened for Vietnam

## Context

AltProtein Vietnam's study "Alternative protein in Vietnam: a supply-side scoping study" is in this repository (version 0.9). Today is 15 October 2026. Changes from this wave go into version 0.10 (Appendix M5, section M5.16).

The study's position today:

- `ch26-plays` names seven active plays and four public goods. The plays are T1 domestic textured plant protein, T4 a cassava-starch-to-fermentation-sugar hub, T5 shared pilot and tolling fermentation, T7 high-value, low-dose precision-fermentation ingredients, T8 cultivated seafood research, T9 koji and fungal foods on side streams, and T10 mung bean and rice protein for plant drinks. The public goods are P1 a new-food procedure, P4 a protein-quality laboratory, P5 a by-product atlas and P6 an open cost model and price series. Each play is scored 1 to 5 on seven criteria (section 26.1, `data/plays.csv`). Section 26.6 says what the study does not recommend.
- `ch25-demand-to-frontier` has 11 target product profiles (`data/target_product_profiles.csv`) and 20 demand moves (`data/demand_moves.csv`).
- `ch27-policy-options` (`data/policy_options.csv`) has the policy options. `ch28-robust-moves` (`data/robust_moves.csv`) has 21 moves for any 2050.
- `ch10-technology-fit` covers platform fit and `ch21-frontier-technology` covers frontier windows.

Why this wave: the editor asked us to evaluate more solutions, using the Good Food Institute's Solutions Database (https://gfi.org/solutions/) and its "Advancing Solutions for Alternative Proteins" (ASAP) work (https://gfi.org/advancing-solutions-for-alternative-proteins/). On 15 October 2026 the database held 112 entries, read through the site's public listing API. 89 were published in 2021 and the newest in April 2024. GFI tags each one Research, Commercial or Ecosystem (often more than one). The ASAP project report (dated 31 July 2020, published January 2021) was built from GFI research, 39 interviews, 41 online surveys and online ideation sessions. The report counts more than 120 experts; the landing page now says more than 150. GFI tags 33 entries with a maturity level (inception, early adoption, complete whitespace or widespread proliferation); the catalogue gives it as `gfi_maturity`. The database is global and mostly written from a United States and European view.

So the question for each entry is not "is this a good idea?" but **should Vietnam do it, buy it from abroad, or leave it?** A solution earns a place in the study only if there is a Vietnam-specific reason to act. That reason can be an asset (a raw material, a side stream, a species, an industry, skills, cost), a named buyer, a rule, or a gap that no foreign supplier fills. "It would be useful everywhere" is not enough.

`working-papers/wave13/gfi_solutions_catalogue.csv` lists all 112 entries. For each it gives GFI's tags, the line assigned to it and a short excerpt. The full text of each entry, with GFI's challenge, proposed solution and impact sections, is in the lead session's scratchpad (path given in each line's launch prompt). Read the entry before judging it.

Read, in addition to `working-papers/PROTOCOL.md`:

- Pages: `ch26-plays`, `ch25-demand-to-frontier` (25.2 to 25.5), `ch10-technology-fit`, `ch28-robust-moves`, plus the pages named for your line below.
- Data: `plays.csv`, `target_product_profiles.csv`, `robust_moves.csv`, `policy_options.csv`, `demand_moves.csv`, and `open_questions.csv` rows on your topic.
- Earlier working papers on your topic (index in `working-papers/README.md`).

## Lines

| Line | Folder | Source prefix | GFI entries | What result would change which conclusion |
|---|---|---|---|---|
| L1 | `wave13/L1-plant-based/` | SLP | 15: texturisation, ingredient characterisation, protein isolation, products, fats, flavour, formulation | A plant-based solution with a Vietnamese asset and a named buyer would add a play or a target product profile, or change T1 or T10 in `ch26-plays` |
| L2 | `wave13/L2-fermentation/` | SLF | 16: strains, fats, fungi, contract research, co-manufacturing, retrofits, directories, cost models | A local strain or facility asset would add a play or public good, or change T4, T5, T7 or T9, RM-04 or RM-15 |
| L3 | `wave13/L3-cultivated/` | SLC | 34: cell lines, media, scaffolds, bioprocess, safety | A Vietnamese input or capability that cultivated producers abroad would buy would change T8 or `ch10-technology-fit` section 10.8; otherwise a clean negative |
| L4 | `wave13/L4-alt-seafood/` | SLS | 13: species choice, surimi, fish cells, omega-3, seafood LCA and sensory, showcase | Vietnam's seafood industry as a base for alternative seafood (for example hybrid surimi) would add a play or change T8 |
| L5 | `wave13/L5-capital-markets/` | SLK | 20: offtake, loan and leasing funds, factoring, corporate venture, accelerators, investor platforms, procurement, brokers, IP pools, trade facilitation | A financing or market instrument that works under Vietnamese law and has a named provider would change `ch08-capital`, RM-11, RM-12 or the T1 financing advice |
| L6 | `wave13/L6-research-workforce/` | SLW | 14: university centres, programmes, courses, student groups, training, vocational, funding databases, events, makerspaces | A named Vietnamese programme, or a costed gap, would change `ch06-knowledge-talent`, RM-09 or the public goods |

The lead session runs the overall screen and the fold-in as L0 (prefix GSD). It registers the GFI database and the ASAP documents as sources once (GSD-01 onwards), so lines cite those IDs. **Do not register individual GFI solution pages as sources.** Cite GSD-01 and give the solution's GFI number (GFI-001 to GFI-112) in your table.

- **GSD-01** is the GFI Solutions Database (112 entries, accessed 15 October 2026).
- **GSD-02** is the ASAP landing page.
- **GSD-03** is the ASAP project report (dated 31 July 2020, published January 2021).
- **GSD-04** is the ASAP executive summary (2021).

### Every line: the screen (all entries assigned to you)

For each GFI entry, answer these questions:

1. **In scope?** The study is about protein for people. Feed ingredients, insect protein, consumer marketing plans and market-size forecasts are out of scope (see `CLAUDE.md`).
2. **Already covered?** Name the study IDs (T, P, RM, PO, TPP, DMV, OQ) that already cover it, and the page and section.
3. **Vietnam angle?** Is there a Vietnam-specific reason to act? What exists in Vietnam already: named actors, assets, rules, gaps? Give retrieved evidence.
4. **Verdict**, one of:
   - `new candidate play`
   - `new candidate public good`
   - `strengthens existing` (name the ID and what it adds: a component, partner, kill test or constraint)
   - `already covered` (name the ID)
   - `global frontier, monitor` (Vietnam would buy the result, not make it; name the signal to watch)
   - `not for Vietnam now` (say why)
   - `out of scope` (say which rule)

Most entries will end as `already covered` or `global frontier, monitor`. That is a valid result. Do not stretch the evidence to create new plays.

### Every line: the deep evaluation (shortlist)

Pick the 2 to 5 entries with the strongest Vietnam angle and evaluate them properly with retrieved Vietnamese evidence: actors, volumes, prices, rules, capacity. For any `new candidate play` or `new candidate public good`, complete a row in the shape of `data/plays.csv`. Score the seven criteria 1 to 5, calibrated against the existing plays (read their scores and rationales first). Give the "what", "why Vietnam", "must be true", "kill tests", "first customers", "partners", "horizon" and "capital note". Propose at most three new candidates per line, and only where the evidence carries them.

### L1: plant-based (SLP)

Also read: `ch12-chay-baseline`, `ch13-consumers`, `ch16-business-buyers`, `app-s2-retail-audit`, `app-s4-feedstocks`, `app-d5-buyers`.

1. Texturisation beyond extrusion (fibre spinning, shear cell; GFI-025). Does it change T1, or is it frontier? Does any Vietnamese institute or firm have this capacity?
2. Ingredient characterisation service and protein functionality database (GFI-017, GFI-011). How do they overlap with P4? Are functional data missing for Vietnamese crops and side streams (mung bean, rice and broken rice, peanut, sesame, okara, rice bran)? Would a functional-properties service be a new public good or an extension of P4?
3. Biological (enzymatic or fermentation) protein isolation (GFI-018) for Vietnamese streams such as rice bran, okara and mung bean starch water. Does it link to T10?
4. Products and formats: meat snacks in Vietnamese formats (GFI-040), private label (GFI-036; check the retail audit), hybrids (GFI-096 against TPP-03), animal-ingredient substitution such as egg and gelatin (GFI-078), fat systems and fat profiles (GFI-059, GFI-103; is coconut or another local fat an asset?), a flavour catalogue for Vietnamese dishes (GFI-106), open formulation sheets (GFI-035), product partnerships (GFI-041), plant molecular farming (GFI-037), plant-based turkey (GFI-039).

Out of scope for L1: alternative seafood (L4) and fermentation-made fats (L2).

### L2: fermentation (SLF)

Also read: `ch05-industrial-base`, `ch09-economics`, `app-s5-facilities`, `app-s8-labs-talent`, `app-s12-costs`, `app-f3-frontier-tech`, `data/engineering_suppliers.csv`, `data/pilot_labs.csv`.

1. Strain screening and pathway discovery (GFI-045, GFI-010). Are Vietnam's culture collections (for example the Vietnam Type Culture Collection) and traditional ferments (*mẻ*, *tương*, *chao*, *men* starters, fish sauce) an asset? Would a "local strain library" public good be defensible? What do Vietnam's access and benefit-sharing rules for genetic resources require?
2. Fats by fermentation (GFI-006, GFI-058) on cassava or molasses sugar. Is it plausible against palm and coconut fat prices? Does it link to T4?
3. Filamentous fungi (GFI-007) against T9.
4. Strain-development contract research organisations (GFI-033), Raman sorting (GFI-104), food-safe selection markers (GFI-063) and a bioreactor company (GFI-084). Is Vietnam a taker, or could it host a low-cost service? Could Vietnamese fabricators make food-grade vessels?
5. Co-manufacturing capacity, retrofitting facilities, directories of contract manufacturers and engineering firms, and open facility blueprints (GFI-048, GFI-089, GFI-064, GFI-066, GFI-043), against T5, RM-04 and RM-15. Are idle Vietnamese ethanol, yeast, MSG or brewery assets retrofit candidates? Check the effect of the E10 mandate from June 2026 on idle ethanol plants.
6. Techno-economic models and a data lake (GFI-009, GFI-067), against P6.

### L3: cultivated meat and seafood, excluding seafood-specific entries (SLC)

Also read: `ch10-technology-fit` section 10.8, `ch14-frontier-demand`, `ch21-frontier-technology`, `app-s13-science`, `app-s8-labs-talent`, `app-s9-regulation`.

1. Triage all 34 entries. Most will be `global frontier, monitor`. Group them and do not spend calls on each.
2. Media inputs from Vietnamese side streams, such as hydrolysates from soy, rice bran, yeast or fish processing. Also a business-to-business media company, growth factors (GFI-079, GFI-055, GFI-044), plant-made albumin (GFI-090) and media formulations (GFI-012). Is there a Vietnamese ingredient angle?
3. Food-safety and sterility controls (GFI-099, GFI-095) and consumer education on safety (GFI-098), against P1. Does Vietnam's regulator or testing capacity (VFA, the national food-control institute) have anything to build on?
4. Transferable animal-cell skills in Vietnam: vaccine makers, stem-cell and in vitro fertilisation laboratories. Who could host cell-line work for T8?
5. Scaffolds from local biomaterials (GFI-085, GFI-094, GFI-109), for example rice, soy, seaweed polysaccharides or jackfruit fibre. Is anything Vietnamese and defensible?
6. Co-product valorisation (GFI-020).

### L4: alternative seafood across platforms (SLS)

Also read: `ch10-technology-fit` section 10.8, `ch14-frontier-demand`, `ch17-export-demand`, `app-d6-export`, `app-s13-science`; earlier aquaculture and seafood lines in `working-papers/wave3/`.

1. Surimi (GFI-111). How big is Vietnam's surimi industry (volume, exports, provinces, main firms)? What are its raw-material and waste constraints? Has anyone done hybrid (fish plus plant or fungal protein), fermentation-derived or cultivated surimi? Would a hybrid surimi line for Vietnamese surimi makers be a candidate play? Which rules and standards apply to blends?
2. A species decision matrix (GFI-005) applied to Vietnamese species (striped catfish, shrimp, snakehead, tilapia, grouper, cobia, tuna). Which species would a Vietnamese alternative-seafood programme pick, and does that change T8?
3. Fish cell lines from food-relevant species, proliferation, scaffolds and omega-3 uptake (GFI-110, GFI-097, GFI-071, GFI-072, GFI-088). What cell lines from Vietnamese species exist, which partners (for example Nha Trang University, the aquaculture research institutes, Can Tho University), and what gaps?
4. Omega-3 for human food (GFI-073, GFI-074, GFI-075): algal oils, microalgae research in Vietnam, oxidation. Human food only; feed omega-3 is context.
5. Seafood life-cycle assessment and consumer or sensory research (GFI-093, GFI-105), and the showcase product (GFI-032). Which gaps are not already covered by Part III?

### L5: capital, markets and business services (SLK)

Also read: `ch08-capital`, `ch15-channels`, `ch16-business-buyers`, `ch17-export-demand`, `app-s11-capital`, `app-d4-channels`, `app-d5-buyers`, `data/regional_deals.csv`, `data/instruments.csv`, `data/funding_programs.csv`.

1. Guaranteed offtake (GFI-034) and pooled procurement or group purchasing (GFI-019). Could chay makers pool soy-flour purchases or offtake behind a T1 line? Who could write offtake (caterers, retailers, public meals)? Which Vietnamese contract forms apply?
2. Finance instruments under Vietnamese law: an infrastructure loan fund (GFI-052), equipment leasing (GFI-053; Vietnamese finance-leasing companies and their rules), factoring (GFI-060; rules and providers), corporate venture arms of Vietnamese food groups (GFI-062), accelerators (GFI-061), investor coordination, deal-flow and matchmaking platforms, and investor events (GFI-026, GFI-065, GFI-051, GFI-056). Compare with `ch08-capital`, RM-11 and RM-12.
3. Market services: a marketplace exchange (GFI-002), a business-to-business broker and toolkit (GFI-038, GFI-013), a directory of foodservice and retail players (GFI-049, against D4), intellectual-property pooling (GFI-050), and import and export facilitation (GFI-077, against ch17 and D6).
4. Check scope for category marketing (GFI-076), demand forecasts (GFI-003) and climate and biodiversity synergies (GFI-107) against the study's rules.

### L6: research system and workforce (SLW)

Also read: `ch06-knowledge-talent`, `app-s7-research`, `app-s8-labs-talent`, `data/talent.csv`, `data/institutions.csv`, `data/research_funding.csv`, RM-09.

1. University centres of excellence, programmes, majors and courses (GFI-022, GFI-023, GFI-024). Which Vietnamese universities teach food biotechnology, fermentation and food process engineering, and does any offer alternative-protein content?
2. Student groups, conference sessions, events and workshops, outreach and a high-school programme (GFI-028, GFI-021, GFI-004, GFI-091, GFI-082). What exists in Vietnam already (for example GFI APAC activity, Alt Protein Project groups, industry events)?
3. Industry training and vocational programmes (GFI-054, GFI-068), against RM-09. Fermentation operators and process engineers: who trains them now, and at what cost?
4. Research funding database and matchmaking (GFI-015). What Vietnamese and international funding sources exist (NAFOSTED, national programmes, GFI grants to Vietnamese researchers)?
5. Academic-industry collaboration and makerspaces (GFI-057, GFI-080, GFI-081).

## Tools and budget

- WebSearch: up to 25 calls per line. Prefer WebFetch on known URLs, and search in Vietnamese where Vietnam-direct material matters.
- Public APIs (OpenAlex, Crossref, UN Comtrade, FAOSTAT) via `curl` are allowed. No personal identifiers in requests.
- Roughly 60 to 100 tool calls per line. Stop early if a cluster is all `global frontier, monitor`, and say so.
- Lines do not run git and do not edit `content/`, `data/`, `charts/` or `sources/`.

## Output

As in `working-papers/PROTOCOL.md` section 6, plus two tables:

1. **`data_solution_screen.csv`**: one row for every GFI entry assigned to the line. Columns:
   `gfi_no,slug,gfi_title,line,in_scope,scope_note,maps_to,vietnam_angle,vietnam_evidence,verdict,verdict_note,signal_to_watch,source_ids,evidence_label,confidence`
   `maps_to` takes study IDs separated by semicolons. `verdict` takes one of the seven values above, exactly as written.
2. **`data_candidates.csv`** (0 to 3 rows): new candidate plays or public goods. Columns as in `data/plays.csv` (without `status_v0_8`), with `play_id` as a line-local ID (for example `SLP-C1`), plus `gfi_nos`.

Consolidation: the lead session (L0, prefix GSD) folds the wave into the study following `CLAUDE.md`. It builds one 112-row screen for `data/`, and decides which candidates enter `ch26-plays` and at what status.

## Wave-specific rules

- GFI is an advocacy organisation. Its descriptions of challenges are useful context, but its claims about impact are claims. Tag them `general` and at most `Medium`, and check them against peer-reviewed or primary sources before relying on them.
- The database is mostly from 2021. Before treating a gap as current, check whether it has been filled since then (for example, a cell line released or a service launched).
- Use the study's existing IDs wherever possible. A new candidate must beat the existing plays on at least one criterion, or fill a gap none of them covers. Say which.

## Addendum (15 October 2026): three more sources to review

The editor asked us to review the solutions with three more sources in mind. Three more lines read them, screen what they find with the same seven verdicts, and point to the GFI entry (GFI-001 to GFI-112) that covers the same idea where one exists. They deepen only where a Vietnam angle exists.

| Line | Folder | Source prefix | Source | What result would change which conclusion |
|---|---|---|---|---|
| L7 | `wave13/L7-protein-project-eu/` | PPE | The Protein Project (EU), publications: https://www.theproteinproject.eu/publications | A diversification method, scenario or policy design that transfers to Vietnam's protein and soy import position would change `ch01-why-vietnam`, `ch22-protein-balance-2050`, `ch27-policy-options` or `ch28-robust-moves` |
| L8 | `wave13/L8-berkeley-alt-meat-lab/` | AML | Berkeley Alt:Meat Lab (Sutardja Center for Entrepreneurship and Technology, UC Berkeley): https://altmeatlab.berkeley.edu | A research result, open method or venture-building model that a Vietnamese university or firm could use would change `ch06-knowledge-talent`, a play, or the L6 findings |
| L9 | `wave13/L9-coefficient-giving-grantees/` | CGG | Grantees of Coefficient Giving (formerly Open Philanthropy), Farm Animal Welfare Fund, focus area "Alternatives to Animal Products": https://coefficientgiving.org/funds/farm-animal-welfare/ | Published research by grantees that answers a cost, technology or rule question the study holds open (for example a techno-economic result, a resilient-food or feedstock result, or a sensory result) would close or change an open question, a play's kill test or `ch21-frontier-technology` |

### L7: The Protein Project (EU)

1. Catalogue every publication on the page: eight on 15 October 2026, dated May 2025 to October 2026. Include the external Systemiq and World Economic Forum reports it lists. Find out who runs and funds the project (About and Manifesto pages).
2. For each publication, extract the solutions, instruments or methods it proposes, for example:
   - protein diversification scenarios and soy import dependency by 2035;
   - fermentation for food;
   - legume value-chain taskforces;
   - livestock transition pathways;
   - EAT-Lancet policy translation;
   - multi-stakeholder dialogue on fermentation rules.
3. Screen each solution for Vietnam, and say whether the study already does it. For example, `ch22-protein-balance-2050` and RM-01 cover the protein balance, and wave 11 covers soy import dependency. The soy-dependency scenario method and the legume value-chain roadmap are the most likely to transfer: Vietnam imports about 98% of its soybeans. Compare the method, not just the conclusion.
4. Feed is context only. A European feed-protein measure is relevant only for what it shows about food protein or import security.

### L8: Berkeley Alt:Meat Lab

1. Map the lab: people (roles, not personal details), classes, the blog, partners, alumni startups, and research outputs. Include peer-reviewed papers by lab-affiliated researchers: use the OpenAlex MCP tools if connected (ToolSearch "OpenAlex"), or Crossref.
2. Screen the research topics and open resources, for example fat systems, plant-based seafood and texture. Flag any that Vietnam could use or partner on.
3. Screen the teaching and venture-building model: challenge-lab classes, student startups, industry partners. Could a Vietnamese university copy it? Compare with the L6 findings on Vietnamese universities.
4. The site front page mostly links to press. Follow the blog, the classes and the people pages before concluding there is little research.

### L9: Coefficient Giving grantees with published research

1. **Access gap.** coefficientgiving.org returns HTTP 403 from its Cloudflare edge to this environment, on every path, including robots.txt. The old openphilanthropy.org grants URLs redirect there. Do not get round this: no mirrors, no web archives or caches, and no third-party copies of the grants database used as a substitute listing. Record the gap.
2. **Build the grantee list from legitimate routes:**
   - **Crossref funder metadata.** Open Philanthropy Project is funder 100014895; `https://api.crossref.org/funders/100014895/works` listed 484 works on 15 October 2026. Filter it to alternative protein topics.
   - **OpenAlex.** Use the MCP tools if connected (ToolSearch "OpenAlex"), filtering by funder. The public OpenAlex API is out of its shared daily budget today.
   - **Grantee announcements**, such as university news, grantee websites and annual reports.
   - **Reputable press reports** of grants, such as the 2026 call of up to USD 10 million for alternative protein taste research.
3. **Focus on grantees that have published research** (peer-reviewed papers, preprints, techno-economic analyses, datasets). For each, go deep:
   - what the research found;
   - its numbers, with units and year;
   - how robust it is;
   - whether it bears on a Vietnam question the study holds open. Examples: cultivated meat cost and scale-up (`ch10-technology-fit` 10.8, T8); fermentation cost (T5, T7, P6); single-cell or resilient-food protein from cassava, natural gas or carbon dioxide (`ch21-frontier-technology`); sensory and taste parity; plant protein functionality (T1, T10).
4. **Reuse sources the study already holds.** Some may already be registered: search `data/sources.csv` by DOI and title, and reuse the existing IDs.
5. **Advocacy and diet-change grants.** Out of scope as solutions (see `ch25-demand-to-frontier` section 25.4 on funder fit). Note them only as funder-fit context.

### Output for L7 to L9

As in `working-papers/PROTOCOL.md` section 6, plus:

1. **`data_item_screen.csv`**: one row per publication, research output or grantee screened. Columns:
   `item_id,line,item_title,item_type,owner,date,url,doi,in_scope,scope_note,related_gfi_nos,maps_to,vietnam_angle,vietnam_evidence,verdict,verdict_note,signal_to_watch,source_ids,evidence_label,confidence`
   - `item_id` is line-local, for example `PPE-I01`.
   - `verdict` takes one of the seven values above.
2. **`data_candidates.csv`** (0 to 3 rows), as for L1 to L6.

L9 also writes **`data_grantees.csv`**: grantee, grant purpose, amount and date where a retrievable source gives them, published outputs (DOIs), source_ids, confidence.
