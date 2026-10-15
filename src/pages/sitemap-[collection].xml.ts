import type { APIRoute } from 'astro';

/**
 * EmDash would serve a sitemap per collection listing every published page, including the
 * appendices that only editors can read. The site's own /sitemap.xml lists the public pages.
 */
export const GET: APIRoute = () =>
  new Response('Not found', { status: 404, headers: { 'Cache-Control': 'public, max-age=3600' } });
