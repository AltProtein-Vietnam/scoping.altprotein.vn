# Prompt for Claude Cowork: Coefficient Giving grants in "Alternatives to Animal Products"

Why this exists: coefficientgiving.org returns HTTP 403 to the cloud research session (wave 13, line L9), so the grants list could not be read there. This prompt runs the same lookup in a browser session. Paste everything below the line into Claude Cowork. Put the three files it produces in `working-papers/wave13/L9-coefficient-giving-grantees/cowork/`, or paste them back into the research session.

---

You are helping AltProtein Vietnam with a research study, "Alternative protein in Vietnam: a supply-side scoping study". I need a complete, accurate list of the grants Coefficient Giving (formerly Open Philanthropy) has made in its "Alternatives to Animal Products" focus area, plus the research those grants produced. Use the browser to read the website directly.

## Where to look

1. Open the Farm Animal Welfare Fund page: https://coefficientgiving.org/funds/farm-animal-welfare/
2. Open the grants list filtered to the focus area: https://coefficientgiving.org/funds?focus-area=alternatives-to-animal-products (the old Open Philanthropy link https://www.openphilanthropy.org/grants/?focus-area=alternatives-to-animal-products redirects there). If that filter does not work, find the grants database on the site and filter it to "Alternatives to Animal Products" yourself.
3. Go through every page of results. If the site offers a CSV or spreadsheet download of grants, download it, use it, and say so.
4. Open each grant's own page for the purpose text when the list does not show it.

## What to record

### File 1: `cg_grants.csv` (one row per grant)

Columns, in this order:

`grant_id,grantee,grant_title,purpose_summary,amount_usd,date,focus_area,fund,grant_url,grant_type,geography,has_published_research,output_ids,notes,accessed`

- `grant_id`: CG-G001, CG-G002, and so on, in date order, oldest first.
- `amount_usd` and `date`: exactly as the site shows them. Amount as a plain number with no symbols or commas. Date as YYYY-MM, or YYYY-MM-DD if the day is shown. Leave a cell blank if the site does not show the value; never estimate.
- `purpose_summary`: one plain-English sentence, from the grant page.
- `grant_type`: one of `research` (academic or technical research meant to be published), `R&D` (product or process development, open-access tools, data), `field-building` (education, competitions, events, talent), `policy` (public funding or regulation advocacy), `consumer or diet change`, `general support`, `other`.
- `geography`: where the work happens, as stated (for example United States, Global, India, China, Southeast Asia). Flag anything in Vietnam or Southeast Asia in `notes`.
- `has_published_research`: `yes`, `no` or `unknown`.
- `output_ids`: the IDs from file 2, separated by semicolons.
- `accessed`: the date you read the page (YYYY-MM-DD).

At the end of your notes file, give the number of grants you found and the total of `amount_usd`. If the site states a count or a total for the focus area, compare the two.

### File 2: `cg_outputs.csv` (one row per published output of a research or R&D grant)

For each grant typed `research` or `R&D`, look for published outputs: peer-reviewed papers, preprints, techno-economic analyses, reports and datasets. Check the grant page, the grantee's website, publisher pages and Google Scholar. Include an output only if you opened its page or abstract and it links to the grant or grantee. A paper that thanks Open Philanthropy or Coefficient Giving in its funding statement counts.

Columns, in this order:

`output_id,grant_id,grantee,title,authors,year,venue,doi_or_url,output_type,topic,key_findings,key_numbers,link_to_grant,notes`

- `output_id`: CG-O001, CG-O002, and so on.
- `authors`: as printed on the output.
- `output_type`: `peer-reviewed`, `preprint`, `report`, `dataset` or `other`.
- `topic`: a few words, for example "cultivated meat cost", "fermentation scale-up", "single-cell protein", "plant protein functionality", "taste and sensory", "resilient foods".
- `key_findings`: one or two sentences, from the abstract or summary.
- `key_numbers`: the main numbers with units and the year they refer to (for example "USD 63 per kg at 10 kt per year, 2021 model"). Copy them exactly.
- `link_to_grant`: how you know it came from the grant (for example "funding statement names Open Philanthropy", or "listed on grant page").

Go deepest on outputs about:
- the cost and scale-up of cultivated meat;
- fermentation cost and capacity;
- single-cell or microbial protein from sugar, starch (for example cassava), natural gas or carbon dioxide;
- taste and sensory parity;
- plant protein functionality.

Include results from the 2026 call for alternative protein taste research (up to USD 10 million) if any have been announced.

### File 3: `cg_notes.md`

- What the fund page says about its strategy for alternatives to animal products: three to six sentences, with short quotes.
- Any open or recent calls for proposals: name, amount, deadline, priorities, and awardees if announced.
- The grant count and total, and the comparison with any figures the site states.
- Anything about Vietnam or Southeast Asia.
- Limits: pages that would not load, results you could not reach, and anything you were unsure of.

## Rules

- Never guess or fill in from memory. Every value must come from a page you opened in this session. Leave a cell blank rather than estimate.
- Keep the site's own wording for grantee names and grant titles.
- Do not sign in, create accounts, submit forms or contact anyone. Do not use web archives, caches or third-party copies of the grants database. Use the site itself, and for outputs, publisher, grantee and scholar pages.
- Write CSV files with a header row, UTF-8, and double quotes around any cell that contains a comma.
- In text, use plain English and British spelling, and no em dashes or en dashes (use commas, colons or "to").

When you have finished, give me the three files to download, and a five-line summary: the number of grants, the total amount, how many have published research, the three most relevant outputs for a country building food-protein manufacturing, and the biggest gaps.
