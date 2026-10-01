---
id: app-m1-method
title: "M1. Method, evidence rules and limits"
short_title: "M1. Method"
section: appendix
order: 1
summary: "The study's scope (protein for people first, feed only as context) and how it was designed around six audiences: the first two research waves and the retail audit, the tools used, how evidence was labelled and checked, how earlier drafts were used, and the limits. Sections M1.10 to M1.13 summarise the later rounds, described in full in Appendices M2 to M4."
audiences: [research, investors, policy, international, startups, manufacturers]
reading_time_min: 9
key_numbers: [kn-sources-count, kn-open-questions, kn-disagreements]
related_data: [sources.csv, open_questions.csv, disagreements.csv]
related_pages: [front-prologue, app-m4-actor-check-waves, front-how-to-read, app-m5-changelog, app-r1-open-questions, app-r2-disagreements, app-r4-sources, ch30-unknowns, app-m2-futures-method, app-f4-balance-model, app-m3-demand-method, app-s6-feed-market, app-f6-aquafeed-feedstock-futures]
charts: [chart-sources-by-type]
---

# M1. Method, evidence rules and limits

**What this appendix contains.** How we designed, researched and checked the study, and its limits. Sections M1.1 to M1.9 describe the first version (0.1). Sections M1.10 to M1.13 summarise the later rounds; their full methods are in Appendices M2 to M4.

**Scope.** This study is about protein for people: what Vietnam could make at home for people to eat, from what, at what cost, under which rules, and who would buy it, now and to 2050. Feed appears only as context. It is the hidden import behind the meat, eggs, milk and farmed fish that people eat, and so part of the food-security picture. But the study no longer treats feed ingredients (fishmeal replacements, or microbial, insect or duckweed feed) as something to make. Versions 0.1 to 0.7 covered food and feed together and assessed feed ingredients as products; that record stays in [[app-s6-feed-market]], [[app-f6-aquafeed-feedstock-futures]] and the changelog ([[app-m5-changelog]]).

Insect protein is a benchmark and incumbent only. Diet change is not a goal the study sets: Part III sizes what people and firms would buy, as labelled scenarios. Market-size forecasts are out of scope.

## M1.1 Design: six audiences, eleven questions

The study started from the decisions that six groups of readers face. We set a research goal for each group. These are the goals set for version 0.1, when food and feed manufacturers were one audience; feed makers are now readers for context only.

| Audience | Decision they face | Research goal |
|---|---|---|
| Investors (venture capital, impact investors, development finance) | Is there investable deal flow, and which theses? | Deal history and investors; cost inputs; 4 to 8 evidence-backed theses with what must be true and kill tests |
| Policy makers (Vietnamese ministries and provinces; ASEAN bodies; foreign governments) | What to write, fund or change | Full instrument register; precedents; ranked policy options with owners |
| Startups | What to build, where, with whom, through which legal route | Feedstock, facility, laboratory and programme directories; routes to market by product type |
| Food and feed manufacturers | Whether to add lines, source Vietnamese ingredients or site production | Capacity map; formulation analysis; import dependence; export routes |
| Research bodies | What to research, with whom, with what funding | Bibliometric map; institution directory; gaps Vietnam is placed to fill |
| International organisations | Where programmes can move the frontier | Partner map; fundable public goods |

We turned these goals into eleven macro questions, which became the chapters: protein economy, asset map, industrial capacity, the existing market, rules, knowledge base, capital, regional position, economics, technology fit and synthesis. We also set a list of micro deliverables (directories, registers, data sheets), which became the appendices and data files.

After the first research wave we re-read the goals and recorded, for each audience, what was still missing. We designed the second wave to close those gaps.

## M1.2 Research waves

AltProtein Vietnam carried out the research with AI research assistants. They worked as parallel research streams (called "agents" in the working papers), each with a written brief, a shared protocol and its own source-ID prefix. We then consolidated, checked and synthesised their notes into this report.

