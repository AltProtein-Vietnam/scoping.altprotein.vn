# Editor log E04-part2b: chapters 8, 9 and 10

Date: 2026-10-01. Files edited: `content/01-report/ch08-capital.md`, `content/01-report/ch09-economics.md`, `content/01-report/ch10-technology-fit.md`. Brief: `working-papers/wave11/EDITORIAL-v0.8.md`.

All three pages: the opening box is now `**In brief.**` with five or six bullets. Long sentences and paragraphs are split, section headings say what each section finds, and abbreviations and specialist terms are explained on first use. Terms explained include IFC, DFI, IPO, limited partner, offtake, first-loss tranche, capex, TEA, SCP, tolling, COD, FOB, HS, ACFTA, RCEP, NPV, titer, DIAAS, PDCAAS, GMO, EFSA and perfusion.

No other page links to an anchor in these three chapters (`grep -rn "ch0[89]-...#\|ch10-technology-fit#" content` found nothing). `tools/validate.py` reports 0 errors. Its two warnings, `kn-no-regret-plays` and `chart-play-robustness`, come from other editors' files. No em or en dashes. Version label and draft notices are untouched.

## ch08-capital

| Section | Change | Type |
|---|---|---|
| Frontmatter `summary` | Says plainly that the Entobel deal is an insect-feed deal outside the study's focus, kept as the one proven deal structure | reframed for food |
| In brief | Paragraph replaced by five bullets. First bullet: "One large deal, and it is in insect feed", with the structure kept as the template | reframed for food |
| 8.1 table | "Black soldier fly insect meal" now reads "(feed)". Added one line explaining seed, Series A and Series B | clear language only |
| 8.2 | Retitled "The Entobel template: an insect-feed deal with a structure food ventures can copy". New opening says the deal is outside the focus and why it is described. New paragraph "What a food venture can take from it": a named food manufacturer as anchor buyer, local feedstock, local private-equity lead, small development-finance ticket. Five parts, IFC caution sentence [@CAP-06] and the USD 20 million capex sentence all kept | reframed for food; retitled |
| 8.3 | Removed De Heus (a feed company) from the list of plausible acquirers | pruned feed |
| 8.7 Reading | "Vietnam's advantages (feedstock, feed demand, processing skills)" now reads "(feedstock and processing skills)" | pruned feed |
| 8.8 | Retitled "What this means for food ventures". Investors: "B2B feed or ingredient revenue" becomes "business-to-business food-ingredient revenue". International bodies: "first-loss tranche for a first Vietnamese fermentation-feed plant" becomes "for a first shared food-grade fermentation plant in Vietnam (play T5)" | reframed for food; retitled |
| 8.4 to 8.6 | Sentences split, headings made into findings; "committed" changed to "promised" (Bezos Earth Fund) | clear language only |

Tiles and charts: none removed. `kn-entobel-financing` stays because the deal stays.

## ch09-economics

