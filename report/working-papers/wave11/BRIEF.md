# Wave 11: Food security hypotheses for the protein people eat

## Context

AltProtein Vietnam's study "Alternative protein in Vietnam: a supply-side scoping study" is in this repository (version 0.7, being revised to version 0.8). Today is 2026-10-01.

The study's position today: the case for alternative protein in Vietnam is "food and feed security, industrial value and trade" (`ch01-why-vietnam`, sections 1.2 to 1.6). That case rests almost entirely on one exposure: about 99% of the soy protein in Vietnamese feed is imported, and feed is 60 to 70% of livestock cost. Disease appears as a shock (African swine fever in 2019 and 2025, section 1.3; endemic ASF, recombinant strains and H5N1 as a wildcard in `ch20-drivers-2050` and `app-f2-drivers-signals` sections F2.2.1 to F2.2.3, F2.11). The balance model (`app-f4-balance-model`) holds meat self-sufficiency constant from OECD-FAO 2025 data (pork 96.1%, poultry 87.5%, beef 52.2%), but no page examines imported meat, offal or dairy, or whether they are subsidised at origin.

Why this wave: for version 0.8 the owner has asked us to (1) test more food-security hypotheses, including reliance on subsidised meat protein from overseas and pandemic risk, and (2) refocus the study on protein for human consumption, keeping feed only as context. The lines below test hypotheses; a clean negative ("the evidence does not support this") is as useful as a positive. Each line must also say whether alternative protein *for human food* would reduce the exposure, increase it, or make no difference.

Read, in addition to `working-papers/PROTOCOL.md`:

- Pages: `ch01-why-vietnam`, `ch11-protein-diet` (sections 11.1, 11.5), `ch20-drivers-2050`, `ch22-protein-balance-2050`, `ch23-scenarios-2050` (section 23.1), `app-f2-drivers-signals` (F2.2, F2.11, shock register), `app-f4-balance-model` (self-sufficiency rows), `front-prologue` (the arguments for and against, wave 10).
- Data: `data/macro_indicators.csv`, `data/shock_register.csv`, `data/wildcards.csv`, `data/balance_assumptions.csv` (rows BLA-033 to BLA-042), `data/diet_quality_vietnam.csv`, `data/demand_protein_intake.csv`, `data/trade_flows.csv`, `data/tariffs.csv`.
- Earlier working papers: `working-papers/wave3/geo_macro/`, `working-papers/wave3/horizon_scan/`, `working-papers/wave3/balance_model/`, `working-papers/wave6/diet/`, `working-papers/wave10/` (B arguments for and against, prefix PRB).
- Search `data/open_questions.csv` and `data/disagreements.csv` for your topic before starting.

## Lines

| Line | Folder | Source prefix | Question | What result would change which conclusion |
|---|---|---|---|---|
| L1 | `wave11/L1-meat-imports/` | MIM | How much of the meat, offal and dairy Vietnamese people eat is imported, from where, at what price against domestic product, and is it subsidised at origin? | If imports are a large or fast-growing share of a protein food, and origin support is material, ch01 gains a second import exposure beyond feed, and the plays gain an import-substitution target in food. If imports are small or unsubsidised, ch01 says so and the hypothesis is closed. |
| L2 | `wave11/L2-disease-pandemic/` | PAN | How exposed is the protein people eat to animal disease, zoonoses and pandemics, and does alternative protein for food reduce that exposure? | Quantified losses, price effects and human-health risk would strengthen or weaken the disease leg of the food-security case in ch01, ch20 and ch23; evidence that alternative protein reduces risk (or only claims) sets how strongly the study can say so. |
| L3 | `wave11/L3-security-exposures/` | SEC | Which other food-security exposures matter for the protein people eat (climate, wild fish, trade routes, concentration of origins, price shocks, official food-security policy), and would alternative protein for food reduce, shift or add to them? | Adds or removes legs of the case in ch01 and the scenario axes in ch23; tests the counter-hypothesis that alternative protein made from imported soy, pea or sugar only moves the import dependence. |
| L4 | `wave11/L4-protein-for-people/` | FBS | Where does the protein Vietnamese people eat come from today (food balance sheets by source, self-sufficiency and import dependence by food), and how is human protein consumption projected to 2050? | Gives the study a human-food protein balance to lead chapter 1 and chapter 22, replacing the feed-first framing; shows which human foods are already import-dependent. |

### L1: Imported meat, offal and dairy, and the subsidy hypothesis (MIM)

