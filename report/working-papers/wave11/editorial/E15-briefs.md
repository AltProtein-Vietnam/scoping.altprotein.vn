# E15-briefs: editorial log for the six audience briefs (version 0.8)

Editor: E15-briefs. Date: 2026-10-01. Files: `content/02-briefs/brief-investors.md`, `brief-policy.md`, `brief-startups.md`, `brief-manufacturers.md`, `brief-research.md`, `brief-international.md`.

Applied `working-papers/wave11/EDITORIAL-v0.8.md` sections 2, 4 and 6, including the coordinator's two later corrections: "three lead under almost every weighting" (not "every"), and no claim that milk is mostly produced in Vietnam. No wave 11 findings were added. "Version 0.7", the draft notices and the not-for-citation status were not touched. `python3 tools/validate.py`: 0 errors. The 2 warnings are about tiles and charts that briefs never used. No em or en dashes.

Every brief now has:
- the scope line "Protein for people first; feed only as context";
- the seven active plays, with T1, T4 and T5 leading "under almost every weighting";
- the three top policy steps (new-food clause, joint note on precision-fermented proteins and GMO status, novel-food procedure in the decree);
- the seven no-regret moves;
- the new vision.

These use the shared headline wording. Retired codes (T2, T3, T6, P2, P3, PO-017, PO-018, PO-021, PO-029, PO-007) no longer appear. Each footer's code example changed from PO-017 to PO-015.

Token audit, against commit 97231c9:
- **Removed citations:** only those of feed claims: FM-01, FM-12, FBA-01 to FBA-05, FBA-07, FBA-17 (startups and investors only), FBA-20, EXP-50.
- **Added citations:** copied from the chapters with their original tags. DIE-01, DIE-02, DIE-03 `{VN-direct|Medium}` and DIE-07, DIE-08 `{VN-direct|High}` come from ch11 (meat intake 136.4 g; 42% of protein from animal foods). DIE-25 `{VN-direct|Medium}` comes from ch11 (pig price +70% after African swine fever, policy only). APR-07 `{VN-direct|Medium}` is the Food Safety Law timing (startups).
- **Added model numbers:** taken from section 6 of the editorial brief and tagged `{VN-direct|Low} {fx:estimate}`. They are 1.01 to 1.45 Mt meat protein; 7.2 to 10.4 Mt soybean meal; 4.5 t and 9.5 t avoided per t; 0.4% displaced in 2050; and the vision's 67,000 to 172,000 t and 59,000 to 147,000 t.
- No `{fx:vision}` tag is used outside chapter 24.

## brief-investors

| section | change | type |
|---|---|---|
| frontmatter summary | Rewritten: food-ingredient and fermentation theses; T1 debt-financed; T4 and T5 with strategic partners; scope line added; T2 sentence removed | reframed for food |
| The short version | Scope line first; three bullets (T1 debt-financed import substitution; T4 and T5 with strategic partners; capital cost and Chinese imports); T2 sentence removed | reframed for food |
| What you need to know 1 | Entobel kept only as a deal-structure template, labelled "an insect-feed deal, outside this study's focus"; "B2B feed product" removed | reframed for food |
| What you need to know 3 | Fungal cost stack described as "fungal biomass protein" (editorial 2.6); fishmeal-protein comparator (USD 2,625 to 3,846) removed | pruned feed |
| What you need to know 4 | Claim that Chinese bacterial biomass is sold into Vietnamese feed [@FM-12] removed; heading now "The competitor is Chinese" | pruned feed |
| What you need to know 5 | "Feed is open" and feed-list gaps removed; now "Food rules have no gate yet" | pruned feed |
| Theses table | T2 and T3 rows removed. T4 reworded (food fermentation, strategic partners, "hub" explained). New rows for T5, T9 and T10, built only from `plays.csv` and ch26 kill tests; no new numbers. Intro sentence on the seven plays added | pruned feed; reframed for food |
| Who else is here | Made a list; "feed" dropped from strategic buyers | pruned feed |
| What would make this more investable | "Options 1 and 5" became the three top options (1 to 3). Feed-list fixes (options 3 and 4) removed. First-loss tranche now for a food-ingredient or fermentation plant (T2 feed case removed) | pruned feed; reframed for food |
| The demand side | "Feed demand is revealed but priced low" bullet removed (inactive yeast, Skretting, Nutreco, BAP; FBA-17, FBA-07, FBA-01, FBA-05). Other bullets split into shorter sentences | pruned feed |
| Looking to 2050 | Scenario axis renamed "stress on imported protein". Plays list now T4, T5, T9 (T2, T6 removed) and T7 as the bet (T3 removed). Removed: fishmeal pricing advice, "fungal feed protein" became "fermentation protein", the "Mind the scale" microbial-feed-capacity bullet, power-to-protein on the shrimp coast. Seven moves and vision added | pruned feed; reframed for food |
| tiles | Removed `kn-salt-plants-2050` (embed and frontmatter), `kn-feed-yeast-imports` (embed and frontmatter), and `kn-cost-fungal-feed`, `kn-fishmeal-protein-price`, `kn-p2p-cost-vn-2050` (frontmatter only) | tile or chart removed |
| whole page | Shorter sentences; abbreviations explained (IFC, ADB Ventures, HS, FOB, ACFTA, GMO, CO2e, titer, tolling); "IPOs" became "stock-market listings" | clear language only |

