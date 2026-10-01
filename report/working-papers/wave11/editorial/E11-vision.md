# Editor log E11-vision (version 0.8)

Editor: E11-vision. Date: 2026-10-01. Files: `content/01-report/ch24-vision-2050.md`, `data/vision_milestones.csv`.

Chapter 24 is rewritten around protein for people, as brief section 2.5 asks. The nine-section structure, the "Vision, not forecast." callouts and the section 24.1 benchmark evidence are kept. The feed goals are gone as vision goals. The new numeric indicators come from the demand model (`data/demand_outputs.csv`, D-BENCH to D-STRETCH, with D-DRIFT for comparison). The policy milestones come from chapters 27 and 28 and the robust moves and policy options data. No model was re-run and no number was changed. Every number on the page is either kept from v0.7 or read from `demand_outputs.csv`, `demand_assumptions.csv`, `balance_outputs.csv`, chapter 18, chapter 22, Appendix D8 or Appendix F5.

Checks after editing:

- `python3 tools/validate.py`: 0 errors. The 2 warnings are in other editors' tiles or charts (`kn-no-regret-plays`, `chart-play-robustness` unused).
- No em or en dashes in either file (checked with Python and grep).
- `grep -rn "ch24-vision-2050#" content`: no page links to an anchor in chapter 24. Appendix M2 cites "section 24.8" (revision triggers), so the section numbers 24.1 to 24.9 are kept.
- Every citation used resolves in `data/sources.csv`. New citation pairings are claims copied with their citations from other pages: APR-07 (Food Safety Law timing, chapter 27), RGN-19/21/34 (Korea, chapter 7), INF-03/10/11/13/14 (laboratory pages, chapter 6), BUY-02/BRD-05/BRD-06 (ingredient pool, chapter 18), FS-01/FS-13/RGN-51/RGN-55 (cassava starch and glucose, chapters 1 and 4), FTR-32 (duty-free, chapter 18), HXE-04/HXE-09/TRU-22/TRU-07 (no declared blend, chapter 18), GEO-31 (ageing, chapter 20), GT-12 (UN population, chapter 18), CLM-13/CLM-14 (subsidence, chapter 28).

## ch24-vision-2050

