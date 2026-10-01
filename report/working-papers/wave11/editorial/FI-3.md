# Editor log FI-3: wave 11 food-security findings carried into the summaries, FAQ, prologue and briefs

Editor: FI-3 (consolidating editor for the summary pages and briefs). Date: 2026-10-01.

Files edited: `content/00-front/front-cover.md`, `front-two-minute.md`, `front-exec-summary.md`, `front-at-a-glance.md`, `front-faq.md`, `front-prologue.md`; `content/02-briefs/brief-policy.md`, `brief-international.md`, `brief-investors.md`, `brief-research.md`, `brief-manufacturers.md`, `brief-startups.md`; `content/01-report/ch14-frontier-demand.md`, `ch16-business-buyers.md`. No other file edited. No data, tile, chart, register or manifest file edited. Chapters 20 and 23 and Appendix F2 not touched.

Checks at the last run: `python3 tools/validate.py` 81 pages, 0 errors, 0 warnings; `python3 tools/check_registers.py` 0 errors. No em or en dash, no contraction in my files. "Version 0.7", the draft notices and "not for citation" are unchanged.

Sources of the wording: chapter 1 (authoritative statement of the food-security case), chapter 11 (soy origin), chapter 20 (wild fish, disease), chapter 22 (import share to 2050), chapter 30 (eighteen unknowns) and the line papers L1 to L4. Every number, citation and tag was copied from those pages or papers. No new number was calculated. Only registered IDs are used (OQ-448, OQ-453, OQ-462, OQ-463). The summary pages (cover, two-minute, executive summary, at a glance, FAQ) carry no inline citations by the existing convention of those pages; every number on them is cited in the chapter the page links to. The prologue, the briefs and chapters 14 and 16 carry citations and tags on every new claim.

## Per page

### front-exec-summary

| Section | Added or changed | Tiles (frontmatter) and where the numbers come from |
|---|---|---|
| Frontmatter | Summary: the case is a security case "real but narrow"; two thirds of animal protein rests on imports; only domestic inputs reduce that. Reading time 12 to 14. `related_pages` + ch11, ch20, ch30 | `key_numbers` + kn-protein-supply-imported, kn-animal-protein-on-imports, kn-soybean-import-dependence, kn-milk-self-sufficiency, kn-meat-imports-2025, kn-origin-price-support, kn-imported-meat-displaceable-2035, kn-pork-price-2020, kn-asf-recombinant-share, kn-asf-culls-vs-spared, kn-china-share-plant-protein-ingredients, kn-marine-stock-fall (the page embeds no tiles) |
| Why Vietnam | "about 90% in 2023" added for meat produced at home; closing sentence "The security case is real but narrow, as the next section shows" | ch01 1.1 (DIE-07) |
| New section "Food security: what the evidence supports, and what it does not" | Seven bullets (see the numbered list below) | ch01 1.1, 1.3, 1.6; ch11 11.1; ch20 20.1; ch28 28.1 |
| Demand item 2 | "pork prices jumped 70%" now "pig producer prices jumped 70%" (FI-1 note 6: the 70% is the FAOSTAT producer price, not the consumer price) | ch11 (DIE-25) |
| For each reader | Investors, policy makers, research bodies and international bodies each gain one sentence | ch01 1.6, 1.7 |
| What would change our view | New last item on a measured study of disease risk | ch01 1.6 (DG-356) |
| Closing line | "twenty unknowns" now "eighteen unknowns ..., four of them on food security" | ch30 |
| About this report | "ten rounds of desk research (2,384 sources)" now "eleven rounds (2,474 sources)" | `check_registers.py` count; ch30 "eleven research rounds" |

### front-two-minute

New paragraph "Food security: real, but narrow." after Why Vietnam: 61% to 71% of animal protein on imports (2023, our calculation); pork prices +57% in 2020; no evidence of reliance on subsidised meat; no evidence that alternative protein lowers disease or pandemic risk; imported soy only moves the dependence; only domestic inputs reduce it; small effect at the scale demand supports. Tile `kn-animal-protein-on-imports` embedded and added to frontmatter. The disease sentence in Why Vietnam moved into the new paragraph. Summary mentions food security. Exec summary reading time in "Read next" 12 to 14 minutes. Reading time stays 2.