## brief-policy

| section | change | type |
|---|---|---|
| frontmatter summary | Scope line added; case framed as the security of the protein people eat | reframed for food |
| The short version | Scope sentence first. Feed-import and feed-target numbers moved to a new section. Food Safety Law deadline kept | reframed for food |
| New section "Why it matters: the security of the protein people eat" | Shared "Why Vietnam" wording, with meat-intake and 42% claims copied from ch11 and ASF price claim from ch11. Feed imports (99% soy protein, three-quarters maize, USD 10 billion) and the 30 to 32 Mt feed target kept as context. The 0.2% limit added from ch18. "milk" dropped from "produced in Vietnam on imported feed" (coordinator correction) | reframed for food |
| New section "What could be made first" | Seven plays, T1, T4 and T5 leading, shared wording | reframed for food |
| What you need to know | Item "Feed rules are more open but have two gaps" (aquafeed list, livestock list, Decree 211/2026 fines) removed | pruned feed |
| Options, ranked | Ranks renumbered to v0.8: 1 PO-015, 2 PO-016, 3 PO-019 (was 5), then "4 to 9". Old rank 3 (aquafeed list) and rank 4 (livestock list) removed, and "public feed trials" removed from the grouped row. Ministry names explained; "All 33 options in the register" | pruned feed; reframed for food |
| Alignment | Made a list; Decision 1520 described as "by-product use" (feed dropped) | pruned feed |
| For provinces | "Mekong Delta provinces hold the aquafeed buyers" removed | pruned feed |
| The demand side | Content kept; long sentences split; school-menu tools and trade asks made into sub-lists; abbreviations explained (TCVN, VFA, MOET, NIN, CPTPP; FTA acronyms written out); "Corporate pledges" became "Corporate targets" | clear language only |
| Looking to 2050 | Removed the bullet on the 2030 feed target covering livestock only (26.4 Mt against 30 to 32 Mt). "Feed efficiency does about twice the work" replaced by the editorial's context sentence (3.4 Mt, outside the study's focus). Trend paragraph added (meat protein, soybean meal behind it, food route saves most imports). "Nine no-regret moves" became seven (feed-efficiency and omega-3 moves removed). "Feed-protein sites" became "food-fermentation sites". Vision rewritten (soybean-meal, microbial-share and omega-3 goals removed) | pruned feed; reframed for food |
| tiles | Removed `kn-feed-target-livestock-2030` (embed and frontmatter) and `kn-vision-sbm-2050` (frontmatter). Added existing tiles `kn-meat-intake-2020` and `kn-sbm-need-2050` to frontmatter only | tile or chart removed |

## brief-startups