| Section | Change | Type |
|---|---|---|
| Frontmatter | **Retitled** "Vietnam 2050: a vision for a measured, more diverse and more secure protein supply" (was "... measured, efficient and diversified ..."). `short_title` kept. Summary rewritten around the demand-model numbers. `reading_time_min` 10 to 16 (about 3,700 words with tables). `key_numbers`: removed `kn-vision-sbm-2050`, `kn-vision-microbial-share-2050`, `kn-vision-omega3-2050`; added the existing `kn-demand-bench-2035`. `related_data` adds `demand_outputs.csv`, `demand_assumptions.csv`, `signposts_2050.csv`, `play_robustness.csv`. `related_pages` adds `ch18-demand-sizing`, `app-d8-demand-model`, `ch26-plays`. `charts` keeps `chart-vision-backcast` (see below). | retitled; tile or chart removed |
| Opening box | `**In one paragraph.**` became `**In brief.**` with six bullets: vision for the protein people eat; measured, more diverse and more secure; five pillars; 67,000 to 172,000 t supplied and 59,000 to 147,000 t made in Vietnam by 2050; cheap first steps; no 2050 plan abroad, so review each plan. The "led by feed security" framing is removed. | reframed for food |
| Callout | "The ranges come from chapter 22" became "from the demand model of chapter 18 and Appendix D8, on the same basis as chapter 22". | reframed for food |
| 24.1 | All five benchmark bullets kept with their citations and tags (no 2050 protein plan; official plans cover inputs; security and industry framing; plans without a statistic; backcasting). The framing bullet now says the vision is about the security of the protein people eat; diet change is not a goal. **New bullet "Feed is context, not a goal"**: the one allowed context sentence (10.4 Mt soybean meal on trend by 2050; 4.5 t avoided per tonne of meat protein replaced; our calculation, chapter 22), plus the brief's limit statement (a second source, not a change in national exposure on its own). | reframed for food; pruned feed |
| 24.2 | **Vision statement replaced** by the brief section 6 text, adapted (see "Unsure" 1). Split into three short paragraphs, each tagged `{fx:vision}`. **Removed:** soybean-meal need 7.0 to 8.8 Mt; 4 to 8% microbial feed protein; 15 to 50% non-marine aquafeed omega-3; "supplies the world's shrimp and pangasius buyers"; "regional supplier of aquafeed functional ingredients". **Added** a short "scale behind it" paragraph from existing model outputs: population 101.6 to 110.0 million (balance model S-BASE, UN projections [GT-12]); meat protein 1.01 to 1.45 Mt, 27 to 36 g per person per day (demand_outputs.csv); 65 and over 9.5% to 20.0% (GEO-31, as in chapter 20); displacement about 0.4% (benchmark) and 1.5% (stretch) in 2050. | pruned feed; reframed for food |
| 24.3 | **Pillars renamed**: Measure, Economise, Diversify, Specialise, Decarbonise and adapt became **Measure, Make, Diversify, Specialise, Secure**. Measure: protein balance for people (memo line for feed), protein-quality laboratory, price series. Make: made in Vietnam and domestic share of the ingredient pool. Diversify: protein supplied by new routes. Specialise: cassava fermentation sugar for food, contract fermentation, contract-made precision-fermentation ingredients, cultivated seafood research. Secure: second source, climate-proof sites, residue carbon and clean power, the 56 MtCO2e cap. **Removed with their claims:** the Economise pillar (soybean-meal need; China and Norway pace; GEO-10, GEO-11, VIS-19); microbial feed protein and omega-3 (VIS-18, VIS-20, AQF-19, AQF-23, AQF-24); aquafeed functional ingredients and the Ca Mau shrimp tonnage (HUB-15, HUB-13, IND-66 in that row). Two glosses added (precision fermentation, cultivated seafood). | pruned feed; reframed for food |
| 24.4 | **Indicator table rebuilt.** Removed rows: soybean-meal need; microbial feed-protein share; domestic-origin share of feed protein; non-marine aquafeed omega-3. New rows from the demand model for 2030, 2035, 2040 and 2050: protein supplied by new routes; of which made in Vietnam (model reading); domestic share of the food plant-protein ingredient pool (demand assumptions DMA-015 to DMA-023); meat protein displaced. Comparison column now D-DRIFT. Policy rows: protein balance for people from 2028; new-food route (Food Safety Law vote considered May 2027, decree 2027 to 2028); open food-grade pilot capacity 10,000 to 30,000 L by 2030 (kept); protein-quality laboratory; public food-protein innovation line USD 5 to 15 M (kept, renamed from "protein and feed-innovation line"; the feed scheme of about USD 6 M stays only as the comparison). Four reading notes added: model reading of "made in Vietnam" (strict 2035 reading 11.4 kt); most is import substitution (44.6 of 66.7 kt in 2050); the stretch path is a stretch; meat displaced is not a diet target. The note "2050 microbial share matches S-ALT" is removed. | pruned feed; reframed for food; tile or chart removed |
| 24.4 tiles | **Embeds removed:** `{{kn:kn-vision-sbm-2050}}`, `{{kn:kn-vision-microbial-share-2050}}`, `{{kn:kn-vision-omega3-2050}}`. **Embed added:** `{{kn:kn-demand-bench-2035}}` (existing tile, no new id). | tile or chart removed |
| 24.5 | Milestone table rebuilt per plan period from the new `vision_milestones.csv` (25 rows). Removed: aquafeed raw-material entries for microbial biomass and algal oils; soybean-meal and microbial-share values for 2030 to 2050; "residues cover about 10 to 15% of the S-ALT sugar need in 2040" (an S-ALT number driven by microbial feed); the 2041 to 2045 protein-from-power plant on the Mekong shrimp coast (FTG-01); omega-3 and domestic-origin feed share for 2050. Added: food-fermentation sites (was "fermentation and feed-protein sites"); siting rule; protein-quality laboratory and price series; demand-model values; regional supply of cassava sugar and contract food fermentation (2045). Kept: official 2045 goals as `{fx:projection}`; the 56 MtCO2e cap; first full review in 2035; the chart embed. | pruned feed; reframed for food |
| 24.6 | Six hubs kept, five reframed for food and one marked context. Ho Chi Minh City with Dong Nai: unchanged claim, plays T1, T5, T7 named, former provinces added. Tay Ninh: sugar for food fermenters (T4); **removed** "not enough roots to carry a national sugar route alone" (it referred to the S-ALT need, mostly microbial feed); **added** the existing F5.5.8 figure (a 20 kt a year protein plant needs 3.9 to 4.7% of former Tay Ninh root capacity, our calculation). Mekong river belt: "feed ingredients and side streams" became side streams, with rice bran and broken rice for T9 and T10 (from `candidate_hubs.csv`). North: adds candidate home for the protein-quality laboratory and T8 (from `candidate_hubs.csv`). South-central coast: **removed** the shrimp-hatchery niche (HUB-23); **added** seaweed protein and spirulina as small food niches (from `candidate_hubs.csv`, CH-5 assets). Mekong shrimp coast: **now context only** (aquafeed and power-to-protein are feed); demonstration and scale dates removed; the siting point kept (CLM-14). | reframed for food; pruned feed |
| 24.7 | Axis renamed "stress on imported protein" (as in brief 2.5). World table rebuilt for the new pillars (our judgement from chapter 23 and `play_robustness.csv`): Measure achievable everywhere; Make upper half in A and C, near drift in B (duty-free imports, FTR-32), lower half in D; Diversify achievable everywhere, with more imported ingredients in B and D; Specialise unchanged; Secure achievable everywhere, small in B, urgent in C, dearer in D. The play statement is exact to the scores: T1, T4 and T5 hold in every world; they thrive only in A and C, and T1 only in A. | reframed for food |
| 24.8 | Upward triggers: **removed** fishmeal above USD 2,500 per t and green hydrogen below USD 2 per kg (feed); **kept** ASEAN reliance and a cellulosic sugar plant; **added** a declared blend that buyers accept, a caterer default, and per-serving price parity (D-STRETCH conditions in chapter 18). Downward triggers: **removed** a sustained soy glut; "no feed-protein balance by 2030" became "no protein balance"; **kept** Chinese dumping of microbial protein and a novel-food scandal; **added** the chapter 23 signpost on Chinese yeast and protein-preparation imports (above 20% a year for three years) and no new-food procedure by 2028. Both lists now bullets. Review cycle unchanged. | reframed for food; pruned feed |
| 24.9 | Policy makers: adds the laboratory and the May 2027 deadline (APR-07). International bodies: unchanged. Investors: **removed** microbial feed capacity "about nine times Entobel's" and the power-to-protein option; now an ingredient business worth about USD 200 million a year by 2050 on the benchmark path, two-thirds import substitution (chapter 18). Manufacturers: **removed** "your largest lever is feed efficiency"; now purchasing, declared blends, and the brief's first firm steps. Startups and researchers: "Vietnamese feedstocks" became carbohydrate and side streams; adds the protein-quality dataset (chapter 6). | pruned feed; reframed for food |

