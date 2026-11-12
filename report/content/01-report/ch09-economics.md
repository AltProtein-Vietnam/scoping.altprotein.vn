---
id: ch09-economics
title: "Economics: what it costs and what it must beat"
short_title: "Economics"
section: report
part: "II. Supply: what Vietnam can make"
order: 9
summary: "In fermentation, capital decides cost, and fungal protein made in Vietnam is a premium ingredient, not a bulk one. Textured soy is cheap to make, but duty-free Chinese imports mean the price of food-grade soy flour decides whether a domestic line pays."
audiences: [investors, startups, manufacturers, policy, research]
reading_time_min: 10
key_numbers: [kn-power-blended, kn-min-wage-2026, kn-grid-emission-factor, kn-tvp-cost, kn-retail-protein-floor, kn-cooling-penalty, kn-tvp-line-capex, kn-t1-flour-breakeven]
related_data: [cost_inputs.csv, commodity_prices.csv, tea_benchmarks.csv, ingredient_prices.csv, t1_cost_per_kg.csv, t1_equipment_listings.csv, t1_landed_competitor.csv, t1_margin_payback.csv, inactive_yeast_trade.csv, tariffs.csv]
related_pages: [app-s12-costs, ch16-business-buyers, ch11-protein-diet, ch04-asset-map, ch10-technology-fit, ch26-plays, app-s6-feed-market]
charts: [chart-cost-stack-fungal, chart-capex-per-tonne, chart-retail-price-per-protein]
---

# 9. Economics: what it costs and what it must beat

**In brief.**

- **Capital matters more than cheap inputs.** Power, labour and factory space are cheap in Vietnam. But in fermentation, capital and maintenance are 54% to 67% of cost.
- **Fungal protein is a premium ingredient, not a bulk one.** It would cost USD 4.05 to 14.7 per kg of protein to make in Vietnam. That is more than imported plant proteins (USD 1.7 to 2.4), but overlaps egg and dairy proteins (USD 7 to 11). So it can compete where it does a job, such as binding or texture.
- **Textured soy is cheap to make**, at a small fraction of the retail price of meat protein.
- **Soy flour decides whether a domestic line pays.** Chinese textured soy enters duty-free at USD 1.29 to 1.38 per kg, inside the domestic cost range. Flour is 63% to 85% of cost, so its delivered price decides the margin.

> **Read with care.** The cost estimates in this chapter combine sourced Vietnamese prices with stated engineering assumptions. They show orders of magnitude and which costs matter. They are not feasibility studies.

---

## 9.1 Input costs: cheap power, labour and land

| Input | Value (2026) | Sources |
|---|---|---|
| Electricity for a plant running around the clock | USD 0.073 to 0.081 per kWh (our calculation) | [@COST-01; @COST-03] {VN-direct\|High} |
| Grid emissions | 0.66 t CO2 per MWh | [@COST-08; @COST-09] {VN-direct\|High} |
| Minimum wage, highest region | About USD 204 a month | [@COST-19; @COST-20] {VN-direct\|High} |
| Ready-built factory | About USD 5 per m² a month | [@COST-21; @COST-22] {VN-direct\|Medium} |
| Industrial water (Ho Chi Minh City) | About USD 0.64 per m³ | [@COST-10; @COST-13; @COST-14] {VN-direct\|Medium} |
| Urea (nitrogen) | About USD 425 per t | [@COST-30; @COST-33] {VN-direct\|Medium} |
| Cassava starch | USD 520 to 540 per t at the port (April 2026), up from 405 to 415 in January | [@FS-01; @FS-11; @FS-12] {VN-direct\|Medium} |
| Sugar | About VND 16,500 per kg, a three-year low | [@FS-31; @FS-33] {VN-direct\|Medium} |

**Power rules add some risk.** The utility can now raise prices by up to 5% after review, and large users face a new capacity charge from 2026 [@COST-04; @COST-05; @COST-06] {VN-direct|Medium}. Buying renewable power directly is allowed, but the savings are unproven [@COST-06; @COST-07] {VN-direct|Low}.

