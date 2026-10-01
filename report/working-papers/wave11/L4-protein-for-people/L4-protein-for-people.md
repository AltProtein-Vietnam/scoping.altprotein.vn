# Protein for people: food balance sheets, import dependence and projections

Line: L4, Protein for people: food balance sheets and projections (wave 11). Source prefix: FBS. Date: 2026-10-01.

## Verdict

On FAO food balance sheets for 2023, about 19% to 23% of Vietnam's protein supply was imported food, up from 11% to 13% in 2010. Counting the imported feed behind domestic meat, eggs and farmed fish, about 61% to 71% of animal protein and 40% to 46% of all protein rests on imports (our calculation). The human foods imported directly are soybeans for tofu and soy milk, wheat, milk, beef, offal, groundnuts and dry beans; pork, eggs, fish and rice are domestic at the farm gate. Alternative protein for food would cut imported tonnage per gram of protein but, made from imported soy, keeps the dependence, and at the scale the demand evidence supports it makes no measurable difference. Yield class: **changed a conclusion** (chapters 1 and 22 can lead with a protein balance for people) and **added a constraint** (the domestic-input share of food protein, not product volume, decides security); projections to 2050 add nothing new.

## Headline findings

1. **About one fifth of the protein supply is imported food.** In 2023, directly imported food supplied 19.7 to 23.9 g of the 102.2 g of protein per person per day, 19% to 23%. In 2010 the share was 11% to 13%. The lower figure counts net imports; the higher counts gross imports on FAO's import dependency ratio (our calculation) [VN-direct, Medium, DIE-07].
2. **Two thirds of animal protein rests on imports, directly or through feed.** Of 43.2 g of animal protein per person per day in 2023, 5.8 to 7.6 g was imported food and a further 20.7 to 23.1 g came from domestic animals and fish raised on imported compound feed. Together that is 26.5 to 30.6 g, 61% to 71% (our calculation) [VN-direct, Low, DIE-07; MAC-01; FS-23].
3. **For meat alone the share is 69% to 77% (2023).** On the balance model's trend scenario (S-BASE) it rises to about 79% to 87% by 2050, as household pig feeding gives way to compound feed and poultry grows fastest. That is about 1.1 to 1.3 Mt of meat protein a year in 2050 (our estimate) [VN-direct, Low, QNT-01; MAC-01, estimate 2050].
4. **Imported feed is 82% of compound-feed ingredients by weight and about 93% by protein.** USDA's 2025 table shows 23.57 Mt imported of 28.62 Mt. Weighted by crude protein, the imported share is about 93% (range 90.4% to 94.4% across protein contents tested; our calculation) [VN-direct, Medium, MAC-01; FS-23; DIE-12; FBS-04; FBS-05].
5. **The import-dependent foods people eat directly** (2023 import dependency ratio): wheat about 100%, soybeans 97.5%, maize 74.6%, milk and dairy 71.6%, groundnuts 46.7%, beef 44.3%, pulses 44.0%, offal 39.5%, poultry 12.3% [VN-direct, High, DIE-07].
6. **The foods that are not import-dependent:** pork (import dependency 3.0%), eggs (1.1%), freshwater fish (2.4%), rice (Vietnam exports more than it imports) and vegetables (8.4%). Rice still supplies 27.0 g and pork 13.3 g of protein a day [VN-direct, High, DIE-07].
7. **Soy foods are already a large, almost wholly imported protein for people.** Soybeans eaten as food supplied 4.9 g of protein per person per day in 2023, about 181,000 t of protein a year. Domestic soybeans (48 kt) could cover at most 9% of the 533 kt of beans used as food (our calculation) [VN-direct, High, DIE-07].
8. **The official dairy strategy sets a self-sufficiency path far above trend.** Decision 309/QĐ-TTg (2026) targets domestic raw milk meeting 60% to 65% of processing demand by 2030 and 80% to 85% by 2045, with 2,600 million litres in 2030. FAOSTAT puts milk self-sufficiency at 30% in 2023, and OECD-FAO projects 1,649 kt of raw milk in 2030 [VN-direct, High, APR-11; DIE-07; QNT-01, projection 2030].
9. **OECD-FAO to 2035 puts the growth in poultry and dairy, not pork.** Food use per person rises 51.5% for poultry, 42.9% for fresh dairy, 31.2% for skim milk powder and 10.0% for pork between 2025 and 2035, while rice falls 7.2% [VN-direct, Medium, QNT-01, projection 2035]. Its baseline also lifts poultry self-sufficiency from 87.5% to 96.2%, which the balance model does not.
10. **Protein made for people from imported soy cuts import tonnage but not dependence.** Per tonne of protein, a plant food uses about 3.3 t of imported beans, against about 15.3 t of imported soybean-meal bean equivalent and maize for the meat it replaces (our calculation from F4 factors). At the benchmark demand path (0.18% of meat protein displaced in 2035), the national exposure does not change measurably [VN-direct, Low, DIE-07; QNT-01, estimate 2035].
11. **Child diet quality, not protein supply, is the nutrition gap.** Only 55.2% of children aged 6 to 23 months met minimum dietary diversity in 2020 to 2021; 37.3% in the poorest fifth, 23.0% in Khmer households and 8.7% in Mong households (34 children) [VN-direct, High, FBS-01]. A 2026 press report quotes 14.8% under-five stunting for 2025, but this is unverified (FBS-02).

