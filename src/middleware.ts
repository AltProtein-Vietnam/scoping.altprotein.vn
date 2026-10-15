import { defineMiddleware } from 'astro:middleware';
import { VIEW_COOKIE, isEditorUser } from './lib/access';

const json = (status: number, message: string) =>
  new Response(JSON.stringify({ error: { code: 'FORBIDDEN', message } }), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'private, no-store' },
  });

/**
 * Runs after EmDash's middleware, which sets `locals.user` from the editor session.
 * - `/vi/...` serves the same pages with a Vietnamese interface.
 * - `locals.canEdit` is true for signed-in Editors and Administrators; `locals.editor` is true
 *   when they have not switched to the public view. Pages, links, search and files read these.
 * - EmDash's own site-search endpoints are public by default and would return text from the
 *   restricted appendices, so they are closed to visitors without an editor session.
 */
export const onRequest = defineMiddleware((context, next) => {
  const { pathname, search } = context.url;
  const canEdit = isEditorUser(context.locals.user);
  context.locals.canEdit = canEdit;
  context.locals.editor = canEdit && context.cookies.get(VIEW_COOKIE)?.value !== 'public';

  if (pathname === '/_emdash/api/search' || pathname === '/_emdash/api/search/suggest') {
    if (!canEdit) return json(403, 'Search is available on the site at /search.');
    return next();
  }

  if (pathname === '/vi' || pathname.startsWith('/vi/')) {
    const rest = pathname.slice(3) || '/';
    context.locals.lang = 'vi';
    context.locals.basePath = rest;
    return next(rest + search);
  }
  context.locals.lang ??= 'en';
  context.locals.basePath ??= pathname;
  return next();
});
