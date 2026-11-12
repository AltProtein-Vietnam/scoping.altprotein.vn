---
id: ch22-protein-balance-2050
title: "The protein balance to 2050: what people will eat, and the imports behind it"
short_title: "Protein balance 2050"
section: report
part: "IV. Futures: 2035 and 2050"
order: 22
summary: "On trend, Vietnamese people eat more meat protein each year to 2050, and the imported soybean meal behind it rises 44%. New protein made at the scale demand supports adds a second source of protein but does not change national import exposure on its own."
audiences: [policy, investors, manufacturers, research, international, startups]
reading_time_min: 9
key_numbers: [kn-meat-protein-on-imports-2050, kn-sbm-need-2050, kn-sbm-range-2050, kn-land-abroad-feed]
related_data: [balance_outputs.csv, demand_outputs.csv, meat_protein_on_imports_projection.csv, animal_protein_import_reliance.csv, self_sufficiency_by_food.csv, balance_assumptions.csv, balance_sensitivity.csv, balance_published_projections.csv, protein_crops_vn.csv, protein_strategies_benchmark.csv]
related_pages: [ch18-demand-sizing, ch11-protein-diet, ch19-outlook-2035, ch23-scenarios-2050, ch24-vision-2050, ch28-robust-moves, ch30-unknowns, app-f4-balance-model, app-d8-demand-model, app-f6-aquafeed-feedstock-futures, app-s6-feed-market]
charts: []
---

# 22. The protein balance to 2050: what people will eat, and the imports behind it

**In brief.**
- On trend, Vietnamese people eat more meat protein each year: about 1.01 Mt in 2025 and 1.45 Mt in 2050 (our model). Most of the rise comes from each person eating more.
- Most of that meat is produced at home on imported feed. The soybean meal behind it rises from 7.2 Mt in 2025 to about 10.4 Mt in 2050, almost all imported.
- About 70% to 78% of the meat protein people eat rested on imports in 2025, directly or through feed. On trend this rises to 79% to 87% by 2050 (our estimate).
- Replacing 1 t of meat protein avoids about 4.5 t of soybean meal and 9.5 t of maize imports (our calculation). But a plant food made from imported soybeans stays import-dependent.
- At the scale demand supports, new protein displaces about 0.4% of meat protein by 2050. It adds a second source; it does not replace meat.

> **Method note.** No one has published a projection of Vietnamese meat or feed demand beyond 2035, and official targets stop at 2030. So we built a simple, reproducible balance model. It matches published outlooks to 2035 within about 2%, and extends them to 2050 under four scenarios. Every 2040 and 2050 value in this chapter is our estimate {VN-direct|Low} {fx:estimate}.

---

## 22.1 What people will eat: more meat protein per person

**Most of the growth comes from each person eating more.** Population grows about 8%, to about 110 million in 2050 [@GT-12] {VN-direct|Medium} {fx:projection}. Meat demand per person rises about 32% on trend {VN-direct|Low} {fx:estimate}. These are supply figures, not measured intake ([[ch11-protein-diet]]).

**What people will eat on trend (scenario S-BASE)** {VN-direct|Low} {fx:estimate}

| Indicator | 2025 | 2035 | 2050 |
|---|---|---|---|
| Population, million | 101.6 | 106.5 | 110.0 |
| Meat per person, kg carcass weight | 66.5 | 81.9 | 87.6 |
| Meat protein per person, g a day | 27.3 | 33.7 | 36.0 |
| Meat protein, all people, kt | 1,013 | 1,309 | 1,446 |
| Share of meat protein resting on imports | 70% to 78% | 76% to 84% | 79% to 87% |
| Eggs per person a year | 210.6 | 247.5 | 275.1 |
| Farmed fish and seafood eaten at home, kg per person | 29.3 | 33.5 | 37.6 |
| Meat produced in Vietnam, Mt | 6.0 | 7.8 | 8.5 |

**Most of that meat protein rests on imports, and the share rises.** Counting imported meat plus the imported feed behind domestic meat, the share reaches 79% to 87% by 2050 (our estimate) [@QNT-01; @MAC-01; @FS-23] {VN-direct|Low} {fx:estimate}. It rises because more pigs move to factory feed and poultry, which relies most on it, grows fastest. This is an estimate, not a measured flow ([[ch01-why-vietnam]]) [@DIE-07] {VN-direct|Low}.

{{kn:kn-meat-protein-on-imports-2050}}

**Readings.**
- **Demand is already steep.** The OECD-FAO outlook puts Vietnamese meat use at 61.9 kg per person in 2035, above Korea and China [@QNT-01] {VN-direct|Medium} {fx:projection}.
- **Our slowdown after 2035 is a judgement.** The official growth path gives 101 kg per person by 2050, a stress case.
- **Part of the meat is imported.** About 90% of the meat supply was domestic in 2023 [@DIE-07] {VN-direct|High}. The model keeps today's import shares for each meat, the more import-exposed case [@QNT-01] {VN-direct|Medium}.

