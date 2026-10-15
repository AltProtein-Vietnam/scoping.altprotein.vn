# Deploying scoping.altprotein.vn

The site runs as the Cloudflare Worker `altprotein-scoping` in the Parker Vu Cloudflare account, on the custom domain `scoping.altprotein.vn`. Bindings are set in `wrangler.jsonc` under `env.production`:

| Binding   | Resource                      | Purpose                                                         |
| --------- | ----------------------------- | --------------------------------------------------------------- |
| `DB`      | D1 database                   | Page content, revisions, schema, CMS settings, users            |
| `MEDIA`   | R2 `altprotein-scoping-media` | CMS media and backups                                           |
| `SESSION` | KV namespace                  | Editor sessions                                                 |
| `ASSETS`  | Worker static assets          | CSS, JS, fonts, logo; editor-only data and zips under `/files/` |

The Worker upload is about 6.2 MB gzipped for report v0.10 (EmDash, the bundled seed of about 4 MB, and the build-time charts and data), within the 10 MB limit of the Workers Paid plan. Static assets (about 31 MB, including the editor-only files in `dist/client/files/`) are served by Workers static assets.

## 1. Validate and build

Use the checked-in lockfile and Node.js 24, and run the checks in the README. Then:

```sh
pnpm exec wrangler login
pnpm build:production
```

`build:production` regenerates `src/generated/` and the editor-only files from `report/`, builds with the production bindings, and then copies the files into `dist/client/files/`. Inspect `dist/server/wrangler.json` before deploying: it must name `altprotein-scoping` and the production D1 and R2 resources, and its `assets` must keep `"run_worker_first": ["/files/*"]`.

## 1a. Files for editors only

The data tables, Markdown files and zips are shared with reviewers only (see "Who sees what" in the README). Two things keep them closed:

- They are **not in `public/`** in a build. Astro's Cloudflare handler serves any file it found in `public/` straight from the asset binding, before routes or middleware run. `scripts/build.mjs` writes the files to `.files-build/` and copies them into `dist/client/files/` after `astro build`, and fails if `dist/client/files/` already came from `public/`.
- **`run_worker_first: ["/files/*"]`** in `wrangler.jsonc` (top level and `env.production`) sends those requests to the Worker before the asset server. `src/pages/files/[...path].ts` answers 403 without an Editor or Administrator session and otherwise fetches the asset with `private, no-store`.

So the build command must stay `pnpm build` (or `pnpm build:production`): a plain `astro build` would leave the files out. Tested on 15 October 2026 with `wrangler dev --local` on the production build: anonymous requests for files and zips got 403, and the route served the CSV and zip through the asset binding once past the session check.

## 2. Automatic deploys (Workers Builds)

Workers Builds is connected to this repository. A push to `main` builds with `pnpm build` and deploys with `wrangler deploy`. Other branches get previews, built with `pnpm build` and deployed with `wrangler preview`.

The previews fail at the deploy step, so pull requests show a red "Workers Builds: altprotein-scoping" check. A preview uses the top-level environment of `wrangler.jsonc`, which has no IDs for D1 or KV, and stops with "binding SESSION of type kv_namespace must have a namespace_id specified". That check says nothing about the code: the GitHub Actions `check` builds and tests every branch. To end the red check, either give the top-level environment its own preview D1 database, KV namespace and R2 bucket, or turn previews off under the Worker's Settings, Builds.

Each preview has its own build configuration in the Cloudflare API, under its own ID, which reports its branch as the "production" branch. Do not mistake it for the Worker's: the Worker `altprotein-scoping` builds `main`.

The repository moved from `parkervu/scoping.altprotein.vn` to the `AltProtein-Vietnam` organisation after the v0.7 deploy (30 September 2026). Workers Builds then received no pushes, so the merge of report v0.8 was not built, until it was reconnected to `AltProtein-Vietnam/scoping.altprotein.vn` on 1 October 2026. Reconnecting does not build commits already on `main`; the next push does. If the repository moves again, reconnect it under the Worker's Settings, Builds, and check that the next merge to `main` shows a "Workers Builds: altprotein-scoping" check.

`pnpm build` (`scripts/build.mjs`) selects the `production` environment of `wrangler.jsonc` when Workers Builds builds `main` (`WORKERS_CI=1` and `WORKERS_CI_BRANCH=main`), so production deploys bind the production D1, R2 and KV. Preview branches and local builds keep the default bindings (`altprotein-scoping-local` and `altprotein-scoping-media-local`), so code under review never touches production data. Setting `CLOUDFLARE_ENV` explicitly overrides this. If the Workers Builds build command is changed from `pnpm build` (or `npm run build`), keep this behaviour, or set the deploy command to `pnpm deploy:production`.

## 3. Replacement of the first edition (done on 24 September 2026)

Edition 1.1 replaced the first site's `report` and `chapters` collections with one `pages` collection, on a new database:

- Production `DB` is `altprotein-scoping-v2` (`0d53e2ec-79d3-4fd9-8638-ceb2cae66f86`, APAC).
- The edition 1 database `altprotein-scoping` (`24951da1-734d-45c8-91ca-8a72934de162`) is unchanged and kept as a backup. An SQL export is in the private R2 bucket at `backups/d1-altprotein-scoping-edition-1-2026-09-24.sql`.
- The content was imported with EmDash's setup endpoint (bundled content included). The first attempt stopped after 51 of 57 pages; rerunning it is safe because existing entries are skipped, and the second run created the remaining 6.
- The administrator registers a passkey in the setup wizard at `/_emdash/admin`.

