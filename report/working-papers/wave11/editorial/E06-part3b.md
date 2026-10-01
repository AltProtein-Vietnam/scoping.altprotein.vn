# Editor log E06-part3b: chapters 13 and 14

Editor: E06-part3b. Date: 2026-10-01. Brief: `working-papers/wave11/EDITORIAL-v0.8.md`.

Files edited: `content/01-report/ch13-consumers.md`, `content/01-report/ch14-frontier-demand.md`. No other content file changed. No wave 11 findings added. "Version 0.7" labels and draft notices untouched (neither page carries them). `data/key-numbers.json` and `charts/chart-specs.json` untouched. `python3 tools/validate.py`: 0 errors after editing. The 2 warnings left (`kn-no-regret-plays`, `chart-play-robustness` unused) come from other editors' files. No em or en dashes in either file.

**Feed pruning.** Neither chapter carried a feed argument or a reference to a retired play or public good (T2, T3, T6, P2, P3, TPP-11). So the work was clear language. The one feed-adjacent fact, that the cultivated seafood partners of Vinh Hoan and Minh Phu now sell cultivated seafood as pet food (14.1), stays. It describes those firms' revenue and is not a feed recommendation.

**Integrity check.** A script compared the old and new text of each page. Every citation token, evidence tag, `{dx:...}` tag, cross-link and embed in the body is still there, with the same count. The body lost no numbers. The only changes are punctuation, the play codes T1, T7 and T8, and "1 L" folded into "per litre". Every number in the new `In brief` boxes also appears in the page body.

**Anchors and section numbers.** `grep -rn "ch13-consumers#\|ch14-frontier-demand#" content` returns nothing. But data files and registers cite section numbers: `actor_questions.csv`, `label_rules.csv`, `firm_outcomes.csv`, `disagreements.csv`, `open_questions.csv`, `hybrid_sensory_limits.csv` and `expansion_lines.csv`, plus Appendices R1 and R2 ("ch13.5", "ch14.2", "ch14.4" and so on). So sections 13.1 to 13.9 and 14.1 to 14.6 keep their numbers and their content. Several headings now say what the section finds. Page titles and ids are unchanged.

## ch13-consumers

| section | change | type |
|---|---|---|
| frontmatter | `summary` split into three sentences; `reading_time_min` 19 to 20 (glosses added) | clear language only |
| opening | "In one paragraph" became an `**In brief.**` box of five bullets. Cut from the box, all still in the body: 90% aware and 42% tried (13.2 table), entry "from 2019", the soy-milk protein-claim result, and the regional firms' pivots. The box had said respondents "have often tried it (42%)"; the survey measure is "have ever tried", so the figure now sits only in the table, where it is labelled correctly | clear language only |
| 13.1 | Heading now "...almost all of it is what people say". Added a plain definition of stated, revealed and tested evidence. GFI APAC spelled out as the Good Food Institute Asia Pacific; snowball sample explained; the source list became bullets | clear language only |
| 13.2 | Heading now "Aware and curious, but rarely buying"; lead sentence added; the three cautions became bullets; flexitarian explained | clear language only |
| 13.3 | Heading now "What would make people eat more: availability, variety and know-how"; main point first. "An order of magnitude" became "a real price gap of 12 to 18 times (section 13.4)", using the page's own figure | clear language only |
| 13.4 | Stated, revealed and tested labels glossed in plain words; "+50%" written as "50% dearer"; GMO and non-GM explained; "what 20 g costs" leads with its conclusion; "borrowed label protein range" explained | clear language only |
| 13.5 | Heading now "What people buy: plant milk, not plant meat". Mintel, extruded, Vu Lan, cumulative counters, FAIRR, excise and TCVN (Vietnamese national standard) explained. "Incumbents" became "established makers" or "established local firms". Long Vinasoy, excise and GoldSoy sentences split. In the table's price cell, "per bottle of OatSide's size, 1 L" became "per litre" (same values). "OatSide" made "Oatside" throughout | clear language only |
| 13.6 | Heading now "Who buys first: urban meat eaters, not students"; ceiling paragraph given a bold lead | clear language only |
| 13.7 | Heading now "Abroad, plant-based meat peaked and then stalled". Household penetration, repeat rate, price elasticity, private label and co-manufacturing explained. The regional-firms bullet split into three: firms' pivots, the TiNDLE founder's quote, and Vietnam's surviving familiar-format makers | clear language only |
| 13.8 | Heading now "Words on the pack: a protein claim is an open position". Codex, PCR (a DNA screen) and QUATEST 3 explained. Vietnamese label phrases glossed. Dropped "the phrase an earlier draft used" after *giàu đạm*: it marked a version in reading text (STYLE section 7) and was not a finding | clear language only |
| 13.9 | Heading "What this means for the frontier" became "What this means for new protein products", because "frontier" is not defined on this page or in the glossary. "Underwrite" became "judge deals" | clear language only |

## ch14-frontier-demand