## 1. Data, access and definitions

**FAO food balance sheets.** The FAOSTAT data API (fenixservices.fao.org) returned HTTP 521 on 2026-10-01. The FAOSTAT bulk file for Asia was reachable. Its internal files are dated 14 October 2025, and the FAOSTAT catalogue gives 28 October 2025 as the last FBS update, with data to 2023 [FBS-03]. This is the same file the study cites as DIE-07, so we reuse DIE-07. No 2024 food balance sheet for Viet Nam existed at access. All 1,704 Viet Nam rows (area code 237, all items and elements, 2010 to 2023) are saved in `raw/faostat_fbs_vnm_2010_2023.csv`.

**What the study already had.** `data/demand_protein_intake.csv` holds FBS protein supply by 16 food groups for 2010 to 2023 (rows DPI-001 to DPI-231). This line adds the balance elements (production, imports, exports, stock change, food and feed use), the import dependency and self-sufficiency ratios, a protein-weighted import share and the imported feed behind animal protein.

**Definitions (FAO).** Import dependency ratio (IDR) = imports / (production + imports minus exports) x 100. Self-sufficiency ratio (SSR) = production / (production + imports minus exports) x 100. An IDR can exceed 100% when imports are processed and re-exported (wheat flour and noodles). Food balance sheets measure supply available for consumption, not intake: they include household waste (DG-171).

**Scripts and raw data.** `tools/build_tables.py` rebuilds every table from the raw files. Its printed output is in `raw/build_tables_output.txt`. Raw inputs: the FAOSTAT extract; `raw/oecd_fao_2026_2035_vnm_protein_foods.csv` and `raw/oecd_fao_2026_2035_vnm_maize.csv` (OECD-FAO Agricultural Outlook 2026-2035, dataflow version 1.1, re-queried 2026-10-01; same dataflow as QNT-01); `raw/usda_gain_vm2026-0012_feed_tables.txt` (USDA Table 1 and Table 2, MAC-01); `raw/sdgcw_2020_2021_table_tc77_extract.txt` (FBS-01).

## 2. Where the protein people eat comes from

Protein supply, g per person per day, by source. Full table with shares: `data_protein_supply_by_source.csv`. All rows [VN-direct, High, DIE-07].

| Source | 2010 | 2015 | 2020 | 2023 | Share 2023 |
|---|---|---|---|---|---|
| Rice | 31.4 | 30.3 | 28.8 | 27.0 | 26.4% |
| Wheat | 2.3 | 2.7 | 3.8 | 3.3 | 3.2% |
| Maize | 1.4 | 2.7 | 3.2 | 2.7 | 2.7% |
| Soybeans (tofu, soy milk, other soy foods) | 2.9 | 3.3 | 4.5 | 4.9 | 4.8% |
| Pulses and groundnuts | 3.1 | 3.2 | 3.3 | 4.6 | 4.5% |
| Vegetables | 5.3 | 8.8 | 9.8 | 11.0 | 10.8% |
| Other plant foods (fruit, roots, nuts, other) | 2.7 | 3.0 | 3.3 | 5.5 | 5.3% |
| **All plant foods** | **49.2** | **54.1** | **56.6** | **59.0** | **57.7%** |
| Pigmeat | 9.8 | 10.6 | 10.3 | 13.3 | 13.0% |
| Poultry meat | 5.3 | 4.1 | 7.2 | 8.8 | 8.6% |
| Beef and buffalo | 1.6 | 1.2 | 1.7 | 2.7 | 2.7% |
| Edible offal | 1.8 | 2.0 | 1.6 | 2.9 | 2.9% |
| Fish and seafood | 9.1 | 9.8 | 11.3 | 11.1 | 10.9% |
| Eggs | 1.0 | 1.3 | 1.3 | 1.2 | 1.2% |
| Milk and dairy | 1.4 | 2.4 | 2.8 | 2.5 | 2.4% |
| **All animal foods** | **30.5** | **31.9** | **36.8** | **43.2** | **42.3%** |
| **All foods** | **79.7** | **86.0** | **93.4** | **102.2** | **100%** |

