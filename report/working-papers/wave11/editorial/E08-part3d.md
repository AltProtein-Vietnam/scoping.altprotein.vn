# Editor log E08-part3d: chapters 17 and 18

Editor: E08-part3d. Date: 2026-10-01. Brief: `working-papers/wave11/EDITORIAL-v0.8.md`.

Files edited: `content/01-report/ch17-export-demand.md`, `content/01-report/ch18-demand-sizing.md`. No other file changed. No wave 11 findings added. "Version 0.7" labels and draft notices untouched. `python3 tools/validate.py`: 0 errors, 0 warnings after editing. No em or en dashes in either file.

Anchors: `grep -rn "ch17-export-demand#\|ch18-demand-sizing#" content` returns nothing, so no other page links to an anchor in these chapters. No other page cites a section number of chapter 17 or 18. Section numbers 17.1 to 17.7 and 18.1 to 18.6 are kept; some section headings now say what they find.

## ch17-export-demand

| section | change | type |
|---|---|---|
| frontmatter | `summary`: dropped "and for feed the clearest pull is at home"; split into two sentences | reframed for food |
| frontmatter | `key_numbers`: removed `kn-feed-yeast-imports` | tile or chart removed |
| frontmatter | `related_data`: removed `feed_buyer_register.csv` (register of feed mills scored for relevance to the retired T2 play); kept `inactive_yeast_trade.csv` and `asc_feed_mills.csv` because 17.5 still gives those facts as context | pruned feed |
| frontmatter | `reading_time_min` 18 to 17 | clear language only |
| opening | "In one paragraph" became an `**In brief.**` box of six bullets. The feed sentence (BAP credit, 9,200 t of yeast at USD 1.1 per kg as "the revealed pull") was replaced by a context line: "Seafood buyers' rules for aquaculture feed are context only (17.5). This study concentrates on protein for people." Also cut from the box, and already in the body: the IFS or BRCGS buyers point and CJ's move to Hungary | pruned feed; clear language only |
| 17.1 | Heading now "What Vietnam exports now: wrapped foods, not protein ingredients". HS (harmonised system), ASC, mycelium and MSG explained or written out. In the table's seafood row, the relevance cell "Processing skills; feed-standard pull" became "Processing skills; buyers' feed rules are context (17.5)" | reframed for food; clear language only |
| 17.2 | Heading now "...: less finished plant-based meat"; added a lead sentence repeating the table's finding; hybrids and co-packer explained; long paragraph split | clear language only |
| 17.3 | Heading now "Access: a tariff edge with conditions, and four barriers". MFN, CPTPP, RCEP, GRAS, ex-works, precision fermentation and cultivated meat explained. Barrier 4 (rules of origin) split into four bullets. The `[@ORG-01] {VN-direct\|High} {dx:revealed}` citation, which covered the chapter 19 and heading 2106 text as one block, now appears on both bullets (same source, same claim) | clear language only |
| 17.3 | The EU deforestation sentence on shrimp and pangasius feed moved, unchanged with its tokens, to 17.5 | reframed for food |
| 17.4 | Added a lead sentence (the channel is real but small, and it buys *chay*); split long sentences | clear language only |
| 17.5 | Retitled from "The pull that matters most for the frontier: feed" to "Feed rules for seafood: context, not a target". Now a short context section: an intro (feed is context; T2 and T3 retired in version 0.8; detail in D6.7 and S6) and four bullets (ASC standard, no reward for microbial protein, soy and deforestation, inactive yeast traded for food and feed together) | retitled; pruned feed |
| 17.5 | Deleted: ASC soy cutoff date, the eligible-volume and 1% ingredient rules, medium-risk ingredients until 2029, GLOBALG.A.P. (`[@FBA-05; @FBA-06] {general\|Medium}`); third place for ASC shrimp (`[@EXP-32]`); the 15,000 t insect-protein contract (`[@EXP-50]`); "no published purchase of microbial protein by a named Vietnamese mill" and Nutreco's 0.6% novel ingredients (`[@FBA-13; @FBA-07] {VN-adjacent\|High}`); "the standards-driven pull is concentrated in a shrinking share of sales" | pruned feed |
| 17.5 | Deleted the paragraph reading the feed plays T2 and T3 against export demand: the ASC May 2028 deadline as the hurdle, the domestic T2 price test against yeast at USD 1.1 per kg, and the 1.2 to 1.8% of shrimp-feed cost head-to-head trial gain (our calculation) `{VN-direct\|Low} {dx:inferred}`, with its link to ch25's kill test | pruned feed |
| 17.5 | Removed the embed `{{kn:kn-feed-yeast-imports}}` | tile or chart removed |
| 17.6 | Deleted the bullet "For seafood buyers and their feed mills: a domestic microbial ingredient priced against commodity yeast, with traceability data for ASC mills from 2028". "Greenfield brand", "near-shoring" and "tier 1 supplier lists" put in plain words; IFS Food and BRCGS explained | pruned feed; clear language only |
| 17.7 | Manufacturers: deleted "Feed mills supplying ASC farms will need certified status by May 2028 and should ask any microbial ingredient supplier for head-to-head trials...". Research bodies: deleted "for feed, the export-relevant test is a head-to-head trial against commodity yeast plus traceability and carbon data". Policy makers: deleted "support ASC-ready feed traceability before the 2028 farm deadline". Funders: deleted "a feed carbon benchmark for Vietnamese shrimp and pangasius feed" (the retired demand move DMV-12). T1 and single-cell protein explained | pruned feed |

