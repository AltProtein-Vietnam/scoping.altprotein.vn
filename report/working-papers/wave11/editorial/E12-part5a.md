# Editor log E12-part5a: chapters 25 and 26

Editor: E12-part5a. Date: 2026-10-01. Brief: `working-papers/wave11/EDITORIAL-v0.8.md`.

Files changed: `content/01-report/ch25-demand-to-frontier.md`, `content/01-report/ch26-plays.md`. No other file edited. `python3 tools/validate.py`: 0 errors, 0 warnings after my edits. No em or en dashes in either file. Every kept number, unit, year, citation token and evidence, foresight and demand tag is unchanged (checked by script against commit 97231c9). The only tokens removed belong to retired feed plays (T2, T3, T6), retired public goods (P2, P3), TPP-11 or DMV-12.

## ch26-plays

| Section | Change | Type |
|---|---|---|
| Frontmatter, H1 | Title "Ten plays and six public goods" becomes "Seven plays and four public goods"; summary rewritten (T1, T4, T5 lead; four public goods); reading time 17 to 15 min; `related_pages` adds `app-m5-changelog`; `related_data` drops `inactive_yeast_trade.csv` and `asc_feed_mills.csv` (T2 only) | retitled |
| Opening | "In one paragraph" becomes a six-bullet `**In brief.**`; T2 removed from the leading three; T5 joins T1 and T4; hub and tolling explained | reframed for food |
| Callouts | "Read with care" and "New evidence on T1": T2 sentences removed (9,200 t inactive-yeast pull, T2 defensibility 3 to 2). T1 thesis kept in full. Wrong cross-reference "scores in 11.2" corrected to "section 26.2" | pruned feed |
| 26.1 | Short explanation of how the weighted score is calculated; DFI explained. Criteria and weights unchanged. The "Route to market" definition still says "Ordinary food or listed feed rules apply", because that is how the scores were set | clear language only |
| 26.2 | T2, T3 and T6 rows removed from the scores table. Top-three table recalculated for the seven active plays (our calculation, unchanged scores and weights). "Reading" rewritten: T1 and T4 in the top three under every preset; T5 under five of seven; balanced order T4 3.90, T1 3.80, T5 3.45, T10 3.05, T9 3.00, T7 2.10, T8 1.55 | pruned feed |
| 26.3 | T2, T3 (with its Correction callout on the 350 to 450 kt fishmeal pool) and T6 sections removed. T4 first customers reworded to food fermenters, T5 first customers to food startups (T7, T9), both from `plays.csv` v0.8. "Must be true" relabelled "What has to be true". Terms explained (FOB, HS, t/h, FIRI, EECi, titer, okara, *tương*, E10) | pruned feed |
| 26.4 | "Six public goods" becomes "Four public goods"; P2 and P3 rows removed; "What it unlocks" names only active plays (P1: T7, T9 and food uses of fungal biomass; P5: T4, T9); P6 renamed "Open cost model and public price series for food protein ingredients" (as in `plays.csv`) | pruned feed |
| 26.5 | T2, T6, T3, P2 and "next feed-list updates" removed from the sequencing | pruned feed |
| 26.6 | New subsection "Feed-ingredient plays are retired" (T2, T3, T6, P2, P3; record in `plays.csv` and Appendix M5). The soybean-meal-in-feed item kept as context there (4.6 to 5.1 times gap). Other not-recommended items unchanged | reframed for food |
| 26.7 | T2, T3, T6 and P2/P3 removed from each audience line; research line now "T8, T9 and P4 to P6"; international "T4 and T5" | pruned feed |
| Whole page | Shorter sentences, active voice, abbreviations explained | clear language only |

Embeds: `{{chart:chart-plays-scoring}}` and `{{chart:chart-plays-horizon}}` kept (both filter `type == play`, so retired plays drop out of the data). No embed removed. Tiles `kn-plays-count` and `kn-top-play-balanced` kept in frontmatter.

