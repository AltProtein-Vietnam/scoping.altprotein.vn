// Progressive enhancement for every page. Everything here is optional: pages work without it.
import { initPlays } from './plays';
import { initScenarios } from './scenarios';

const root = document.documentElement;
const store = {
  get(key: string) {
    try {
      return localStorage.getItem(key);
    } catch {
      return null;
    }
  },
  set(key: string, value: string | null) {
    try {
      if (value === null) localStorage.removeItem(key);
      else localStorage.setItem(key, value);
    } catch {
      /* storage unavailable: the choice lasts for this page only */
    }
  },
};

// Theme: auto -> light -> dark -> auto --------------------------------------------------
document.querySelectorAll<HTMLButtonElement>('[data-theme-toggle]').forEach((btn) => {
  const names: Record<string, string> = JSON.parse(btn.dataset.names ?? '{}');
  const base = btn.getAttribute('aria-label') ?? 'Theme';
  const label = () => {
    const current = root.getAttribute('data-theme') ?? 'auto';
    btn.setAttribute('aria-label', `${base}: ${names[current] ?? current}`);
  };
  label();
  btn.addEventListener('click', () => {
    const current = root.getAttribute('data-theme');
    const next = current === null ? 'light' : current === 'light' ? 'dark' : null;
    if (next) root.setAttribute('data-theme', next);
    else root.removeAttribute('data-theme');
    store.set('theme', next);
    label();
  });
});

// Drawer (menu and contents) ----------------------------------------------------------------
const drawer = document.getElementById('drawer');
let opener: HTMLElement | null = null;
function setDrawer(open: boolean, from?: HTMLElement) {
  if (!drawer) return;
  if (open) {
    opener = from ?? null;
    drawer.setAttribute('data-open', '');
    document.body.style.overflow = 'hidden';
    drawer.querySelector('[aria-current="page"]')?.scrollIntoView({ block: 'center' });
    drawer.querySelector<HTMLElement>('input, a, button')?.focus();
  } else {
    drawer.removeAttribute('data-open');
    document.body.style.overflow = '';
    opener?.focus();
  }
  document
    .querySelectorAll('[data-drawer-open]')
    .forEach((b) => b.setAttribute('aria-expanded', String(open)));
}
document.querySelectorAll<HTMLElement>('[data-drawer-open]').forEach((el) =>
  el.addEventListener('click', (e) => {
    e.preventDefault();
    setDrawer(true, el);
  }),
);
drawer
  ?.querySelectorAll('[data-drawer-close]')
  .forEach((el) => el.addEventListener('click', () => setDrawer(false)));

// Audience: highlight pages written for the chosen audience and show its reading path --------
export function applyAudience(audience: string | null) {
  if (audience) root.setAttribute('data-audience', audience);
  else root.removeAttribute('data-audience');
  document.querySelectorAll<HTMLElement>('[data-aud]').forEach((el) => {
    const list = (el.dataset.aud ?? '').split(' ');
    el.classList.toggle('is-for-you', Boolean(audience && list.includes(audience)));
  });
  document.querySelectorAll<HTMLElement>('.aud-chip[data-key]').forEach((el) => {
    el.classList.toggle('is-you', el.dataset.key === audience);
  });
  document.querySelectorAll<HTMLElement>('[data-audience-path]').forEach((el) => {
    el.hidden = el.dataset.audiencePath !== audience;
  });
  document.querySelectorAll<HTMLButtonElement>('[data-set-audience]').forEach((b) => {
    b.setAttribute('aria-pressed', String((b.dataset.setAudience || null) === audience));
  });
}
document
  .querySelectorAll<HTMLElement>('[data-audience-picker]')
  .forEach((el) => (el.hidden = false));
const params = new URLSearchParams(location.search);
const fromUrl = params.get('for');
if (fromUrl !== null) store.set('audience', fromUrl || null);
applyAudience(fromUrl !== null ? fromUrl || null : store.get('audience'));
document.querySelectorAll<HTMLButtonElement>('[data-set-audience]').forEach((btn) => {
  btn.addEventListener('click', () => {
    const value = btn.dataset.setAudience || null;
    store.set('audience', value);
    applyAudience(value);
  });
});