Clear-language work throughout: short sentences, main point first, and abbreviations explained on first use (MtCO2e, Mt, kt, MAE, MSG, EECi, JRC written out). Backcasting, tolling, hub, precision fermentation and cultivated seafood are glossed, and codes point to `front-how-to-read`. "Deliver" became "supply", except for the model term.

## data/vision_milestones.csv

Columns (12), header, LF line endings, trailing newline and the `VM-NN` id format are kept. **Row count changed from 22 to 25.** All rows keep `foresight_type` = vision.

- **Pillar values** are now Measure, Make, Diversify, Specialise and Secure. The old values were Measure, Rules, Places, Money, Economise, Diversify, Specialise, Decarbonise and Review.
- **New ids by plan:**

| Plan | Rows | What they are |
|---|---|---|
| 2026 to 2030 | VM-01 to VM-09 (9) | Protein balance for people (VM-01); new-food route (VM-02); food-fermentation sites (VM-03); USD 5 to 15 M food-protein line (VM-04, still the money milestone that Appendix F5.3.3 cites with RM-11); climate-proof siting (VM-05); protein-quality laboratory and price series (VM-06); open pilot 10,000 to 30,000 L (VM-07); made in Vietnam in 2030 (VM-08); protein supplied by new routes in 2030 (VM-09) |
| 2031 to 2035 | VM-10 to VM-15 (6) | Successor strategies carry targets from the protein balance (VM-10); made in Vietnam (VM-11), domestic share of the ingredient pool (VM-12), protein supplied (VM-13) and meat displaced (VM-14) in 2035; first full review (VM-15, was VM-12) |
| 2036 to 2040 | VM-16 to VM-18 (3) | Made in Vietnam (VM-16) and protein supplied (VM-17) in 2040; residue carbon and clean power for new food-fermentation capacity (VM-18) |
| 2041 to 2045 | VM-19, VM-20 (2) | Official 2045 goals (VM-19, text unchanged); regional supply of cassava sugar and contract food fermentation (VM-20) |
| 2046 to 2050 | VM-21 to VM-25 (5) | Made in Vietnam (VM-21), domestic share (VM-22), protein supplied (VM-23) and meat displaced (VM-24) in 2050; 56 MtCO2e cap (VM-25) |