## 22.2 Published numbers stop at 2035, so we use four scenarios

| Series | 2025 | 2030 | 2035 | Type | Sources |
|---|---|---|---|---|---|
| Industrial livestock feed, Mt | 24 to 25 | 30 to 32 | none | Official target | [@NTS-23; @REG-54] {VN-direct\|Medium} |
| Meat output, Mt | about 6.0 | 6.0 to 6.5 | none | Official target | [@MAC-23; @REG-54] {VN-direct\|High} |
| Protein-meal imports, Mt | 7.4 | 8.6 | 10.3 | OECD-FAO projection | [@QNT-01] {VN-direct\|Medium} |
| Maize imports, Mt | 12.0 | 14.0 | 16.6 | OECD-FAO projection | [@QNT-01] {VN-direct\|Medium} |

All forward values: {fx:projection}. We found no published projection to 2050 [@QNT-01; @QNT-02; @QNT-15] {VN-direct|Medium}. The 2030 feed target appears to cover livestock feed only, so it now looks out of reach [@NTS-23; @MAC-28] {VN-direct|Medium} {fx:estimate}.

**The four scenarios.**

| Scenario | Diets | Feed efficiency | Alternative protein |
|---|---|---|---|
| **S-BASE** (trend) | Meat per person rises from 66.5 kg to 87.6 kg by 2050 | Slow gains | None |
| **S-HIGH** (official growth path) | 101 kg per person by 2050 | As S-BASE | None |
| **S-EFF** (efficiency) | As S-BASE | Faster gains; less soybean meal per tonne of feed | None |
| **S-ALT** (alternative protein) | As S-BASE, with 1% (2030), 5% (2040) and 10% (2050) of meat replaced by plant-based and fermented foods | As S-BASE | Microbial protein also replaces part of soybean meal and fishmeal in feed |

S-ALT's shares are illustrative what-if levels, not targets {VN-direct|Low}. Its feed side is context only.

## 22.3 The imported feed behind it

**On trend, the soybean meal behind the meat people eat rises 44% by 2050, almost all imported.**

**Soybean meal import need, Mt** {VN-direct|Low} {fx:estimate}

| Scenario | 2025 | 2030 | 2035 | 2040 | 2050 | 2050 against 2025 |
|---|---|---|---|---|---|---|
| S-BASE | 7.20 | 8.46 | 9.47 | 9.95 | 10.40 | +44% |
| S-HIGH | 7.20 | 8.98 | 10.11 | 10.92 | 11.72 | +63% |
| S-EFF | 7.20 | 7.81 | 8.08 | 7.85 | 7.00 | minus 3% |
| S-ALT | 7.20 | 8.32 | 9.01 | 9.15 | 8.78 | +22% |

{{kn:kn-sbm-need-2050}} {{kn:kn-sbm-range-2050}}

**Other feed results** {VN-direct|Low} {fx:estimate}

| Indicator | 2025 | S-BASE 2050 | Range in 2050 |
|---|---|---|---|
| Factory-made feed, Mt | 28.5 | 40.9 | 35.4 to 46.2 |
| Maize import need, Mt | 11.9 | 13.8 | 11.6 to 16.3 |
| Farmland abroad for imported soy and maize, million ha | 4.0 | 4.7 | 3.4 to 5.4 |

{{kn:kn-land-abroad-feed}}

**Readings.**
- **The near term checks out.** The model's 2027 values match US Department of Agriculture forecasts within 2% to 5% [@MAC-01; @MAC-03; @MAC-04; @QNT-01] {VN-direct|Medium}.
- **Vietnam already farms about 4 million hectares abroad for feed,** about five times its own maize area (our calculation) {VN-direct|Low} {fx:estimate}.
- **Domestic soybean is no lever for feed, but could be one for soy foods.** Even a large soybean crop would cover only about 6% of feed needs (our calculation) [@AQF-20; @AQF-02] {VN-direct|Low} {fx:estimate}. But Vietnam's food soybeans, the beans behind tofu and soy milk, are only about 540,000 t a year [@MAC-04] {VN-direct|Medium}. Returning to the 2010 soybean area would cover 76% to 95% of that, at 1.4 to 2.3 times the price of imported beans (our calculation) [@AQF-20; @AIB-06; @SEC-05] {VN-direct|Low}. This is candidate play T12, not ranked until tested ([[ch26-plays]], section 26.8).

**Feed efficiency moves the result most.** Better feed conversion and formulation (S-EFF) would cut 2050 soybean meal need by about 3.4 Mt, twice what S-ALT would {VN-direct|Low} {fx:estimate}. That lever sits outside this study's focus on protein for people.

## 22.4 What protein for people would change

**Protein for people saves the most imports per tonne.** In 2050, replacing 1 t of meat protein avoids about 4.5 t of soybean meal and 9.5 t of maize imports {VN-direct|Low} {fx:estimate}.

