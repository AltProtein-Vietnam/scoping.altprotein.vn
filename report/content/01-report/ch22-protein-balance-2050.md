---
id: ch22-protein-balance-2050
title: "The protein balance to 2050: what people will eat, and the imports behind it"
short_title: "Protein balance 2050"
section: report
part: "IV. Futures: 2035 and 2050"
order: 22
summary: "On trend, the meat protein Vietnamese people eat rises from about 1.01 Mt in 2025 to about 1.45 Mt in 2050 (our model). The share of it resting on imports, directly or through feed, rises from 70% to 78% to about 79% to 87%, and the imported soybean meal behind it from 7.2 Mt to about 10.4 Mt. Replacing meat protein in diets saves the most imports per tonne, but a plant food made from imported soy stays import-dependent, and at the scale demand supports, new protein adds a second source rather than replacing meat."
audiences: [policy, investors, manufacturers, research, international, startups]
reading_time_min: 14
key_numbers: [kn-meat-protein-on-imports-2050, kn-sbm-need-2050, kn-sbm-range-2050, kn-land-abroad-feed]
related_data: [balance_outputs.csv, demand_outputs.csv, meat_protein_on_imports_projection.csv, animal_protein_import_reliance.csv, self_sufficiency_by_food.csv, balance_assumptions.csv, balance_sensitivity.csv, balance_published_projections.csv, protein_crops_vn.csv, protein_strategies_benchmark.csv]
related_pages: [ch18-demand-sizing, ch11-protein-diet, ch19-outlook-2035, ch23-scenarios-2050, ch24-vision-2050, ch28-robust-moves, ch30-unknowns, app-f4-balance-model, app-d8-demand-model, app-f6-aquafeed-feedstock-futures, app-s6-feed-market]
charts: []
---

# 22. The protein balance to 2050: what people will eat, and the imports behind it

**In brief.**
- On trend, Vietnamese people eat more meat protein each year: about 1,013 kt in 2025 and about 1,446 kt in 2050. That is about 27.3 g and 36.0 g per person per day on a supply basis (our model).
- Population grows only about 8% to 2050, so most of the rise comes from each person eating more.
- Most of that meat, and the eggs and farmed fish, is produced in Vietnam on imported feed. The soybean meal behind it rises from 7.2 Mt in 2025 to about 10.4 Mt in 2050, almost all imported. Across four scenarios the 2050 range is 7.0 to 11.7 Mt.
- About 70% to 78% of the meat protein people eat rested on imports in 2025, directly or through the feed behind domestic meat. On trend the share rises to 79% to 87% by 2050 (our estimate).
- Protein for people saves the most imports per tonne: replacing 1 t of meat protein in diets avoids about 4.5 t of soybean-meal and 9.5 t of maize imports (our calculation). But a plant food made from imported soybeans stays import-dependent.
- At the scale the demand evidence supports, new protein displaces about 0.2% of meat protein in 2035 and about 0.4% in 2050. It adds a second source of protein; it does not replace meat.

> **Method note.** No one has published a projection of Vietnamese meat, feed or feed-protein demand beyond 2035, and official targets stop at 2030. So we built a simple, reproducible balance model (`tools/balance_model.py`). It reproduces the published outlooks to 2035 within about 2% and extends them to 2050 under four scenarios.
>
> Every 2040 and 2050 value in this chapter is our estimate {VN-direct|Low} {fx:estimate}. The model is calibrated on 2025 data and published projections to 2035. It treats demand as a macro input, as agreed for this study, and makes no market-size forecast. Assumptions, equations, checks and the full sensitivity test are in [[app-f4-balance-model]]; the demand model used in section 22.4 is in [[app-d8-demand-model]].

---

## 22.1 What people will eat: more meat protein per person

**Most of the growth comes from each person eating more, not from more people.** Vietnam's population grows from 101.6 million in 2025 to about 110 million in 2050, about 8% (UN medium variant) [@GT-12] {VN-direct|Medium} {fx:projection}. On trend, meat demand per person rises from 66.5 kg in 2025 to 87.6 kg in 2050 (carcass weight), about 32% more {VN-direct|Low} {fx:estimate}. In protein terms, that is about 1,013 kt of meat protein in 2025 and about 1,446 kt in 2050 (our model) {VN-direct|Low} {fx:estimate}.