- **Rows retired:** old VM-05, VM-09, VM-13 and VM-18 (soybean-meal need), VM-06, VM-10, VM-14 and VM-19 (microbial feed protein), VM-11 and VM-21 (domestic-origin share of feed protein), VM-17 (power-to-protein on the Mekong shrimp coast) and VM-20 (aquafeed omega-3). Old VM-02 lost its aquafeed-entries clause and REG2-01. Its sources are now APR-07, REG-12, RGN-19, RGN-21 and RGN-34.
- **Model rows:** for rows from the demand model, `trend_comparison` now holds the D-DRIFT value, labelled "(drift path, D-DRIFT)", and `source_ids` lists the model's input sources. These are BUY-02, GLB-09, GT-12 and QNT-01, as for the existing tile and chart; CHY-06 and GLB-19 are used for displacement. Confidence is Low.

## Tiles and chart

**Tiles removed from the page and frontmatter** (`key-numbers.json` not edited): `kn-vision-sbm-2050`, `kn-vision-microbial-share-2050`, `kn-vision-omega3-2050`. All three still have `primary_page: ch24-vision-2050`. The consolidating editor should retire them, or re-home `kn-vision-omega3-2050` to Appendix F6 as a record, and remove them from front-exec-summary, front-exec-summary-vi, front-at-a-glance, brief-policy and app-f6.

**Existing tile embedded:** `kn-demand-bench-2035` (section 24.4). Please add `ch24-vision-2050` to its `pages` list.

**Chart kept:** `chart-vision-backcast` plots `data/vision_milestones.csv` directly (period, pillar lane, milestone, value). After the CSV rewrite it no longer plots soybean-meal need, so the embed stays. Its spec in `chart-specs.json` is now stale and needs these changes:
- `annotations[0]`: "Lanes in this order: Measure, Make, Diversify, Specialise, Secure."
- `alt_text`: "Timeline of 25 milestones from 2026 to 2050 in lanes by pillar: a protein balance for people by 2028, a new-food route, a protein-quality laboratory and an open food-grade pilot plant by 2030; new routes supplying 66.7 to 171.5 kt of protein in 2050, of which 59.2 to 146.5 kt made in Vietnam."
- `source_ids`: replace VIS-18 and QNT-01 with BUY-02 and APR-07 (keep VIS-15 and CLM-01).
- `version`: "0.8".

## Proposed replacement tiles (for the consolidating editor to create)

