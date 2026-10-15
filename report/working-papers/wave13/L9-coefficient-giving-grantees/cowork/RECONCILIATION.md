# Coefficient Giving browser check: reconciliation with line L9

Lead session, 15 October 2026. Inputs: `cg_grants.csv` (61 grants), `cg_outputs.csv` (7 outputs) and `cg_notes.md`. These came from a browser session (Claude Cowork) the editor ran, using the prompt in `../../COWORK-PROMPT-coefficient-giving.md`. coefficientgiving.org refused automated access from the cloud research environment (HTTP 403 from its Cloudflare edge) on every path, so the cloud session never fetched the site itself. The three files are kept here unchanged, as the record.

## What the list confirms or changes

| Topic | Line L9 (cloud session) | Grant list (browser session) | Position taken |
|---|---|---|---|
| Size of the focus area | Not known; site blocked | 61 grants, USD 49,310,121, September 2016 to July 2026; site count "Found 61 grants" matches | Use the list (CGG-19) |
| What it funds | Research outputs traced through funding statements | By title: 20 policy, 10 field-building, 9 general support, 8 research, 1 R&D, 7 other, 6 consumer or diet change. Research and R&D come to USD 2,082,256, about 4% | Report as the browser session's classification from titles |
| Vietnam and Southeast Asia | No Vietnamese grantee found (floor) | No grant names Vietnam or Southeast Asia; nearest are Food Frontier, Asia (USD 500,000, 2022) and GFI Asia Pacific (USD 22,500, 2024) | Confirmed |
| Berkeley Alt:Meat Lab | USD 125,000 (2019, lab announcement) and USD 800,000 (2024, search summary CGG-17) | Five grants: 131,579 (2019-01), 700,000 (2019-10), 1,146,201 (2021-10), 800,000 (2024-03) and 600,000 (2026-05); USD 3,377,780 in total | Use the list; log 125,000 against 131,579 as DG-398 |
| FFAR chickpea and corn zein | USD 444,000 or USD 250,000 (search summaries; DG-397 said quote neither) | One grant, "Chickpea and Corn Zein Research", USD 444,000 (2020-06) | Use USD 444,000 for the focus area; DG-397 updated |
| The Good Food Institute | General support, amounts from search summaries | Six grants, USD 22,500,000 (18.5 million general support; 4 million international expansion) | Use the list |
| The Protein Project's funders | Two foundations it does not name (L7) | USD 353,764 (2025-09), "EU Fermentation Technology Advocacy" | One funder identified; recorded in M1.16 and S14.1 |
| Items funded outside the focus area | Penn State and ALLFED resilient food, UC Davis, Tufts, NECTAR, Tra Vinh University, University of Texas at Austin and Toronto; Humbird and Rethink Priorities | None of these is among the 61 grants. Humbird's model and Rethink Priorities' egg report are commissioned contracts | Keep the screen verdicts; note in each row that the funding is outside this focus area |
| 2026 taste call | Up to USD 10 million, then 30 million (DG-396) | Same; the official call page now returns "Page not found"; no open call on Apply for Funding; no awardees announced | DG-396 and OQ-519 notes updated |
| Search summaries (CGG-17) | Used for three grant facts at Low | Superseded by CGG-19 for all three | CGG-17 kept in the register as the record; screen rows now cite CGG-19 |

## New outputs, checked by the lead

The lead re-checked each output the browser session found before adding it. All four were added to `../data_item_screen.csv` and so to `data/solutions_screen.csv`.

- **CGG-I25, Breakthrough Institute (grant CG-G019).**
  - Working paper read in full: "This work was partly funded by Open Philanthropy and Breakthrough Institute".
  - Finding: plant-based meat complements conventional meat at home, and lower plant-based prices are "unlikely to significantly impact" livestock production.
  - Peer-reviewed version (Agricultural Economics, 2025): metadata only.
  - Use: added to chapter 13 (stated preferences).
- **CGG-I26, Food Frontier, "Alternative Proteins and Asia" (grant CG-G020).**
  - The report page names only the top five markets (China, Singapore, South Korea, Thailand, Japan). It does not mention Vietnam, and it names no funder.
  - The browser session reported a trade-press claim that Vietnam ranked among the least favourable markets. It is not verified, so it is not used (OQ-524).
- **CGG-I27, Rethink Priorities' egg report (commissioned by Coefficient Giving).**
  - The report page states the commission and the numbers used: about 80% of sampled products moderately difficult and about 20% difficult to replace (low confidence).
  - It also reports the IMPROVE (2023) finding that potato protein comes closest to egg white.
  - Use: added to TPP-05's egg-white job in chapter 25.
- **CGG-I28, Stanford, Nature Food (2025).** Crossref metadata only. Consumer interest, out of scope.

## Not used

- Purpose text quoted from old grant pages by a background check in the browser session. The browser session itself did not use it, because the tool may have served a cached copy, and neither did we.
- The award sizes and fish species of the 2026 call reported by the background check, which could not be re-checked. The study already cites the call page (CAP-57) and the staff post (CGG-03) for these.
- Three further Purdue zein papers with the same FFAR award number (not opened), and the CEEW, Solutions for Our Climate and Plant Based Foods Association items (no funder named, or not about alternative protein).