These are supply figures, not intake: we convert meat in carcass weight to protein at 0.15 kg per kg ([[app-d8-demand-model]]). Chapter 11 describes what people eat today ([[ch11-protein-diet]]).

**What people will eat on trend (scenario S-BASE, explained in section 22.2)** {VN-direct|Low} {fx:estimate}

| Indicator | 2025 | 2035 | 2050 |
|---|---|---|---|
| Population, million | 101.6 | 106.5 | 110.0 |
| Meat demand per person, kg carcass weight | 66.5 | 81.9 | 87.6 |
| Meat protein per person, g a day (supply basis) | 27.3 | 33.7 | 36.0 |
| Meat protein, all people, kt | 1,013 | 1,309 | 1,446 |
| Share of meat protein resting on imports, directly or through feed | 70% to 78% | 76% to 84% | 79% to 87% |
| Meat protein resting on imports, kt | 713 to 790 | 994 to 1,103 | 1,136 to 1,261 |
| Eggs per person a year | 210.6 | 247.5 | 275.1 |
| Fresh milk produced in Vietnam, Mt | 1.30 | 1.95 | 2.75 |
| Farmed fish and seafood kept for the home market, kg live weight per person | 29.3 | 33.5 | 37.6 |
| Meat produced in Vietnam, Mt carcass weight | 6.0 | 7.8 | 8.5 |

2025 values are calibrated to 2025 data. Population follows the UN medium variant [@GT-12]. Values from `balance_outputs.csv`, `demand_outputs.csv` and `meat_protein_on_imports_projection.csv`.

**Most of that meat protein rests on imports, and the share rises.** Counting imported meat plus the imported compound feed behind domestic meat, about 70% to 78% of meat protein rested on imports in 2025. On trend the share reaches 79% to 87% in 2050, about 1.1 to 1.3 Mt of meat protein a year (our estimate) [@QNT-01; @MAC-01; @FS-23] {VN-direct|Low} {fx:estimate}. It rises because the model moves pigs from household feed to compound feed, and poultry, which relies most on compound feed, grows fastest. On FAO food balance sheets the 2023 share was 69% to 77% ([[ch01-why-vietnam]]) [@DIE-07] {VN-direct|Low}. The method holds each meat's self-sufficiency and the imported share of feed at 2025 values; it is an attribution, not a measured flow.

{{kn:kn-meat-protein-on-imports-2050}}

**Readings.**
- **Demand is already steep.** The OECD-FAO Agricultural Outlook (the joint outlook of the Organisation for Economic Co-operation and Development and the UN Food and Agriculture Organization, FAO) puts Vietnamese pig, poultry and beef food use at 61.9 kg per person in 2035. That is above Korea (59.2 kg) and China (48.5 kg) in the same outlook [@QNT-01] {VN-direct|Medium} {fx:projection}.
- **Our taper after 2035 is a judgement.** The official growth path (S-HIGH) gives 101 kg of meat per person by 2050. It is a stress case, not a central view.
- **Part of the meat is imported.** The model holds each meat's 2025 self-sufficiency ratio (domestic output divided by consumption) constant, using OECD-FAO data [@QNT-01] {VN-direct|Medium}. So meat demand runs above domestic output. On FAO food balance sheets about 90% of the meat supply was domestic in 2023 [@DIE-07] {VN-direct|High}.
- **OECD-FAO expects more home-grown poultry.** Its baseline lifts poultry self-sufficiency from 87.5% in 2025 to 96.2% in 2035 [@QNT-01] {VN-direct|Medium} {fx:projection}. The model keeps 87.5%, the more import-exposed case. Higher poultry self-sufficiency would cut meat imports but raise feed needs ([[app-r2-disagreements]], DG-361).
- **Domestic meat output grows from 6.0 Mt in 2025 to 8.5 Mt in 2050 on trend.** Across the four scenarios, 2050 output ranges from 7.7 Mt (S-ALT, the alternative-protein scenario) to 9.9 Mt (S-HIGH) {VN-direct|Low} {fx:estimate}.