All values are read from `data/demand_outputs.csv` or `data/demand_assumptions.csv`; none is new. Common fields: `as_of: "vision"`, `horizon: "2050"`, `foresight_type: "vision"`, `demand_evidence_type: "inferred"`, `derived: true`, `evidence: "VN-direct"`, `confidence: "Low"`, `primary_page: "ch24-vision-2050"`, `version: "0.8"`. Suggested `pages`: ch24-vision-2050, front-exec-summary, front-exec-summary-vi, brief-policy (as the pages that carried the old vision tiles).

1. **`kn-vision-protein-new-routes-2050`** (replaces `kn-vision-sbm-2050`)
   - label: "Vision: protein from new routes, 2050"; label_vi: "Tầm nhìn: lượng đạm từ các kênh mới năm 2050"
   - value: "about 67,000 to 172,000 t of protein a year"; value_low 66.7; value_high 171.5; unit "kt protein"
   - context: "Normative goal, not a forecast: the benchmark (D-BENCH) and stretch (D-STRETCH) paths of the demand model (demand_outputs.csv, total_delivered). Routes: import substitution (about two-thirds on the benchmark path), upgraded chay, blends, canteen dishes, analogues, plant drinks and exports. The stretch path assumes conditions not yet seen anywhere. Drift path: about 10.7 kt."
   - source_ids: BUY-02, GLB-09, GT-12, QNT-01
2. **`kn-vision-made-in-vietnam-2050`** (replaces `kn-vision-microbial-share-2050`)
   - label: "Vision: protein made in Vietnam for the home market, 2050"; label_vi: "Tầm nhìn: lượng đạm sản xuất tại Việt Nam cho thị trường trong nước năm 2050"
   - value: "about 59,000 to 147,000 t of protein a year (model reading)"; value_low 59.15; value_high 146.51; unit "kt protein"
   - context: "domestic_delivered (routes R1 to R6) in demand_outputs.csv, D-BENCH to D-STRETCH. Only import substitution applies an explicit domestic share; the other routes count protein of any origin, so this is the upper, model reading (the strict 2035 benchmark reading is about 11.4 kt against 16.6 kt). Most of it is plant protein processed in Vietnam in place of imported ingredients."
   - source_ids: BUY-02, GT-12, QNT-01
3. **`kn-vision-domestic-ingredient-share-2050`** (replaces `kn-vision-omega3-2050`)
   - label: "Vision: domestic share of food plant-protein ingredients, 2050"; label_vi: "Tầm nhìn: tỷ lệ nguyên liệu đạm thực vật cho thực phẩm do doanh nghiệp trong nước cung cấp năm 2050"
   - value: "40 to 60% of the ingredients food makers now import"; value_low 40; value_high 60; unit "%"
   - context: "Share of the food plant-protein ingredient pool (textured soy, gluten, isolates; about 35,000 to 40,000 t of product in 2025) supplied by domestic makers: demand-model assumptions DMA-018 (D-BENCH) and DMA-023 (D-STRETCH). 25 to 45% in 2035; drift path 10% in 2050."
   - source_ids: BUY-02, BRD-05, BRD-06
4. Optional: **`kn-vision-meat-displaced-2050`**
   - label: "Vision: meat protein displaced by new protein, 2050"; label_vi: "Tầm nhìn: tỷ lệ đạm thịt được thay thế bởi đạm mới năm 2050"
   - value: "0.41 to 1.52% of meat protein (about 6,000 to 22,000 t)"; value_low 0.41; value_high 1.52; unit "%"
   - context: "A second source, not a diet target. displaced_share_of_meat_protein and total_displaced in demand_outputs.csv, D-BENCH to D-STRETCH. Existing chay days already avoid about 2.5% (about 36 kt). Each tonne of meat protein replaced avoids about 4.5 t of imported soybean meal (chapter 22, our calculation)."
   - source_ids: CHY-06, GLB-19

## Knock-on edits needed in files I do not own

- `content/PAGE-IDS.md` (line 47) and `site-manifest.json` (line 653): new chapter 24 title.
- `data/data-dictionary.md`, `vision_milestones.csv` section: rows 22 to 25; the pillar list; `trend_comparison` is now "value on trend or the drift path (D-DRIFT), for comparison". Also the summary table row near line 1289.
- `content/03-appendices/app-f5-targets-hubs.md`:
  - F5.6 lists all 22 old rows and needs regenerating from the CSV.
  - F5.3.3 (line 232) says "protein and feed-innovation line"; it is now "food-protein innovation line" (VM-04 id unchanged).