| Wave | Stream | Prefix | Topic |
|---|---|---|---|
| 1 | Macro | MAC | Protein economy, feed, trade, targets |
| 1 | Feedstock | FS | Crops, residues, side streams, prices |
| 1 | Industry | IND | Fermentation, feed, food and processing capacity |
| 1 | Ecosystem | ECO | Companies and actors |
| 1 | Regulation | REG | Food, feed, GMO, labelling, incentives, sandboxes |
| 1 | Research and development | RD | Institutions, research output, talent, funding |
| 1 | Capital | CAP | Deals, investors, programmes |
| 1 | Regional | RGN | Neighbouring countries, approvals, trade |
| 1 | Costs | COST | Input costs, commodity prices, cost benchmarks |
| 1 | Formulation | FORM | Retail audit analysis and ingredient supply |
| 2 | Science | SCI | State of the science by technology family; checks of earlier claims |
| 2 | Regulation 2 | REG2 | Draft Food Safety Law, aquafeed list, sandbox, tax |
| 2 | Feed market | FM | Fishmeal, inclusion rates, trials, prices to beat |
| 2 | Geography and time | GT | Administrative reforms, milestones, outlook |
| 2 | Company verification | VCO | Checks of company facts and capacities |
| 2 | Infrastructure | INF | Pilot plants, laboratories, parks, talent |
| 2 | Bibliometrics | BIB | Research output counts and comparisons |

In total the streams logged **806 sources** (599 in wave 1, 207 in wave 2): 180 press, 175 peer-reviewed, 133 company, 124 government or statistics, 78 legal texts and the rest from databases, advocacy groups and market research ([[app-r4-sources]]).

{{chart:chart-sources-by-type}}

## M1.3 Tools and their limits

- **Web search** was available for part of the first wave only; the session's search budget ran out part-way through. After that, research used direct reads of known pages, the search functions inside legal databases, scholarly indexes (Scite, and the OpenAIRE research graph) and trade data (World Bank WITS, UN Comtrade). General search engines were not used as a workaround.
- **Bibliometrics.** OpenAlex, the planned bibliometric source, refused requests (HTTP 429) during the run, so counts come from OpenAIRE, with OpenAlex queries saved for a rerun ([[app-s7-research]]). Counts are lower bounds; Vietnamese-language journals are only partly indexed.
- **Unreachable sources** (blocked pages, rate limits, image-only PDFs) are logged in the working papers and in `open_questions.csv`.
- **Language.** Vietnamese legal texts and press were read in Vietnamese.

## M1.4 The retail audit

AltProtein Vietnam recorded 186 alternative-protein and plant-based products (stock-keeping units, SKUs) in 11 stores, from hypermarkets to specialty importers. Five stores were in Nha Trang (6 September 2026) and six in Ho Chi Minh City (16 and 20 September 2026). Records include price, pack size, ingredients and label nutrition where legible; low-confidence price reads are flagged. The audit is a convenience sample in two cities, not a national survey ([[app-s2-retail-audit]]). Source ID FORM-01.

## M1.5 Evidence rules

- **Labels.** Every finding carries VN-direct, VN-adjacent (with the transfer stated) or general.
- **Confidence.** High (primary source read), Medium (reputable secondary or primary read in part), Low (single claim, press, company marketing, or our derivation from weak inputs).
- **Measured, estimated, claimed.** Kept distinct; our calculations are marked.
- **Disagreements.** Never averaged. Both values and the position taken are recorded (142 entries, [[app-r2-disagreements]]).
- **Currency.** Regulatory and market claims older than 12 months were re-checked where possible.
- **Earlier drafts are leads, not sources.** This project produced internal scoping drafts before version 0.1. Their claims were listed as leads and each was re-checked against a primary or reputable source before use; several were wrong and are corrected in [[app-m5-changelog]].

## M1.6 Checking

- Every headline number in the chapters was traced to a source ID and checked against the working note that produced it.
- Every citation token in the content resolves to `sources.csv`; cross-links, evidence tags and key-number and chart references were validated by script.
- An independent review pass re-checked the headline numbers against notes and sources before publication.
- Wave 2 re-verified a sample of wave 1 company and regulatory claims; corrections are recorded in the `change_log` fields of the data files.

## M1.7 Synthesis methods