Rows "pulses and groundnuts" and "other plant foods" sum the named FBS groups in the CSV. Two series need care. The FAO egg supply looks far too low against national egg output (DG-174). The FAO milk series swings between years through residual and trade adjustments (DG-175). Tree-nut supply jumps from 0.4 kg per person in 2010 to 9.7 kg in 2023, which looks like a balancing effect of the cashew processing trade rather than a real change in diets (our reading) [VN-direct, Low, DIE-07].

In tonnes, 102.2 g a day is about 3.74 Mt of protein a year in 2023; animal foods are about 1.58 Mt and meat about 0.92 Mt (our calculation from the FBS population of 100.35 million) [VN-direct, Medium, DIE-07].

## 3. Self-sufficiency and import dependence by food, 2023

Full table for 2010, 2015, 2020 and 2023: `data_self_sufficiency_by_food.csv`. All values kt, FAOSTAT 2023; ratios our calculation on FAO definitions [VN-direct, High, DIE-07].

| Food | Production | Imports | Exports | Import dependency | Self-sufficiency | Trend since 2010 |
|---|---|---|---|---|---|---|
| Wheat | 93 | 6,227 | 472 | 106.5% | 1.6% | Imports nearly doubled (3,372 kt in 2010) |
| Soybeans | 48 | 1,835 | 1 | 97.5% | 2.6% | Production fell from 299 kt; IDR from 45% |
| Maize | 4,437 | 12,372 | 230 | 74.6% | 26.8% | IDR from 26% in 2010 |
| Milk and dairy (milk equivalent) | 1,247 | 2,955 | 74 | 71.6% | 30.2% | SSR from 14% in 2010; series unstable |
| Groundnuts | 400 | 344 | 7 | 46.7% | 54.3% | IDR from almost 0% in 2015 |
| Beef and buffalo | 337 | 266 | 2 | 44.3% | 56.1% | Imports exclude live cattle (counted as domestic) |
| Pulses | 286 | 216 | 11 | 44.0% | 58.2% | IDR from 0% in 2010 |
| Edible offal | 471 | 307 | 1 | 39.5% | 60.6% | IDR from 0% in 2010 and 3.5% in 2015 |
| Poultry meat | 1,740 | 243 | 10 | 12.3% | 88.2% | IDR 49% in 2010, 9% in 2015 |
| All meat (excluding offal) | 5,676 | 625 | 26 | 10.0% | 90.5% | |
| Vegetables | 19,580 | 1,763 | 413 | 8.4% | 93.5% | Imports jumped in 2023 |
| Pigmeat | 3,549 | 111 | 11 | 3.0% | 97.3% | |
| Freshwater fish | 3,414 | 56 | 1,133 | 2.4% | 146.1% | Net exporter |
| Eggs | 472 | 5 | 6 | 1.1% | 100.2% | FAO egg output too low (DG-174) |
| Rice (paddy equivalent) | 43,498 | 1,369 | 10,897 | 4.0% | 128.0% | Net exporter; imports mostly milled and re-exported |
| Fish and seafood, all | 8,276 | 1,113 | 3,507 | 18.9% | 140.7% | Net exporter; part of imports processed for export |

Readings:

- **The human foods that are already import-dependent are plant foods, dairy and the cheaper meat cuts.** Wheat, soybeans and maize are almost or mostly imported. Milk is about 70% imported (milk equivalent). Beef, offal, groundnuts and dry beans are 40% to 47% imported, and all four have risen from near zero since 2010 or 2015 [VN-direct, High, DIE-07]. Line L1 covers the meat and dairy trade in detail.
- **The big animal proteins are domestic at the farm gate.** Pork, eggs and fish are 97% to 100% self-sufficient or net exported. Their exposure runs through feed, not through food imports (section 5).
- **Beef is undercounted as imported.** Food balance sheets count meat from imported live cattle as domestic production, so the 44% understates beef import dependence [VN-direct, Medium, DIE-07]. Line L1 has the live-cattle trade.

