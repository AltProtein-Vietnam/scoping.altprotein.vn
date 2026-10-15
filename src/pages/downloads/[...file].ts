import type { APIRoute } from 'astro';
import { FILES_PREFIX } from '../../lib/access';

/** Zip downloads moved under /files/ (editors only) in the v0.10 site. */
export const GET: APIRoute = ({ params, redirect }) =>
  redirect(`${FILES_PREFIX}/downloads/${params.file ?? ''}`, 301);
