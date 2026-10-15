// Build the site: generate the build-time data, run `astro build`, then add the editor-only files.
//
// The editor-only files (data, Markdown, zips) must not be in public/: Astro's Cloudflare handler
// serves every public file straight from the asset binding, before any route runs. So they are
// written to .files-build/ and copied into the built assets (dist/client/files/) afterwards, where
// the `run_worker_first` rule in wrangler.jsonc sends their requests to the Worker, which checks
// the editor session (src/pages/files/[...path].ts) before fetching them.
//
// Workers Builds deploys the production branch with a plain `wrangler deploy`, which uses the
// configuration Astro generates at build time. So when Workers Builds builds `main`, select the
// production environment in wrangler.jsonc; preview branches and local builds keep the default
// (non-production) bindings. An explicit CLOUDFLARE_ENV always wins.
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';

const env = { ...process.env };
if (!env.CLOUDFLARE_ENV && env.WORKERS_CI === '1' && env.WORKERS_CI_BRANCH === 'main')
  env.CLOUDFLARE_ENV = 'production';
if (env.CLOUDFLARE_ENV) console.log(`Building for Cloudflare environment: ${env.CLOUDFLARE_ENV}`);

const STAGING = '.files-build';
for (const [cmd, args] of [
  [process.execPath, ['scripts/build-data.mjs', '--files-out', STAGING]],
  ['pnpm', ['exec', 'astro', 'build']],
]) {
  const result = spawnSync(cmd, args, { stdio: 'inherit', env });
  if (result.status !== 0) process.exit(result.status ?? 1);
}

const client = 'dist/client';
if (!fs.existsSync(client)) throw new Error(`${client} is missing after astro build`);
if (fs.existsSync(`${client}/files`))
  throw new Error(`${client}/files came from public/: restricted files would be served openly`);
fs.cpSync(STAGING, `${client}/files`, { recursive: true });
fs.rmSync(STAGING, { recursive: true, force: true });
console.log(`Added the editor-only files to ${client}/files.`);