## 4. Directly imported protein in the food supply

We weighted each FBS item's protein supply by its import share (our calculation; script section 3a). Two bases bracket the result: the gross FAO import dependency ratio (capped at 100%), and the net import share, which is zero for net exporters such as rice and fish.

| Year | Protein supply, g per person per day | Directly imported, g (net to gross) | Share |
|---|---|---|---|
| 2010 | 79.7 | 8.9 to 10.6 | 11.2% to 13.3% |
| 2015 | 86.0 | 10.1 to 13.0 | 11.8% to 15.1% |
| 2020 | 93.4 | 16.2 to 19.5 | 17.4% to 20.8% |
| 2023 | 102.2 | 19.7 to 23.9 | 19.3% to 23.4% |

All rows (our calculation) [VN-direct, Medium, DIE-07].

The largest directly imported protein items in 2023, in g per person per day (net to gross basis):

- soybeans 4.8; wheat 3.2 to 3.3; maize as food 2.0; milk 1.7 to 1.8;
- beef 1.2; offal 1.2; poultry 1.0 to 1.1;
- groundnuts 0.9; dry beans 0.8 to 0.9; tree nuts 0.9 to 1.6 (mostly the cashew trade).

Plant foods give 13.9 to 16.3 g of the total and animal foods 5.9 to 7.6 g.

**Sensitivity.** FAOSTAT puts maize food use at 1,617 kt (16.1 kg per person) in 2023; OECD-FAO puts it at 639 kt (6.4 kg) [DIE-07; QNT-01]. On the OECD-FAO figure, maize food would give about 1.1 g of protein, and the direct import share would fall to about 18% to 22% (our calculation). We keep FAOSTAT, because its items sum to the protein total, and log the gap (disagreements.csv).

## 5. The imported feed behind the animal protein people eat

**Question.** How much of the animal protein people eat rests on imported feed? We keep the estimate simple and label every input. It is an attribution, not a measured flow.

**Step 1: imported share of compound feed (2025).** USDA's ingredient table adds up to its 28.62 Mt of feed demand in 2025 (22.12 Mt of animal feed and 6.5 Mt of aquafeed) [MAC-01; FS-23]:

| Ingredient | Imported, kt | Local, kt | Crude protein, as fed | Source of protein content |
|---|---|---|---|---|
| Soybean meal (including local crush of imported beans) | 7,206 | 0 | 46% | Study convention (F4.3.4) |
| Maize | 9,214 | 1,700 | 8.6% | DIE-12 (dried yellow maize) |
| Distillers dried grains (DDGS) | 1,550 | 0 | 27% | Study convention (F4.3.4) |
| Feed wheat | 2,580 | 0 | 11.0% | FBS-04 (12.6% of dry matter at 87% dry matter) |
| Rice bran and broken rice | 545 | 2,800 | 10% (range 7.9% to 13.3%) | DIE-12 (polished rice 7.9%); FBS-05 (bran 13.3% as fed); mix our assumption |
| Plant-based meal and bran | 1,825 | 0 | 30% (range 15% to 35%) | Study convention for other oilseed meals; composition not given |
| Other protein meals | 650 | 0 | 55% (range 45% to 65%) | Our assumption (fishmeal and animal meals) |
| Cassava | 0 | 550 | 3.0% | DIE-12 (dried cassava) |
| **Total** | **23,570** | **5,050** | | |

Imported share: 82.4% by weight; about 93% by crude protein (5.77 of 6.21 Mt of crude protein; range 90.4% to 94.4% when every protein content moves against or in favour of imports). All our calculation [VN-direct, Medium, MAC-01; FS-23; DIE-12; FBS-04; FBS-05]. Imported feed protein (about 5.8 Mt in 2025) is about 3.7 times the animal protein in the national food supply (1.58 Mt in 2023). One reason is that about half of farmed fish and shrimp output is exported (F4.3.2) (our calculation).

**Step 2: which animal foods are fed.** We apply the balance model's compound-feed shares (F4.3.3). Pigs are 0.81, also used for offal. Poultry meat and eggs are 0.96. Freshwater fish are 0.68, the "other fish" share, since pangasius is mostly exported. Crustaceans are 0.80, our weighting of whiteleg shrimp (1.00) and other shrimp (0.30) by 2025 output. Beef, buffalo, goat and milk are treated as feed-free (grazing and crop residues), as are capture fish and molluscs. That is a lower bound: fattened cattle and dairy cows eat some imported concentrate. Non-compound feed (household mixes of rice bran, broken rice, cassava and some maize) is treated as domestic, which is also conservative.