**Tax favours food plants over feed plants.** Animal feed is outside value added tax (VAT), so a feed-protein plant cannot reclaim the VAT on its inputs; a food-ingredient plant can [@COST-24] {VN-direct|High}. We estimate this adds 5% to 10% to a feed plant's taxed inputs {VN-direct|Low}.

## 9.2 Fermentation: capital is most of the cost

**Published cost models** give a range [@COST-43; @COST-44; @COST-45; @COST-46; @COST-47] {general|Medium}:

| Technology | Cost | Plant capital cost | Study |
|---|---|---|---|
| Mycoprotein (fungal protein for food) | USD 29.6 per kg of protein | About USD 108 M | Risner et al. 2023 |
| Bacterial protein from factory off-gas (feed) | USD 4.15 per kg | USD 320 M for 20 kt a year | Vlaeminck et al. 2023 |
| Microbial protein with renewable power | EUR 5.5 to 6.1 per kg of protein (2028) | n/a | Fasihi et al. 2025 |
| Cultivated meat | USD 37 to 51 per kg of wet cells | USD 663 M for 6.9 kt a year | Humbird 2021 |

**Capital cost varies widely.** Per tonne of yearly capacity, it is USD 16,000 to 23,000 for microbial protein and USD 48,000 to 96,000 for cultivated meat (our calculation) [@COST-43; @COST-44; @COST-47] {general|High}. Design and hygiene grade explain the spread, so a Vietnamese plan needs its own equipment-level estimate.

{{chart:chart-capex-per-tonne}}

**Cooling in the tropics adds a little.** Fermentation gives off heat, and warm cooling water in southern Vietnam means more chilling. We estimate this adds 2% to 4% to the cost of fungal protein. Strains that grow at 40 to 45 °C avoid most of it [@COST-50; @COST-51] {general|Low}.

### Cost stack A: fungal biomass protein, 10,000 t a year

This estimate is for dried fungal biomass, 45% to 55% protein, grown on sugar.

| Cost line | USD per t of product (low to high) | Basis |
|---|---|---|
| Carbon (sugar) | 600 to 1,100 | Assumed USD 300 to 500 per t |
| Nitrogen (urea) | 72 to 145 | [@COST-30; @COST-33] |
| Other nutrients | 50 to 150 | Assumption |
| Electricity, including cooling | 65 to 234 | [@COST-01] |
| Steam | 78 to 218 | [@COST-16; @COST-17] |
| Water and wastewater | 18 to 58 | [@COST-10; @COST-13; @COST-14] |
| Labour (60 to 100 staff) | 44 to 124 | [@COST-19; @COST-20] |
| Land | 99 to 185 | [@COST-21] |
| Capital charge | 960 to 3,600 | Below published benchmarks, allowing for a cheaper local build |
| Maintenance and insurance | 240 to 800 | Assumption |
| **Total per t of product** | **2,227 to 6,612** | |
| **Total per t of protein** | **4,050 to 14,700** | |

Source: our calculation from sourced prices and stated assumptions [@COST-01; @COST-19; @COST-21; @COST-33; @COST-43; @COST-44; @COST-47] {VN-direct\|Low}.

{{chart:chart-cost-stack-fungal}}

**Reading.** Capital and maintenance are 54% to 67% of cost. Labour and power together are under 10%. Two lines matter most:
- **Carbon.** At 2026 cassava starch prices, carbon sits at the top of the range. Cassava pulp is near-free but needs treatment first ([[ch04-asset-map]]). Domestic sugar is a clean alternative in surplus years.
- **Capital.** This line decides the case. Tolling, which means renting time on someone else's fermenter, is the main way to avoid it ([[ch05-industrial-base]]).

## 9.3 The prices to beat in food: fungal biomass is a premium ingredient