### front-at-a-glance

- First section retitled "Where the protein people eat comes from" (links ch01, ch11), with a three-sentence lead (one fifth of protein imported food; two thirds of animal protein on imports). Tiles embedded: kn-protein-supply-imported, kn-animal-protein-on-imports, kn-soybean-import-dependence, kn-milk-self-sufficiency (beside the existing six). New line "Imported meat and dairy are a second, smaller exposure" with kn-meat-imports-2025, kn-dairy-imports-2025, kn-origin-price-support.
- New section "Food security: disease, wild fish and what new protein would change" (links ch01, ch20): kn-pork-price-2020, kn-asf-recombinant-share, kn-asf-culls-vs-spared, kn-china-share-plant-protein-ingredients, kn-imported-meat-displaceable-2035, kn-marine-stock-fall.
- Futures: one sentence on the share of meat protein resting on imports (70% to 78% in 2025 to about 79% to 87% in 2050, ch22) and one on imported soy keeping the dependence; kn-meat-protein-on-imports-2050 embedded.
- Vision: one sentence ("For security, what counts is the share made from domestic inputs, not the share made in Vietnam"); kn-vision-protein-new-routes-2050, kn-vision-made-in-vietnam-2050, kn-vision-domestic-ingredient-share-2050 embedded.
- Frontmatter: 17 tiles added to `key_numbers`; ch11 and ch20 added to `related_pages`; summary mentions where protein comes from. Reading time stays 4.

### front-faq

- New Q&A "Does Vietnam depend on subsidised imported meat?" (978,000 t, USD 2.0 billion, 2025; about 90% of meat domestic; beef, buffalo meat and milk most import-dependent; no price support for most of what Vietnam buys; India taxes buffalo meat; export subsidies ended under WTO rules; Russian pork the partial exception; pig farm prices 1.6 to 2.8 times origin prices, 2024). Source chapter: ch01 1.1 and 1.6 (MIM-04, MIM-05, MIM-15, MIM-16, MIM-17, DIE-07).
- New Q&A "Would alternative protein lower the risk of pandemics or animal disease?" (no measuring study; claims from reviews and opinion, several by advocacy or company authors; risk tied to wildlife trade, live-bird markets, biosecurity and antibiotic use; 142,000 pigs spared in 2035 against 2025 culls 8.4 times that; value is a second source). Source chapter: ch01 1.3 and 1.6 (PAN-25 to PAN-33, MAC-01, PAN-03).
- "Why Vietnam?" gains the two-thirds sentence and "real but narrow: only protein made from domestic inputs reduces import dependence".
- "Would domestic production make Vietnam self-sufficient?" gains one sentence on domestic inputs; link to ch01 added.
- Counts: "ten rounds" to "eleven rounds; the eleventh tested food-security claims"; "184 tables, 2,384 sources" to "194 tables, 2,474 sources" (194 CSV files in `data/` now; 184 in v0.7). "Twelve minutes" to "Fourteen minutes". Summary mentions food security. Reading time 7 to 8.

### front-cover

The intro paragraph is the cover's case in brief, so it gains one sentence: "Counting that feed, about two thirds of the animal protein people eat rests on imports, so the case for making protein at home is first a security case: real, but narrow." Tile `kn-animal-protein-on-imports` embedded and added to frontmatter. Counts "184 tables (among them 2,384 sources" to "194 tables (among them 2,474 sources". Reading times in Start here: prologue 17 to 22 minutes (the page's own frontmatter now says 22), executive summary 12 to 14 minutes. Vietnamese reading times (16 and 17 phút) not changed: see "For the lead".

### front-prologue

See the numbered list below. Frontmatter: reading time 20 to 22; `related_data` + meat_dairy_imports.csv, origin_support.csv; `related_pages` + app-d8-demand-model. No tile added. Sources cited in the new text: MAC-01, PAN-03, PAN-27, PAN-28, PAN-29, PAN-30, PAN-31, BUY-02, MIM-01, MIM-04, MIM-05, MIM-12, MIM-15, MIM-16.

### brief-policy