1. Volumes and values of Vietnamese imports of meat and edible offal (HS 0201 to 0210, with pork, poultry, beef and buffalo separated), live cattle for slaughter (HS 0102), and dairy (HS 0401 to 0406, especially milk powder), 2015 to 2025 or latest, by origin. Use UN Comtrade (public API via curl), Vietnamese customs, MAE or Department of Livestock Production statements, USDA FAS GAIN (Livestock and Products, Poultry, Dairy annual reports for Vietnam) and Vietnamese press (search "nhập khẩu thịt", "thịt nhập khẩu giá rẻ", "phụ phẩm nhập khẩu").
2. Share of domestic consumption: compare with OECD-FAO (already used in the balance model: pork 96.1%, poultry 87.5%, beef 52.2% self-sufficiency in 2025), FAOSTAT and USDA. Are imports rising? Which products (frozen leg quarters, offal, Indian buffalo meat, frozen pork)?
3. Prices: landed import prices against domestic farm-gate or wholesale prices; documented complaints by Vietnamese producers (for example pig or poultry associations about cheap imported meat or offal), and any trade-defence petitions or safeguard actions.
4. The subsidy hypothesis: what support do the main origins give their meat and dairy sectors (OECD Producer Support Estimate by country and commodity, the single commodity transfers for pigmeat, poultry, beef and milk; India's buffalo-meat export support; Brazil's credit; US and EU programmes)? Distinguish producer support in general from export subsidies (WTO Nairobi decision 2015 eliminated agricultural export subsidies). Is there evidence that support lowers the price at which meat reaches Vietnam? Say plainly where the evidence is only general.
5. Tariff schedule: what Vietnam charges on these imports under MFN, CPTPP, EVFTA, RCEP and ATIGA, and the phase-down path to the 2030s (check `data/tariffs.csv` first).
6. Does alternative protein for food plausibly substitute for these imports (for example processed-meat raw material, mechanically deboned meat for sausages, milk powder in drinks), or is it a different product? Tie to the demand evidence in ch14 to ch16 (blends, extenders, plant milks).

Out of scope: feed imports (established); disease (L2); overall food balance sheets (L4 does the all-food view; L1 does trade detail and subsidies).

### L2: Animal disease, zoonoses and pandemic risk (PAN)

Build forward from F2.2.1 to F2.2.3 and the shock register; do not repeat what is there.

1. African swine fever in 2025 and 2026: outbreaks, pigs culled, price effects on pork for consumers, the state of the Vietnamese live vaccines (AVAC, NAVETCO, Dabaco) and recombinant-strain escape. Economic losses to households and to the protein supply in 2019 and since (peer-reviewed or official estimates).
2. Highly pathogenic avian influenza in Vietnam: poultry outbreaks 2023 to 2026, human H5N1 cases in Vietnam since 2024 (WHO Disease Outbreak News, Vietnamese MOH), H9N2 and other subtypes; effects on poultry supply and prices.
3. Foodborne and occupational zoonoses tied to animal protein in Vietnam: *Streptococcus suis* (raw pig blood, *tiết canh*), and others with Vietnamese data; disease burden figures (WHO FERG or Vietnamese studies).
4. Antimicrobial use and resistance in Vietnamese livestock and aquaculture: latest use figures, the 2026 rules (Circular on antibiotic use from 1 January 2026), and the national action plan.
5. Pandemic risk from animal production and wildlife: what the evidence says about intensive livestock, live-bird markets and wildlife trade as pandemic sources in Vietnam (for example Directive 29/CT-TTg 2020 on wildlife trade, One Health partnership plans). Separate peer-reviewed risk evidence from advocacy claims.
6. Does alternative protein for food reduce these risks? Find the best evidence (peer-reviewed, WHO, FAO, UNEP-ILRI) on whether replacing part of animal-source food lowers zoonotic or AMR risk, and the main counter-arguments (for example that risk depends on how animals are farmed, not on how much meat is eaten; that a small displacement does not change herd sizes). Use the study's own numbers: the benchmark demand path displaces about 0.2% of meat protein by 2035 (ch18), which is too small to change risk on its own.
7. Supply-side resilience: during the 2019 ASF shock and COVID-19, what did Vietnamese consumers switch to (ch11 says chicken, not tofu)? Any evidence that plant protein or other foods bridged the gap.

Out of scope: aquaculture feed (context only); shrimp disease except as one line of context.

### L3: Other food-security exposures, and whether alternative protein for food reduces them (SEC)

1. Vietnam's official food-security framing: Resolution 34/NQ-CP (2021) on national food security to 2030 and any successor; the 2050 agriculture strategy; how they define food security and whether protein, imports or "diversified food sources" appear. Also MAE statements in 2025 and 2026.
2. Concentration of origins and routes for the protein inputs and foods Vietnam imports (soy from Brazil, United States and Argentina; meat and dairy origins from L1 if available, otherwise list for L1); any shipping or chokepoint disruptions that hit Vietnam (2022, 2024 Red Sea, 2026 Middle East conflict as already noted in ch01 and ch20).
3. Climate exposure of domestic animal and aquatic protein for people: heat stress in pigs and poultry, Mekong salinity and aquaculture, wild-capture fisheries decline and fish for direct human consumption (check `ch20` and `app-f2` first).
4. Export restrictions and price shocks in protein foods and inputs (2007 to 2008, 2022), and Vietnamese consumer price effects for meat and fish.
5. The counter-hypothesis: alternative protein for food made from imported soy, pea or wheat gluten, or from imported equipment, strains and sugar, may only move the dependence. Quantify where possible using the study's own numbers (for example the about 54,000 t of plant proteins imported from China in 2025, ch16; domestic carbohydrate in ch04). Which alternative-protein routes use domestic inputs (cassava and sugar for fermentation, rice and mung bean protein, local soy) and which use imported ones?
6. How peer governments frame alternative protein inside food security: China (the "big food view" and the 2025 and 2026 No. 1 documents on new food resources such as microbial protein), Singapore (Food Story 2, dropping 30 by 30), Japan, Korea, the EU (2026 plan already cited as VIS-15), Gulf states. Check what is already cited (VIS, NTS, PRC prefixes) and only add what is new.