## ch18-demand-sizing

| section | change | type |
|---|---|---|
| frontmatter | `reading_time_min` 19 to 20 (definitions added). Title, summary, key numbers and charts unchanged | clear language only |
| opening | "In one paragraph" became an `**In brief.**` box of six bullets. Explained S-ALT (the balance model's exploratory alternative-protein scenario in Part IV), *chay* days, CO2e, Mt and extrusion. Cut from the box, and already in 18.4: the S-ALT 2030 route-by-route translation, and the domestic-share qualifiers on 11,000 to 17,000 t | clear language only |
| callout | "Scenarios, not forecasts" kept; S-BASE explained as the balance model's trend scenario | clear language only |
| 18.1 | Heading now "Why we give no market-size number"; long bullet split; the closing sentence on forecasts made at the peak moved after the chart | clear language only |
| 18.2 | Added a lead naming routes R1 to R7 and defining delivered protein (supplied to buyers) and kt. Compensation and analogues defined in the table; displacement factor defined. The three scenario definitions (D-DRIFT, D-BENCH, D-STRETCH) moved before the route checks, so the codes are defined before first use. Added two sentences introducing S-ALT as the comparison and pointing to 18.6. The R3 and R4 check bullets split into five shorter, headed bullets. "Analogues observed elsewhere" became "comparable cases observed elsewhere", to avoid a clash with meat analogues | clear language only |
| 18.3 | Reading 3 "Feed is the bigger protein market ... Nothing in the demand evidence changes the supply study's conclusion that feed leads food" was replaced by "Feed is context, not a target": S-ALT puts microbial protein in feed at about four times its food volumes; the study concentrates on protein for people, so the chapter does not size feed demand; the 9,200 t inactive-yeast import figure is kept as a fact (food and feed together) | reframed for food |
| 18.3 | Table row label "For comparison: Part IV S-ALT, microbial protein in feed" became "For context only: ..."; values unchanged (55.8, 160.2, 514.1 kt) | reframed for food |
| 18.3 | Heading now "What the routes deliver: mostly replaced ingredient imports"; HS 3504, isolates and play T1 explained; long sentences split | clear language only |
| 18.4 | Heading now "What the routes displace: far below S-ALT". The D-STRETCH against S-ALT sentence moved to the front. Funder-unit methods turned into a three-item list; FAOSTAT explained | clear language only |
| 18.5 | Heading now "Sensitivity: no single assumption closes the gap"; main point first; three largest effects as a list | clear language only |
| 18.6 | "The feed side of S-ALT is outside this chapter's scope" became "The feed side of S-ALT is context only, outside this study's concentration on protein for people". Funders bullet split into sub-bullets. "Only 4 of the 19 demand moves" became "Only 4 of the original 19 demand moves", the wording other pages use. "Naming and GMO rules" written out. Offtake explained | reframed for food; clear language only |

Every number, citation, evidence tag and `{fx:...}`/`{dx:...}` tag in chapter 18 is kept (checked by a token diff against HEAD: nothing removed). The only token added is a second link to `[[ch22-protein-balance-2050]]`. No model number changed; the model was not re-run.

## Tiles and charts removed

- `kn-feed-yeast-imports`: embed and frontmatter entry removed from ch17, which is the tile's `primary_page`. The tile is still used by `brief-investors` and `brief-manufacturers`. Its `context` ends "The revealed price a Vietnamese microbial feed ingredient must beat", which is a feed-target framing. The consolidating editor should either reword the context as a plain trade fact and re-embed it in ch17 section 17.5 (the figure is still given there), or re-home or retire the tile.
- No charts removed. `chart-tariff-edge`, `chart-demand-routes`, `chart-displacement-vs-salt`, `chart-funder-units` and `chart-forecast-vs-actual` stay.

## Unsure or left for the consolidating editor

- **"Delivered" kept.** The brief lists "deliver" among words to avoid, but "delivered protein" is the demand model's defined term. It is used in the ch18 tables, `chart-demand-routes` ("What the routes deliver"), `kn-demand-bench-2035` and Appendix D8. So I kept it, and defined it at first use in 18.2 as "the protein it delivers (supplies to buyers)". The In brief box says "supplies".
- **Version markers in 17.5.** Following brief 2.2, ch17 says once that T2 and T3 "were retired in version 0.8 because feed is now context only", which conflicts slightly with STYLE.md section 7 (no version markers in reading text). Ch18 avoids version wording.
- **The ch18 S-ALT feed row.** The table row "For context only: Part IV S-ALT, microbial protein in feed" is kept so the "about four times" sentence has its numbers. If chapter 22 or Appendix F4 rename or drop the microbial-feed part of S-ALT, this row and reading 3 in 18.3 should follow.
- **Demand-move count.** With DMV-12 retired, chapter 25 may now count 18 active demand moves. Ch18 keeps "4 of the original 19", which matches `brief-international`, `brief-research`, `front-faq` and `front-exec-summary`. DMV-12 had no full funder fit, so the 4 is unaffected.
- **Wrapped-food values in 17.1.** One bullet still lists six partner-country import values in one sentence. I left it, because a table inside a bullet would be awkward. The values are also in `wrapped_food_trade.csv` and D6.5.
- **Correction callouts.** Both chapters keep their v0.6 correction callouts word for word. Neither corrected claim was removed.