- New section "Food security: measure first, and be precise about what new protein does", four bullets: (1) 19% to 23% of protein supply imported food [DIE-07]; 61% to 71% of animal protein on imports [DIE-07; MAC-01; FS-23]; Resolution 34/NQ-CP has no import, feed or protein indicator [SEC-01]. (2) A national protein balance for people is the first move; chapter 1 is a first version; MAE's 2026 "reduce import dependence" task is the hook [SEC-02]; define the indicator by input origin, since about 84% of food plant-protein ingredients came from China in 2025 [BUY-02]. (3) Consumer pork +57.23% in 2020 [SEC-08]; 79% recombinant in the north and licensed vaccines "have no protective effect" [PAN-33]; new protein is a second source, not disease control [PAN-27; PAN-30; PAN-31]; 142,000 pigs against 8.4 times that [MAC-01; PAN-03] {fx:estimate}. (4) Meat imports 978,000 t, USD 2.0 billion [MIM-04; MIM-05]; no price support for most of what Vietnam buys [MIM-15]; no trade-defence case [MIM-25].
- Embedded kn-animal-protein-on-imports, kn-asf-recombinant-share. Frontmatter `key_numbers` + kn-protein-supply-imported, kn-animal-protein-on-imports, kn-pork-price-2020, kn-asf-recombinant-share, kn-asf-culls-vs-spared, kn-china-share-plant-protein-ingredients, kn-meat-imports-2025, kn-origin-price-support; `related_pages` + app-d8-demand-model.
- "Why it matters": "about 90% of the meat supply was domestic in 2023 [@DIE-07] {VN-direct|High}" added (answers E15 note 6).
- MAE and FAO now explained at first use in the new section. Summary adds the protein-balance sentence. Reading time 9 to 11.

### brief-international

- "Why Vietnam matters": new bullet on 61% to 71% [DIE-07; MAC-01; FS-23], no import or protein indicator [SEC-01], no Vietnamese food balance, protein balance as a public good for statistical cooperation; the per-tonne bullet adds that only domestic inputs reduce dependence (84% from China [BUY-02]).
- "Motivations and framing": two new paragraphs, "The pandemic claim is not supported by measured evidence" [PAN-27; PAN-30; PAN-31; PAN-28; PAN-29; Vietnam: PAN-25; PAN-26] and the One Health levers (surveillance, biosecurity, wildlife-trade control; One Health explained), with the 142,000 pigs and 8.4 times scale [MAC-01; PAN-03] {fx:estimate}.
- Entry point 5 (open data) adds a yearly national protein balance (RM-01, link to ch28). Column count unchanged.
- Frontmatter: summary rewritten in shorter sentences, names the protein balance and says the evidence does not support funding alternative protein as pandemic prevention; `key_numbers` + kn-animal-protein-on-imports, kn-asf-culls-vs-spared, kn-china-share-plant-protein-ingredients; `related_pages` + app-d8-demand-model. Reading time 8 to 9.

### brief-investors

- New item 7 in "What you need to know": "The security case is real but narrow, and it favours domestic inputs" [DIE-07; MAC-01; FS-23; BUY-02; SEC-05; SEC-14; FS-24; FS-01]; check input origin; do not pitch disease or pandemic benefits.
- Summary adds one sentence; `key_numbers` + kn-animal-protein-on-imports, kn-china-share-plant-protein-ingredients; `related_pages` + ch01. Reading time stays 9.

### brief-research

- New section "Four gaps that decide the food-security case": OQ-463 domestic share of soybeans for tofu and soy milk [DIE-07]; OQ-453 input origin of alternative-protein foods by route [TIC-12; TIC-13]; OQ-462 a Vietnamese food balance [DIE-07]; OQ-448 an ASF vaccine for the recombinant strains [PAN-33]. Embedded kn-soybean-import-dependence.
- Summary adds the four gaps; `key_numbers` + kn-soybean-import-dependence, kn-protein-supply-imported, kn-asf-recombinant-share; `related_pages` + ch01, ch30. Reading time 7 to 8.

### brief-manufacturers