## 22.2 Published numbers stop at 2035, so we use four scenarios

| Series | 2025 | 2030 | 2035 | Beyond 2035 | Type | Sources |
|---|---|---|---|---|---|---|
| Industrial livestock feed, Mt | 24 to 25 | 30 to 32 | none | none | Official target | [@NTS-23; @REG-54] {VN-direct\|Medium} |
| Meat output, Mt | about 6.0 | 6.0 to 6.5 | none | none | Official target | [@MAC-23; @REG-54] {VN-direct\|High} |
| Aquaculture, Mt | 5.7 (OECD-FAO base) | 7.0 target; 6.12 OECD-FAO | 6.83 OECD-FAO | qualitative 2045 vision | Target and projection | [@NTS-08; @AQF-02] {VN-direct\|Medium} |
| Protein-meal feed use, Mt | 9.5 | 11.1 | 12.9 | none | Projection (OECD-FAO baseline) | [@QNT-01] {VN-direct\|Medium} |
| Protein-meal imports, Mt | 7.4 | 8.6 | 10.3 | none | Projection (OECD-FAO baseline) | [@QNT-01] {VN-direct\|Medium} |
| Maize imports, Mt | 12.0 | 14.0 | 16.6 | none | Projection (OECD-FAO baseline) | [@QNT-01] {VN-direct\|Medium} |

All forward values: {fx:projection}. We found no projection to 2050 for Vietnamese meat, feed or feed protein from FAO, IFPRI (the International Food Policy Research Institute), the GLOBIOM land-use model or a peer-reviewed study [@QNT-01; @QNT-02; @QNT-15] {VN-direct|Medium}.

> **Correction.** An earlier draft left open whether the 2030 target of 30 to 32 Mt of industrial feed includes aquafeed ([[ch30-unknowns]], OQ-127). The feed scheme (Decision 1625/QD-TTg, December 2023), which the earlier draft did not cite, sets 24 to 25 Mt of industrial *livestock* feed for 2025 and 30 to 32 Mt for 2030, so the target appears to cover livestock feed only [@NTS-23] {VN-direct|Medium}. Our model gives 26.4 Mt of livestock and poultry feed in 2030. On that reading the 2030 target looks out of reach, and the 2025 target looks likely to have been missed (about 21.5 Mt in 2024) [@NTS-23; @MAC-28] {VN-direct|Medium} {fx:estimate}.

**The four scenarios.** Each has a short code. S-BASE follows the trend. S-HIGH follows the official growth path. S-EFF adds a feed-efficiency programme. S-ALT replaces part of meat with plant-based and fermented foods, and part of feed protein with microbial protein.

| Scenario | Diets | Aquaculture | Feed efficiency and formulation | Alternative protein |
|---|---|---|---|---|
| **S-BASE** (trend) | OECD-FAO growth to 2035, then tapering: 66.5 kg of meat per person (2025) to 87.6 kg (2050) | OECD-FAO growth to 2035, then +1% a year: 8.5 Mt in 2050 | Feed conversion improves 0.4% a year (livestock) and 0.3% (aquaculture); soybean-meal inclusion constant | None |
| **S-HIGH** (official growth path) | Incomes follow the power plan's 10% then 7.5% a year: 101 kg of meat per person by 2050 | Official 7.0 Mt by 2030, 9.0 Mt by 2050 | As S-BASE | None |
| **S-EFF** (efficiency) | As S-BASE | As S-BASE | Feed conversion improves 1.0% and 0.8% a year; soybean-meal inclusion falls 1% a year (amino acids, low-protein diets, by-products) | None |
| **S-ALT** (alternative protein) | As S-BASE, with 1% (2030), 5% (2040) and 10% (2050) of meat demand replaced by plant-based and fermented foods | As S-BASE | As S-BASE | Microbial protein replaces 1%, 5% and 10% of soybean-meal protein and 10%, 25% and 40% of fishmeal protein (2030, 2040, 2050) |

The S-ALT shares are illustrative what-if levels, not targets {VN-direct|Low}. The study no longer treats feed ingredients as something to make, so S-ALT's feed side is kept as context only (section 22.4).

