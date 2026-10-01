# Research protocol for new waves (wave 11 onwards)

Read this fully before starting a research line. It replaces the protocols in earlier waves (`wave3/design/00-agent-protocol-wave3.md`, `wave7/BRIEF-*.md`, `wave8/BRIEF-lines.md`, `wave9/BRIEF-lines.md`) for new work; those remain as the record of how earlier waves were run. Where your brief and this protocol differ, the brief wins on scope and this protocol wins on evidence rules and output format.

## 1. What you are doing

You are one research agent extending AltProtein Vietnam's study "Alternative protein in Vietnam: a supply-side scoping study" (version 0.8 in this repository). You run one **line**: a focused question set out in your brief. You write a working paper and clean tables that someone can fold into the study.

The test for every line: **does it change a conclusion or recommendation, add a new candidate or route, add a constraint a plan would otherwise hit late, close an open question, or close a question with a clean negative?** If the answer is none of these, say so plainly. That is useful information about where to stop.

## 2. Read first

1. `CLAUDE.md` and `STYLE.md` at the repository root.
2. The chapters and appendices your brief names, in `content/`. Do not repeat what they already establish.
3. The working papers of earlier lines that touch your topic (index in `working-papers/README.md`). Read their verdict, "What this changes" and "Next-wave candidates" sections.
4. The rows of `data/open_questions.csv` and `data/disagreements.csv` on your topic.
5. **Reuse existing sources:** search `data/sources.csv` (by URL, title or DOI) before registering a source. Cite sources already registered by their existing IDs.

## 3. Tools in a cloud session

- `WebSearch` and `WebFetch` (load with ToolSearch if deferred). Your brief may set a WebSearch budget; keep to it. Prefer WebFetch on known URLs and site-internal search or listing pages.
- Primary sources first: government portals and legal databases (thuvienphapluat.vn, luatvietnam.vn, vanban.chinhphu.vn, chinhphu.vn, moh.gov.vn, mae.gov.vn, nso.gov.vn, customs.gov.vn), USDA FAS GAIN reports, FAO and FAOSTAT, UN Comtrade, World Bank, peer-reviewed literature, company, retailer, school and procurement sites.
- Search in Vietnamese as well as English where Vietnam-direct material matters (for example "thức ăn chăn nuôi", "đạm thực vật", "protein thay thế", "đồ chay").
- Public data APIs (UN Comtrade, FAOSTAT, World Bank, OpenAlex, Crossref) may be called with `curl` in Bash. Save raw API responses you rely on in your line folder (small JSON or CSV) so the numbers can be rechecked.
- Scholarly MCP tools (OpenAlex, Scite) only if connected to the session (check with ToolSearch). Cite DOIs.
- No desktop browser in cloud sessions.
- If a page is blocked or a fetch fails, do not get round it with mirrors, caches or scraping tricks. Record the gap and the URL in your Limits section.
- **Privacy:** never put an email address, name or other personal identifier in any request, URL parameter or API call (no `mailto=`). Never sign in, create accounts, solve CAPTCHAs or submit forms other than search boxes.
- Bash and Python for arithmetic and for writing CSV files. Keep any calculation script in your line folder.

## 4. Evidence rules (strict, same as the study)

- **Never fabricate.** Every number needs a source you actually retrieved and read. Snippet-only or metadata-only evidence is Low and says so. A clean negative ("we found no ...") is a finding; say where you looked.
- Tag every substantive claim in the working paper: `[evidence label, confidence, SRC-ID]` plus, where relevant, foresight type and horizon, and demand evidence type. For example `[VN-direct, High, PFX-03]`, `[general, Medium, PFX-07, projection 2035]`, `[VN-direct, Medium, PFX-11, revealed]`.
  - Evidence label: `VN-direct` (about Vietnam), `VN-adjacent` (a comparable country or the same species; state the transfer assumption), `general` (global; no claim it applies to Vietnam).
  - Confidence: `High` (primary source read), `Medium` (reputable secondary, or primary read in part), `Low` (single claim, press, company marketing, or derived from weak inputs).
  - Foresight type: `trend`, `projection` (a published model or official target; name it, the scenario and base year), `estimate` (our calculation), `signal`, `wildcard`. `vision` is reserved for chapter 24. Always state the horizon year.
  - Demand evidence type: `stated` (surveys, intentions), `revealed` (sales, prices, trade, menus, shelves, rules and specifications of institutional buyers), `tested` (tastings, auctions, trials), `inferred` (our inference). When stated and revealed disagree, follow revealed and say so.