- New bullet in "The demand side": "Imported pork sets a lower bar for some blends": frozen pork landed at about VND 42,600 per kg CIF in January to July 2026, about half the carcass-equivalent price of domestic pigs [MIM-09; MIM-07]; processors using imported trimmings save less from extension; frozen pork and mechanically deboned meat are the only meat imports a blend could plausibly displace; feet, offal and buffalo meat for *phở* have no substitute [MIM-05; MIM-06]; at most about 1.6% of imported meat protein by 2035 [MIM-04; QNT-01] {fx:estimate}.
- Summary adds one sentence; `key_numbers` + kn-meat-imports-2025, kn-imported-meat-displaceable-2035; `related_pages` + ch01. Reading time 8 to 9.

### brief-startups

- New bullet in "Design for Vietnam": "Inputs, if security is part of your pitch" [BUY-02; SEC-05; SEC-14; FS-24; FS-01]; no disease or pandemic claims.
- Summary adds "If food security is part of the pitch, prefer domestic inputs."; `key_numbers` + kn-china-share-plant-protein-ingredients; `related_pages` + ch01. Reading time 7 to 8.

### ch14-frontier-demand (section 14.4)

New paragraph "Imported pork lowers the bar for some processors" after the soy-extension paragraphs: VND 42,600 per kg CIF, January to July 2026, about half the carcass-equivalent price of domestic pigs [@MIM-09; @MIM-07] {VN-direct|Medium} {dx:revealed}; frozen pork and mechanically deboned meat the only plausible displacement; at most about 1.6% of imported meat protein by 2035 [@MIM-04; @QNT-01] {VN-direct|Low} {fx:estimate} {dx:inferred}. MIM-09 is the source of the CIF price (pork 112,090 t, USD 1,638 per t); MIM-07 gives the domestic live pig price used in L1's comparison. Frontmatter: `key_numbers` + kn-imported-meat-displaceable-2035; `related_data` + meat_dairy_imports.csv; `related_pages` + ch01. Reading time unchanged.

### ch16-business-buyers (section 16.3, meat processors)

Same finding in three sentences after the Vissan extension paragraph, with the same sources and tags. Same frontmatter additions. Reading time unchanged.

## Executive summary: numbered list of substantive changes (for `front-exec-summary-vi`)

1. Frontmatter summary: the case is "a security case, real but narrow: about two thirds of the animal protein people eat rests on imports, directly or through feed, and only protein made from domestic inputs reduces that".
2. Why Vietnam: "Most of that meat (about 90% in 2023), and the eggs and farmed fish, is produced in Vietnam on imported feed."
3. Why Vietnam, end: "The security case is real but narrow, as the next section shows."
4. New section after Why Vietnam, "Food security: what the evidence supports, and what it does not", with an intro line and seven bullets:
   1. Two thirds of animal protein rests on imports: 19% to 23% of protein supply imported food (2023); 61% to 71% of animal protein on imports counting feed (our calculation); soybeans for tofu and soy milk 97.5% imported; milk about 30% self-sufficient on FAO's measure (FAO spelled out).
   2. Imported meat is growing, but not subsidised: 978,000 t, USD 2.0 billion (2025); the evidence does not support reliance on subsidised meat; for most of what Vietnam buys the origin gives no price support, and farm costs abroad are lower; new protein would displace at most about 1.6% of imported meat protein by 2035 (our calculation).
   3. Disease is the shock consumers feel: consumer pork prices +57.23% in 2020; people switched to chicken and imported pork, not tofu; the agriculture ministry says the licensed vaccines do not protect against the recombinant strains now dominant in the north.
   4. We found no evidence that alternative protein lowers disease risk: no study measures lower zoonotic, pandemic or antimicrobial-resistance risk from replacing meat; risk depends on how animals are farmed and traded; 2025 culls were 8.4 times the pigs new protein would spare in 2035 (our calculation).
   5. Only domestic inputs reduce dependence: alternative protein from imported soy, pea or wheat gluten moves it; about 84% of food plant-protein ingredients from China (2025, our calculation); fermentation on cassava or sugar, rice and peanut protein, and soy foods from Vietnamese beans reduce it.
   6. Wild fish is under most pressure: marine fish stock in 2016 to 2020 22.1% below 2000 to 2005; alternative protein does not touch this at the scale demand supports.
   7. Official food security counts volumes, not imports: Resolution 34/NQ-CP has no import or protein indicator; a national protein balance by food, source and origin is the first move; chapter 1 builds a first version from FAO data.