// Sources popover: select a citation number to see its sources and the claim's evidence --------
const pop = document.getElementById('pop');
let popOwner: HTMLElement | null = null;
function hidePop(restore = false) {
  if (!pop || pop.hidden) return;
  pop.hidden = true;
  if (restore) popOwner?.focus();
  popOwner = null;
}
function showPop(link: HTMLAnchorElement) {
  if (!pop) return false;
  const sup = link.closest('sup.cite');
  if (!sup) return false;
  const links = [...sup.querySelectorAll<HTMLAnchorElement>('a[data-src]')];
  const items = links
    .map((a) => ({ n: a.textContent ?? '', li: document.getElementById(`src-${a.dataset.src}`) }))
    .filter((x) => x.li);
  if (!items.length) return false;
  pop.replaceChildren();
  const ol = document.createElement('ol');
  for (const { n, li } of items) {
    const item = document.createElement('li');
    item.value = Number(n) || 0;
    item.innerHTML = li!.innerHTML;
    ol.append(item);
  }
  pop.append(ol);
  const note = sup.nextElementSibling;
  if (note?.classList.contains('evn')) {
    const p = document.createElement('p');
    p.className = 'pop-ev';
    p.textContent = note.getAttribute('title') ?? '';
    pop.append(p);
  }
  const all = document.createElement('p');
  all.className = 'pop-all';
  const a = document.createElement('a');
  a.href = '#sources-cited';
  a.textContent = document.getElementById('sources-cited')?.textContent ?? '';
  all.append(a);
  pop.append(all);
  pop.setAttribute('aria-label', a.textContent ?? '');
  pop.hidden = false;
  const r = link.getBoundingClientRect();
  const w = pop.offsetWidth;
  const left = Math.max(12, Math.min(window.innerWidth - w - 12, r.left - 24));
  pop.style.left = `${left + window.scrollX}px`;
  pop.style.top = `${r.bottom + window.scrollY + 8}px`;
  popOwner = link;
  return true;
}
document.addEventListener('click', (e) => {
  const target = e.target as Element;
  const link = target.closest?.<HTMLAnchorElement>('sup.cite a[data-src]');
  if (link) {
    if (popOwner === link) {
      e.preventDefault();
      hidePop();
    } else if (showPop(link)) {
      e.preventDefault();
      if ((e as PointerEvent).pointerType === '') pop?.querySelector('a')?.focus();
    }
    return;
  }
  if (pop && !pop.contains(target)) hidePop();
  if (target.closest?.('#pop a[href="#sources-cited"]')) hidePop();
});
document.addEventListener('keydown', (e) => {
  if (e.key !== 'Escape') return;
  if (pop && !pop.hidden) hidePop(true);
  else if (drawer?.hasAttribute('data-open')) setDrawer(false);
});
window.addEventListener('resize', () => hidePop());

// Tooltips for chart marks -------------------------------------------------------------------
const tip = document.getElementById('tip');
let tipOwner: Element | null = null;
function showTip(target: Element, text: string, x?: number, y?: number) {
  if (!tip || !text) return;
  tipOwner = target;
  tip.textContent = text;
  tip.hidden = false;
  const r = target.getBoundingClientRect();
  const px = x ?? r.left + r.width / 2;
  const py = y ?? r.top;
  const w = tip.offsetWidth;
  const h = tip.offsetHeight;
  tip.style.left = `${Math.max(8, Math.min(window.innerWidth - w - 8, px - w / 2))}px`;
  tip.style.top = `${py - h - 12 < 8 ? py + 18 : py - h - 12}px`;
}
function hideTip() {
  if (tip) tip.hidden = true;
  tipOwner = null;
}
document.querySelectorAll<SVGElement>('.chart-body .mark').forEach((mark) => {
  const title = mark.querySelector(':scope > title');
  const text = mark.getAttribute('data-tip') || title?.textContent || '';
  if (text) {
    mark.setAttribute('data-tip', text);
    mark.setAttribute('aria-label', text);
    mark.setAttribute('role', 'img');
  }
  title?.remove();
});
document.addEventListener('pointerover', (e) => {
  const el = (e.target as Element).closest?.('.chart-body .mark');
  if (!el || el === tipOwner) return;
  showTip(el, el.getAttribute('data-tip') ?? '', e.clientX, e.clientY);
});
document.addEventListener('pointermove', (e) => {
  if (tipOwner && tip && !tip.hidden)
    showTip(tipOwner, tip.textContent ?? '', e.clientX, e.clientY);
});
document.addEventListener('pointerout', (e) => {
  if (tipOwner && !(tipOwner as Element).contains(e.relatedTarget as Node)) hideTip();
});
document.addEventListener('focusin', (e) => {
  const el = (e.target as Element).closest?.('.chart-body .mark');
  if (el) showTip(el, el.getAttribute('data-tip') ?? '');
});
document.addEventListener('focusout', hideTip);
window.addEventListener('scroll', hideTip, { passive: true });

// On this page: mark the section in view ----------------------------------------------------
const tocLinks = [...document.querySelectorAll<HTMLAnchorElement>('.rail-toc a[href^="#"]')];
if (tocLinks.length && 'IntersectionObserver' in window) {
  const byId = new Map(tocLinks.map((a) => [decodeURIComponent(a.hash.slice(1)), a]));
  const headings = [...byId.keys()]
    .map((id) => document.getElementById(id))
    .filter(Boolean) as HTMLElement[];
  let active: HTMLAnchorElement | undefined;
  const visible = new Set<Element>();
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((en) =>
        en.isIntersecting ? visible.add(en.target) : visible.delete(en.target),
      );
      const first = headings.find((h) => visible.has(h));
      const link = first ? byId.get(first.id) : undefined;
      if (link && link !== active) {
        active?.removeAttribute('aria-current');
        link.setAttribute('aria-current', 'true');
        active = link;
      }
    },
    { rootMargin: '-100px 0px -60% 0px' },
  );
  headings.forEach((h) => io.observe(h));
}

// Print button ------------------------------------------------------------------------------
document
  .querySelectorAll('[data-print]')
  .forEach((b) => b.addEventListener('click', () => window.print()));

// Open details that contain a targeted anchor (a play card or a key-number context).
function openTarget() {
  const id = decodeURIComponent(location.hash.slice(1));
  if (!id) return;
  const el = document.getElementById(id);
  if (el instanceof HTMLDetailsElement) el.open = true;
  el?.closest('details')?.setAttribute('open', '');
}
window.addEventListener('hashchange', openTarget);
openTarget();

initPlays();
initScenarios();