- `content/03-appendices/app-m2-futures-method.md`:
  - M2.7.2 table (soybean meal, microbial share, domestic-origin feed share, omega-3) no longer matches chapter 24. The new indicators are demand-model outputs and need no extra calculation.
  - M2.7.3 needs the new grouping above.
  - M2.7.4 cites VM-12 as the first full review; it is now VM-15.
  - "Left out on purpose" may need a line on why meat displaced is tracked but is not a diet target.
- `content/03-appendices/app-f6-aquafeed-feedstock-futures.md` line 213: "Chapter 24 adopts the 15 to 50% range as a normative goal" is no longer true.
- `content/01-report/ch22-protein-balance-2050.md` line 151: "[[ch24-vision-2050]] builds on this range" (7 to 9 Mt) is no longer true.
- `content/00-front/front-exec-summary.md` line 76, `content/02-briefs/brief-policy.md` line 75, the Vietnamese summary and front-at-a-glance quote the old vision.
- `app-m5-changelog.md` (M5.14): the substantive changes above, in particular retitled chapter 24, three feed goals retired, new indicators from the demand model, 22 to 25 milestones, and the Mekong shrimp coast as context only.
- Open questions: OQ-396 (Germany's EUR 6 M) and OQ-397 (tolling in Ho Chi Minh City and Dong Nai) still apply to chapter 24 as written.

## Unsure

1. **The vision statement departs from brief section 6 in three places.** All three keep the numbers.
   - "Domestic makers supply most of the plant-protein ingredients" became "40 to 60%". The model has 40% on the benchmark path and 60% on the stretch path, so "most" holds only on the stretch path.
   - "Much of it on Vietnamese carbohydrate and side streams" became "Most of it is plant protein processed at home in place of imported ingredients; some is grown on Vietnamese carbohydrate and side streams". Import substitution is about three-quarters (73 to 75%) of the made-in-Vietnam figure in 2050, and it is textured soy, gluten and isolates.
   - "Deliver" became "supply" (GOV.UK word list).

   Please align section 6 and the other pages, or tell me to revert.
2. **"Made in Vietnam" (59 to 147 kt) is the model's `domestic_delivered`.** The CSV labels it "Protein delivered in Vietnam (R1 to R6)", and R2 to R6 count protein of any origin. Chapter 18 gives a strict reading for 2035 only (11.4 kt). The page says so, but the headline figure is an upper reading.
3. **Meat protein displaced is used as an indicator** (brief 2.5 lists it), framed as the size of the second source, "not a diet target". If the owner reads it as a diet goal, it could move to context.
4. **The 24.7 world table is new judgement**, especially the Make and Diversify rows. It is consistent with `play_robustness.csv` and chapter 23 but has no new evidence behind it.
5. **New revision triggers carry no new numbers.** The declared blend, caterer default and price parity come from the D-STRETCH conditions in chapter 18. The above-20%-a-year-for-three-years threshold comes from the chapter 23 signposts.
6. **The protein-quality laboratory "by 2030"** is a vision date. It combines RM-05 (start by 2028) and PO-027 (12 to 24 months) and is not in any source.
7. **Benchmark for VM-10.** "EU protein plan targets for 2035" (VIS-15) is a feed-protein self-sufficiency target. It is kept only as an example of a 2035 target in a successor strategy.
8. **Seaweed and spirulina** (south-central coast) and **rice bran and broken rice for T9 and T10** (Mekong river belt) are attributed to `candidate_hubs.csv`, not to a source ID. I did not check which ID in the CH-5 row supports spirulina.
9. **The page is longer**: about 3,700 words against 2,350 in v0.7 (reading time 16 minutes, was 10). This is mostly the indicator table and the reading notes. Section 24.5 now points to 24.4 for repeated indicators.