## 22.3 The imported feed behind it

**Most of the meat, eggs and farmed fish people eat is produced in Vietnam on imported feed.** On trend, the soybean meal behind it rises 44%, from 7.2 Mt in 2025 to about 10.4 Mt in 2050, almost all imported. The range across scenarios is 7.0 to 11.7 Mt.

**Soybean-meal import need, Mt** {VN-direct|Low} {fx:estimate}

| Scenario | 2025 | 2030 | 2035 | 2040 | 2050 | 2050 against 2025 |
|---|---|---|---|---|---|---|
| S-BASE | 7.20 | 8.46 | 9.47 | 9.95 | 10.40 | +44% |
| S-HIGH | 7.20 | 8.98 | 10.11 | 10.92 | 11.72 | +63% |
| S-EFF | 7.20 | 7.81 | 8.08 | 7.85 | 7.00 | minus 3% |
| S-ALT | 7.20 | 8.32 | 9.01 | 9.15 | 8.78 | +22% |

{{kn:kn-sbm-need-2050}} {{kn:kn-sbm-range-2050}}

**Other feed results, 2050** {VN-direct|Low} {fx:estimate}

| Indicator | 2025 | S-BASE 2050 | Range across scenarios, 2050 |
|---|---|---|---|
| Compound feed, Mt | 28.5 | 40.9 (livestock and poultry 31.6; aquafeed 9.2) | 35.4 (S-EFF) to 46.2 (S-HIGH) |
| Maize import need, Mt | 11.9 | 13.8 | 11.6 (S-EFF) to 16.3 (S-HIGH) |
| Farmland abroad for imported soy and maize, million ha | 4.0 | 4.7 | 3.4 (S-EFF) to 5.4 (S-HIGH) |

{{kn:kn-land-abroad-feed}}

**Readings.**
- **The near term checks out.** Interpolated 2027 values (30.5 Mt of feed; 7.7 Mt of soybean meal) match the April 2026 forecasts of USDA (the US Department of Agriculture) at 30.6 and 7.8 Mt. They sit about 2 to 5% below its August revision (31.2 and 8.1 Mt), and protein-meal use is within about 2% of OECD-FAO for 2030 and 2035 (+2.3% and minus 2.2%) [@MAC-01; @MAC-03; @MAC-04; @QNT-01] {VN-direct|Medium}.
- **Vietnam already farms about 4 million hectares abroad for feed**, about five times its own maize area, rising to 4.7 million by 2050 on trend (our calculation) {VN-direct|Low} {fx:estimate}.
- **Maize imports depend more on domestic output and fuel use than on diets.** If E10 petrol (10% ethanol) shifted to maize and non-feed use reached the OECD-FAO 2035 level, 2050 imports would rise by 2.8 Mt {VN-direct|Low} {fx:estimate}.
- **Domestic soybean is not a lever.** Even 300,000 ha at 2.5 t per ha would give 5.6% of the 2050 S-BASE bean-equivalent need. That area and yield are our generous assumption (the source gives about 1.6 t now and 2.0 t in the ministry scheme), and domestic beans sell into food at about twice the import price [@AQF-20; @AQF-02] {VN-direct|Low} {fx:estimate}.

**Feed efficiency moves the result most; it sits outside this study's focus.** In the balance model, better feed conversion and formulation (S-EFF) would cut 2050 soybean-meal need by about 3.4 Mt, about twice what S-ALT would (1.6 Mt, 16%) {VN-direct|Low} {fx:estimate}. The two act through different channels, and we did not model a combined case. Tested one at a time, the soybean-meal inclusion trend swings 2050 imports by 3.7 Mt and feed-conversion gains by 2.4 Mt {VN-direct|Low} {fx:estimate}. Aquaculture growth, poultry demand per person, meat self-sufficiency and population each move them by about 0.8 to 1.1 Mt.

**Aquafeed is context.** Feed for farmed fish and shrimp is short of omega-3 fats more than of protein to 2050 {VN-direct|Low} {fx:estimate}. Our aquaculture paths and the omega-3 balance are in [[app-f6-aquafeed-feedstock-futures]].

