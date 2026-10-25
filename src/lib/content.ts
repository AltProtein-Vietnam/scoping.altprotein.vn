import { getEmDashEntry } from 'emdash';
import { renderMarkdown, type RenderResult } from './markdown';
import type { Lang } from './i18n';
import { PAGE_BY_ID } from './site';

export interface PageData {
  id: string;
  title: string;
  short_title: string;
  subtitle?: string | null;
  summary?: string | null;
  body: string;
  updatedAt?: Date | string;
}

export function mayPreview(user?: { role: number }) {
  return Boolean(user && user.role >= 40);
}

/**
 * Load a report page from EmDash. Returns null when it does not exist or is unpublished.
 * `editing` is true in EmDash's edit mode (the toolbar switch, for signed-in editors): the entry
 * is the latest draft, `entry.edit` marks the elements that show its fields, and EmDash reports
 * the request as a preview too, so the render is not cached.
 */
export async function loadPage(id: string) {
  const result = await getEmDashEntry<'pages', PageData>('pages', id);
  if (result.error && result.error.name !== 'LiveEntryNotFoundError')
    throw new Error(`Unable to load page ${id}`, { cause: result.error });
  // Outside edit mode the edit proxy is a no-op with no keys.
  const editing = Boolean(result.entry && Object.keys(result.entry.edit).length > 0);
  return { entry: result.entry, isPreview: Boolean(result.isPreview), editing };
}

// Rendering is pure, so cache it per isolate by page, revision, language and view.
const cache = new Map<string, RenderResult>();
export function renderPage(
  id: string,
  body: string,
  lang: Lang,
  version: string,
  preview: boolean,
  editor = false,
): RenderResult {
  const page = PAGE_BY_ID.get(id);
  const key = `${id}|${lang}|${version}|${editor ? 'e' : 'p'}|${body.length}`;
  const hit = !preview && cache.get(key);
  if (hit) return hit;
  const result = renderMarkdown(body, { lang, contentLang: page?.lang, pageId: id, editor });
  if (!preview) {
    if (cache.size > 320) cache.delete(cache.keys().next().value!);
    cache.set(key, result);
  }
  return result;
}