| Section | Change | Type |
|---|---|---|
| Frontmatter `summary` | Rewritten around fungal biomass protein as a food ingredient. The fishmeal comparison is out of the headline | reframed for food |
| Frontmatter `key_numbers` | Removed `kn-cost-fungal-feed` and `kn-fishmeal-protein-price` | tile or chart removed |
| Frontmatter `charts` | Removed `chart-price-to-beat`; its embed in section 9.3 is also removed | tile or chart removed |
| Frontmatter `related_data` | Removed `feed_benchmarks.csv`, `inclusion_rates.csv` and `replacement_trials.csv`; added `ingredient_prices.csv` (the chapter 16 ladder) | pruned feed |
| In brief | Five bullets: capital dominates; fungal biomass is a premium ingredient (above commodity plant proteins, overlapping egg and dairy proteins); textured soy is cheap to make; soy flour decides the T1 margin; feed is context only. The "functional shrimp or fish-feed ingredient at 1 to 5%" conclusion is removed. Soybean-meal replacement now appears only as context ("would not compete as a bulk feed protein either") | reframed for food; pruned feed |
| 9.1 VAT paragraph | Retitled "Feed is not subject to VAT, which favours food-ingredient plants". Same claims, numbers and tags | reframed for food |
| 9.2 | Cost stack A retitled "fungal biomass protein, 10,000 t a year" (was "for aquafeed"). New line says the stack was built for a feed ingredient. In the cooling text, "fungal feed protein" becomes "fungal biomass protein". In the capex bullet, fishmeal parity below USD 6,000 per annual tonne stays as one context sentence, and tolling is now defined | reframed for food |
| 9.3 | Retitled from "The prices to beat in feed" to "The prices to beat in food: fungal biomass is a premium ingredient". New comparison table in USD per kg of protein using comparators already in the package: cost stack B, the chapter 16 price ladder (commodity rung, Chinese landed textured protein, hydrated-soy extender, egg/dairy/premium rung), the published mycoprotein model [@COST-43], and retail eggs, chicken breast and lean pork (S12.10 and chapter 11), marked "for scale only" and "not ingredient prices". Added binder and extender job prices from chapter 16. New inference: a food-grade plant would sit towards the top of the cost range or above it (RNA-reduction step and higher hygiene grade) `{VN-direct|Low}`. Inactive-yeast import fact kept (food and feed together), with the Chinese yeast protein marketed to food makers (chapter 16). Fishmeal and soybean-meal prices are kept as one short "Feed prices, for context" paragraph | retitled; reframed for food |
| 9.3 (removed) | Removed: the feed price-to-beat table (bulk fishmeal replacement, functional pangasius and shrimp ingredients, soybean-meal replacement, gap ratios, verdicts; [@FM-04; @FM-10; @FM-31]); "the real competitor is imported microbial protein", including the USD 1,100 per t revealed price, Chinese glutamic-acid bacterial biomass [@FM-12; @ECO-69] and Calysseo FeedKind [@FM-13]; the working assumption of 70 to 90% of fishmeal-protein parity; the whole "Buyer economics" paragraph on shrimp feed [@FM-10; @FM-04] | pruned feed |
| 9.5 | Precision fermentation defined. The regional study is named on first use (GFI APAC and Hawkwood Biotech, [@RGN-01]) | clear language only |
| 9.6 | Removed "Tax neutrality: allowing new feed ingredients to reclaim input VAT" (PO-029 retired). "Every month of feed or food approval" becomes "every month of food approval" | pruned feed |
| 9.7 | Investors: the fishmeal-protein test becomes a test against the food rung (USD 1.7 to 2.4 per kg of protein for commodity plant proteins, or USD 7 to 11 for egg and dairy). Manufacturers: feed-mill sentences removed; food makers told to compare fungal or yeast protein with egg and dairy proteins and with the Chinese yeast protein. Policy: input-VAT neutrality for feed ingredients removed. Research: "domestic feed-ingredient prices" becomes "food protein-ingredient prices" (P6) | reframed for food; pruned feed |

### New calculations in ch09 (all marked "(our calculation)" with inputs in the table)

| Value | Inputs |
|---|---|
| Textured soy made in Vietnam, about USD 1.5 to 3.0 per kg of protein | Cost stack B full cost USD 761 to 1,573 per t of product ÷ 0.52 protein ÷ 1,000 = USD 1.46 to 3.03 |
| Fungal biomass protein, USD 4.05 to 14.7 per kg of protein | Cost stack A USD 4,050 to 14,700 per t of protein ÷ 1,000 (unit change only) |
| Eggs and chicken breast at retail, about USD 13.2 to 17.5 per kg of protein | S12.10 USD 1.32 to 1.75 per 100 g of protein (eggs 1.32 to 1.54, chicken breast 1.52 to 1.75; [@COST-40; @COST-41]) × 10 |
| Lean pork at retail, about USD 27.3 per kg of protein | S12.10 and chapter 11 USD 2.73 per 100 g of protein [@COST-39] × 10 |

The other figures in the new table come straight from chapter 16 (USD 1.7 to 2.4; 2.0 to 2.1; 2.6 to 2.8; 7 to 11; binder USD 3.3 and 3.9 to 4.6 per kg; extender USD 0.7 to 1.2 per kg dry) or from the benchmarks already on the page (USD 29.6). The consolidating editor may want to add the four inputs above to Appendix S12 (S12.15 or S12.10).

## ch10-technology-fit