- Separate measured, estimated and claimed. Label company claims as claims. Prefer peer-reviewed and official sources over advocacy and company sources. Flag hype.
- Numbers with units and the year they refer to; ranges with "to". USD unless stated; 26,000 VND per USD if you convert (say so). Show the inputs to every calculation and mark it "(our calculation)".
- **Never average disagreeing numbers.** Give both, the position you take and why, and log it in `disagreements.csv`.
- Regulatory and market claims older than 12 months: re-check where possible.
- No probabilities unless a source gives them. No market-size forecasts. Published market sizes without a traceable method are not findings.
- Insect protein: benchmark and incumbent only, never a recommendation.
- Names: post-1 July 2025 province names with the former unit in brackets on first use; current ministry names (MAE, MOST, MOF, MOIT, MOH).

## 5. Style

Plain English, short sentences, British spelling. **No em dashes or en dashes anywhere**, including CSV cells (use commas, colons, "to" or separate sentences). Place and company names unaccented in English text; Vietnamese terms in italics with diacritics and an English gloss on first use. No hype.

## 6. Output

Write only inside your line folder: `working-papers/wave<N>/<line-folder>/` (for example `working-papers/wave11/L1-soy-flour-quotes/`). **Write incrementally:** create the working paper early and append as you go, and commit and push regularly, so work survives an interrupted session.

1. **`<line-folder>.md`, the working paper:**
   - Title, then: "Line: <ID and name> (wave N). Source prefix: <PFX>. Date: <today>."
   - **Verdict** (3 to 5 sentences): what the line found and its yield class: *changed a conclusion*, *added a candidate or route*, *added a constraint*, *closed a question*, *clean negative*, or *noise* (more citations, no change). Be honest.
   - **Headline findings** (6 to 12, tagged).
   - **Detailed findings** by sub-question, with tables where useful.
   - **What this changes in the package:** a table `where (page and section, or data file) | current text or value | proposed change | evidence | strength`. Only changes the evidence supports.
   - **Signposts** (futures lines only): observable events that would show a trajectory unfolding, and where to watch.
   - **Next-wave candidates:** for each, whether it is a *different kind* of question or a *deeper* version of this one, whether desk research could close it, and what result would change which conclusion. Say so if further desk work here would be noise.
   - **Limits:** what you could not reach (with URLs), tool failures, what remains unverified.
2. **`sources.csv`:** `source_id,citation,title,author_or_publisher,date,url,doi,source_type,accessed,notes`. IDs `<PFX>-01`, `<PFX>-02` and so on. `source_type` one of: gov/statistics, law, intergovernmental, peer-reviewed, preprint, market-research, company, press, advocacy, database, other. `accessed` is the date you read it (YYYY-MM-DD). Only new sources; reuse existing IDs for sources already registered.
3. **`data_<name>.csv`:** one or more clean tables the study can publish. snake_case column names. Every row carries `source_ids,evidence_label,confidence,notes`, plus `foresight_type,horizon_year` or `demand_evidence_type` where relevant.
4. **`open_questions.csv`:** `question,why_it_matters,cheapest_way_to_close,owner_org_to_ask,priority,closes_oq` (`closes_oq`: an existing OQ id this answers or partly answers, if any).
5. **`disagreements.csv`:** `topic,claim_a,claim_b,position_taken,notes`.
6. **`key_numbers.csv`** (0 to 6 rows): `label,label_vi,value,unit,as_of,context,source_ids,evidence,confidence,foresight_type,horizon,demand_evidence_type`.
7. **`changes.csv`:** `where,current,proposed,evidence_source_ids,strength,type` with strength `strong|moderate|weak` and type `corrects|updates|adds|strengthens|closes`. Same content as the "What this changes" table.

Do not edit `content/`, `data/`, `charts/` or `sources/` during a research line unless your brief says you are also the consolidating agent. Folding results into the study is a separate step (see `CLAUDE.md`, "Folding research into the study").

## 7. Stopping rule

Aim for depth within roughly 60 to 110 tool calls. Stop a thread when returns are mostly repetition, and say so. If the line only adds citations, classify it as noise and stop early.

## 8. Final message

Under 300 words: files written, verdict and yield class, the 3 to 5 most important findings, the changes to the package you recommend, the biggest gaps, next-wave candidates, and how many WebSearch calls you used. Do not paste the notes.