**Step 3: combine.** For each animal food: imported food (step A) plus domestic supply x compound-feed share x imported share of compound feed. Low case: net imports and the 82.4% weight share. High case: gross imports and the 93% protein share. Full rows: `data_animal_protein_import_reliance.csv`.

| Animal food, 2023 | Protein, g per day | Imported food, g | From imported feed, g | Rests on imports |
|---|---|---|---|---|
| Pigmeat | 13.3 | 0.4 | 8.6 to 9.7 | 68% to 76% |
| Poultry meat | 8.8 | 1.0 to 1.1 | 6.1 to 6.9 | 82% to 91% |
| Fish and seafood | 11.1 | 0.3 to 1.8 | 3.8 to 4.1 | 37% to 53% |
| Edible offal | 2.9 | 1.2 | 1.2 to 1.3 | 79% to 85% |
| Beef, buffalo, goat and other meat | 3.0 | 1.2 | 0 (lower bound) | 40% to 41% |
| Milk and dairy | 2.5 | 1.7 to 1.8 | 0 (lower bound) | 70% to 72% |
| Eggs | 1.2 | 0 | 1.0 to 1.1 | 79% to 89% |
| **All (table covers 42.9 of 43.2 g)** | **42.9** | **5.8 to 7.6** | **20.7 to 23.1** | **61% to 71% of 43.2 g** |

All rows our calculation [VN-direct, Low, DIE-07; MAC-01; FS-23]. Meat alone: 17.4 to 19.3 g of 25.1 g, 69% to 77%. Adding the directly imported plant protein, about 40.4 to 47.0 g of the 102.2 g protein supply, 40% to 46%, rests on imports directly or through feed (our calculation). The year mismatch (2023 food supply, 2025 feed table) is small next to the attribution assumptions.

**What it does not count.** It leaves out imported fertiliser, fuel, veterinary drugs, breeding stock and day-old chicks. Meat from imported live cattle counts as domestic beef. Soy and wheat inside processed foods made in Vietnam are counted once, at the primary level, through FBS standardisation.

## 6. Projections to 2035 and 2050

**OECD-FAO Agricultural Outlook 2026-2035 (baseline).** This is still the only published model with Vietnamese food use by commodity. The study already uses its meat and fish series (QNT-01, DIE-11). We re-queried it for the other protein foods [VN-direct, Medium, QNT-01, projection 2035]:

| Food use per person, kg | 2025 | 2030 | 2035 | Change 2025 to 2035 |
|---|---|---|---|---|
| Pigmeat (retail weight) | 28.6 | 31.1 | 31.5 | +10.0% |
| Poultry (retail weight) | 17.0 | 21.2 | 25.8 | +51.5% |
| Beef and veal (retail weight) | 4.0 | 4.3 | 4.6 | +15.2% |
| Fish | 42.4 | 46.4 | 46.8 | +10.4% |
| Fresh dairy products | 11.3 | 13.5 | 16.1 | +42.9% |
| Skim milk powder | 0.88 | 1.01 | 1.15 | +31.2% |
| Eggs | 3.9 | 4.4 | 5.0 | +29.4% (from a base that is probably too low, DG-174) |
| Rice | 132.8 | 128.0 | 123.2 | minus 7.2% |
| Wheat | 18.1 | 18.3 | 17.5 | minus 3.2% |
| Pulses | 3.4 | 3.4 | 3.3 | minus 1.0% |
| Soybeans (food) | 0 | 0 | 0 | not modelled from 2024 |

Self-sufficiency on the same baseline (production over consumption, our calculation) [VN-direct, Medium, QNT-01, projection 2035]:

- pork 96.1% (2025) to 95.5% (2035);
- poultry 87.5% to 96.2%, with imports falling from 407 to 231 kt;
- beef 52.2% to 50.1%; pulses 55.2% to 49.4%;
- soybeans 1.9% to 1.4%, with imports rising from 2.6 to 3.1 Mt;
- wheat imports from 5.6 to 6.5 Mt; skim milk powder imports from 107 to 141 kt.

Two cautions. First, the API's convention field labels poultry as RTOC (ready to cook) and pork and beef as CWE (carcass weight). OECD-FAO's 2023 poultry output (2,329 kt RTOC) is 34% above FAOSTAT's 1,740 kt carcass weight, so we use OECD-FAO for growth only, as the balance model already does. Appendix F4.9.4 says the base "probably uses live weight"; the label says RTOC, so that wording needs a correction. Second, OECD-FAO has no soybean food use for Vietnam from 2024, against 533 kt in FAOSTAT for 2023, so it cannot project soy foods.