## 22.4 What protein for people would change

**Protein for people saves the most imports per tonne.** In 2050, on the trend feed structure, replacing 1 t of meat protein in diets avoids about 4.5 t of soybean-meal and 9.5 t of maize imports; microbial protein in feed replaces soybean meal but not maize {VN-direct|Low} {fx:estimate}. Diet change is outside this study's scope; we report the arithmetic only.

**A plant food made from imported soy cuts the tonnage but keeps the dependence.** The food route has an import of its own: when half the substitute is plant-based, it needs about 1.65 t of imported soybeans per tonne of meat protein replaced (our calculation; [[app-f4-balance-model]], F4.5.5) {VN-direct|Low} {fx:estimate}. A wholly plant food made from imported soybeans uses about 3.3 t of beans per tonne of protein. That is about one fifth of the roughly 15.3 t of imported soybeans and maize behind the meat protein it replaces, counting the soybean meal as beans (our calculation from the F4 factors) {VN-direct|Low} {fx:estimate}. So it cuts imported tonnage. But it stays import-dependent unless the beans or the protein are Vietnamese: 97.5% of the soybean supply was imported in 2023 [@DIE-07] {VN-direct|High}.

**But the tonnes that demand supports are small.** Part III tested the food side of S-ALT against demand evidence ([[ch18-demand-sizing]]). No market has shown modern plant-based or fermented products displacing a measurable share of meat. The best retail share anywhere is 3 to 4% of pre-packaged meat after a decade, with little displacement. Our demand model's benchmark path (D-BENCH) and stretch path (D-STRETCH) displace far less than S-ALT assumes.

**Meat protein displaced: S-ALT against the demand paths** {VN-direct|Low} {fx:estimate} {dx:inferred}

| Meat protein displaced | 2030 | 2035 | 2050 |
|---|---|---|---|
| S-ALT assumption | 11.8 kt (1%) | 39.3 kt (3%) | 144.6 kt (10%) |
| D-BENCH (benchmark path) | 0.4 kt (0.04%) | 2.4 kt (0.18%) | 6.0 kt (0.41%) |
| D-STRETCH (stretch path) | 3.1 kt (0.27%) | 9.2 kt (0.71%) | 21.9 kt (1.52%) |
| Existing chay days (already in the baseline) | about 29 kt (2.5%) | about 32 kt (2.5%) | about 36 kt (2.5%) |

Read S-ALT's food shares as an exploratory what-if, not a demand path. Existing *chay* (traditional vegetarian) days already avoid a similar share of meat protein and are part of the baseline ([[ch12-chay-baseline]]).

**So new protein adds a second source; it does not replace meat.** On the benchmark path, new routes deliver about 19,000 t of protein a year by 2035 and about 67,000 t by 2050, mostly by replacing imported ingredients such as textured soy and gluten ([[ch18-demand-sizing]]) {VN-direct|Low} {fx:estimate} {dx:inferred}. At that scale, protein for people does not change national exposure to imported feed on its own. Its value for security is a second source of protein made at home.

**The import saving is about 0.1% in 2035.** Displacing 2.4 kt of meat protein in 2035 avoids about 11 kt of soybean meal, about 0.1% of the 9.5 Mt needed on trend (our calculation) {VN-direct|Low} {fx:estimate}. A check from feed rates by species, with the new protein made from domestic inputs, gives at most about 0.24% of the soybean-meal protein fed in 2025 ([[app-r2-disagreements]], DG-358). Tofu, soy milk and other soy foods already carried about 181,000 t of protein in 2023, nearly ten times what the benchmark path delivers in 2035, on the same imported beans (our calculation) [@DIE-07] {VN-direct|Medium}. For security, the measure that matters is the share of food protein made from domestic inputs, not the volume of new products ([[ch01-why-vietnam]]).

