# Editor log E01-front: front pages (version 0.8)

Editor: E01-front. Date: 2026-10-01. Files edited: `content/00-front/front-cover.md`, `front-two-minute.md`, `front-exec-summary.md`, `front-at-a-glance.md`, `front-how-to-read.md`, `front-faq.md`. No other content, data, tile or chart files edited. "Version 0.7", the draft notices and "not for citation" are unchanged (one stale "0.6" fixed, see below).

Checks: `python3 tools/validate.py` reports 0 errors (2 warnings, `kn-no-regret-plays` and `chart-play-robustness`, not in my files). No em or en dashes (checked with Python for U+2013 and U+2014). The front pages carry no citation or tag tokens except the two examples in front-how-to-read (`[@MAC-04]`, `{VN-direct|High}`), which are unchanged. A script compared every number with the version 0.7 text (commit 97231c9): every added number comes from the editorial brief section 6 or from a chapter (ch09: 54 to 67%; ch21: USD 3.3 to 6.5 per kg in 2050 and the food window from about 2028). No page links to an anchor in these pages, so heading changes are safe.

Coordinator corrections applied: "three lead under almost every weighting" (not "every"); milk dropped from "Most of that meat, and the eggs and farmed fish, is produced in Vietnam on imported feed". The 90% meat and 30% milk self-sufficiency figures were not added (wave 11 findings, no existing page to cite).

Note: commits 7fbb7e1 and 43f2be7 picked up part of my edits while I was still working. The files on disk are the final state.

## Tiles and charts

Removed (embeds and frontmatter entries):

| Page | Removed | Why |
|---|---|---|
| front-cover | `kn-fishmeal-aug-2026`, `kn-sbm-need-2050` | Feed tiles; the cover now leads with protein for people |
| front-exec-summary (frontmatter only; no embeds) | `kn-fishmeal-aug-2026`, `kn-cost-fungal-feed`, `kn-fishmeal-protein-price`, `kn-efficiency-vs-alt`, `kn-vision-sbm-2050`, `kn-vision-microbial-share-2050` | Feed tiles; vision tiles retired by the brief |
| front-at-a-glance | `kn-fishmeal-aug-2026`, `kn-feed-target-livestock-2030`, `kn-feed-mills`, `kn-cost-fungal-feed`, `kn-fishmeal-protein-price`, `kn-sbm-range-2050`, `kn-efficiency-vs-alt`, `kn-vision-sbm-2050` | Feed tiles |
| front-at-a-glance | `chart-price-to-beat` | "The price to beat in feed" |
| front-at-a-glance | `chart-plays-scoring` | Titled "Ten plays" and drawn from all rows of `plays.csv`, so it would show retired T2, T3 and T6. Re-add once the chart shows only the seven active plays. |

Added (existing ids only; no new tile ids). The `pages` field in `key-numbers.json` and the `placement` field in `chart-specs.json` need updating by the consolidating editor:

| Page | Added | Why |
|---|---|---|
| front-cover | `kn-meat-intake-2020`, `kn-demand-bench-2035` | Replace the two feed tiles with people-side tiles |
| front-exec-summary (frontmatter) | `kn-meat-intake-2020` | The opening now leads with meat intake |
| front-at-a-glance | `kn-animal-protein-share`, `kn-t1-flour-breakeven`, `kn-top-play-balanced`, `kn-funder-fit` (was embedded but missing from frontmatter) | Food-side replacements for removed feed tiles and the plays chart |
| front-at-a-glance | `chart-ingredient-price-ladder` | Food price to beat, replacing the feed price-to-beat chart |

## front-cover

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary now "what alternative protein Vietnam could make for people to eat ... with feed only as context". Key numbers changed as above. | reframed for food |
| Opening | Leads with "Protein for people first; feed only as context." The sentence "Vietnam turns imported plant protein into pork, poultry, eggs, fish and shrimp at a scale few countries match" replaced by "Vietnamese people eat more meat each year, and most of it is raised in Vietnam on imported feed". "It covers food and feed" removed; new sentence that feed is the hidden import behind the meat, eggs, milk and farmed fish people eat. | reframed for food |
| Start here | "ten plays" to "seven plays"; summary reading time 15 to 12 minutes. | reframed for food |
| What is inside | Part II "for people to eat"; Part IV "the protein people will eat and the imports behind it" (matches new ch22 title); Part V "robust moves" to "moves that pay off in any 2050" (ch28 title). | retitled |
| Data paragraph and footer | Sentences split. Footer scope "food and feed" to "protein for people first and feed only as context". | reframed for food |

