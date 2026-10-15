import type { APIRoute } from 'astro';
import { env } from 'cloudflare:workers';

/**
 * Data, Markdown and zip files, served only to signed-in Editors and Administrators.
 * The files are static assets under /files/ (written by scripts/build-data.mjs). The
 * `run_worker_first` rule in wrangler.jsonc sends these requests to the Worker before the
 * asset server, so this check runs first; then the asset server answers.
 */
export const GET: APIRoute = async ({ request, locals, url }) => {
  if (!locals.canEdit)
    return new Response('Editor sign-in is required for this file.', {
      status: 403,
      headers: {
        'Content-Type': 'text/plain; charset=utf-8',
        'Cache-Control': 'private, no-store',
        'X-Robots-Tag': 'noindex',
      },
    });
  const asset = await env.ASSETS.fetch(new Request(url, request));
  const headers = new Headers(asset.headers);
  headers.set('Cache-Control', 'private, no-store');
  headers.set('X-Robots-Tag', 'noindex');
  if (/\.(csv|md)$/.test(url.pathname) && !/charset/i.test(headers.get('Content-Type') ?? ''))
    headers.set(
      'Content-Type',
      `${url.pathname.endsWith('.md') ? 'text/markdown' : 'text/csv'}; charset=utf-8`,
    );
  return new Response(asset.body, { status: asset.status, headers });
};