5. Demand item 2: "pork prices jumped 70%" becomes "pig producer prices jumped 70%".
6. For each reader, investors: "If a thesis rests on food security, check that the inputs are domestic."
7. For each reader, policy makers: "Publish a national protein balance that shows where the protein people eat comes from."
8. For each reader, research bodies: "For food security, the gaps are the domestic share of soybeans in tofu and soy milk, and a Vietnamese food balance."
9. For each reader, international bodies: "Do not fund alternative protein as pandemic prevention: the levers for that are surveillance, biosecurity and control of the wildlife trade."
10. What would change our view, new last item: "A study measures lower zoonotic or antimicrobial-resistance risk from replacing meat with alternative protein. We found none."
11. Closing line: "The eighteen unknowns that matter most, four of them on food security, and who can answer each, are in [[ch30-unknowns]]." (The Vietnamese page still says "Hai mươi".)
12. About this report: "eleven rounds of desk research (2,474 sources)" (the Vietnamese page says "mười đợt ... (2.384 nguồn)").

## Prologue: numbered list of substantive changes (for `front-prologue-vi`)

1. Method note: research notes are in `working-papers/wave10/` "and for disease risk and imported meat and dairy in `working-papers/wave11/`".
2. P.3 item 2 (Security and resilience), new paragraph after the swine fever sentence: a second source helps because it does not fail when animals fall sick; that is not the same as lowering disease risk, which depends on how animals are farmed and traded (section P.4); in Vietnam, at the scale demand supports, new protein would spare about 142,000 pigs a year in 2035, while 2025 swine fever culls were 8.4 times that (our calculation from [@MAC-01; @PAN-03] and app-d8) {VN-direct|Low} {fx:estimate}.
3. P.3 item 5 (Public health), after the 60% and 72% zoonosis sentence: "These figures show where the risk comes from; they do not show that replacing meat lowers it (section P.4)." The global evidence is kept unchanged.
4. P.4, new bullet after "Processing and health": "Disease risk depends on how animals are farmed and traded." No study measures a fall in zoonotic, pandemic or antimicrobial-resistance risk from replacing animal-source food [@PAN-27; @PAN-30; @PAN-31] {general|Medium}; research ties these risks to the wildlife trade, farm biosecurity and antibiotic use [@PAN-28; @PAN-29] {general|Medium}; a costed study of preventing pandemics at source looks at surveillance, wildlife-trade control and less deforestation, not diet change [@PAN-28] {general|Medium}; in Vietnam, at the scale demand supports, the effect would be negligible (P.3 item 2; ch01).
5. P.4 "New dependencies": adds "China supplied about 84% of the tonnage of food plant-protein ingredients (soy isolate, textured protein and gluten) that reached Vietnam in 2025 (our calculation) [@BUY-02] {VN-direct|Medium}", and the last sentence changes from "A security case needs domestic production, not just a different product" to "A security case needs domestic inputs, not just a different product or a factory in Vietnam" (links ch01 and ch16). **Conclusion narrowed** to match chapter 1.
6. P.6, new paragraph after the soybean paragraph: "Vietnam also imports finished meat and dairy, but origin subsidies do not drive it." 978,000 t of meat and meat products worth USD 2.0 billion and USD 1.44 billion of dairy in 2025 [@MIM-04; @MIM-05; @MIM-12] {VN-direct|Medium} {dx:revealed}; among the largest lines by value in 2023 were frozen beef and buffalo meat (mostly Indian buffalo meat) and skim milk powder [@MIM-01] {VN-direct|High} {dx:revealed}; for most of what Vietnam imports the origin gives no price support, and India taxes its buffalo meat [@MIM-15; @MIM-16] {general|High}.
7. Frontmatter: reading time 20 to 22; `related_data` + meat_dairy_imports.csv, origin_support.csv; `related_pages` + app-d8-demand-model.

## For the lead (outside my files)