## front-two-minute

| Section | Change | Type |
|---|---|---|
| Opening | New scope line. | reframed for food |
| Why Vietnam | Leads with meat intake (136.4 g against 50 to 80 g); feed import shown as the hidden import behind meat, eggs and farmed fish; African swine fever added from the shared wording. "Food and feed security" to "the security of that supply". | reframed for food |
| What it could make first | Removed "functional microbial feed ingredients for shrimp and pangasius" (T2). Now T1, T4, T5 as bullets, then T9 and T10. | pruned feed |
| What to do first | Removed "fix the two feed lists" and "public feed trials"; added the novel-food procedure in the decree; pilot line is now food-grade. Firms: "test feed ingredients head to head against the yeast mills already buy" replaced by "test extenders against the soy recipe buyers already use". | pruned feed |
| By 2050 | Leads with meat protein people eat (1.01 Mt in 2025 to 1.45 Mt in 2050); soybean meal as the import behind it. Removed "Better feed efficiency cuts that about twice as much as alternative protein". "Nine" to "seven" no-regret moves. | reframed for food |
| Whole page | Sentences split; glosses for chay, hub, tolling, GMO, precision fermentation, extenders. | clear language only |

## front-exec-summary

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary rewritten: security of the protein people eat; openings T1, T4, T5 (T2 removed). Reading time 15 to 12. Tiles as above. | reframed for food |
| Opening | New scope paragraph (brief section 1): feed only as context; earlier feed assessments stay in S6, F6 and M5. Removed "It covers food and feed". | reframed for food |
| Why Vietnam | Rebuilt on the shared paragraph: meat intake, 42% animal share, imported feed behind meat, eggs and farmed fish, ASF. Removed USD 11.3 billion seafood exports and "In August 2026 fishmeal reached USD 2,500 a tonne". | pruned feed |
| Finding 1 | Removed "The most advanced alternative-protein market is feed: an insect-meal plant ... Chinese microbial protein is already imported". | pruned feed |
| Finding 4 | Removed "Feed mills (269, about half used) ... are ready partners"; frozen-food co-packers kept. | pruned feed |
| Finding 5 | Removed "aquafeed trials" from Vietnam's research strengths and the research-intensity ratio (detail). | pruned feed |
| Finding 6 | Removed "Feed is more open: insects, duckweed, algae and yeasts are already on the livestock feed list, though the aquafeed list is unclear". | pruned feed |
| Finding 7 | Entobel kept as the one large deal and as a deal structure, but stated plainly as an insect-feed deal outside the study's scope. | reframed for food |
| Finding 8 | Removed the comparison with fishmeal protein (USD 2,625 to 3,846) and soybean meal (USD 880) and "marginal as bulk fishmeal replacement, plausible as a functional aquafeed ingredient at 1 to 5% of the diet". Now "fungal biomass protein" with the capital share (54 to 67%, ch09) and the new ch09 food comparator wording. | pruned feed |
| Finding 9 | "Two technology families fit now" (including functional microbial feed ingredients) to "One technology family fits now: textured plant protein for food". Duckweed feed removed from "worth proving". | pruned feed |
| Demand 8 | Removed "a feed pull", the aquafeed-standards sentence (BAP) and the 9,200 t inactive-yeast import. | pruned feed |
| Demand 1 to 9 | Shortened; detail cut where the chapters hold it (lean pork VND 71,000, the 31% processor share, the 84% non-GM premium, Decision 3958, HS 3504, Vinamilk pea protein, US 12.5% tariff, USD 128 million dumplings, seventh-lunar-month sales). | clear language only |
| Futures 1 | "more imported protein and more compound feed" to "more imported protein". Smallholder pig farms detail cut. | reframed for food |
| Futures 2 and 3 | Lead with meat protein people eat; soybean meal as the import behind it; food route saves most imports per tonne (4.5 t soybean meal and 9.5 t maize per t of meat protein, our calculation); 0.4% displaced in 2050. "Efficiency does twice the work of alternative protein" headline removed; kept as one context sentence (brief 2.4). Omega-3 sentence removed. Farmland abroad detail cut. | reframed for food |
| Futures 4 | Fishmeal and soybean-meal price comparators and the feed window (2040 to 2045) removed; replaced by the 2050 cost (USD 3.3 to 6.5 per kg) and the earlier food window (about 2028), both from ch21. | reframed for food |
| Futures 5 | Axis renamed "stress on imported protein" (feed behind domestic meat and imported protein foods). | reframed for food |
| Vision callout | Replaced the soybean-meal, microbial feed-share and omega-3 goals with the new vision (shared wording): measured, more diverse, more secure; 67,000 to 172,000 t of protein a year, 59,000 to 147,000 t made in Vietnam. | reframed for food |
| What to do | "Ten plays; three lead" to "Seven plays; three lead under almost every weighting" (T1, T4, T5); T2 bullet removed; one sentence that earlier feed plays are retired; four public goods. | pruned feed |
| Policy | "Four highest-ranked" to "three highest-ranked"; aquafeed-list and livestock-list items removed; novel-food procedure in the decree added; "public feed trials" removed from the larger outlays. Ranks 1 and 2 cost little and rank 3 takes more drafting, matching ch27. | pruned feed |
| Product targets | "Eleven" to "ten" target product profiles and "twenty-one" to "twenty" demand moves (TPP-11 and DMV-12 retired; ch25 uses the same counts). | pruned feed |
| No-regret moves | "Nine" to "seven", listed as in the brief; feed-efficiency programme, new-feed route, trial capacity and omega-3 plan removed. | pruned feed |
| Checked against the actors | Shortened; detail cut where ch29 holds it. | clear language only |
| For each reader | Investors: "back B2B feed and ingredient revenue ... on the Entobel template" removed. Policy: "two feed-list fixes" removed. Startups: "listed feed materials" removed. Manufacturers: "functional feed additives" removed. Research: "soy-wastewater protein in shrimp" removed. International: "public feed trials" removed. Other detail shortened. | pruned feed |
| What would change our view | Removed "Fishmeal falls back below about USD 1,800 a tonne". "Chinese microbial protein" to "microbial food protein". Tolling item rewritten for food (T5 and the food-fermentation plays, instead of T2, T3 and T5). | pruned feed |
| Whole page | Prose about 2,870 words against 3,440 in version 0.7. Sentences split; glosses for GMO, precision fermentation, koji, mycoprotein, co-packers, offtake, okara, MtCO2e, tolling, hub, *tương*. | clear language only |

