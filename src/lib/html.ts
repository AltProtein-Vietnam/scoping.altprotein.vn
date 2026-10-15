import { t, type Lang } from './i18n';

export const escapeHtml = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const e = escapeHtml;

export type Scope = 'direct' | 'adjacent' | 'general';
export const scopeOf = (label: string): Scope =>
  label === 'VN-direct' ? 'direct' : label === 'VN-adjacent' ? 'adjacent' : 'general';

/** One evidence statement: the report's {VN-direct|High} {fx:...} {dx:...} tokens for a claim. */
export interface Evidence {
  label?: string;
  confidence?: string;
  fx?: string;
  dx?: string;
}

/** Three-step confidence meter (decorative; the sentence carries the meaning). */
export function meter(confidence: string): string {
  const c = confidence.toLowerCase();
  return `<span class="meter" data-conf="${e(c)}" aria-hidden="true"><i></i><i></i><i></i></span>`;
}

/** The full sentence a screen reader hears, and the tooltip text. */
export function evidenceSentence(ev: Evidence, lang: Lang): string {
  const s = t(lang);
  const parts: string[] = [];
  if (ev.label && ev.confidence) {
    const scope = scopeOf(ev.label);
    parts.push(
      `${s.evidenceLabel}: ${s.scopeLong[scope]}; ${s.confLong[ev.confidence.toLowerCase()] ?? ev.confidence}.`,
    );
  }
  if (ev.fx) parts.push(`${s.foresightLabel}: ${s.fx[ev.fx] ?? ev.fx}, ${s.fxLong[ev.fx] ?? ''}.`);
  if (ev.dx) parts.push(`${s.demandLabel}: ${s.dx[ev.dx] ?? ev.dx}, ${s.dxLong[ev.dx] ?? ''}.`);
  return parts.join(' ');
}

/**
 * The evidence note for a claim. On wide screens it floats into the margin beside the line that
 * holds the claim; on narrow screens, and inside tables and callouts, it is a small inline mark.
 * `nums` are the per-page source numbers of the claim's citations, shown so the eye can match
 * the note to the superscript in the text.
 */
export function evidenceNote(
  ev: Evidence,
  lang: Lang,
  opts: { nums?: number[]; inline?: boolean } = {},
): string {
  const s = t(lang);
  const bits: string[] = [];
  if (opts.nums?.length && !opts.inline)
    bits.push(`<span class="evn-nums">${opts.nums.join(', ')}</span>`);
  if (ev.label && ev.confidence) {
    const scope = scopeOf(ev.label);
    const conf = ev.confidence.toLowerCase();
    bits.push(
      `${meter(conf)}<span class="evn-scope" data-ev="${scope}">${e(s.scope[scope])}</span><span class="evn-conf"> · ${e(s.conf[conf] ?? ev.confidence)}</span>`,
    );
  }
  if (ev.fx)
    bits.push(`<span class="evn-tag" data-fx="${e(ev.fx)}">${e(s.fx[ev.fx] ?? ev.fx)}</span>`);
  if (ev.dx)
    bits.push(`<span class="evn-tag" data-dx="${e(ev.dx)}">${e(s.dx[ev.dx] ?? ev.dx)}</span>`);
  const sentence = evidenceSentence(ev, lang);
  const kinds = [ev.label ? 'ev' : '', ev.fx ? `fx-${ev.fx}` : '', ev.dx ? `dx-${ev.dx}` : '']
    .filter(Boolean)
    .join(' ');
  return `<span class="evn${opts.inline ? ' is-inline' : ''}" data-kinds="${kinds}" title="${e(sentence)}"><span class="evn-body" aria-hidden="true">${bits.join(' ')}</span><span class="visually-hidden">${e(sentence)}</span></span>`;
}

/** A compact inline mark for tiles, charts and widgets (never floated). */
export function evidenceBadge(label: string, confidence: string, lang: Lang): string {
  return evidenceNote({ label, confidence }, lang, { inline: true });
}

export function foresightBadge(type: string, lang: Lang): string {
  return evidenceNote({ fx: type }, lang, { inline: true });
}

export function demandBadge(type: string, lang: Lang): string {
  return evidenceNote({ dx: type }, lang, { inline: true });
}
