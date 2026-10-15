# scoping.altprotein.vn

The website for **Alternative protein in Vietnam: a supply-side scoping study** (AltProtein Vietnam, draft v0.10, October 2026). It publishes the report package in `report/`: 80 pages (seven front pages, 30 chapters in five parts, six audience briefs and 37 appendices coded M, S, D, F and R), 198 data tables, 2,669 active sources, 57 charts and the working papers.

Astro and EmDash on Cloudflare Workers, with D1 (content), R2 (CMS media) and KV (editor sessions).

## Who sees what

While the report is a draft, the public site carries the findings and the evidence stays with reviewers.

|                                                                           | Public                     | Signed-in Editors and Administrators |
| ------------------------------------------------------------------------- | -------------------------- | ------------------------------------ |
| Front pages, 30 chapters, 6 briefs                                        | Yes                        | Yes                                  |
| Glossary (R3) and source list (R4)                                        | Yes                        | Yes                                  |
| Charts with their data tables, key-number tiles, citations                | Yes                        | Yes                                  |
| Appendices M1 to M5, S1 to S14, D1 to D8, F1 to F6                        | No: a sign-in notice (403) | Yes                                  |
| Registers R1 (open questions) and R2 (disagreements)                      | No                         | Yes, also as filterable tables       |
| Data browser (`/data`), every CSV, JSON and Markdown file, the three zips | No (403)                   | Yes, under `/files/`                 |
| Workbench (`/workbench`): everything above in one place                   | No                         | Yes                                  |

- The rule is in `src/lib/access.ts` (`isRestrictedPage`, editor role 40 or higher). Pages, cross-links, search, the sitemap, reading paths, the pager and the play cards all use it: for the public, a link to a restricted page is plain text.
- Files are written to `/files/` and are never in `public/`. Astro's Cloudflare handler serves any file in `public/` straight from the asset binding, before routes or middleware run, so `scripts/build.mjs` stages the files outside `public/` and adds them to `dist/client/files/` after `astro build`. The `run_worker_first` rule in `wrangler.jsonc` sends `/files/*` to the Worker, and `src/pages/files/[...path].ts` checks the editor session before fetching the asset. In `pnpm dev` the files sit in `public/files/`, where the dev server routes them the same way.
- EmDash's own public endpoints that would expose restricted text are closed to visitors without an editor session: `/_emdash/api/search` and `/search/suggest` (`src/middleware.ts`), and `/sitemap-pages.xml` (overridden by `src/pages/sitemap-[collection].xml.ts`).
- Editors see an editor bar with a link to the workbench and a switch to see the public view (a cookie; `/workbench/view`).
- Any signed-in CMS account can read page text through the CMS API, so invite only reviewers who may see the appendices.
- Old addresses `/data/<file>.csv` and `/downloads/<file>.zip` redirect to `/files/…`.

## What the site does