Out of scope: meat and dairy import volumes (L1); disease (L2); food balance sheets (L4).

### L4: Protein for people: food balance sheets and projections (FBS)

1. FAOSTAT Food Balance Sheets (new methodology, 2010 onwards, latest year available) for Viet Nam: protein supply in g per person per day by item group (cereals, pulses, soybeans, vegetables, meat by species, offal, fish and seafood, milk, eggs) and total; with the trend from 2010. Use the FAOSTAT API via curl (for example `https://fenixservices.fao.org/faostat/api/v1/en/data/FBS?area=237&element=...`; Viet Nam is area code 237) or the bulk download; save the raw response you rely on.
2. For each main protein food: production, imports, exports, domestic supply and the import-dependency ratio and self-sufficiency ratio (FAO definitions), latest year and trend. Which foods that people eat directly are import-dependent (wheat, dairy, soybeans for tofu and soy milk, beef)?
3. "Embedded" import dependence: combine with the study's established feed figures (about 99% of soy protein in feed imported, 74% of maize supply imported, ch01) to give a simple, labelled estimate of how much of the animal protein people eat rests on imported feed. Show the inputs and mark "(our calculation)". Keep it simple and transparent.
4. Projections of human protein consumption to 2035 and 2050: OECD-FAO Agricultural Outlook 2025 to 2034 for Viet Nam (meat, fish, dairy per person), FAO "The future of food and agriculture", IFPRI IMPACT or other published projections that cover Vietnam. Compare with the study's own balance model per-person meat demand (`data/balance_outputs.csv`, indicators `pc_*_demand_kg_cwe`). Never average disagreeing projections.
5. Nutrition context for protein security: the study says adults eat enough protein and children's stunting is 18% (2023). Check whether any new national nutrition survey data (2024 to 2026) changes this, and record protein quality issues (for example animal-source food access for poor or ethnic minority households).

Out of scope: detailed meat trade and subsidies (L1); disease (L2); policy framing (L3).

## Tools and budget

- WebSearch budget: about 30 calls per line. Prefer WebFetch on known URLs and public APIs.
- Public APIs via curl (UN Comtrade public preview API, FAOSTAT, World Bank, OECD data API, OpenAlex, Crossref) are allowed. Never put a personal identifier in a request.
- Tool calls: roughly 60 to 110 per line.

## Output

As in `working-papers/PROTOCOL.md` section 6. Extra files for this wave:

- L1: `data_meat_dairy_imports.csv` (year, product, hs_codes, quantity_t, value_usd, main_origins, share_of_consumption, source_ids, evidence_label, confidence, notes) and `data_origin_support.csv` (country, commodity, indicator, value, unit, year, source_ids, evidence_label, confidence, notes).
- L2: `data_disease_shocks.csv` (event, years, species, losses, price_effect, human_cases, source_ids, evidence_label, confidence, notes).
- L3: `data_security_exposures.csv` (exposure, protein_food_affected, evidence_of_exposure, does_alt_protein_for_food_reduce_it, inputs_domestic_or_imported, source_ids, evidence_label, confidence, notes).
- L4: `data_protein_supply_by_source.csv` (year, item_group, protein_g_per_person_day, share_of_total, source_ids, evidence_label, confidence, notes) and `data_self_sufficiency_by_food.csv` (year, food, production_kt, imports_kt, exports_kt, domestic_supply_kt, import_dependency_ratio, self_sufficiency_ratio, source_ids, evidence_label, confidence, notes).

Consolidation: a separate consolidating agent will fold the results into the study. Do not edit `content/`, `data/`, `charts/` or `sources/`. Do not commit; the consolidating agent commits.

## Wave-specific rules

- Test the hypothesis; do not argue for it. Say plainly when the evidence is weak, only general, or points the other way.
- For every exposure, state whether alternative protein **for human food** would reduce it, and by roughly how much at the scale the study's demand model gives (benchmark path about 19,000 t of protein a year by 2035; about 0.2% of meat protein displaced). Do not claim reductions that this scale cannot deliver.
- Feed is context only in version 0.8: do not propose feed-ingredient plays.