| Section | Change | Type |
|---|---|---|
| Frontmatter `summary` | "Textured plant protein for food fits now". Functional microbial aquafeed ingredients no longer fit now, and duckweed feed is no longer "worth proving". Feed uses stay as a record, context only | reframed for food |
| Frontmatter `key_numbers` | Removed `kn-shrimp-fishmeal-replacement` (it was not embedded in the body) | tile or chart removed |
| Frontmatter `related_data` / `related_pages` | Removed `replacement_trials.csv`; added `ch07-rules` | pruned feed |
| In brief | Six bullets, following brief section 2.6: fits now, textured plant protein (food); worth proving, local legume and rice proteins and fungal foods (koji first, mycoprotein watch); precision fermentation contract-made only; cultivated meat and seafood research; feed context only, insects a benchmark | reframed for food |
| 10.2 matrix | All rows and ratings kept as the record. New verdicts: functional microbial feed ingredients "Build with partners" becomes "Feed: context only"; bulk microbial protein "Marginal; test only with near-free carbon and tolling" becomes "Feed: context only; marginal on price"; duckweed "Prove first (feed)" becomes "Watch (food, as a protein concentrate); feed is context". Added an intro sentence saying the matrix keeps feed rows as a record. Heading now reads "one family to build now" | reframed for food |
| 10.4 | Cut to a short context note, "Microbial protein for feed: context, not a target". Removed the shrimp replacement science ([@SCI-23; @SCI-24; @SCI-27]), the soybean-wastewater preprint [@SCI-25], "function sells better than protein" with the pangasius and shrimp premiums ([@FM-20; @FM-26; @FM-31; @FM-45]), and the feed-list fit paragraph (aquafeed drafting gap, [@REG2-01]). Kept: Chinese by-product bacterial biomass sold in Vietnam [@FM-12] and gas fermentation [@RGN-57; @FM-13] as context. The thermotolerant-yeast fact [@SCI-44; @SCI-45] moved to 10.5 | pruned feed; retitled |
| 10.5 | Added the thermotolerant-yeast bullet and a "Fit" line: koji and fungal foods on food-grade side streams worth proving (T9), mycoprotein watch (matches the matrix verdict) | reframed for food |
| 10.6 | Duckweed fit changed from "feed on aquaculture effluent now, food as a protein concentrate later" to "watch as a food protein concentrate, which needs a new-food route and testing for manganese and heavy metals". The feed-list fact [@REG-32; @REG-33] is kept as context | reframed for food |
| 10.9 Insects: the benchmark | Heading kept. Removed "the incumbent that every microbial or plant feed protein must match on price, digestibility and supply security"; now "the feed incumbent and a benchmark". Added one sentence: its lesson for protein for people is about finance (links to ch08) | pruned feed |
| 10.10 | Investors: one "build now" family, not two. Startups: removed "listed feed materials". Manufacturers: removed "functional feed additives". Research: removed "soy-wastewater protein in shrimp" | pruned feed |
| 10.3, 10.7, 10.8 | Sentences split. DIAAS, PDCAAS, titer, host strain, tolling, fetal bovine serum and perfusion explained. "No true continuous shrimp cell line was found" now reads "We found no ..." | clear language only |

## For the consolidating editor (tiles, charts, data)

- `kn-cost-fungal-feed` (USD 4,050 to 14,700 per t of protein) is still the central number in ch09, but its label reads "fungal feed protein". Suggest relabelling it "Indicative cost of fungal biomass protein in Vietnam" and adding it back to ch09 `key_numbers`. It is also used on front-at-a-glance, both executive summaries, brief-investors and app-s12-costs.
- `kn-fishmeal-protein-price`, `chart-price-to-beat` and `kn-shrimp-fishmeal-replacement` are no longer used by ch09 or ch10. `chart-price-to-beat` still lists `ch09-economics` in its `placement`.
- The `chart-cost-stack-fungal` subtitle reads "Indicative cost of fungal feed protein"; suggest "fungal biomass protein".
- `charts/data/technology_fit.csv` still holds the old verdicts for three rows ("Build with partners", "Marginal", "Prove first (feed)"), and the chart's `alt_text` says functional microbial feed ingredients rate strong or moderate. The page table now shows the new verdicts. The chart data and alt text need updating to match.
- Appendix S12.15 is titled "Cost stack A: fungal biomass protein for feed" and compares only with fishmeal. It could take the food comparison and the four calculation inputs above.

## Unsure or unresolved

1. **ch09 title** "Economics: what it costs and what it must beat" uses "must" in a non-legal sense. I kept it because the title is repeated in `site-manifest.json` and `content/PAGE-IDS.md`, which are not my files. A suggested title is "Economics: what it costs and what it has to beat".
2. **ch09 section 9.1, two-part power tariff.** The page says it "was planned for large users from 1 January 2026, after parallel billing to the end of 2025" [@COST-04; @COST-05]. Appendix S12.1 has a correction saying shadow bills ran in the first half of 2026 and real two-part billing was planned from 1 July 2026. I left the wording and tags unchanged because changing them is a substantive fix outside this refocus. It needs reconciling.
3. **ch10 section 10.10, policy bullet.** It says fungal foods move from "weak" to "moderate" on route to market with a new-food procedure, but the matrix already rates fungal foods "Moderate" on route (koji has a route; mycoprotein does not). This inconsistency predates version 0.8 and was left unchanged.
4. **ch09 food-grade inference.** The statement that a food-grade fungal plant "would sit towards the top of the range, or above it" is our inference, tagged `{VN-direct|Low}`. It rests on the RNA-reduction step (ch10, [@SCI-20]) and the hygiene-grade capex spread (S12.12). No food-grade Vietnamese cost stack exists.
5. **ch08 acquirer list.** I removed De Heus as feed-only. C.P. Vietnam, Vinh Hoan and Minh Phu stay because they also make or sell food.