- **Answer-first home page.** The argument of the two-minute summary, one step per row: the step's text, its main number as a large tile, one chart from the chapter that holds the evidence, and links to those chapters. Then the briefs by role (with reading paths), the five parts and an evidence legend. The words come from the cover and the two-minute summary in the CMS, so editors change them there.
- **Navigation by question.** Each part of the report is a question with its own page (`/report/part-i` to `/report/part-v`): what it answers (from the cover's table) and each chapter with its summary.
- **Reading pages.** Chapters open with their "In brief" in an answer box (briefs: "The short version"). Each claim's citation numbers stay in the text and its evidence tags become one note: a three-step confidence meter, where the evidence comes from (Vietnam, a comparable country, global) and any forecast or demand tag. On wide screens the notes sit in the margin beside the claim; on narrow screens, in tables and in callouts they are inline. Selecting a citation number opens its sources. Key-number tiles, charts and tables span the text and the margin.
- **Charts** are drawn as inline SVG at build time from `report/charts/chart-specs.json` (no chart library), in light and dark themes, each with its data table and source line. Their colours were checked with a palette validator in both themes.
- **Plays ranking** (chapter 26) and **scenario explorer** (chapter 23), with static fallbacks.
- **Search** across the pages the reader may open and the glossary (editors: also companies, facilities, open questions, disagreements and policy options); a bilingual glossary at `/glossary`.
- **English or Vietnamese interface** under `/vi/…`. Report text stays in English, except the bilingual glossary and the Vietnamese key-number labels. The Vietnamese executive summary and prologue are held back until a translation pass for version 1.0 (`report/working-papers/vi-pages/`); their old addresses `/tom-tat` and `/loi-mo-dau` redirect to the English pages (`WITHDRAWN_PATHS` in `src/lib/redirects.ts`).
- Light and dark themes, print styles, keyboard navigation, no trackers.

Type: Be Vietnam Pro (headings, interface, numbers, charts) and Literata (reading text), both under the SIL Open Font License (`docs/`).

## Local development

Use Node.js 24 and pnpm 11.19.0 (Node 22.12 or later works).

```sh
pnpm install --frozen-lockfile
pnpm dev
```

In another terminal, initialise the **local** CMS and import the report:

```sh
pnpm setup:local
```

Open [the site](http://127.0.0.1:4321) and [the local editor](http://127.0.0.1:4321/_emdash/api/auth/dev-bypass?redirect=/_emdash/admin). The helper is an EmDash development-only endpoint; it does not exist in production. Signed in this way you see the editor view. Local D1, R2 and sessions persist under `.wrangler/`; delete `.wrangler/state` to start again from the seed.

`pnpm dev`, `pnpm build` and `pnpm typecheck` first run `scripts/build-data.mjs`, which reads `report/` and writes `src/generated/` (bundled into the Worker) and the editor-only files (`public/files/` for dev; `dist/client/files/` in a build). These outputs are not committed.

## Where things live

| Path                                             | What it is                                                                                                                                                                                                       |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report/`                                        | The report package as delivered: content, data, charts, sources, tools, working papers, and its own `README.md` (build brief) and `STYLE.md` (writing and token rules).                                          |
| `seed/seed.json`                                 | EmDash schema and initial content, generated from `report/content` by `pnpm content:seed`.                                                                                                                       |
| `scripts/build-data.mjs`                         | Build-time data: page tree, key numbers, sources, glossary, plays, scenarios, data dictionary, search records, charts, files and zip downloads.                                                                  |
| `scripts/build.mjs`                              | `astro build` with the editor-only files added to the assets afterwards.                                                                                                                                         |
| `scripts/charts/`                                | The SVG chart renderer (`pnpm charts:check` renders a preview and checks every chart).                                                                                                                           |
| `src/lib/access.ts`                              | Who sees what.                                                                                                                                                                                                   |
| `src/lib/markdown.ts`, `src/lib/html.ts`         | The report-token renderer and the evidence notes.                                                                                                                                                                |
| `src/lib/front.ts`                               | Reads the argument from the two-minute summary and the part questions from the cover.                                                                                                                            |
| `src/lib/site.ts`, `src/lib/i18n.ts`             | Page tree, parts, URLs, and interface text in English and Vietnamese.                                                                                                                                            |
| `src/styles/tokens.css`, `src/styles/global.css` | The design system: colour tokens (light and dark), type, layout and components.                                                                                                                                  |
| `src/pages/`                                     | Routes: `/`, `/summary`, `/report`, `/report/part-…`, `/report/{id}`, `/briefs/{id}`, `/appendices/{id}`, `/glossary`, `/search`, `/about`; for editors `/workbench`, `/data`, `/files/…`; and `/vi/…` for each. |

## Editorial workflow

- **Report pages** in the EmDash admin holds all 80 pages. Each has a title, a short title, a summary (used for cards and meta descriptions) and a **body in Markdown with the report tokens** exactly as in the package (see `report/STYLE.md`): `[@MAC-04]`, `{VN-direct|High}` (escaped as `{VN-direct\|High}` inside tables), `{fx:projection}`, `{dx:revealed}`, `[[ch07-rules]]`, `{{kn:…}}`, `{{chart:…}}` and `> **Correction.** …` callouts. Save a draft, preview, then publish.
- The home page follows the two-minute summary: each paragraph that opens with a bold lead ("**Why Vietnam.** …") is a step, and the key numbers after it are its tiles. The part pages follow the cover's "What is inside" table.
- Previews need a signed-in Editor or Administrator. Public pages send `private, no-store`.
- The **structure** (which pages exist, their order, part and section, navigation, audiences and reading paths) comes from `report/site-manifest.json` and the page frontmatter, and the **data** (key numbers, sources, charts, CSVs) from `report/data` and `report/charts`. Changing those is a code change: edit `report/`, run `python3 report/tools/validate.py` (needs PyYAML) and `pnpm content:check`, and deploy.
- After first setup, EmDash (D1) is the source of truth for page text. `pnpm content:seed` regenerates the seed from `report/content`; it does **not** overwrite a running CMS.
- The site does not change the substance of the content. Where a chart spec's note was an instruction to the builder rather than a note for readers, `src/lib/charts.ts` shows a reader-facing version; the spec is unchanged.

## Updating to a new report package

1. Replace `report/` with the new package (copy the files tracked in the research repository, without its `CLAUDE.md` and `.gitignore`) and run `python3 report/tools/validate.py` (0 errors).
2. `pnpm content:seed`, then fix anything `pnpm test` reports. The tests fail if a page the interface refers to by role (`ROLE` in `src/lib/site.ts`) was renamed, or if a chart spec has no renderer in `scripts/charts/`.
3. If page ids changed, add the old ids to `src/lib/redirects.ts` so links keep working. If a new appendix should be public, change `src/lib/access.ts`.
4. Deploy, then bring the live CMS in line with the seed. An administrator creates an API token (content read and write) in the admin, and:

   ```sh
   EMDASH_TOKEN=ec_pat_... node scripts/sync-content.mjs --url https://scoping.altprotein.vn          # shows the plan
   EMDASH_TOKEN=ec_pat_... node scripts/sync-content.mjs --url https://scoping.altprotein.vn --apply  # applies it
   ```

   It creates new pages, updates changed ones (EmDash keeps the earlier version as a revision), and moves pages that left the report to the trash. Pages whose text already matches are left alone, so edits made in the CMS since the last package survive unless the package changed the same page.

## Validation

```sh
pnpm content:check     # seed matches report/content; the package validator reports 0 errors
pnpm test              # rendering, tokens, access rules, scores, search, charts
pnpm cf:types
pnpm typecheck
pnpm test:e2e          # every page as public and editor, access to files, widgets, mobile, CMS editing
pnpm charts:check      # optional: chart preview and checks
pnpm build:production
```

For a preinstalled Chromium, set `PLAYWRIGHT_EXECUTABLE=/path/to/chromium` (or `PLAYWRIGHT_CHANNEL=chrome`). Browser tests run only against `127.0.0.1:4321` and restore the page they edit.

GitHub Actions runs these checks on pull requests with read-only permissions. It does not deploy.

See [deployment and recovery](docs/deployment.md).