## front-at-a-glance

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary refocused; reading time 3 to 4; tiles and charts as above. | reframed for food |
| Intro and first section | "The protein gap" retitled "The protein people eat rests on imported feed"; new two-line intro; meat intake and animal-protein share lead. | retitled |
| Raw materials, money | Feed-mills tile removed; one line that Entobel is an insect-feed deal outside the scope. | pruned feed |
| Costs and prices to beat | Feed costs and fishmeal price removed; soy-flour break-even and the food ingredient price ladder added; one-line intro from ch09. | pruned feed |
| Who would buy it | Meat-intake tile moved to the first section; sub-heading "What Vietnam pays for protein". UHT and IFS or BRCGS explained. | clear language only |
| Futures | New lead paragraph on meat protein people eat and the import saving per tonne. World table column "Imports" to "Imported protein"; last column "What Vietnam does best" to "What it means for protein made in Vietnam", rewritten from the revised ch23 (functional aquafeed, residue-based feed protein, protein from power and non-traded local feeds removed). Seven no-regret moves sentence; vision line from the shared wording. | reframed for food |
| What to do | Seven plays line. Table: T2, T3, T6, aquafeed and livestock feed-list fixes and public feed trials removed; shared food-grade pilot line added to public steps. | pruned feed |

## front-how-to-read

