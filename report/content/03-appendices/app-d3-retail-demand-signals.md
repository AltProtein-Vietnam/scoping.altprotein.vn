---
id: app-d3-retail-demand-signals
title: "D3. The retail audit re-read for demand"
short_title: "D3. Retail demand signals"
section: appendix
order: 43
summary: "What the September 2026 audit of 186 products in 11 stores says about demand: prices, the cost of a serving of protein, the range on the shelf and label claims. Mass stores carry almost no imported products. Twenty grams of protein from a vegetarian (chay) wrapper costs more than a whole street meal, and no chay food carries a protein claim."
audiences: [startups, manufacturers, research, investors, policy, international]
reading_time_min: 15
key_numbers: [kn-protein-cost-serving]
related_data: [retail_demand_signals.csv, retail_audit_skus.csv, protein_claim_eligibility.csv, marketplace_sku_counters.csv, kitchen_platform_counters.csv, plant_milk_sugar.csv]
related_pages: [app-s2-retail-audit, ch13-consumers, ch12-chay-baseline, ch15-channels, ch02-alt-protein-today, app-m3-demand-method]
charts: [chart-protein-cost-serving]
---
# D3. The retail audit re-read for demand

**What this appendix contains.** The September 2026 retail audit ([[app-s2-retail-audit]]) logged 186 products in 11 stores to study their recipes and ingredients. It covered Nha Trang (6 September) and Ho Chi Minh City (16 and 20 September). Here we re-read the same records for what they say about demand. Eight stores are mass modern retail (Lotte Mart, Co.opmart, GO!, WinMart, Emart) and three are premium or import-led (Annam Gourmet, Nam An Market, Moonmilk).

The audit is a convenience sample of modern and premium stores. It has no wet markets, *chay* shops (shops selling Vietnamese vegetarian food, made without meat, poultry or fish), online-only brands or foodservice. So these are signals about the shelf, not measures of the market [@FORM-01] {VN-direct|Medium} {dx:revealed}. Section D3.3 adds the first sales counters: 96 listings read on two online marketplaces, and 185 on a kitchen supply platform and two specialist shops.

Short forms: an SKU (stock-keeping unit) is one product in one pack size. TVP is textured vegetable protein: extruded plant protein with a meat-like texture, sold dry as granules, chunks or slices. A meat analogue is a plant product made to look and eat like meat.

## D3.1 Six signals