**A plant food made from imported soy cuts the tonnage but keeps the dependence.** A wholly plant food made from imported soybeans uses about 3.3 t of beans per tonne of protein. That is about a fifth of the imported soy and maize behind the meat it replaces (our calculation) {VN-direct|Low} {fx:estimate}. So it cuts imported tonnage. But it stays import-dependent unless the beans or the protein are Vietnamese: 97.5% of the soybean supply is imported [@DIE-07] {VN-direct|High}.

**But the tonnes that demand supports are small.** No market has shown modern plant-based or fermented products displacing a measurable share of meat ([[ch18-demand-sizing]]).

**Meat protein displaced: S-ALT against the demand paths** {VN-direct|Low} {fx:estimate} {dx:inferred}

| Meat protein displaced | 2030 | 2035 | 2050 |
|---|---|---|---|
| S-ALT assumption | 11.8 kt (1%) | 39.3 kt (3%) | 144.6 kt (10%) |
| Benchmark demand path | 0.4 kt (0.04%) | 2.4 kt (0.18%) | 6.0 kt (0.41%) |
| Stretch demand path | 3.1 kt (0.27%) | 9.2 kt (0.71%) | 21.9 kt (1.52%) |
| Existing chay days (already in the baseline) | about 29 kt (2.5%) | about 32 kt (2.5%) | about 36 kt (2.5%) |

Read S-ALT's food shares as a what-if, not a demand path. Existing *chay* (vegetarian) days already avoid a similar share ([[ch12-chay-baseline]]).

**So new protein adds a second source; it does not replace meat.** On the benchmark path, new routes deliver about 19,000 t of protein a year by 2035 and 67,000 t by 2050, mostly by replacing imported ingredients ([[ch18-demand-sizing]]) {VN-direct|Low} {fx:estimate} {dx:inferred}. On its own, that does not change national exposure to imported feed.

**The import saving is about 0.1% in 2035.** Displacing 2.4 kt of meat protein avoids about 11 kt of soybean meal (our calculation) {VN-direct|Low} {fx:estimate}. Tofu and soy milk already carry nearly ten times more protein than the benchmark path delivers in 2035, on the same imported beans [@DIE-07] {VN-direct|Medium}. For security, what matters is the share of food protein made from domestic inputs ([[ch01-why-vietnam]]).

**S-ALT's feed side is context only.** Most of its cut in soybean meal comes from microbial protein in feed. Together, its food and feed sides would need sugar equal to about half of Vietnam's cassava harvest, competing with starch exports and fuel ethanol [@FS-01; @FS-31; @GT-10] {VN-direct|Low} {fx:estimate}.

## 22.5 Reality check: what other countries have achieved

S-ALT sits above every real-world comparison we found; S-EFF sits at the low end of what China has done {general|Medium}.
- **Feed recipes change faster than land use.** China cut the soybean meal share of feed by up to 0.45 points a year from 2017 to 2025. Norway cut fish ingredients in salmon feed from 90% to about 30% over two decades [@GEO-10; @GEO-11; @VIS-19] {general|Medium} {fx:trend}.
- **Self-sufficiency targets are usually missed, then cut.** Japan's feed self-sufficiency was 26% in 2000 and 26% in 2024, and its 2030 target was cut [@VIS-11; @VIS-12] {general|High} {fx:trend}.
- **Novel feed ingredients stay tiny.** They were 0.4% of Norwegian salmon feed in 2020 [@VIS-18; @VIS-20] {general|High}. S-ALT's 8% microbial share by 2050 is unprecedented {VN-direct|Low} {fx:estimate}.
- **Even the EU struggles.** To cut soy imports 20% by 2035 with flat demand, an EU analysis needs four levers at their limits, with diet change carrying 40% of the cut [@PPE-03; @PPE-04] {general|Medium} {fx:projection}. On Vietnam's growing numbers, the same target is far out of reach (our calculation) [@PPE-04; @MAC-04] {VN-direct|Low} {fx:estimate}.

On this evidence, a credible ambitious range for Vietnam's soybean meal need in 2050 is about 7 to 9 Mt, against 10.4 Mt on trend {VN-direct|Low} {fx:estimate}. The study sets no goal; the range is context.

## 22.6 What this means

- **Policy makers:** publish a national protein balance each year, showing the protein people eat by food, source and origin, with the imported feed behind it ([[ch28-robust-moves]]). The 2030 feed target needs a clear scope and a statistic to be judged.
- **Investors:** plan on the demand that exists: about 67,000 t of protein a year by 2050 on the benchmark path, mostly ingredients that replace imports.
- **Manufacturers:** demand for meat keeps rising, and new protein grows beside it as ingredients, extenders and plant drinks ([[ch18-demand-sizing]]).
- **Startups:** size plants against the demand for ingredients that replace imports, not against S-ALT ([[ch25-demand-to-frontier]]).
- **Researchers and international bodies:** the gaps that matter most are measured inputs, such as how many people keep chay days, and Vietnamese data on feed conversion and soybean meal use by species.

**Related:** [[ch18-demand-sizing]], [[ch19-outlook-2035]].