| Section | Change | Type |
|---|---|---|
| What it covers | Retitled "What it covers: protein for people"; new scope paragraph; "Food and feed" bullet became "Technologies" and a new "Feed is context only" bullet (brief section 1); insects as incumbent and benchmark; motivation led by the security of the protein people eat. | reframed for food |
| Organisation table | Part IV "the protein people will eat and the imports behind it"; Part V "moves that pay off in any 2050". | retitled |
| Codes table | T codes: seven plays, T2, T3, T6 retired in version 0.8. P codes: four public goods, P2 and P3 retired. PO: 19 ranked, five feed options retired. TPP-11 and DMV-12 retired. RM: "Moves that pay off in any 2050", 16 active, five feed moves retired. Worlds A to D: the two axes named, with "stress on imported protein". AQ codes marked "feed context". T4 hub and T5 tolling explained. | pruned feed |
| Tags | Long sentences split; "key numbers" to "stat tiles". | clear language only |
| Corrections and versions | "This is draft version 0.6; versions 0.1 to 0.5 were earlier drafts" corrected to "0.7" and "0.1 to 0.6" to match the draft notice. | clear language only |

## front-faq

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary mentions the scope; related pages add ch01 and ch28. | reframed for food |
| What is this report | "for food and animal feed" to "for people to eat"; feed as context. | reframed for food |
| Who is it for | "food and feed manufacturers" to "food manufacturers". | reframed for food |
| What is alternative protein | Definition no longer says "for food or feed"; adds "This study looks at alternative protein for people to eat". | reframed for food |
| Fake meat | Removed "and in feed for fish, shrimp and livestock". | pruned feed |
| Insects | Reworded: incumbent and benchmark; feed is context only. | reframed for food |
| New Q and A | "Why does the study no longer recommend feed ingredients?" answered from brief section 1. No new facts. | reframed for food |
| Why Vietnam | Now leads with the protein people eat, imported feed behind it and ASF; "food and feed security" to "food security". | reframed for food |
| Best opportunity | T2 replaced by T5; seven plays, three lead under almost every weighting; T1 and T4 first or second under every weighting. | pruned feed |
| Government first | Four steps to three (feed lists removed; novel-food procedure added); "public feed trials" removed from outlays; "need no new agency", first two cheap (ch27). | pruned feed |
| Money | Entobel stated as a feed deal outside the scope. | reframed for food |
| 2050 | Leads with meat protein people eat; "better feed efficiency would cut that about twice as much" removed; nine to seven moves. | reframed for food |
| What would change | Fishmeal example replaced by tolling (from the summary list). | pruned feed |
| Where to start; earlier drafts | Summary 15 to 12 minutes. "This version reorders the report and changes no finding" (no longer true) replaced by a line on the scope change. | reframed for food |

## Unsure or for the consolidating editor

1. **`kn-no-regret-moves` shows "9 of 21 moves"**. I kept it on front-at-a-glance and in the summary frontmatter because the text now says seven; the tile value needs changing to 7 of 21. `kn-plays-count` ("10 plays and 6 public goods") is not on my pages but is stale too.
2. **`chart-scenarios-2050`** is kept on front-at-a-glance. Its subtitle still says "feed-protein import stress"; it should read "stress on imported protein".
3. **`chart-plays-scoring`** was removed from front-at-a-glance because it shows ten plays. Re-add it if the chart is filtered to the seven active plays.
4. **The `pages` and `placement` fields** in `key-numbers.json` and `chart-specs.json` need updating for the tiles and chart I added or removed (tables above).
5. **Version text in front-how-to-read.** I corrected a stale "draft version 0.6 ... 0.1 to 0.5" to "0.7 ... 0.1 to 0.6" so your 0.7 to 0.8 sweep finds it. The codes table says "retired in version 0.8" (brief 2.2), which reads oddly beside "Version 0.7" until the sweep. The FAQ "What changed from earlier drafts?" now names the scope change without a version number.
6. **Wave 11 food-security findings** (imported meat, about 90% meat and about 30% milk self-sufficiency, disease) are not added. The "Why Vietnam" paragraphs in the summary, two-minute page and FAQ, and the summary's futures section, are where they would go.
7. **Exec summary "Demand 5"** keeps no processor share. Version 0.7 said 31%; the tile `kn-vissan-soy-share` says 33% (22 of 67). I dropped the number for brevity; the gap may need a check in ch14 or ch16.
8. **The at-a-glance world table** follows the revised ch23 text. If the ch23 editor changes the world descriptions again, the last column needs to follow.
9. **Fungal cost wording.** "Fungal biomass protein ... fits as a functional food ingredient, not a bulk one" follows the revised ch09 summary. The tile label `kn-cost-fungal-feed` still says "fungal feed protein".