**The balance model, converted to protein people eat.** Using the unchanged model outputs (S-BASE) and 0.15 kg of protein per kg of carcass weight (FAOSTAT 2023 implies 0.151) (our calculation; `data_meat_protein_on_imports_projection.csv`) [VN-direct, Low, QNT-01, estimate 2050]:

| S-BASE | 2025 | 2030 | 2035 | 2040 | 2050 |
|---|---|---|---|---|---|
| Meat, kg carcass weight per person | 66.5 | 75.4 | 81.9 | 84.3 | 87.6 |
| Meat protein, g per person per day | 27.3 | 31.0 | 33.7 | 34.6 | 36.0 |
| Meat protein, kt a year | 1,013 | 1,178 | 1,309 | 1,371 | 1,446 |
| Share resting on imports | 70% to 78% | 74% to 82% | 76% to 84% | 78% to 86% | 79% to 87% |
| Meat protein resting on imports, kt | 713 to 790 | 876 to 971 | 994 to 1,103 | 1,063 to 1,179 | 1,136 to 1,261 |

On S-HIGH, meat protein reaches 1,666 kt in 2050, of which 1,310 to 1,453 kt rests on imports. The share rises because the model moves pigs from household to compound feed (0.81 to 0.97) and poultry grows fastest. It holds self-sufficiency at OECD-FAO's 2025 values; OECD-FAO's own rising poultry self-sufficiency would lower direct imports but raise feed needs.

**What we did not find.** We again found no FAO, IFPRI or peer-reviewed projection of Vietnamese meat, fish, dairy or protein consumption to 2050. Van Eenennaam (2024, PNAS) and Naylor and others (2021, Nature Communications, fish demand to 2050 in 10 countries) do not cover Vietnam (read, not registered). Official volume targets still stop at 2030, except the dairy strategy.

**The dairy strategy (Decision 309/QĐ-TTg, 23 February 2026).** Targets [VN-direct, High, APR-11, projection 2030 to 2045 (official target)]:

| | 2030 | 2035 | 2045 |
|---|---|---|---|
| Milk and dairy consumption, litres per person a year | about 40 | about 60 | about 100 |
| Domestic raw milk, million litres | about 2,600 | about 4,500 | about 8,000 |
| Share of domestic processing demand met by domestic raw milk | 60% to 65% | 70% to 75% | 80% to 85% |

Against this, OECD-FAO projects 1,649 kt of raw milk in 2030 and 2,009 kt in 2035 [QNT-01], and FAOSTAT's 2023 milk self-sufficiency (milk equivalent) is 30.2% [DIE-07]. A litre of milk weighs about 1 kg, so the 2030 target is about 1.6 times the projection (our approximation). The bases differ (processing demand against all dairy supply), so we report both and do not reconcile them.

## 7. Nutrition context: protein security for children

- **Stunting.** The study uses 18% for children under 5 in 2023 and 32% among ethnic minority children [APR-27; DIE-01; DIE-03]. A press report of 25 August 2026 quotes the National Institute of Nutrition (NIN) director: 14.8% in 2025 [VN-direct, Low, FBS-02]. It does not name the survey, and 14.8% is also the 2019 to 2020 survey's stunting rate for ages 5 to 19. We do not change 18% until NIN publishes the 2025 figure (open question).
- **We found no new national nutrition survey** with intake by food group for 2024 to 2026 (searches in Vietnamese; also OQ-156).
- **Diet diversity for young children is the gap that matches the stunting pattern.** In 2020 to 2021, 55.2% of children aged 6 to 23 months ate from at least 5 of 8 food groups (which include flesh foods, eggs, dairy and legumes). The share was 59.2% in Kinh and Hoa households, 45.8% in Tay, Thai, Muong and Nung households, 23.0% in Khmer households and 8.7% in Mong households (34 children, small sample). It was 37.3% in the poorest fifth and 67.9% in the richest [VN-direct, High, FBS-01]. The report gives no breakdown by flesh food or egg.
- **Reading.** National protein supply (102 g a day) is not the constraint. Access to diverse, animal-source and fortified foods for poor and ethnic minority infants is. This supports chapter 11's position that new protein should not be pitched as the answer to child undernutrition (our inference) [VN-direct, Medium, FBS-01; DIE-07].

## 8. Would alternative protein for human food change the exposure?

