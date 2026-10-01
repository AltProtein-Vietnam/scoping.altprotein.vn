# Editorial log E03-part2a (version 0.8)

Editor: E03-part2a. Date: 2026-10-01. Files: `content/01-report/ch04-asset-map.md`, `ch05-industrial-base.md`, `ch06-knowledge-talent.md`, `ch07-rules.md`.

All four pages: "In one paragraph" replaced by an `**In brief.**` box of five or six bullets. Long sentences were split, abbreviations spelled out on first use, "must" kept only for legal duties, and "therefore", "purchased" and "underwrite" replaced with plain words. Every number, unit, year, citation and tag that stays is unchanged. `python3 tools/validate.py` gives 0 errors and 0 warnings, and there are no em or en dashes. No anchors into these four pages are linked from other pages (`grep -rn "ch0[4-7]-...#" content` finds nothing). Section numbers stay the same, so "section 6.3" in `brief-research` still resolves.

## ch04-asset-map

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary rewritten around protein for people (carbon for food fermentation; okara and brewer's grain for koji). Removed "points to microbial conversion of carbohydrate with added nitrogen". `ch26-plays` added to related pages. Reading time 11 to 14 | reframed for food |
| In brief | Bullets; carbohydrate framed as clean carbon for food fermentation; food-grade side streams for koji and fungal foods | reframed for food |
| 4.1 | New "What each group means for protein for people" list. "For scale" split into two sentences, numbers unchanged. Added: best use of the residues is food made near the source | reframed for food |
| 4.2 | New "What cassava means for protein for people" paragraph (play T4, with "hub" explained). Pulp: one sentence that food use needs a safety package (links to the 6.3 gap). Factory-count estimates turned into a bullet list under one citation | reframed for food |
| 4.3 | "Reading" became "What it means for food", with a link to T10. Rice distillers' grain flagged as a possible food ingredient | reframed for food |
| 4.4 | Sugar and broken rice framed as carbon for food fermentation | reframed for food |
| 4.5 | Lead paragraph: okara and brewer's grain for koji and fungal foods (T9). Seafood by-products: removed "benchmarks and competitors for alternative protein in feed"; now "context only" | pruned feed |
| 4.5 | Fermentation co-products: removed Ajinomoto liquid feed-ingredient capacity (30,000 to 50,000 m3) and the sentence "Whether Vietnamese MSG plants make a similar protein-rich biomass stream is an open question worth one phone call". The rest is kept as context | pruned feed |
| 4.6 | "Reading" became "What it means for food", with links to T1 and T10 | reframed for food |
| 4.7 | Duckweed is now food only. Added the EFSA manganese caveat, copied with its citation and tag from ch10 (`[@SCI-28; @SCI-29; @SCI-30] {general\|High}`), and a heavy-metal note linking to ch10. Feed-list status is now one line of context | reframed for food |
| 4.9 and "For each reader" | Rule 5 names the by-product atlas (P5). Manufacturers: "too small to replace soybean meal" became "small; suit niche food products near the source". Startups: koji or fungal foods next to a brewery or soy plant. Researchers: added duckweed manganese and heavy metals for food | reframed for food |

Tiles and charts: none removed.

## ch05-industrial-base

| Section | Change | Type |
|---|---|---|
| Frontmatter | Title changed to "The industrial base: fermentation and food processing". Summary rewritten: "feed-mill trial capacity" removed. `app-s6-feed-market` added to related pages. Reading time 9 | retitled |
| Frontmatter | `kn-shrimp-feed-concentration` removed from `key_numbers` (the aquafeed concentration claim was pruned) | tile or chart removed |
| In brief | Bullets. Feed mills now one context bullet | reframed for food |
| 5.1 | Aerobic, biomass and precision fermentation explained. Breweries now framed as sources of food-grade side streams. Added that the lack of contract fermentation is why T5 is one of the three leading plays | reframed for food |
| 5.2 | Retitled "Feed mills: large and half used, but context only" and cut to one paragraph. Kept: 269 mills, 43.2 Mt capacity, 20.8 Mt output, about 48% utilisation `[@IND-39]` | pruned feed |
| 5.2 | Removed: foreign-invested shares (90 mills, 51.3%, 62.5%); the aquafeed capacity and six-firm shrimp-feed concentration (640 kt, 70%, 920 kt) `[@IND-41; @IND-43]`; the De Heus and CJ deal `[@VCO-07; @VCO-08]` with its Correction callout `[@VCO-07]`; De Heus's 21 plants `[@VCO-09]`; the Vinh Long mill `[@IND-45; @VCO-10]`; Cargill's exit and the C.P. Ca Mau plant `[@IND-42; @IND-43]`; the Skretting and Entobel insect-meal shrimp feed `[@VCO-28]`; and "What this means" (feed buyers, spare pelleting, fishmeal substitutes). Points to app-s6 and app-s5 for the record | pruned feed |
| 5.3 | New "What this means for food" line: a food-grade soy stream for T1 | reframed for food |
| 5.4 | Cassava glucose framed as carbon for food fermentation. Processor list turned into sub-bullets | clear language only |
| 5.5 | Feed-trial centres cut to one context bullet | pruned feed |
| 5.6 | Heading "venture" became "food-protein venture". Row "Official feed and aquafeed trials" deleted. Feed pelleting row moved last, marked "(context)", and "Trials easy to host" became "Not a partner for food plays" | pruned feed |
| For each reader | Investors: "feed co-product businesses" removed from the reasons. Startups: path (c) "feed-mill trials" replaced by cassava glucose as fermentation carbon | pruned feed |

## ch06-knowledge-talent

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary: binding gap framed "for protein for people". Reading time 8 | reframed for food |
| In brief | Bullets | clear language only |
| 6.1 | Heading now "regional-level in algae and aquafeed". DIAAS and PDCAAS explained | clear language only |
| 6.2 item 1 | "they are exactly the evidence a feed-first play needs" became "They show a working applied-nutrition research base, but they are not a reason for a play: feed is context only in this study". The aquafeed trial results are kept as fact | reframed for food |
| 6.3 | Item 6 is now duckweed protein for food with manganese and heavy-metal checks (was "protein extraction and feeding trials"). Item 8 is now "Seaweed protein for food" (was "for food and feed"). Item 11 (bacterial single-cell protein and fungal meal in pangasius and shrimp diets) is removed from the list, with one line saying it stays in the record in app-s7. That matches the brief-research note | pruned feed |
| 6.4 | Feed-trial bullet cut to one context sentence. Removed the uncited line on university wet labs and ShrimpVet | pruned feed |
| 6.6 | Funders turned into sub-bullets. ACIAR, GFI and VINIF spelled out | clear language only |
| 6.7 | Retitled "What this means for protein for people". Investors and startups: partners are now named for food (HUST, koji genetics). Aquafeed groups are now "a fact, but feed is context only". Policy kit turned into sub-bullets | reframed for food |

Tiles and charts: none removed.

## ch07-rules

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary: "while feed rules are more open" removed; GMO status added; "Feed rules appear only as context". Reading time 17 to 16 | reframed for food |
| Frontmatter | `kn-feed-trial-agency-days` and `kn-unlisted-feed-fine` removed from `key_numbers` (feed tiles; both are frontmatter only, with no inline embed). The facts themselves stay as context in 7.5 | tile or chart removed |
| In brief | Bullets. The feed sentence ("insects, duckweed, algae and several yeasts are already permitted ... aquafeed list has a drafting gap ... fines") removed; it is now a pointer to 7.5 | pruned feed |
| 7.1 | Ministry changes turned into bullets under the same citation. MOH, MOST, MOF and IP spelled out | clear language only |
| 7.2 | New-law paragraph front-loaded and split into bullets. WTO spelled out | clear language only |
| 7.5 | Retitled "Feed rules: context only" and cut to four bullets: the livestock list; the trial (about 40 working days); the aquafeed list with no raw-material section; and the fines. The Correction callout is kept because the trial claim stays | pruned feed |
| 7.5 | Removed: "6 to 18 months" (our estimate); the state-research trial exemption `[@REG-29]`; the claim of no list amendment since February 2023 `[@REG-33; @REG2-07; @REG2-09]`; the names of the 30 aquafeed microorganisms; "Read literally ... practice evidently differs"; the ask "A written opinion from the Department of Fisheries is the cheapest fix"; "Running the trial first is now clearly worth its cost"; and the provinces bullet `[@REG-35; @REG-41]` (15 and 10 working days) | pruned feed |
| 7.6 | The three feed rows merged into one "Feed materials (context only)" row. The "20 days + trial + 10 working days" aquafeed time was dropped. Column count unchanged; source line unchanged | pruned feed |
| 7.7 | VAT bullet reframed as "VAT favours food-ingredient makers". Removed our estimate that the VAT exemption adds about 5% to 10% to feed producers' taxed input costs (it cross-referred to ch09). Tariff bullet: the food lines now come first, in sub-bullets; FTA and HS names spelled out | pruned feed |
| 7.12 | Removed "Feed: relatively open ..." from the binding-constraint list (now a pointer to 7.5). Investors: Department of Fisheries opinion removed. Startups: "inputs already listed (feed)" removed; "province" became "city if you need a sandbox" | pruned feed |
| 7.3, 7.4, 7.7, 7.8, 7.10, 7.11 | Long sentences split; OECD, TCVN, Codex, Thai FDA, MFN, ACFTA, RCEP, ATIGA and AKFTA explained. Headings 7.7, 7.8 and 7.10 now state the finding | clear language only |

Charts: `chart-route-to-market` kept.

## Unsure or for the consolidating editor

- **Tiles taken out of frontmatter whose primary page is still mine:** `kn-shrimp-feed-concentration` (primary ch05; still used in `brief-manufacturers` and `app-s5-facilities`), and `kn-feed-trial-agency-days` and `kn-unlisted-feed-fine` (primary ch07; still listed for `app-s9-regulation`). Their `pages` and `primary_page` fields in `data/key-numbers.json` need re-homing (for example to app-s5 and app-s9). `kn-feed-mills` is kept in ch05 because the brief keeps "feed mills are large and half used" as context.
- **Repeats elsewhere that now disagree with ch07:**
  - `front-exec-summary` item 6 and `brief-investors` item 5 still say "Feed is more open ... the aquafeed list is unclear".
  - `front-at-a-glance` still lists "aquafeed and livestock feed-list fixes".

  These belong to other editors.
- **ch09:** may still carry the "5% to 10%" VAT estimate for feed producers that I removed from ch07.
- **ch04 tag:** I added `{VN-direct|High}` to the first half of a split sentence (cassava starch exports to China). It is the same tag the whole sentence carried before.
- **ch04 claim:** "Duckweed grown on effluent would also need heavy-metal testing" has no inline citation. It cross-refers to ch10, which says the same.