- **Technology fit** ([[ch10-technology-fit]]) rates ten families on seven conditions (strong, moderate, weak).
- **Plays** ([[ch26-plays]]) are scored 1 to 5 on seven criteria, with weight presets per audience in `play_weight_presets.csv`. Scores are judgements based on the cited evidence. Seven plays and four public goods are active. Three feed plays (T2, T3, T6) and two feed public goods (P2, P3) keep their scores in `plays.csv` as a record, but are no longer recommended, because the study now concentrates on protein for people.
- **Policy options** ([[ch27-policy-options]]) are ranked by impact on investability, feasibility and time-criticality. Five feed options keep their earlier rank in `policy_options.csv` as a record but are no longer ranked.
- **Scenarios** ([[ch19-outlook-2035]]) are internally consistent pictures with signposts, not forecasts.
- **Cost stacks** ([[ch09-economics]]) combine sourced Vietnamese prices with stated engineering assumptions and are indicative.

## M1.8 Limits

- No interviews in this draft; the remaining gaps need phone calls and letters ([[ch30-unknowns]]).
- Search limits mean some recent press and grey literature were missed; absence in our logs means "not found", not "does not exist".
- Company capacities are often self-reported or old.
- Trade tonnages in some databases are estimated; we use values and mirror data where so.
- Provincial statistics before and after the July 2025 merger need re-aggregation ([[app-s10-admin-map]]).
- The study is not investment, legal or engineering advice.

## M1.9 Data and reuse

All tables are in `data/` with a data dictionary. The unedited research notes are in `working-papers/`. Where notes and report disagree, the report is the current position.

## M1.10 Version 0.2: the futures round

Version 0.2 (September 2026) adds the futures chapters to 2050 (now chapters 20 to 24 and 28) and Appendices M2 and F2 to F6. The futures round followed the same evidence rules as v0.1, with four additions. The full method is in [[app-m2-futures-method]].

- **Scope decisions.** New futures chapters in the same package; evidence-anchored foresight plus one normative vision, clearly labelled; four topics (frontier production technology, drivers and shocks, economy and policy futures, quantitative projections); demand as a macro input only, with no consumer research or market-size forecast. Insects remain a benchmark, not a play.
- **Research waves 3 to 5.** Eight streams in wave 3 (frontier gas fermentation, frontier biology and AI, climate, the balance model, geopolitics and macro drivers, economics and policy, horizon scan, national targets), three gap-closing streams in wave 4 (next-generation feedstocks, aquaculture futures, spatial hubs) after an actor review, and one in wave 5 (vision benchmarks and foresight practice). They added 469 sources (1,275 in all) under the prefixes FTG, FTB, CLM, QNT, GEO, ECF, HSC, NTS, NGF, AQF, HUB and VIS.
- **Tools.** Web search with per-stream caps (about 137 searches in total), direct reading of official texts, OpenAlex for bibliometrics and literature (it worked in this round, unlike wave 2), and a desktop browser as a read-only fallback for pages that direct fetches could not reach. No sign-in, form, download or personal identifier was used in any request.
- **Foresight tags.** Every forward-looking claim carries a foresight type (trend, projection, estimate, signal, wildcard or, in chapter 24 only, vision) and a horizon year ([[front-how-to-read]]).
- **Quantitative model.** A transparent protein and feed balance model (`tools/balance_model.py`) reproduces published outlooks to 2035 within about 2% and extends them to 2050 under four scenarios ([[app-f4-balance-model]]).
- **Checks.** An actor review after wave 3, consolidation of all new sources into `sources.csv`, the extended validator (which now also checks foresight tags) and an independent verification pass on the Part IV numbers and model arithmetic.
- **Corrections to v0.1.** Corrections are listed in section M5.9 of [[app-m5-changelog]]; the new open questions (OQ-128 onwards) and disagreements (DG-143 onwards) are in [[app-r1-open-questions]] and [[app-r2-disagreements]].

## M1.11 Version 0.3: the demand round

Version 0.3 adds Part III on the demand side, built from eight research streams (wave 6, 451 sources), a re-read of the retail audit for demand signals and a reproducible demand sizing model. It introduces a demand evidence tag (stated, revealed, tested or inferred) alongside the evidence and foresight tags. The full method, evidence rules, rejected claims and limits are in [[app-m3-demand-method]].