| section | change | type |
|---|---|---|
| frontmatter summary | "listed feed materials" removed; scope line added | pruned feed |
| The short version | Scope line; "concentrated feed buyers" removed; four founder rules made a list | pruned feed |
| Pick a food with a route | Three feed rows removed (livestock-feed materials, aquafeed, bacterial SCP in feed) with the feed-fine sentence. Pointer added to ch07 for feed routes. Three top policy steps added, with the APR-07 law timing | pruned feed; reframed for food |
| Plays that suit founders | T2 (functional feed ingredients, FBA-17 yeast claim) and T6 (duckweed feed) removed. T10 and T8 added from `plays.csv` and ch10 (no new numbers). Seven-plays sentence added | pruned feed; reframed for food |
| Where to locate | "Aquafeed buyers and trials" bullet removed | pruned feed |
| Borrow capacity | "Feed mills ... can host trials" bullet removed; scale-up options and abbreviations (CDMO, NIFC) explained | pruned feed |
| Design for Vietnam | Feed VAT bullet removed | pruned feed |
| Money | Made a list; Entobel labelled an insect-feed maker | reframed for food |
| Looking to 2050 | "Functional feed ingredients" removed from the windows (made a list). "Species-specific function" removed from edges. Omega-3 bullet removed. Seven moves and vision added | pruned feed; reframed for food |
| tiles | Removed `kn-omega3-need-2050` (embed and frontmatter) and `kn-fungal-protein-floor` (frontmatter). Added existing `kn-food-law-window` to frontmatter | tile or chart removed |

## brief-manufacturers

| section | change | type |
|---|---|---|
| title | "Brief for food and feed manufacturers" became "Brief for food manufacturers"; short title "Food manufacturers" | retitled |
| frontmatter summary | Feed companies and yeast removed; scope line added | pruned feed |
| The short version | Fishmeal price and feed-output target removed. Feed protein behind meat kept as context (99% soy protein, linked to ch01). T2 removed. Firm first steps added from shared wording | pruned feed; reframed for food |
| Food and beverage | Kept; long sentences split; HS, FOB, ACFTA explained; three top policy steps added under "Rules to watch" | clear language only |
| New section "What could be made first" | Seven plays, T1, T4 and T5 leading, and the manufacturer's role in each | reframed for food |
| Feed (7 items) | Replaced by "Feed: context only". Removed: fishmeal price (FM-01, FBA-20), fishmeal replacement rates, T2 function premium, aquafeed legal route, Chinese microbial feed protein, ASC and BAP certification (FBA-01 to FBA-05). Kept: inactive-yeast import fact (food and feed) and feed mills as context | pruned feed |
| What you could do | T2 feed-trial action removed; "volume commitment" became "agreed volume" | pruned feed |
| Export angles | Made a list; CPTPP explained | clear language only |
| The demand side | Kept; sentences split; "SKUs" became "products"; HoReCa written out | clear language only |
| Looking to 2050 | Soybean-meal "levers in your hands" (feed formulation) removed; replaced by the shared trend paragraph. "Fishmeal shortages" dropped from shocks. Omega-3 and trash-fish bullets removed. Seven moves and vision added | pruned feed; reframed for food |
| tiles and charts | Removed `chart-price-to-beat` (embed and frontmatter), `kn-efficiency-vs-alt` (embed and frontmatter), and `kn-fishmeal-aug-2026`, `kn-shrimp-feed-concentration`, `kn-shrimp-fishmeal-replacement` (frontmatter). Added existing `kn-soy-protein-import`, `kn-food-law-window` to frontmatter. `app-s6-feed-market` removed from related pages and read next (still linked once in the feed-context section) | tile or chart removed |

## brief-research

