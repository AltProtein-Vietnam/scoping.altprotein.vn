# Editor log E13-part5b: chapters 27 and 28 (version 0.8)

Editor: E13-part5b. Date: 2026-10-01. Files edited: `content/01-report/ch27-policy-options.md`, `content/01-report/ch28-robust-moves.md`. No other files edited. `python3 tools/validate.py`: 0 errors, 0 warnings (whole package at the time of the run). No em or en dashes in either file.

Token check: every citation, evidence tag, foresight tag and number that was kept is unchanged (checked by script against `HEAD`). The only citation tokens removed or changed belong to retired feed items; they are listed below.

## ch27-policy-options

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary rewritten: "two feed-list fixes" replaced by the novel-food procedure in the decree; "24 current options" now 19. Reading time stays 11. `app-r3-glossary` added to related pages. | reframed for food |
| In brief | "In one paragraph" box became five bullets. Removed the aquafeed raw-material section and livestock-list microbial-biomass entries as the next steps; the next two steps are now the joint MAE and MOH note and the novel-food procedure in the decree. Removed "public feed trials" from the costly options. Count now "33 options, 19 ranked". | pruned feed |
| Timing and labels callout | Option numbers renumbered to the new ranks: option 16 is now 12 (PO-024), option 24 is now 19 (PO-025). Split into bullets; citation kept with the claims it supports. | clear language only |
| Neutrality note | "food and feed security" became "food security". | reframed for food |
| 27.1 Principles | "ordinary foods or feeds" became "ordinary foods"; "novel foods and feeds" became "novel foods". Citation of principle 2 now sits on the factual sentence it supports (same claim, split into two sentences). | reframed for food |
| 27.2 ranked options | Renumbered to `report_rank` in `policy_options.csv`: Tier 1 ranks 1 to 3 (PO-015, PO-016, PO-019); Tier 2 ranks 4 to 9; Tier 3 ranks 10 to 19. Removed rows PO-017 (v0.7 rank 3), PO-018 (4), PO-021 (7), PO-029 (15), PO-007 (18). Added a "Five feed options retired" paragraph with their v0.7 ranks. Added a short-forms line for ministry and agency abbreviations and a glossary link. | pruned feed |
| 27.2 Tier 1 sources line | Removed REG2-01 (Circular 16/2026, aquafeed list), REG-32 (Circular 21/2019) and REG-33 (Circular 31/2022): these supported only the retired PO-017 and PO-018 (see their `source_ids`). | pruned feed |
| 27.2 "Why these first" | Removed the sentence on options 3 and 4 (feed-list ambiguities and Decree 211/2026 fines of VND 10 to 20 million per unlisted feed material). Added one sentence saying option 3 gives the clause its detail in the decree (restates the table). | pruned feed |
| 27.2 Tier 3 sources | "changes to options 13, 16 and 24" became "options 10, 12 and 19" (same options, new ranks). | clear language only |
| 27.3 Trade-offs | Option references renumbered (reliance lane is option 3, transition rules option 14, pilot line option 7). Long sentences split; trade agreements written out in words (each is used once). | clear language only |
| 27.4 Who does what | MAE row: removed aquafeed and livestock list fixes and public feed trials; added the joint note (2). MOF row: removed VAT neutrality. All rank numbers updated; ranks added where the action maps to one option. Merger paragraph: "feed, aquafeed" shortened to "as well as feed". | pruned feed |
| 27.5 What this means | "Options 1 to 4" became "the three highest-ranked options" (options 1 and 2 cheap; option 3 more drafting). International bodies: removed "funding for public feed trials". Research bodies: "options 7, 13 and 14" became "options 10 and 11" (feed trials retired). Investors: "options 1 to 5" became "options 1 to 3". | pruned feed |
| Whole page | Abbreviations explained on first use (MAE, MOH, GMO, VFA, MOST, MOF, FIRI, ASEAN, MFN, DIAAS or PDCAAS); OECD and G20 left as known. Glosses added for precision fermentation, sandbox, tolling, first-loss window, single-cell protein, access and benefit-sharing, capacity charges. Tay Ninh given its former units. | clear language only |

## ch28-robust-moves