- **Direction: it reduces import tonnage per gram of protein, but keeps a soy dependence.** Replacing 1 t of meat protein avoids about 4.5 t of soybean meal and 9.5 t of maize imports (chapter 22). That is about 15.3 t of imported grain and bean equivalent (our conversion at 0.78 t of meal per t of beans, F4). A plant food from imported soybeans uses about 3.3 t of beans per t of protein (F4.3.6). So it needs about one fifth of the imported tonnage. But it is still almost wholly imported unless the beans or protein are domestic (our calculation) [VN-direct, Low, QNT-01, estimate].
- **Scale: no measurable change by 2035.** The benchmark demand path displaces about 2.4 kt of meat protein in 2035, 0.18% (ch18). That avoids about 11 kt of soybean meal, about 0.1% of the 9.5 Mt needed on S-BASE. It also removes about 1.7 to 1.9 kt of the 1.0 to 1.1 Mt of meat protein resting on imports (our calculation) [VN-direct, Low, estimate 2035].
- **Existing soy foods are ten times larger.** Tofu, soy milk and other soy foods already supply about 181 kt of protein a year (2023). That is nearly ten times the 19 kt the benchmark path delivers in 2035. About 91% to 97.5% of the beans are imported (our calculation) [VN-direct, Medium, DIE-07]. For security, the indicator that matters is the domestic-input share of food protein ingredients, not the volume of new products.

## What this changes in the package

| Where | Current text or value | Proposed change | Evidence | Strength |
|---|---|---|---|---|
| ch01 section 1.1 (after "Animal foods supply a growing share of protein") | Gives supply by source, not by origin | Add a short paragraph and table: in 2023 about 19% to 23% of protein supply was imported food (11% to 13% in 2010); with the feed behind domestic animals, 61% to 71% of animal protein and 40% to 46% of all protein rests on imports (our calculation). List the import-dependent foods (wheat, soybeans, milk, beef, offal, groundnuts, beans) and the domestic ones (pork, eggs, fish, rice) | DIE-07; MAC-01; FS-23 | strong (data), moderate (attribution) |
| ch01 In brief and section 1.6 argument 1 | "Vietnam's meat, eggs, milk and farmed fish rest on imported feed: about 99% of the soy protein in feed..." | Add the food-level number: "about two thirds of the animal protein people eat rests on imports, directly or through feed (2023, our calculation)" | DIE-07; MAC-01 | moderate |
| ch22 opening and new first section | Leads with feed (title being changed to "what people will eat, and the imports behind it") | Lead with meat protein per person (27.3 g in 2025, 33.7 g in 2035, 36.0 g in 2050 on S-BASE) and in total (1.01, 1.31, 1.45 Mt), and the share resting on imports (70% to 78% in 2025, 79% to 87% in 2050) | QNT-01; balance_outputs.csv | moderate |
| ch22 section 22.5 reading "The food route saves the most imports per tonne" | Gives 4.5 t SBM and 9.5 t maize avoided | Add: a plant food from imported soy uses about 3.3 t of beans per t of protein, about one fifth of the meat route's imported tonnage, but stays import-dependent unless inputs are domestic | F4 factors | moderate |
| ch11 section 11.1 Supply paragraph | "Rice still supplies 27.0 g of protein a day and soy foods only 4.9 g" | Add origin: 97.5% of soybeans and all wheat are imported; soy foods carry about 181 kt of protein a year; domestic beans could cover at most 9% of food use | DIE-07 | strong |
| ch11 section 11.2 and kn-stunting | 18% (2023) | Keep 18%; add a note that a 2026 press report gives 14.8% for 2025, unverified. Add SDGCW 2020 to 2021 minimum dietary diversity (55.2%; poorest 37.3%; Khmer 23.0%; Mong 8.7%) | FBS-01; FBS-02 | weak (stunting), moderate (diversity) |
| app-f4 F4.9.4 "Poultry basis" row | "OECD-FAO probably uses live weight" | Replace with: the SDMX convention field labels poultry RTOC; OECD-FAO 2023 output (2,329 kt) is 34% above FAOSTAT's 1,740 kt carcass weight; use growth only | QNT-01; DIE-07 | moderate |
| app-f4 F4.2.1 and balance_published_projections.csv | No dairy, egg, pulse or wheat rows; poultry SSR path not shown | Add OECD-FAO rows: fresh dairy 11.3 to 16.1 kg, SMP 0.88 to 1.15 kg and imports 107 to 141 kt, eggs, pulses, wheat imports 5.6 to 6.5 Mt, soybean imports 2.6 to 3.1 Mt; poultry SSR 87.5% to 96.2% (2035); Decision 309 dairy targets | QNT-01; APR-11 | strong |
| app-r2 and data/disagreements.csv | | Add six disagreements (see disagreements.csv) | QNT-01; DIE-07; APR-11; FBS-02 | moderate |
| ch28 RM-01 (publish a national protein balance) and ch30 | Proposed as a public good | Cite this line as a first version and method: protein by food, source and origin, with the imported-feed memo line; note no Vietnamese agency publishes a food balance sheet we could find | DIE-07 | moderate |
| ch23 axis "stress on imported protein" | Axis renamed in v0.8 | Use the 61% to 71% (animal protein) and 19% to 23% (direct food imports) as the starting values for the axis | DIE-07; MAC-01 | moderate |
| data/ (new files) | | Add `protein_supply_by_source.csv`, `self_sufficiency_by_food.csv`, `animal_protein_import_reliance.csv`, `meat_protein_on_imports_projection.csv` with data-dictionary sections | DIE-07; QNT-01; MAC-01 | strong |
| data/key-numbers.json | | Up to six new tiles (key_numbers.csv) | as listed | moderate |

