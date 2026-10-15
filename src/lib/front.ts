// Structured views of two front pages, read from their Markdown so the home page and the part
// pages follow whatever editors publish in the CMS:
// - the cover's "What is inside" table gives the question each part answers;
// - the two-minute summary gives the argument, one bold-led paragraph per step.

/** Part numeral ("II") to the cover's "What it answers" cell. */
export function coverPartAnswers(body: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (const line of body.split('\n')) {
    const cells = line.split('|').map((c) => c.trim());
    // | II. Supply | What Vietnam could make ... | [[ch04-asset-map]] · ... |
    const m = /^([IVX]+)\.\s/.exec(cells[1] ?? '');
    if (m && cells[2]) out[m[1]] = cells[2];
  }
  return out;
}

export interface Step {
  /** The bold lead, without its full stop ("Why Vietnam"). */
  lead: string;
  /** The step's Markdown without the lead and without key-number embeds. */
  body: string;
  /** Key numbers embedded after the step, in order. */
  kn: string[];
  /** Pages the step cross-links, in order. */
  pages: string[];
}

export interface Argument {
  /** The opening paragraph (the scope statement). */
  lede: Step | null;
  steps: Step[];
}

/**
 * Split the two-minute summary into steps. A step starts at a paragraph that opens with a bold
 * lead ("**Why Vietnam.** ...") and takes the blocks after it (lists, key numbers) up to the next
 * lead. The draft callout, the title and the closing "Read next" line are left out.
 */
export function parseArgument(body: string): Argument {
  const blocks = body
    .replace(/\r\n/g, '\n')
    .split(/\n{2,}/)
    .map((b) => b.trim())
    .filter(Boolean);
  const steps: Step[] = [];
  let current: Step | null = null;
  for (const block of blocks) {
    if (block.startsWith('# ') || block.startsWith('>') || block === '---') continue;
    const lead = /^\*\*([^*]+?)\.?\*\*\s*([\s\S]*)$/.exec(block);
    if (lead && !/^(Read next|Đọc tiếp)/i.test(lead[1])) {
      current = { lead: lead[1].replace(/[.:]$/, ''), body: lead[2], kn: [], pages: [] };
      steps.push(current);
      continue;
    }
    if (lead) {
      current = null;
      continue;
    }
    if (!current) continue;
    const embeds = [...block.matchAll(/\{\{kn:([a-z0-9-]+)\}\}/g)].map((m) => m[1]);
    const rest = block.replace(/\{\{kn:[a-z0-9-]+\}\}/g, '').trim();
    current.kn.push(...embeds);
    if (rest) current.body += `\n\n${rest}`;
  }
  for (const step of steps)
    step.pages = [
      ...new Set([...step.body.matchAll(/\[\[([a-z0-9-]+)(?:#[a-z0-9-]+)?\]\]/g)].map((m) => m[1])),
    ];
  const [first, ...rest] = steps;
  // The first paragraph states the scope; it opens the page rather than being a step.
  const isScope = first && first.kn.length === 0 && first.pages.length === 0;
  return isScope ? { lede: first, steps: rest } : { lede: null, steps };
}
