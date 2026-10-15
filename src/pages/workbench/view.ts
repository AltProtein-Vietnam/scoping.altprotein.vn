import type { APIRoute } from 'astro';
import { VIEW_COOKIE } from '../../lib/access';

/** Editors switch between the editor view and the public view (a cookie; no data changes). */
export const GET: APIRoute = ({ url, cookies, redirect, locals }) => {
  const back = url.searchParams.get('back') ?? '/';
  // Only same-site paths, never a full URL or a protocol-relative one.
  const target = /^\/(?!\/)/.test(back) ? back : '/';
  if (!locals.canEdit) return redirect(target, 302);
  if (url.searchParams.get('mode') === 'public')
    cookies.set(VIEW_COOKIE, 'public', {
      path: '/',
      httpOnly: true,
      sameSite: 'lax',
      secure: url.protocol === 'https:',
      maxAge: 60 * 60 * 8,
    });
  else cookies.delete(VIEW_COOKIE, { path: '/' });
  return redirect(target, 302);
};