## Next-wave candidates

1. **Repeat with the 2024 food balance sheet when FAO releases it** (deeper, desk). It would extend the series past the 2025 African swine fever wave. It would change chapter 1 only if the direct import share moves by more than a few points. Watch the FAOSTAT catalogue (FBS-03).
2. **Ask NSO or MAE whether Vietnam compiles a national food balance** (different kind: a call). We found none published. A national series would replace FAO estimates for eggs and milk, where FAO looks wrong (DG-174, DG-175). This is the cheapest step towards RM-01.
3. **The domestic share of soybeans used for tofu and soy milk** (different kind: two calls to soy-food makers). This sets the domestic-input share of the largest existing plant protein for people. Desk research cannot close it.
4. **Feed composition behind the attribution** (deeper; feed is context only). The "plant-based meal and bran" and "other protein meals" lines move the protein share by about 2 points; one call to USDA Post or the feed association would close it. It would not change any conclusion. Further desk work here is noise.
5. **Official 2025 stunting rate** (closes a question; one email to NIN). It decides whether kn-stunting changes from 18%.

## Limits

- FAOSTAT data API `https://fenixservices.fao.org/faostat/api/v1/en/data/FBS` returned HTTP 521 on 2026-10-01. We used the bulk file (same data). No 2024 FBS existed.
- FBS is supply, not intake, and it carries known errors for Vietnam: eggs (DG-174), milk (DG-175), tree nuts (cashew trade) and maize food use (against OECD-FAO). We report bases and ranges rather than correcting them.
- The imported-feed attribution is ours and simple. It uses a 2025 feed table on 2023 food supply, species compound-feed shares that are model assumptions (F4), and protein contents for two USDA lines that the source does not define. Ruminants and dairy are treated as feed-free, which understates reliance.
- The thuvienphapluat.vn page for Decision 309 returned HTTP 403; we read the full text on the Government portal (APR-11).
- We did not read FAO's "The future of food and agriculture" data portal or IFPRI IMPACT country tables. Searches found no Vietnam-level 2050 consumption projection in either.
- The SDGCW report gives minimum dietary diversity but not consumption of flesh foods or eggs by group; the Mong estimate rests on 34 children.
- The 14.8% stunting figure for 2025 comes from one press report (FBS-02) and is unverified.
- WebSearch calls used: 14.

## Working notes (record of the run)

- 2026-10-01. FAOSTAT API down (HTTP 521); bulk file reachable; same file as DIE-07; data to 2023. Viet Nam rows saved in `raw/`.
- First results from `tools/build_tables.py`: direct import share 19.3% to 23.4% (2023); animal protein resting on imports 61% to 71%.
- OECD-FAO re-queried for dairy, eggs, pulses, wheat, soybeans, rice and maize. Convention field: poultry RTOC, pork and beef CWE. Soybean food use zero from 2024.
- Crude protein contents: wheat and rice bran from Feedipedia (FBS-04, FBS-05); maize, rice and cassava from the Vietnamese Food Composition Table (DIE-12); the rest are study conventions or labelled assumptions.
- Nutrition: one press report gives 14.8% stunting in 2025 (FBS-02); SDGCW 2020 to 2021 minimum dietary diversity extracted (FBS-01).