| Comparator | USD per kg of protein | Sources |
|---|---|---|
| Textured soy made in Vietnam (cost stack B) | about 1.5 to 3.0 | Section 9.4 {VN-direct\|Low} |
| Imported wheat gluten, textured soy and soy isolate, 2025 | about 1.7 to 2.4 | [@BUY-02; @BUY-07] {VN-direct\|Medium} |
| Chinese textured protein, landed duty-free, 2025 | about 2.0 to 2.1 | [@TIC-12; @FTR-32] {VN-direct\|Low} |
| **Fungal protein made in Vietnam (cost stack A)** | **4.05 to 14.7** | Section 9.2 {VN-direct\|Low} |
| Imported egg, dairy and premium plant proteins, 2025 | about 7 to 11, and more | [@BUY-02; @BUY-09] {VN-direct\|Medium} |
| Mycoprotein in a published US plant model | 29.6 | [@COST-43] {general\|High} |
| For scale: eggs and chicken breast in shops, 2026 | about 13 to 18 | [@COST-40; @COST-41] {VN-direct\|Medium} |

**Reading.** Fungal protein costs more than any commodity plant protein. It overlaps egg and dairy proteins, so it can compete only where it does their job, binding, texture or flavour, and is priced against them ([[ch16-business-buyers]]) [@BUY-02; @TIC-12] {VN-direct|Low}:
- **As a binder** in 1% to 3% of a recipe, it could fetch about USD 3.3 to 4.6 per kg, if it works as well as egg white or milk protein. The low end of cost stack A fits.
- **As a meat extender**, it would have to match hydrated soy, about USD 0.7 to 1.2 per kg. None of the range reaches that.

**Food grade costs more.** Cost stack A was built for a feed ingredient. A food ingredient needs an extra processing step and higher hygiene, so it would sit at the top of the range or above (our inference) {VN-direct|Low}.

**Imported microbial ingredients arrive duty-free.** Vietnam imported about 9,200 t of inactive yeast and similar products in 2025, mostly at about USD 1.1 per kg [@FBA-17; @FTR-32] {VN-direct|Medium}. A Vietnamese fungal or yeast ingredient meets that competition first.

**Feed, for context.** On a protein basis, fishmeal cost USD 2,625 to 3,846 per tonne and soybean meal about USD 880 (our calculation) [@FM-01; @FM-02] {general|High}. Fungal protein costs more than either, so it is not a bulk feed protein.

## 9.4 Plant-based food: factory cost is not the problem

### Cost stack B: textured soy protein on a Chinese-equipped line

| Line size and use | Output, t a year | Full cost, USD per t | VND per 100 g of protein |
|---|---|---|---|
| 0.5 t an hour, half the time | 2,000 | 858 to 1,573 | 4,290 to 7,860 |
| 1 t an hour, 90% of the time | 7,200 | 761 to 1,294 | 3,800 to 6,470 |
| Of which food-grade soy flour (USD 627 to 925 per t delivered) | | 63% to 85% of cost | |
| Of which equipment | | 5 to 91 | |

Source: our calculation [@TIC-12; @TIC-13; @COST-01; @COST-16; @COST-17; @COST-19; @COST-20; @COST-21; @TIC-02; @TIC-03; @TIC-07] {VN-direct\|Low}. Full cost includes utilities, labour, rent, quality checks, delivery, maintenance and finance, but not VAT or profit.

**Equipment is cheap; flour and working capital are not.** Chinese makers list complete lines at USD 11,000 to 100,000, and a Ho Chi Minh City dealer sells them [@TIC-02; @TIC-03; @TIC-07; @FORM-34] {general|Low}. Installed in a rented factory, a line costs about USD 0.28 to 1.38 million. Working capital, at USD 0.6 to 3.5 million, is the larger need (our calculation) {VN-direct|Low}.

{{kn:kn-tvp-line-capex}}

**Shop prices to beat.** Per 100 g of protein in September 2026, eggs cost VND 34,000 to 40,000, chicken breast 39,500 to 45,500 and lean pork about 70,900. Tofu cost 39,000 to 121,000, and an imported plant-based burger about 542,000 [@COST-39; @COST-40; @COST-41; @COST-42; @FORM-01] {VN-direct|Medium}.

{{chart:chart-retail-price-per-protein}}

**Reading.** Textured soy costs one-eighteenth to one-quarter of the shop price of meat and egg protein to make (our calculation). Distribution, brand, shop margins and product quality take the gap.