| Section | Change | Type |
|---|---|---|
| Frontmatter | Title "Robust moves: what to do now that pays off in any 2050" became "Moves that pay off in any 2050"; short title "Moves for any 2050". Summary rewritten (seven no-regret moves; two bets). Reading time 9. `ch22-protein-balance-2050` added to related pages. Page id unchanged. | retitled |
| In brief | Became six bullets. Counts now seven no-regret, six options, two bets, one hedge; 16 of 21 moves active. Removed the closing claim that feed efficiency is the single strongest lever (moved, in brief's wording, to the retired paragraph as context). | pruned feed |
| Method note | Added the four world names; wording only otherwise. | clear language only |
| 28.1 no-regret moves | Removed RM-02 and RM-07 rows. Reworded RM-01 (national protein balance of what people eat, with a feed memo line; lead actors now MAE, NSO and MOH National Institute of Nutrition, as in `robust_moves.csv`), RM-03 (new-food route only), RM-04 (food-grade pilot capacity with sensory and food-safety testing; public tank and pond trials removed), RM-05 (price series for food protein ingredients), RM-06 (adds okara; food-safety rules for food-grade side streams), all from `robust_moves.csv`. RM-03 citation `[@REG-12; @REG2-01]` became `[@REG-12]`: REG2-01 is the aquafeed circular and supported only the removed aquafeed-entries half. Ca Mau and Vinh Long given former units. | pruned feed |
| 28.1 public goods paragraph | Now covers the four active public goods (P1, P4, P5, P6); P2 and P3 removed. "No-regret or robust" restated as "P4 and P6 scored no-regret, and P1 and P5 held in every world" (from the chapter 23 table). | pruned feed |
| 28.2 options | RM-10 "fermentation and feed-protein sites" became "food-fermentation hubs" (hub explained); RM-11 "for food-protein innovation"; RM-12 "feed-mill offtake" became "offtake from a named food manufacturer"; all from `robust_moves.csv`. | reframed for food |
| 28.3 bets | "Four bets" became "Two bets". Removed RM-16 (with VIS-18 and the fishmeal USD 2,500 per t trigger) and RM-17 (with HUB-05 and the hydrogen and power triggers). Added a two-sentence lead-in. | pruned feed |
| 28.4 hedges | "Two hedges" became "One hedge". Removed RM-20 (with MAC-24, COST-33 and the 10 to 14% feed-price rise). RM-21 reworded to food protein-ingredient imports and food-safety rules, from `robust_moves.csv`. | pruned feed |
| New paragraph "Five feed moves retired" | Names RM-02, RM-07, RM-16, RM-17, RM-20 as retired in version 0.8 and adds the brief's feed-efficiency context sentence (3.4 Mt, about twice S-ALT), tagged `{VN-direct|Low} {fx:estimate}` with "(our calculation)" and a link to chapter 22. RM-02's China comparison (GEO-10, GEO-11) removed with RM-02. "Focus" in the brief's sentence written as "scope". | pruned feed |
| 28.5 Sequencing | Removed RM-02 and RM-07 from the list; "eight of the nine" became "six of the seven" (all no-regret moves except RM-04, as before). "Protein and feed balance" became "national protein balance". Decision 1002 described as on the high-tech workforce (from Appendix F5). Numbered list. | pruned feed |
| 28.6 By actor | MAE: removed adding microbial biomass and algal oils to aquafeed lists. Feed mills and integrators: now only share inclusion and conversion data for the feed memo line (omega-3 oil removed). Investors: "robust plays" became "plays that hold in every world". Startups: "species-specific functional feed ingredients" (retired T2) replaced by T9 and T10, both of which hold in every world in the chapter 23 table. Research bodies: feed-conversion measurement folded into "the measurements behind the protein balance". Provinces given former units. | reframed for food |
| 28.7 Open questions | Dropped "the current status of Thai Duong Feed's yeast-protein line" (feed). Kept feed-conversion and inclusion series as needed for the balance's memo line. NDC 3.0 explained. Bulleted. | pruned feed |
| Whole page | "Robust" removed from reading text. Abbreviations explained (MAE, MOH, MOST, MOF, NSO, DFIs, ASEAN; MOET written in words); glosses for no-regret, wildcard, stillage, okara, concessional, offtake, dumping, precision fermentation. | clear language only |

## Tiles and charts

No embeds or frontmatter entries removed. All five tiles and both charts are still needed, but four carry v0.7 values that now contradict the text. For the consolidating editor:

- `kn-no-regret-moves` (embedded in ch28 and used on front pages and briefs): value "9 of 21 moves" should become "7 of 21 moves"; context should list the seven moves in the brief's section 6 wording.
- `kn-policy-options-count` (ch27 frontmatter): "33 options (24 ranked)" should become "33 options (19 ranked)"; context should mention five retired feed options and nine superseded.
- `kn-low-effort-options` (ch27 frontmatter): "16 of 24 ranked options" should become "13 of 19 ranked options" (our count from `policy_options.csv`); its context line "ranks 1 to 4 are all low effort" is no longer true (rank 3, PO-019, is Medium).
- `kn-capital-charge-lever` (ch28): context refers to "fungal feed protein"; consider "fungal biomass protein" to match the chapter 9 reframing. Value unchanged.
- `chart-robust-moves`: `charts/data/robust_moves_matrix.csv` still has 21 rows with v0.7 names, and the subtitle and alt text say "21 moves" and "nine no-regret". It should filter to the 16 active moves (or mark the five retired), use the reworded names, and say seven no-regret. Title "Robust moves across the four worlds" could become "Moves for any 2050 across the four worlds".
- `chart-policy-effort-impact`: the filter "report_rank is not empty" already drops the retired options, but the alt text says "24 ranked options"; should say 19.

## Other repeats outside my files (not edited)

- `site-manifest.json` (ch27 and ch28 entries) and `content/PAGE-IDS.md` still carry the old ch28 title, short title and both old summaries.
- `content/00-front/front-how-to-read.md` line 66 defines "RM-01 to RM-21" as "Robust moves".
- `content/01-report/ch23-scenarios-2050.md` section 23.6 still recommends T2 and T6 and quotes the RM-16 fishmeal trigger with a link to ch28.
- `data/robust_moves.csv` RM-03 still lists REG2-01 among its sources and mentions feed-list updates as its trigger; not edited (data file is read-only for me).

## Unsure

- Tier 2 sources line in ch27 still includes REG2-14 (search for the controlled-testing decrees under the science law). In `policy_options.csv` it is listed only under the retired PO-021, but it also bears on the sandbox decree in PO-020, so I kept it.
- RM-06 keeps "EU feed law bans some waste streams" with NGF-14. It is a feed rule, but it stays as evidence that side-stream rules exist; the consolidating editor may prefer to drop it.
- The startup row in 28.6 is a reframing, not a new finding: T9 and T10 are the active business plays that hold in every world in chapter 23 and suit startups. Please check it agrees with the edited ch26.