1. **Two shelves, two markets.** Imported finished products are 2.9% of the 140 products logged in mass stores and 67% of the 46 in premium stores. Imported frozen meat analogues appeared only in premium stores in Ho Chi Minh City; Nha Trang had none [@FORM-01] {VN-direct|Medium} {dx:revealed}. Modern plant-based products are an import-led premium niche. The mass shelf is Vietnamese chay, tofu and plant milk.
2. **Price points are low.** In mass stores the median pack costs VND 12,650 for tofu, VND 27,500 for plant milk, VND 45,500 for a frozen chay wrapper pack (dumplings, spring rolls or buns) and VND 71,500 for a frozen chay meat analogue. In premium stores the median is VND 179,000 for a frozen analogue pack and VND 94,900 for a plant milk [@FORM-01] {VN-direct|Medium} {dx:revealed}. For comparison, households spend on average about VND 43,700 per person per day on food and drink (VND 1,310,000 a month in 2024, our division) [@DIE-05] {VN-direct|Medium} {dx:inferred}.
3. **Twenty grams of protein costs more than a meal.** The median cost of 20 g of protein is about VND 13,000 from tofu or dried textured soy, VND 56,000 from a frozen meat analogue, VND 60,000 from a ready meal, VND 74,000 from a filled chay wrapper and VND 91,000 from plant milk (our calculation on label protein). From eggs or chicken it is VND 7,000 to 9,000 and from lean pork about VND 14,000 ([[ch11-protein-diet]]). A street rice plate with meat costs VND 29,000 to 35,000 in Ho Chi Minh City (2026) [@FORM-01; @CHY-40] {VN-direct|Medium} {dx:inferred}.
4. **Makers do not sell on protein, though much of the shelf could claim it.** Only two locally made products carry a protein claim in their name, both variants of Vinamilk's high-protein nut milk (5 g per 100 ml). No chay food does. The audit captured protein values for only 44% of mass-store products and 35% of premium-store products, so the gap is in capture as well as in labelling [@FORM-01] {VN-direct|Low} {dx:revealed}. Since 1 January 2026, protein has had to appear on the labels of pre-packaged foods that are not exempt (Circular 29/2023, now Circular 30/2026). So the gap is mostly in capture and in small makers, who are exempt [@LBL-01; @LBL-02] {VN-direct|High} {dx:revealed}. The national standard TCVN 14429:2025 sets the claim conditions: 5 g of protein per 100 g for a "source" claim and 10 g for a "high" claim. Of 43 audited plant-protein foods with a label value, 20 (47%) already meet "source" and 7 (16%) meet "high"; all seven are frozen analogues. Counting the per 100 kcal route, 27 of 38 and 13 of 38 do (our calculation; `protein_claim_eligibility.csv`) [@FORM-01; @LBL-03] {VN-direct|Medium} {dx:revealed}. A numeric protein claim is an open position on the chay shelf, not a regulatory problem.
5. **Chay on the pack is a religious and culinary word, not a vegan standard.** *Chay* appears in 87 of 186 product names. We checked the 64 chay-named products with a logged ingredient list. At least 23 (36%) name onion, garlic, shallot or leek, which strict Buddhist cooking avoids. At least 3 (5%) name egg or dairy in the ingredient list or on the label of a product with the same recipe (our keyword search and label check, a lower bound) [@FORM-01] {VN-direct|Medium} {dx:inferred}. Mass-market chay follows everyday lay practice. Strict buyers need labelled variants.
6. **Plant milk spans a four-fold price ladder.** Mass soy milk sells at about VND 22,900 per litre, below cow milk. Vinamilk's high-protein nut milk sells at about VND 87,000 per litre, and imported oat, almond and nut milks at a median VND 94,900 in premium stores [@FORM-01; @CON-35] {VN-direct|High} {dx:revealed}. Plant milk became Vietnam's modern plant-protein category at scale at the mass price point, not the premium one ([[ch13-consumers]]). The excise tax on sugary drinks may reach sweetened soy milk from 2027. If it does, mass soy milk would cost about VND 25,200 per litre in 2028, still below cow milk (our calculation) [@FORM-01; @FTR-01; @FTR-18; @CON-35] {VN-direct|Low} {dx:inferred}.

{{chart:chart-protein-cost-serving}}

## D3.2 The signals in figures

Generated from `retail_demand_signals.csv`. The n column is the number of products behind each value.

