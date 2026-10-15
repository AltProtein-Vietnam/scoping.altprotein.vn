import type { APIRoute } from 'astro';
import { isRestrictedPage } from '../lib/access';
import { PAGES, PART_LIST, localize, pagePath, partPath } from '../lib/site';

/** Public pages only: the appendices, data and files shared with reviewers are left out. */
export const GET: APIRoute = ({ site }) => {
  const paths = [
    ...PAGES.filter((p) => !isRestrictedPage(p.id)).map((p) => pagePath(p.id)),
    ...PART_LIST.map((p) => partPath(p.key)),
    '/report',
    '/briefs',
    '/glossary',
    '/about',
  ];
  const urls = paths
    .flatMap((p) => [p, localize(p, 'vi')])
    .map((p) => `<url><loc>${new URL(p, site).href}</loc></url>`);
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls.join('')}</urlset>\n`,
    {
      headers: {
        'Content-Type': 'application/xml; charset=utf-8',
        'Cache-Control': 'public, max-age=3600',
      },
    },
  );
};