**The feed side of S-ALT is context only.** Of S-ALT's 1.62 Mt cut in 2050 soybean-meal imports, about 0.65 Mt comes from less meat and about 0.98 Mt from microbial protein in feed ([[app-f4-balance-model]], F4.5.5) {VN-direct|Low} {fx:estimate}. Together, the two sides would need 1,318 kt of glucose for the sugar route in 2050. That equals about half of Vietnam's 2025 cassava harvest or almost all of its sugar, competing with starch exports to China and E10 ethanol [@FS-01; @FS-31; @GT-10] {VN-direct|Low} {fx:estimate}. The full build-out, with energy, land and plant numbers, is in [[app-f4-balance-model]] and [[app-f6-aquafeed-feedstock-futures]].

## 22.5 Reality check: what other countries have achieved

The model's alternative-protein scenario sits above every real-world analogue we found; its efficiency scenario sits at the low end of what China has done. {general|Medium}
- **Formulation moves faster than land.** China cut the soybean-meal share of feed by 0.14 to 0.45 percentage points a year between 2017 and 2025 (our calculation from official and USDA series). Norway cut the marine share of salmon feed from 90% (1990) to about 30% (2013), about 2.6 points a year [@GEO-10; @GEO-11; @VIS-19] {general|Medium} {fx:trend}.
- **Self-sufficiency targets are usually missed, then cut.** Japan's feed self-sufficiency was 26% in FY2000 and 26% in FY2024 (24% provisional in FY2025). Its FY2030 target fell from 34% to 28% (now on a net-domestic basis) [@VIS-11; @VIS-12] {general|High} {fx:trend}.
- **Novel feed ingredients stay tiny even in the most advanced aquafeed market.** Insect meal, single-cell protein, fermented products and microalgae made up 0.4% of Norwegian salmon-feed ingredients in 2020 [@VIS-18; @VIS-20] {general|High}.
- **S-ALT's microbial share (8.4% of high-protein feed protein by 2050) is unprecedented.** Its 2030 share (1.0%) is ambitious but within reach, since novel ingredients of all types were 0.4% of Norwegian salmon-feed ingredients in 2020, a different basis [@VIS-18] {VN-direct|Low} {fx:estimate}.

> **Correction.** In v0.6 this said Japan's feed self-sufficiency was 28% in FY2000 and 27% in FY2024; the source gives 26% in both years (24% provisional in FY2025).

On this evidence, a credible ambitious range for Vietnam's soybean-meal need in 2050 is about 7 to 9 Mt, against 10.4 Mt on trend. Holding need at the 2025 level (7.2 Mt) would be more ambitious still {VN-direct|Low} {fx:estimate}. The study sets no soybean-meal goal; the range is context.

## 22.6 What this means

- **Policy makers:** the missing public good is a national protein balance, published yearly. It would show the protein people eat by food, source and origin, with a memo line for the imported feed behind domestic meat, eggs, milk and farmed fish ([[ch28-robust-moves]]). A first version from FAO data is in [[ch01-why-vietnam]]. The 2030 livestock-feed target needs a scope statement and a statistic to be judged.
- **Investors:** plan on the demand that exists. The benchmark path delivers about 67,000 t of protein a year by 2050, mostly as ingredients that replace imports. S-ALT's food shares are a what-if, not a demand path.
- **Manufacturers:** demand for meat protein keeps rising to 2050, and new protein grows beside it as ingredients, extenders and plant drinks ([[ch18-demand-sizing]]). For feed mills, soybean-meal inclusion and feed conversion matter most for imports; we found no Vietnamese time series of either by species.
- **Startups:** most demand is for ingredients that replace imports, now mostly from China, such as textured soy and gluten ([[ch18-demand-sizing]], [[ch25-demand-to-frontier]]). Size plants against that, not against S-ALT.
- **Research and international bodies:** both models are open and can be rerun ([[app-f4-balance-model]], [[app-d8-demand-model]]). The gaps that matter most are measured inputs, such as how many people keep chay days and Vietnamese series of feed conversion and soybean-meal inclusion.

**Related:** [[ch18-demand-sizing]] (demand routes and scenarios), [[app-f4-balance-model]] (model, assumptions and sensitivity), [[app-d8-demand-model]], [[app-f6-aquafeed-feedstock-futures]], [[app-s6-feed-market]] (2025 feed market), [[ch19-outlook-2035]].