## M1.12 Version 0.4: the actor check

Version 0.4 checks Part III against 80 named actors and 118 decision questions, then runs sixteen research lines in three waves (waves 7 to 9, 577 sources) and stops when no line changes a Part III conclusion. The method, yield by line, stopping rule and limits are in [[app-m4-actor-check-waves]].

## M1.13 Version 0.5: the prologue

Version 0.5 adds a prologue for readers new to alternative protein ([[front-prologue]], [[front-prologue-vi]]). Three research agents, working from a common brief, gathered facts on definitions and technology families, the general arguments for and against alternative protein, and the international landscape (wave 10, 81 sources). Each reused package sources where they applied and recorded a short verbatim quote for every key number; an independent check compared the prologue with those notes before release. The briefs and notes are in `working-papers/wave10/`. The prologue is background: it adds no finding about Vietnam and changes none.

## M1.14 Version 0.8: protein for people, food-security hypotheses and clear language

Version 0.8 made three changes at the owner's request.

**A narrower scope.** The study is now about protein for people. Feed appears only as context: it is the hidden import behind the meat, eggs, milk and farmed fish that people eat. Feed ingredients (fishmeal replacements, and microbial, insect or duckweed feed) are no longer treated as something to make. Three feed plays, two feed public goods, one product profile, one demand move, five moves for 2050 and five policy options were retired from the recommendations. They stay in the data files with a `status_v0_8` column as the record. Chapters 22 and 24 were rebuilt around what people eat; the vision now draws its indicators from the demand model.

**Wave 11: food-security hypotheses.** Four research lines tested hypotheses about the security of the protein people eat (90 sources, 1 October 2026). Each worked from one brief (`working-papers/wave11/BRIEF.md`) and the research protocol, and wrote a working paper, sources, data tables, open questions and disagreements in its own folder:

- **Imported meat, offal and dairy (prefix MIM, 28 sources).** It tested whether Vietnam relies on subsidised imported meat. Meat imports are real and growing, but OECD estimates show little or no price support for meat and milk in most of the main origins, and a large cost gap, so the subsidy hypothesis is not supported.
- **Animal disease, zoonoses and pandemic risk (PAN, 40 sources).** Disease makes pork supply and prices volatile, and the licensed African swine fever vaccines do not protect against the recombinant strains now dominant in the north. We found no study that measures lower disease, pandemic or resistance risk from replacing animal-source food.
- **Other food-security exposures (SEC, 17 sources).** Alternative protein made from imported soy, pea or gluten moves import dependence rather than reducing it; only domestic-input routes reduce it. Wild marine fish stocks have fallen, and the official food-security resolution has no import or protein indicator.
- **Protein for people (FBS, 5 sources).** FAO food balance sheets show where the protein people eat comes from; with the imported feed behind domestic animal protein, about two thirds of animal protein rests on imports.

The lines added 26 open questions (OQ-447 to OQ-472), 21 disagreements (DG-353 to DG-373), ten data files and 16 stat tiles. A consolidating editor folded the results into chapters 1, 11, 14, 16, 20, 22, 23, 28 and 30, Appendix F2, the summaries and the briefs. The scripts used to register sources, questions, data and tiles are in `working-papers/wave11/`. An editorial check of names, glosses and affiliations, run the same day, added six sources under the prefix OIC (`working-papers/wave11/editorial/OPEN-ISSUES-check.md`).

**Clear language.** Every page was edited to the GOV.UK clear-language standard: short sentences and paragraphs, the main point first, active voice, plain words and abbreviations explained on first use. Chapter openings became short "In brief" boxes. Editors worked from a common brief (`working-papers/wave11/EDITORIAL-v0.8.md`) on separate files. They compared their pages with version 0.7 to check that numbers, citations and tags were kept unless a feed claim was deliberately removed, and a final package-wide check lists the sources no longer cited in any page (Appendix M5, section M5.14). The registers (Appendices R1, R2 and R4) were not rewritten. Every substantive change is listed in [[app-m5-changelog]], section M5.14.