1. **Tile `pages` fields** in `data/key-numbers.json` need the new placements. Embedded now: front-cover and front-two-minute (kn-animal-protein-on-imports); front-at-a-glance (kn-protein-supply-imported, kn-animal-protein-on-imports, kn-soybean-import-dependence, kn-milk-self-sufficiency, kn-meat-imports-2025, kn-dairy-imports-2025, kn-origin-price-support, kn-pork-price-2020, kn-asf-recombinant-share, kn-asf-culls-vs-spared, kn-china-share-plant-protein-ingredients, kn-imported-meat-displaceable-2035, kn-marine-stock-fall, kn-meat-protein-on-imports-2050, the three kn-vision tiles); brief-policy (kn-animal-protein-on-imports, kn-asf-recombinant-share); brief-research (kn-soybean-import-dependence). Frontmatter-only additions are listed per page above.
2. **`site-manifest.json`** summaries and reading times are out of sync for front-exec-summary (14), front-faq (8), front-prologue (22), front-two-minute, front-at-a-glance and the briefs (policy 11, international 9, research 8, manufacturers 9, startups 8).
3. **Counts in pages I do not own:** `front-how-to-read` still says "184 tables" (line 44) and "Desk research in ten rounds" (line 143). `front-exec-summary-vi` still says "Hai mươi" unknowns and "mười đợt ... (2.384 nguồn)". I changed rounds, sources and tables on the cover, FAQ and executive summary; if you prefer to change counts only at the version bump, revert those three lines together.
4. **Vietnamese reading times on the cover** (prologue-vi "16 phút", exec-summary-vi "17 phút") do not match the Vietnamese pages' frontmatter (19 and 17) and will change again when those pages mirror this log. I left them.
5. **Chapter 11 line 25** still says "When pork prices jumped 70% after African swine fever"; the 70% is the producer price (FI-1 note 6). I changed the same wording in the executive summary.
6. **Origin support wording in chapter 1** ("no price support in 2022 to 2024 for US, Brazilian, Australian and New Zealand meat and milk") is broader than L1's table, which shows Brazilian pigmeat at an NPC of 1.66 in 2024 (also in the `kn-origin-price-support` tile context). My pages say "for most of what Vietnam buys, the origin gives no price support", which matches L1's reading 1. Consider the same narrowing in chapter 1.
7. **Milk disagreement ID.** Chapter 1 cites DG-367 and DG-368 for the poultry, beef and milk import shares, but those rows cover poultry and beef only; no registered row covers FAO's 30% against the association's "about 40% of demand" for milk (DG-364 is the 2030 target). I did not cite a DG number for milk.
8. **Changelog (M5.14).** Substantive changes from this log: executive summary items 1 to 12 above (new food-security section; producer-price correction; eighteen unknowns); prologue items 2 to 6 (disease-risk counter-evidence; the P.4 "New dependencies" conclusion narrowed to domestic inputs; meat and dairy imports in P.6); new sections in the policy, international, investors, research, manufacturers and startups briefs; the imported-pork note in chapters 14 and 16.

## Unsure

- The summary pages (cover, two-minute, executive summary, at a glance, FAQ) keep their convention of no inline citations and tags. Every number on them is copied from a cited chapter sentence. If the lead wants citations there, the sources are those listed per bullet above.
- "About half the carcass-equivalent price of domestic pigs" (chapters 14 and 16, manufacturers brief) is L1's calculation (USD 1,638 per t at 26,000 VND per USD against VND 85,800 to 95,400 per kg carcass equivalent from MIM-07 at a dressing yield of 0.723). The domestic comparator is early January 2026 and the imported price is January to July 2026, and the products differ (frozen cuts and trimmings against whole carcasses). Both pages say "our calculation".
- The executive summary disease bullet does not give the 79% figure, to keep it short; the at-a-glance tile, the policy and research briefs give it.
- I added the wild-fish bullet to the executive summary from chapter 20 (being edited by another editor). It uses the stock fall (22.1%) only, which matches both chapter 20 and the tile.
- The at-a-glance page now has 17 more tiles. If that is too many for one page, the first to drop are kn-milk-self-sufficiency, kn-dairy-imports-2025 and the three vision tiles.