## ch25-demand-to-frontier

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary: "eleven target product profiles, a demand check of the ten plays and twenty-one cheap moves" becomes "ten active target product profiles (TPP-01 to TPP-10), a demand check of the seven active plays and twenty cheap moves". `related_data` drops `feed_buyer_register.csv`, `inactive_yeast_trade.csv`, `asc_feed_mills.csv`, `t2_price_per_performance.csv`; `related_pages` adds `app-m5-changelog`. Reading time stays 24 | reframed for food |
| Opening | Six-bullet `**In brief.**`; method note adds one sentence that the feed profile, feed plays and feed move are retired | reframed for food |
| 25.1 | No feed content; sentences split, terms explained (SKU, PCR, TCVN, GMO, MOET, extender, co-packer, benchmark path) | clear language only |
| 25.2 | TPP-11 row removed; one line says TPP-11 was retired in version 0.8 and stays in the data file. Table abbreviations explained | pruned feed |
| 25.3 | Heading becomes "The seven active plays, checked against demand"; T2, T3, T6 rows removed with one line on their retirement; T2 paragraph (ASC standards, inactive yeast, Nutreco) removed; T2 kill test removed; "three supply-score changes" becomes the two T1 changes (the T2 defensibility change dropped) | pruned feed |
| 25.3 ranking | "T10 moves up to third place for startups, joint third for manufacturers and fourth for investors" becomes "third place for investors, startups and manufacturers" among the seven active plays (our calculation; changes only because T2 left the set) | pruned feed |
| 25.4 | Heading "Twenty-one cheap moves" becomes "Twenty cheap moves"; DMV-12 bullet replaced by one line saying it is retired; DMV-02 now names buyers of "T1 products" and "a would-be T1 owner" (T2 dropped; HS 2102.20.10 kept in the code list) | pruned feed |
| 25.4 to 25.6, readers | Sentences split; "deliver none" becomes "achieve none of these"; international-funders bullet split into two paragraphs while keeping its citation groups in place | clear language only |

No tiles or charts removed from ch25.

## Unsure or for the consolidating editor

1. **"Three lead under every weighting" is not exactly true.** With the unchanged scores and weights, T1 and T4 are in the top three under all seven presets. But T5 is not third under two presets: under the startup preset T10 is third (3.25) and T5 fourth (3.20); under the investor preset T5 and T9 tie for third (3.00). I wrote it accurately ("T5 is in the top three under five of the seven presets") and did not use the brief's shared sentence. Pages that use "three lead under every weighting" (front pages, summaries, briefs) should be checked.
2. **Tiles needing a new value or context (not edited, as instructed):** `kn-plays-count` still reads "10 plays and 6 public goods" (should be 7 and 4); `kn-top-play-balanced` context still says "T2 and T5 follow at 3.45" (now T5 alone at 3.45). Both have `primary_page: ch26-plays`.
3. **Chart specs:** `chart-plays-scoring` title "Ten plays, scored ..." and its alt text (mentions functional feed ingredients at 3.45) need updating. `chart-plays-horizon` alt text mentions feed ingredients, duckweed and bulk fishmeal replacement.
4. **Repeats outside my files:** `front-how-to-read` codes table (T1 to T10 as "the ten plays", P1 to P6 "six public goods", TPP-01 to TPP-11, DMV-01 to DMV-21); `front-cover` ("ten plays"); `front-exec-summary` ("Ten plays; three lead", "Eleven target product profiles ... twenty-one" moves); `ch23-scenarios-2050` heading 23.5 ("ten plays and six public goods"); `content/PAGE-IDS.md` and `site-manifest.json` titles for ch26.
5. **Move count:** `demand_moves.csv` has no status column, so DMV-12 is still a plain row there. I wrote "twenty cheap moves". `kn-funder-fit` ("4 of 19 moves", the original nineteen) is unaffected and unchanged.
6. **Anchors:** no page links to an anchor in ch25 or ch26 (`grep -rn "ch26-plays#\|ch25-demand-to-frontier#"` finds nothing), so removing the T2, T3 and T6 headings breaks no link. I renamed two headings: "26.2 The scores: T1, T4 and T5 lead" and "26.4 Four public goods".