**Flour decides the margin against imports.** In 2025 China shipped textured protein to Vietnam at USD 1.24 per kg, its lowest price to any partner. It lands at about USD 1.29 to 1.38 per kg, duty-free [@TIC-12; @TIC-14; @FTR-32] {VN-direct|Medium}. That sits inside the domestic cost range (USD 0.76 to 1.57 per kg).

The flour comes from the same countries that export the finished product, and Vietnam makes no food-grade soy flour [@FORM-10] {VN-direct|Medium}. So a domestic line's only natural shelter is the freight on the finished product, about USD 50 to 140 per t (our calculation) {VN-direct|Low}. To earn a 15% margin against Chinese prices, a line needs food-grade flour below about USD 700 to 940 per t. Observed flour prices, USD 627 to 925, straddle that line [@TIC-12; @TIC-13] {VN-direct|Low}.

{{kn:kn-t1-flour-breakeven}}

Chinese lines are on sale in Vietnam, yet nobody has installed one for food. That suggests cheap food-grade flour does not reach Vietnam (our inference). A domestic plant competes on freshness, local recipes and supply security. It suits a *chay* (vegetarian food) maker, co-packer or distributor financed with debt, more than a venture-backed startup ([[ch26-plays]] play T1; [[ch25-demand-to-frontier]]).

**Chicken and eggs set the floor.** Any mass-market plant-based product is priced against them, at VND 34,000 to 45,000 per 100 g of protein ([[ch11-protein-diet]]) [@COST-40; @COST-41] {VN-direct|Medium}.

## 9.5 Precision fermentation and cultivated meat: no near-term production case

- **Precision fermentation.** We could not verify a peer-reviewed cost model for food proteins. In the regional model, feedstock was the largest cost and labour only 4% [@RGN-01] {general|High}. For Vietnam, this favours high-value, low-dose products made under contract, not bulk dairy proteins ([[ch10-technology-fit]]).
- **Cultivated meat.** The published model gives USD 37 to 51 per kg of cells at the factory [@COST-47] {general|High}. That is 7 to 15 times the shop price of lean pork or chicken breast in Vietnam (our calculation from [@COST-39; @COST-40]) {VN-direct|Medium}. On the author's own estimate of shelf price, the gap is 15 to 29 times {VN-direct|Low}. Only an input that does not yet exist would bring it under his test of an affordable food [@COST-47] {general|High}. So there is no near-term production case for Vietnam. The case is for research and regulatory readiness ([[ch26-plays]] play T8).

## 9.6 What policy can change in the numbers

The regional study modelled incentives for typical plants. A 50% capital grant raised project value the most. Cheaper feedstock and a loan guarantee came next. Tax holidays ranked fourth of six [@RGN-01] {general|High}. In Vietnam's case, that points to:
- **Capital:** shared or tolled tanks, capital grants and loan guarantees rather than more tax holidays ([[ch27-policy-options]]).
- **Feedstock:** steady access to cassava glucose or domestic sugar of fermentation grade.
- **Time:** every month waiting for food approval is paid for in capital cost ([[ch07-rules]]).

## 9.7 What this means

- **Investors:** for fermentation, model capital charges, not operating costs. For textured soy, ask for a delivered flour quote before an equipment plan. Test any fermentation pitch against the protein it has to beat, and treat a capital cost below USD 6,000 per tonne of yearly capacity as a claim needing evidence.
- **Startups:** sell function, not tonnage. Choose heat-tolerant strains or plan for cooling from day one. Start in a ready-built factory.
- **Manufacturers:** you can make textured protein cheaply; demand and quality are the limits. A line beats duty-free Chinese imports only with food-grade flour below about USD 700 to 940 per t.
- **Policy makers:** the cheapest levers are capital sharing, such as a public pilot line, and early signals on the power capacity charge.
- **Researchers:** two cheap public goods are missing: an open fermentation cost model with Vietnamese inputs, and a public price series for food protein ingredients (public good P6, [[ch26-plays]]). A global dataset of published cost models already exists to build on [@SLF-10] {general|Medium}.

**Related:** [[ch16-business-buyers]] (the ingredient price ladder), [[ch10-technology-fit]].