| section | change | type |
|---|---|---|
| frontmatter summary | Food research gaps named (protein quality, phytate and zinc, strain safety, sensory tests, duckweed food safety); scope line | reframed for food |
| Where Vietnam stands | Fish and shrimp feeding trials kept as a strength, marked "feed, now context"; DIAAS and PDCAAS explained | reframed for food |
| Research questions | Reordered to lead with food: protein quality, phytate and zinc; strain characterisation; fungal biomass safety; thermotolerant yeasts; duckweed food safety; texturisation; cultivated seafood cells; biogas protein. The two fish-diet questions (SCP and fungal meal in pangasius and shrimp; mixed-culture protein in shrimp, with the preprint's 50% and 90% figures) moved to a short "now context" note | pruned feed; reframed for food |
| New paragraph "How this research fits the plays" | Seven plays, T1, T4 and T5 leading; links T9, T10, T8 to the research above | reframed for food |
| Public goods | "Public feed trials" (PO-021) removed. Price series now for food protein ingredients (P6). Shared pilot fermentation (T5, PO-026) added, with a university or FIRI as possible anchor host (from `plays.csv`). Three top policy steps added | pruned feed; reframed for food |
| Funding and partners | "Chinese groups (cassava-to-protein and gas-to-protein feed)" removed; NAFOSTED, VINIF, ACIAR explained | pruned feed |
| The demand side | Kept; sentences split; list of studies made a sub-list. The correction callout kept unchanged | clear language only |
| Looking to 2050 | Feed questions removed (feed conversion and soybean-meal inclusion by species; EPA plus DHA needs). "Protein and feed balance" became "protein balance". Seven moves and vision added | pruned feed; reframed for food |
| tiles | None removed | |

## brief-international

| section | change | type |
|---|---|---|
| frontmatter summary | Scope line; "trial capacity" replaced by protein-quality testing | reframed for food |
| The short version | "Strong feed industry" removed; feed described as the hidden import; "development finance fits import substitution and feed" became "import substitution"; "leverage points" reworded | pruned feed; clear language only |
| Why Vietnam matters | Seafood exports and aquafeed and fishmeal bullet removed. Meat-intake and 42% bullet (ch11 citations) added. "Food route saves most imports per tonne" bullet added | pruned feed; reframed for food |
| New section "What the study recommends" | Seven plays (T1, T4, T5 leading) and three policy steps | reframed for food |
| Entry points | "Six" became "Five". Entry point 2 "Feed-list and trial capacity" (PO-017, PO-018, PO-021) removed. Entry 1 now covers options 1 to 3 including the joint note. First-plant finance now for a food-ingredient or food-fermentation plant with a food-manufacturer buyer, Entobel as structure only. Open data: "regional Asian fishmeal price series" replaced by a price series for food protein ingredients (P6) | pruned feed; reframed for food |
| Precedents | Entobel labelled an insect-feed deal outside the focus, kept as deal structure | reframed for food |
| Motivations | "Food and feed security" became "the security of the protein people eat" | reframed for food |
| Coordination | "Feed, aquafeed" dropped from MAE's listed remit | pruned feed |
| The demand side | "Development finance: import substitution and feed" became "import substitution". Funder routes made a sub-list. "Corporate commitments" and "pledge campaign" reworded | pruned feed; clear language only |
| Looking to 2050 | "Protein and feed balance" became "protein balance"; seven moves and vision added; long-horizon list made a sub-list | reframed for food |
| tiles | None removed; existing `kn-meat-intake-2020` added to frontmatter | |

## Unsure or for the consolidating editor

1. **`kn-no-regret-moves` still reads "9 of 21 moves"** in `data/key-numbers.json`. It is embedded in brief-policy and brief-international next to text that says seven. The tile needs updating to 7 of 21.
2. **`chart-plays-scoring` is titled "Ten plays, scored ..."** in `charts/chart-specs.json`. Its filter (`type == play`) already drops retired plays, but the title needs changing (embedded in brief-investors).
3. **`chart-route-to-market` (brief-startups)** draws on `data/routes.csv`, which includes feed routes RT-008 to RT-016. I kept the embed because most rows are food. You may want to filter it to food routes.
4. **`site-manifest.json`** still carries the old title ("Brief for food and feed manufacturers"), short title, summaries and reading times for all six briefs. It needs syncing with the new frontmatter. Reading times are now: investors 9, policy 9, startups 7, manufacturers 8, research 7, international 8.
5. **`kn-cost-fungal-feed`** is labelled "fungal feed protein". In brief-investors the same numbers (54 to 67%; USD 4,050 to 14,700 per t of protein) are now described as "fungal biomass protein", following editorial 2.6. The tile label may need the same change.
6. **Uncited shared wording.** "Vietnamese people eat more meat each year" and "Most of that meat, and the eggs and farmed fish, is produced in Vietnam on imported feed" (policy; meat only in the other briefs) carry no citation in the briefs. The consolidating editor may want to add the FAO figure (about 90% of meat, 2023) with its source once it is in the package.
7. **Mycoprotein plant may be stale.** brief-investors keeps "a 20,000 t mycoprotein plant is under construction" unchanged. Chapter 3 now says a 20,000 t mycoprotein plant began commercial runs in June 2026. Worth reconciling, but I did not change the claim.
8. **Biogas protein.** In brief-research, "bacterial protein from pig-farm and cassava-starch biogas" stays in the main research list. Chapter 6 does not say whether it is for food or feed.
9. **Feed target kept as context.** brief-policy keeps the 2030 industrial feed target (30 to 32 Mt [@REG-54; @MAC-28]) as context for the hidden feed import, as chapter 19 does. It dropped the "livestock only, 26.4 Mt" analysis.
10. **"Hub" glosses.** brief-startups and brief-policy explain "hub" as a cluster of plants on one site at first use. Other pages may word it differently.