To repeat this on a fresh database: export the current one, `wrangler d1 create <name> --location apac`, set its name and id under `env.production.d1_databases`, merge (or `pnpm deploy:production`), then complete the setup wizard straight away, including the bundled content. Until an administrator exists, the first visitor to the wizard can claim that role. Check: the admin lists 57 published Report pages; `/`, `/summary`, `/tom-tat`, `/report/ch11-plays`, `/report/ch18-scenarios-2050`, `/data/companies`, `/search?q=cassava`, `/glossary`, `/vi` and `/sitemap.xml` load; `/chapters/anything` redirects to `/report`; an anonymous `?_preview=x` request gets 403.

**Rollback:** point `DB` back at the old database id and deploy the previous release (the commit before edition 1.1) with `wrangler rollback` or a redeploy. Do not point the edition 1.1 code at the old database: its schema has no `pages` collection.

## 4. Content updates from a new package

Deploying never changes page text in the CMS. After deploying a new package, run `scripts/sync-content.mjs` as described in the README (plan first, then `--apply`), with an EmDash API token created by an administrator. Moving from edition 1.1 (57 pages) to v0.6 (81 pages) creates 66 pages, updates 15 and moves the 42 pages whose ids changed to the trash; their old URLs redirect (`src/lib/redirects.ts`). Moving from v0.6 to v0.7 updates 79 pages and leaves 2 unchanged; it creates and trashes none. Moving from v0.7 to v0.8 updates all 81 pages; it creates and trashes none. Moving from v0.8 to v0.10 creates 1 page (Appendix S14, the solutions screen), updates 69 and leaves 12 unchanged; it trashes none. The page text changes with the deploy's key numbers and charts, so deploy first: run the sync only once the new release is live.

## 5. Subsequent deploys

- Build from the lockfile, run CI, and deploy the same reviewed build (`pnpm deploy:production`). Deploying never overwrites page text edited in the CMS.
- Changes to data, charts, key numbers, sources or the page structure are made in `report/` and ship with a deploy. Changes to page text are made in the CMS. If the same page text changes in `report/content` too, copy it into the CMS by hand (or on a fresh setup the seed carries it).
- Before a schema or dependency upgrade, export D1 and create an EmDash backup; store exports outside Git and `public/`.

```sh
pnpm exec wrangler d1 export <database-name> --remote --env production --output <private-backup-path.sql>
pnpm exec wrangler versions list --env production
```

A code rollback does not undo data migrations or content edits. Recover content through EmDash revisions and backups.

## 6. EmDash 1.0 (September 2026)

The site moved from EmDash 0.38 to 1.0.1. It uses none of the APIs that 1.0 removed ([upgrade guide](https://docs.emdashcms.com/upgrade-to-v1/)). On the first request after the deploy, the Worker applies twelve core migrations (up to `089_auto_seed_completion`) to the production D1. They have no undo step, so export the database before merging:

```sh
pnpm exec wrangler d1 export altprotein-scoping-v2 --remote --env production --output <private-backup-path.sql>
```

A code rollback to 0.38 does not reverse the migrations. To go back, restore the database to its state before the deploy (from the export or D1 Time Travel) and redeploy the previous version at the same time. Tested locally: a 0.38 database holding the v0.7 pages migrated on first start, the browser tests passed, and `scripts/sync-content.mjs` moved the pages from v0.6 to v0.7 and back.

## 7. Checks after deploying v0.10

Without signing in:

- `/`, `/report`, `/report/part-ii`, `/report/ch26-plays`, `/briefs/brief-policy`, `/glossary`, `/appendices/app-r4-sources`, `/vi` and `/sitemap.xml` load.
- `/appendices/app-s4-feedstocks`, `/appendices/app-r1-open-questions`, `/data`, `/workbench`, `/files/data/companies.csv` and `/files/downloads/altprotein-vn-data.zip` return 403; `/_emdash/api/search?q=cassava` returns 403; `/sitemap-pages.xml` returns 404.
- `/downloads/altprotein-vn-data.zip` redirects to `/files/downloads/altprotein-vn-data.zip`.

Signed in as an Editor or Administrator: the editor bar shows; `/workbench`, the appendices, `/data/companies` and the zips open; "See the public view" shows the sign-in notice on an appendix and "Back to the editor view" returns.

## Notes

- `workers.dev` and version preview URLs are disabled; the custom domain route is in `wrangler.jsonc`.
- R2 is private. Do not expose the bucket: backups may share it with media.
- The scheduled handler runs EmDash maintenance every minute. Observability is enabled; check Worker logs after deploying.
- No analytics, email sending, paid plugins or AI Search are configured. Previews are limited to signed-in Editors and Administrators.

References: [EmDash deployment](https://docs.emdashcms.com/deployment/cloudflare/), [seed behaviour](https://docs.emdashcms.com/themes/seed-files/), [authentication](https://docs.emdashcms.com/guides/authentication/), [evolving a deployed site](https://docs.emdashcms.com/deployment/schema-evolution/).