| section | change | type |
|---|---|---|
| frontmatter | `summary` split; "must" became "has to" (not a legal requirement); `related_pages` adds `ch26-plays`; `reading_time_min` 17 to 19 | clear language only |
| opening | "In one paragraph" became an `**In brief.**` box of six bullets. It now defines "frontier categories". Cut from the box, all still in 14.1 and 14.2: the cultivated seafood partners' move to pet food and skincare, and the detail on voluntary non-GMO claims and high-inclusion uses | clear language only |
| opening | **Number alignment.** The box said "31% of one large processor's meat formulations list soy protein". The body (14.4), ch16's body, Appendix D5 and tile `kn-vissan-soy-share` all say 22 of 67 (33%). The 31% is the wave 6 count (19 of 61, `working-papers/wave6/buyers/buyers.md`). The box now uses the page's own figure, "22 of 67 meat formulations (33%)". See the unresolved items | clear language only (number aligned to body) |
| opening | **Wording fix.** The box tied "VND 9,100 to 16,600 per kg" to "every annual hog price from 2019 to 2024". The body and tile `kn-hybrid-saving` give that range at 2019 and 2020 hog prices, and say separately that extension pays at every annual price from 2019 to 2024. The box now makes the same two separate statements. No number changed | clear language only |
| 14.1 | Heading now "Cultivated meat and seafood: open attitudes, tiny sales". Cultivated and in-vitro meat and co-manufacturing explained. Play T8 decoded at first use ("play T8, cultivated seafood research") | clear language only |
| 14.2 | Heading now "Precision-fermented proteins: an ingredient for firms that pay for function". The ingredient examples became a list; lactoferrin and recombinant protein explained. The GMO paragraph split in two ("The same buyers sell GMO-free"; "The clash with GMO labels is narrower than it looks"). "High-inclusion" became "uses at high doses" | clear language only |
| 14.3 | Heading now "Fermented foods and fungi: 'fermented' is a positive word". Koji, mycoprotein, mycelium, PHP (Philippine pesos) and clean label explained; long sentences split | clear language only |
| 14.4 | Added a one-line definition of a blend. GFI APAC, A*STAR, value lines, DHA, emulsion sausages, binders, TCVN, DIAAS and free on board explained. "HS 2106.10" written out as "harmonised system code 2106.10", since the abbreviation was used only once. Long cost paragraph split into four | clear language only |
| 14.4 | Domestic-maker sentence now says "a domestic maker of textured plant protein (play T1 in [[ch26-plays]])". The last "why blending" bullet changed from "matters for the supply-security and welfare cases" to "matters for the security of the protein people eat and for animal welfare" | reframed for food |
| 14.5 | Heading now "Words, trust and religion: avoid 'artificial', 'fake' and 'filler'". The long "artificial and fake" bullet split in three. "The same outlet uses *thịt giả*" became "The news site Dan Tri uses *thịt giả*", because "the same outlet" pointed back to a financial outlet, but the search counts are Dan Tri's. The *độn* bullet split in two. *chay*, JAKIM and *giò chả* glossed | clear language only |
| 14.6 | Heading now "What this means for the frontier categories". Item 2 (precision-fermented ingredients) now names play T7 (high-value, low-dose precision-fermentation ingredients) with a link; item 3 names play T8. The policy-makers bullet split in two. *thịt*, *sữa* and *phô mai* glossed. "Underwrite" became "judge"; offtake letters explained | clear language only |
| 14.6 | Research bodies: "the HUST group behind existing Vietnamese studies" became "the university group behind the existing Vietnamese sausage studies" (see the unresolved items) | clear language only |

Tiles and charts: none removed or added. `key_numbers` and `charts` are unchanged on both pages. The correction callout in 14.1 is kept word for word.

## Unsure or for the consolidating editor

1. **Vissan soy share: 31% against 33%.** I changed the ch14 box to 22 of 67 (33%), matching the ch14 body, the ch16 body, Appendix D5 (`app-d5-buyers`) and tile `kn-vissan-soy-share`. These pages still say 31% (the wave 6 count, 19 of 61): `front-prologue` (blends row, line 47), `front-exec-summary` (finding 5, line 59), `brief-research` (line 62), the ch16 opening box (line 19) and `ch25-demand-to-frontier` (line 35). Please check `front-exec-summary-vi` too. This needs an M5 corrections-table entry and propagation. If you prefer to keep 31%, revert the ch14 box.
2. **Soy extension saving.** `ch25-demand-to-frontier` (line 47) and `front-exec-summary` (finding 5) link "VND 9,100 to 16,600 per kg" to "every annual hog price from 2019 to 2024". The tile and the ch14 and ch11 bodies give the range at 2019 and 2020 hog prices. Consider aligning the wording; no number needs to change.
3. **HUST or HCMUT.** `data/hybrid_savings.csv` labels the *chả lụa* recipe "HCMUT best-liked recipe C1". HXE-01 and HXE-02 appear in the Science and Technology Development Journal, which is published in Ho Chi Minh City. So "HUST" (Hanoi University of Science and Technology) may be wrong. I did not retrieve the authors' affiliations. I removed the abbreviation rather than spell out a name that may be wrong. Please confirm the institution and name it if it is useful.
4. **Street-meal price.** Tile `kn-protein-cost-serving` gives a street meal as VND 29,000 to 35,000. ch13 13.4 gives VND 30,000 to 35,000 [@CHY-40]. I left both unchanged, since tiles are out of scope. Please reconcile.
5. **"Frontier".** The package uses "frontier" (frontier categories, frontier technology) without a glossary entry. I defined "frontier categories" in the ch14 box and renamed the ch13 closing section. A glossary entry (Appendix R3) would help other pages.
6. Both pages grew by about 300 words, mostly from first-use explanations of terms and abbreviations. Reading times are updated (ch13 20 minutes, ch14 19 minutes).