| Topic | Metric | Segment | Value | Unit | n | Notes | Source |
|---|---|---|---|---|---|---|---|
| assortment | SKUs logged | mass stores (8) | 140 | SKUs | 140 | Lotte Mart, Co.opmart, GO!, WinMart, Emart in Nha Trang and Ho Chi Minh City; convenience sample. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| assortment | SKUs logged | premium stores (3) | 46 | SKUs | 46 | Annam Gourmet, Nam An Market, Moonmilk; convenience sample. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| assortment | Share of SKUs that are imported finished products | mass stores | 2.9 | % | 140 | 4 of 140 SKUs; origin as logged; excludes one imported ingredient packed in Vietnam. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| assortment | Share of SKUs that are imported finished products | premium stores | 67.4 | % | 46 | 31 of 46 SKUs; origin as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | tofu; mass stores | 12650 | VND per pack | 8 | Range 9,900 to 19,500. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | plant milk; mass stores | 27500 | VND per pack | 31 | Range 3,700 to 133,500. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | plant milk; premium stores | 94900 | VND per pack | 14 | Range 14,000 to 158,900. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | plant yoghurt/creamer; mass stores | 38800 | VND per pack | 7 | Range 10,000 to 41,000. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | dumpling/spring roll/bun with vegetable filling; mass stores | 45500 | VND per pack | 39 | Range 27,900 to 65,000. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | dumpling/spring roll/bun with vegetable filling; premium stores | 85000 | VND per pack | 3 | Range 38,900 to 92,000. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | dried TVP/soy chunks; mass stores | 49000 | VND per pack | 5 | Range 49,000 to 75,000. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | ready meal; mass stores | 46400 | VND per pack | 6 | Range 25,000 to 72,900. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | canned analogue; mass stores | 57000 | VND per pack | 9 | Range 15,100 to 76,000. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | frozen meat/seafood analogue; mass stores | 71500 | VND per pack | 17 | Range 41,800 to 136,000. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | frozen meat/seafood analogue; premium stores | 179000 | VND per pack | 2 | Range 179,000 to 179,000. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | vegan cheese/spread; premium stores | 156600 | VND per pack | 9 | Range 89,900 to 249,900. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | protein powder; premium stores | 875900 | VND per pack | 4 | Range 309,900 to 1,439,900. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Median pack price | snack/jerky; premium stores | 32900 | VND per pack | 5 | Range 32,900 to 32,900. Shelf or online price as logged. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| protein cost | Median cost of 20 g of protein | tofu | 13300 | VND per 20 g protein | 5 | Our calculation: price per 100 g protein divided by 5; label protein. Range 7,834 to 24,211. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | plant milk | 91200 | VND per 20 g protein | 8 | Our calculation: price per 100 g protein divided by 5; label protein. Range 18,332 to 288,889. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | plant yoghurt/creamer | 105800 | VND per 20 g protein | 7 | Our calculation: price per 100 g protein divided by 5; label protein. Range 31,250 to 125,625. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | dumpling/spring roll/bun with vegetable filling | 73800 | VND per 20 g protein | 18 | Our calculation: price per 100 g protein divided by 5; label protein. Range 31,111 to 345,528. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | dried TVP/soy chunks | 12900 | VND per 20 g protein | 4 | Our calculation: price per 100 g protein divided by 5; label protein. Range 9,795 to 17,011. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | ready meal | 59500 | VND per 20 g protein | 3 | Our calculation: price per 100 g protein divided by 5; label protein. Range 58,095 to 76,667. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | canned analogue | 64200 | VND per 20 g protein | 2 | Our calculation: price per 100 g protein divided by 5; label protein. Range 44,741 to 83,700. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | frozen meat/seafood analogue | 55700 | VND per 20 g protein | 9 | Our calculation: price per 100 g protein divided by 5; label protein. Range 13,198 to 124,306. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | vegan cheese/spread | 175200 | VND per 20 g protein | 2 | Our calculation: price per 100 g protein divided by 5; label protein. Range 171,821 to 178,497. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| protein cost | Median cost of 20 g of protein | protein powder | 71900 | VND per 20 g protein | 4 | Our calculation: price per 100 g protein divided by 5; label protein. Range 68,606 to 73,127. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| label | SKUs with chay in the product name | all stores | 87 | SKUs | 186 | 47% of 186 SKUs. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| label | Chay-named SKUs whose ingredient list names an allium (onion, garlic, shallot, leek) | chay-named SKUs with an ingredient list | 35.9 | % | 64 | 23 of 64; our keyword search of the logged main ingredients, which may be incomplete, so this is a lower bound. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| label | Chay-named SKUs whose ingredient list or same-formulation label names egg or dairy | chay-named SKUs with an ingredient list | 4.7 | % | 64 | 3 of 64 (SKU-018 and SKU-100, same formulation, egg; SKU-103, dairy); lower bound. | [@FORM-01] {VN-direct\|Medium} {dx:inferred} |
| label | Share of SKUs with a protein value captured | mass stores | 44.3 | % | 140 | Protein value from label or collector lookup; a gap in capture, not only in labelling. | [@FORM-01] {VN-direct\|Low} {dx:revealed} |
| label | Share of SKUs with a protein value captured | premium stores | 34.8 | % | 46 | As above. | [@FORM-01] {VN-direct\|Low} {dx:revealed} |
| label | Locally made foods or drinks with a protein claim in the product name | all stores | 2 | SKUs | 186 | Only Vinamilk Sữa Hạt Cao Đạm (high-protein nut milk, 5 g per 100 ml), in two variants. No chay food carried a protein claim in its name. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Same-brand chay versus meat price difference, high-confidence pair | Vissan chả giò rế | -37.9 | % per 100 g | 1 | Chay cheaper than meat version; four other pairs rest on low-confidence reads (range -51.9% to +18.5%). | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| price point | Plant milk shelf price, mass soy milk (Fami) | mass stores | 22900 | VND per litre | 2 | Below cow milk (about VND 33,000 to 45,000 per bottle of OatSide's size in 2023, [@CON-35]). | [@FORM-01; @CON-35] {VN-direct\|High} {dx:revealed} |
| price point | Plant milk shelf price, imported oat, almond and nut milks | premium stores | 94900 | VND per litre | 13 | Range 58,000 to 158,900; median about two to three times cow milk ([@CON-35]). | [@FORM-01; @CON-35] {VN-direct\|High} {dx:revealed} |
| price point | High-protein nut milk (Vinamilk, 5 g protein per 100 ml) | mass stores | 87200 | VND per litre | 2 | The only mass-market plant product sold on protein content. One of the two prices is an online reference, not a shelf price. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| assortment | Imported frozen meat or seafood analogues logged | Nha Trang | 0 | SKUs | 84 | Imported frozen meat or seafood analogues; Nha Trang had none, Ho Chi Minh City had them only in premium stores. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |
| assortment | Imported frozen meat or seafood analogues logged | Ho Chi Minh City | 2 | SKUs | 102 | Imported frozen meat or seafood analogues; Nha Trang had none, Ho Chi Minh City had them only in premium stores. | [@FORM-01] {VN-direct\|Medium} {dx:revealed} |

Two rows of the table overstate what some buyers pay (these notes are not in `retail_demand_signals.csv`):

- **Dried textured soy (VND 12,900 per 20 g of protein, store packs).** The bulk format, not the product, makes dried textured soy the cheapest protein in Vietnam's retail data. Online, 1 kg bags of dry soy-and-gluten pieces cost VND 59,000 to 158,680 per kg. That is about VND 1,800 to 6,000 per 20 g of protein, using a protein range of 53.3 to 66.7 g per 100 g borrowed from other labels. A 150 g branded pack online costs VND 12,600 to 15,800 per 20 g, like the store median (our calculation) [@MKT-03; @FORM-01] {VN-direct|Low} {dx:inferred}.
- **Protein powder (VND 71,900 per 20 g, premium stores, n = 4).** The premium-store median overstates what gym users pay. At a sports-nutrition chain (WheyShop), whey costs VND 20,800 to 35,000 and plant powders VND 36,000 to 54,800 per 20 g of protein (5 products with protein facts). Plant powders are 2 of the 25 protein powders listed there [@ECR-08; @FORM-01] {VN-direct|Low} {dx:revealed}. On Lazada, seven plant powder listings show 7,294 sales against 5,455 for six whey listings. The top plant listing, a Vietnamese-made pea and nut powder, costs about VND 14,600 per 20 g of protein, below imported whey (our calculation, `marketplace_sku_counters.csv`) [@MKT-03; @MKT-04; @ECR-08] {VN-direct|Low} {dx:revealed}.

## D3.3 Sales counters online and in kitchens

Online shops in Vietnam show a *đã bán* (units sold) counter on each listing. The counters are cumulative with no start date, so they understate newer listings. Our rows come from the first page of targeted searches, so the sums show orders of magnitude, not market shares. In a logged-out browser, Lazada and Tiki show counters. Shopee needs a login and TikTok Shop a CAPTCHA (a test that blocks automated visitors). So those two, the largest platforms [@ECR-02], stay unread [@MKT-01; @MKT-02; @MKT-03; @MKT-05] {VN-direct|High} {dx:revealed}. The kitchen counters come from Kamereo, a business-to-business platform that supplies restaurants and cafés [@ECR-06] {VN-direct|Low} {dx:revealed}. Rows: `marketplace_sku_counters.csv` (96 listings, 25 September 2026) and `kitchen_platform_counters.csv` (185 listings, September 2026).

| Signal | Consumer marketplaces (Lazada, Tiki) | Kitchen platform (Kamereo) | Source |
|---|---|---|---|
| Plant milk against dairy | Best-selling plant milk SKU sells 60% (Lazada) and 79% (Tiki) of the litres of the best-selling dairy SKU | Plant milks about 4% of 899,000 milk litres and 1.5 to 2.1% of milk protein | [@MKT-03; @MKT-05; @ECR-06] {VN-direct\|Low} {dx:revealed} |
| Leading plant milk | Domestic nut milk (Lazada) and soy milk (Tiki); imported oat under 2% of plant-milk litres read | Imported Oatside oat milk, bought for coffee (36% of plant-milk litres) | [@MKT-03; @MKT-05; @ECR-06] {VN-direct\|Low} {dx:revealed} |
| High-protein nut milk (Vinamilk, 5 g per 100 ml) | About 16,100 cases (about 70,300 L, 3.5 t of protein) at Vinamilk's Lazada store; about 11% of its nut-milk litres read but 29% of their protein; 24% dearer per litre, about 37% of the cost per gram of protein | Not listed | [@MKT-03; @MKT-04] {VN-direct\|Low} {dx:revealed} |
| Protein-claimed soy milk (GoldSoy, 3.2 g per 100 ml) | 3,100 cases against 14,800 for an unclaimed walnut soy milk at 2.0 g in the same store, although GoldSoy is 39% cheaper per litre | 2,609 units against 5,758 and 5,828 for two dearer unclaimed soy milks | [@MKT-03; @ECR-06] {VN-direct\|Low} {dx:revealed} |
| Imported plant-based meat | None listed; searches for *thịt thực vật* (plant meat) and "meat zero" returned pork | Eight Meat Zero listings, 386 units (80 kg) in all, not orderable | [@MKT-03; @ECR-06; @AIS-25] {VN-direct\|Low} {dx:revealed} |
| Dry chay soy-and-gluten pieces | About 40,700 kg dry on Lazada, 82% from one small shop; official stores under 1% of these sales | 240 kg | [@MKT-03; @MKT-04; @ECR-06] {VN-direct\|Low} {dx:revealed} |
| Frozen chay and chay *giò* (meat-style loaf) | Up to about 1,100 kg per listing; one chay *giò lụa* 11 packs; no chay listing carries a numeric protein claim | Vissan chay spring roll 0 units | [@MKT-03; @ECR-06] {VN-direct\|Low} {dx:revealed} |
| Fresh tofu | Not a marketplace product | About 80,800 kg across 32 listings | [@MKT-03; @MKT-05; @ECR-06] {VN-direct\|Low} {dx:revealed} |
| Who sells | Official or LazMall stores take 93 to 100% of milk units read but under 1% of dry chay piece sales | Platform-run | [@MKT-03; @MKT-05] {VN-direct\|Low} {dx:revealed} |

**What this means (our inference)** {VN-direct|Low} {dx:inferred}:

- Plant milk is a mainstream household purchase online, sold through the official stores of established brands.
- Protein sells in that aisle only as a premium niche inside an established brand's range. A protein claim alone did not lift soy milk in either channel.
- The chay product households buy online in bulk is the dry textured piece. It is an ingredient-like product made by small shops, so it fits an ingredient route better than a branded analogue.

A second read of the same listings a month later would turn the counters into monthly rates ([[ch13-consumers]], [[ch15-channels]]).

## D3.4 What a second audit round should add

The first round left gaps in where, when and what it measured. A second round should add:

- Wet markets, dedicated chay shops and pagoda-adjacent stalls, where most chay is bought.
- Meat equivalents with label protein for every chay product logged, so that price per gram of protein can be compared pair by pair.
- A repeat visit before and during the seventh lunar month (the month of the Vu Lan festival), to measure the seasonal rise in chay sales on the shelf.
- Da Nang and Hanoi, to test the north and south difference in tofu and chay reported in [[ch11-protein-diet]] and [[ch12-chay-baseline]].
- Online small makers. Lazada and Tiki can be read in a logged-out browser (section D3.3), which partly closes the small-maker gap for dry chay goods on Lazada. Shopee needs a login and TikTok Shop a CAPTCHA, so reading them needs a person with an account or a paid report. A repeat read of the same listings is needed to turn counters into rates [@MKT-01; @MKT-02; @MKT-03; @MKT-05] {VN-direct|High} {dx:revealed}.
- The makers behind the online dry chay pieces, a named group of buyers for a domestic textured protein. The one product page we opened names no maker, and one listing name says its soy is imported and non-GM (not genetically modified) [@MKT-04] {VN-direct|Low} {dx:revealed}.

**Related:** [[app-s2-retail-audit]], [[ch13-consumers]], [[ch12-chay-baseline]].
