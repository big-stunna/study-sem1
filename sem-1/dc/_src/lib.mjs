// Shared minimalist renderer for DC unit notes.
// Content files export: { meta, blocks } and call helpers below. Run: bun build.mjs <content.mjs> <out.pdf>
import katex from "katex";

const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

// Text -> HTML. Supports $$display$$, $inline$, **bold**, *italic*, `\n\n` paragraph breaks are done by caller.
export function t(s) {
  if (s == null) return "";
  const out = [];
  const re = /\$\$([\s\S]+?)\$\$|\$([^$]+?)\$/g;
  let last = 0, m;
  while ((m = re.exec(s))) {
    out.push(fmt(s.slice(last, m.index)));
    const disp = m[1] !== undefined;
    out.push(katex.renderToString((m[1] ?? m[2]).trim(), { displayMode: disp, throwOnError: true, strict: "ignore", trust: true }));
    last = re.lastIndex;
  }
  out.push(fmt(s.slice(last)));
  return out.join("");
}
const fmt = s => esc(s).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/(^|[^*])\*(?!\*)(.+?)\*/g, "$1<i>$2</i>");

const mk = id => `<span class="mk">@@${id}@@</span>`;
let uid = 0;
const slug = () => "a" + (++uid);

// ---- block constructors (each returns an object; render() turns them into HTML) ----
export const chapter = (title, o = {}) => ({ k: "chapter", title, ...o });          // o.glance = {formula, use, trap}
export const h = title => ({ k: "h", title });
export const p = text => ({ k: "p", text });
export const rule = (title, lines) => ({ k: "rule", title, lines });                 // key formulas box
export const fig = (svg, caption) => ({ k: "fig", svg, caption });
// level: "Easy"|"Medium"|"Hard"; src: e.g. "Prof · Typed p.57 · Q5" | "Tut 3 · P7" | "Book · Thomas 13.4"
export const ex = o => ({ k: "ex", ...o });                                          // {n, level, src, q, steps:[], answer, formula:[], tip}
export const tryit = (items) => ({ k: "try", items });                               // [{q, a}] answers printed at chapter end
export const mistakes = items => ({ k: "mistakes", items });
export const revision = (title, rows) => ({ k: "rev", title, rows });               // rows: [[label, tex]]
export const essentials = (title, blocks) => ({ k: "ess", title, blocks });

export function render(meta, blocks, pages = {}) {
  let chNo = 0;
  const rules = render.rules = [];
  const toc = [];
  const tries = {};      // chapter -> items for answer key
  let curCh = 0;
  const body = [];
  for (const b of blocks) {
    switch (b.k) {
      case "ess":
        body.push(`<section class="ess"><h1 id="ess">${mk("ess")}<span class="no">Essential Rules</span>${t(b.title)}</h1>${b.blocks.map(rb => blk(rb)).join("")}</section>`);
        toc.push({ id: "ess", label: "Essential Rules" });
        break;
      case "chapter": {
        chNo++; curCh = chNo; const id = "ch" + chNo;
        toc.push({ id, label: `${chNo}  ·  ${b.title}`, no: chNo });
        let g = "";
        if (b.glance) g = `<aside class="glance"><div class="lab">In one glance</div><dl>
          <dt>Key idea</dt><dd>${t(b.glance.formula)}</dd><dt>Use when</dt><dd>${t(b.glance.use)}</dd><dt>Watch out</dt><dd>${t(b.glance.trap)}</dd></dl></aside>`;
        body.push(`<h1 id="${id}" class="chap">${mk(id)}<span class="no">Chapter ${chNo}</span>${t(b.title)}</h1>${g}`);
        break;
      }
      case "try": tries[curCh] = (tries[curCh] || []).concat(b.items); body.push(blk(b, curCh)); break;
      case "rev": toc.push({ id: "rev", label: b.title }); body.push(blk(b)); break;
      default: body.push(blk(b));
    }
  }
  // answer key
  const keyHtml = Object.keys(tries).length ? `<section class="key"><h1 id="key">${mk("key")}<span class="no">Answers</span>Try-yourself answers</h1>${
    Object.entries(tries).map(([c, its]) => `<h3>Chapter ${c}</h3><ol>${its.map(i => `<li>${t(i.a)}</li>`).join("")}</ol>`).join("")}</section>` : "";
  const idxHtml = `<section class="idx"><h1 id="idx">${mk("idx")}<span class="no">Index</span>Formula index</h1>${rules.map(r => `<a href="#${r.id}"><span>${r.ch ? "Ch " + r.ch + " · " : ""}${esc(r.title)}</span><span class="dots"></span><span class="pg">${pages[r.id] ?? ""}</span></a>`).join("")}</section>`;
  toc.push({ id: "idx", label: "Formula index" });
  if (keyHtml) toc.push({ id: "key", label: "Try-yourself answers" });

  const tocHtml = `<section class="toc"><h1 class="plain">Contents</h1>${toc.map(e =>
    `<a href="#${e.id}"><span>${esc(e.label)}</span><span class="dots"></span><span class="pg">${pages[e.id] ?? ""}</span></a>`).join("")}</section>`;

  const cover = `<section class="cover"><div class="eyebrow">${esc(meta.eyebrow)}</div><h1>${t(meta.title)}</h1><p class="sub">${t(meta.subtitle)}</p>
    <div class="foot">${esc(meta.foot)}</div></section>`;

  return `<!doctype html><html><head><meta charset="utf-8"><style>${fullCss()}${css}</style></head><body>${cover}${tocHtml}${body.join("")}${idxHtml}${keyHtml}</body></html>`;

  function blk(b, ch) {
    switch (b.k) {
      case "h": return `<h2>${t(b.title)}</h2>`;
      case "p": return `<p>${t(b.text)}</p>`;
      case "rule": { const id = "r" + rules.length; rules.push({ id, title: b.title, ch: chNo }); return `<div class="rule" id="${id}">${mk(id)}<div class="lab">${t(b.title)}</div>${b.lines.map(l => `<div class="ln">${t(l)}</div>`).join("")}</div>`; }
      case "fig": return `<figure>${b.svg}${b.caption ? `<figcaption>${t(b.caption)}</figcaption>` : ""}</figure>`;
      case "ex": {
        const lv = (b.level || "").toLowerCase();
        return `<div class="ex"><div class="exh"><span class="lv ${lv}">${esc(b.level || "")}</span><span class="exn">Example ${b.n ?? ""}</span><span class="src">${esc(b.src || "")}</span></div>
          <div class="q">${t(b.q)}</div>
          ${b.tip ? `<div class="tip"><b>How to recognise it.</b> ${t(b.tip)}</div>` : ""}
          <div class="sol"><div class="main"><div class="lab">Solution</div>${(b.steps || []).map((s, i) => `<div class="step"><span class="sn">${i + 1}</span><div>${t(s)}</div></div>`).join("")}
            <div class="ans"><b>Answer.</b> ${t(b.answer)}</div></div>
            ${b.formula?.length ? `<div class="side"><div class="lab">Formula used</div>${b.formula.map(f => `<div>${t(f)}</div>`).join("")}</div>` : ""}</div></div>`;
      }
      case "try": return `<div class="try"><div class="lab">Try yourself <span class="m">answers at the end</span></div><ol>${b.items.map(i => `<li>${t(i.q)}</li>`).join("")}</ol></div>`;
      case "mistakes": return `<div class="mist"><div class="lab">Common mistakes</div><ul>${b.items.map(i => `<li>${t(i)}</li>`).join("")}</ul></div>`;
      case "rev": return `<section class="rev"><h1 id="rev" class="plain">${mk("rev")}${t(b.title)}</h1><table>${b.rows.map(r => `<tr><th>${t(r[0])}</th><td>${t(r[1])}</td></tr>`).join("")}</table></section>`;
    }
    return "";
  }
}

const css = `
@page { size: A4 }
:root { --ink:#1c1c1e; --mut:#6b6b70; --rule:#d9d9dc; --acc:#2b4acb; --soft:#f6f6f7 }
* { box-sizing: border-box }
html { font: 10.5pt/1.55 "Inter","Noto Sans","DejaVu Sans",sans-serif; color: var(--ink) }
body { margin: 0 }
section.cover, section.toc, section.key, section.rev, section.ess { padding: 0 }
.cover { height: 250mm; display:flex; flex-direction:column; justify-content:center; padding: 0 8mm; page-break-after: always }
.cover .eyebrow { font-size: 9pt; letter-spacing: .18em; text-transform: uppercase; color: var(--mut) }
.cover h1 { font-size: 34pt; font-weight: 600; line-height: 1.12; margin: 10mm 0 6mm; letter-spacing: -.01em }
.cover .sub { color: var(--mut); font-size: 12pt; max-width: 130mm; border-top: 1px solid var(--rule); padding-top: 6mm }
.cover .foot { position:absolute; bottom: 20mm; font-size: 9pt; color: var(--mut) }
.toc { page-break-after: always; padding-top: 4mm }
.toc a { display:flex; gap:6px; color: var(--ink); text-decoration:none; padding: 3.2mm 0; border-bottom: 1px solid var(--rule); font-size: 11pt }
.toc .dots { flex:1 } .toc .pg { color: var(--mut) }
h1 { font-size: 22pt; font-weight: 600; margin: 0 0 7mm; letter-spacing: -.01em; line-height:1.2 }
h1.plain { margin-top: 0 }
h1 .no { display:block; font-size: 8.5pt; letter-spacing:.16em; text-transform:uppercase; color: var(--acc); font-weight:600; margin-bottom: 2mm }
h1.chap { margin-top: 10mm } h1 { break-after: avoid }
.mk { position:absolute; font-size:1px; color:transparent; line-height:0 }
.ess h1, .key h1, .idx h1, .rev h1 { break-before: page }
.toc h1 { break-before: auto }
h2 { font-size: 13pt; font-weight: 600; margin: 9mm 0 3mm; padding-bottom: 1.5mm; border-bottom: 1px solid var(--rule); break-after: avoid }
h3 { font-size: 11pt; margin: 6mm 0 2mm }
p { margin: 0 0 3mm }
.lab { font-size: 8pt; letter-spacing: .12em; text-transform: uppercase; color: var(--mut); font-weight: 600; margin-bottom: 2mm }
.lab .m { text-transform:none; letter-spacing:0; font-weight:400 }
.glance { border-left: 2px solid var(--acc); padding: 1mm 0 1mm 5mm; margin: 0 0 6mm; break-inside: avoid }
.glance dl { display:grid; grid-template-columns: 24mm 1fr; gap: 1.5mm 4mm; margin:0 }
.glance dt { color: var(--mut); font-size: 9pt } .glance dd { margin:0 }
.rule { border: 1px solid var(--rule); border-radius: 3px; padding: 4mm 5mm; margin: 4mm 0; break-inside: avoid; background: var(--soft) }
.rule .ln { margin: 1.5mm 0 }
figure { margin: 5mm 0; text-align:center; break-inside: avoid } figure svg { max-width: 100%; height:auto; color: var(--ink) }
figcaption { font-size: 9pt; color: var(--mut); margin-top: 2mm }
.ex { border: 1px solid var(--rule); border-radius: 3px; margin: 4mm 0; break-inside: auto }
.exh, .q { break-after: avoid } .step, .ans, .side { break-inside: avoid }
.exh { display:flex; gap: 4mm; align-items: baseline; padding: 2.2mm 5mm; border-bottom: 1px solid var(--rule); font-size: 9pt; color: var(--mut) }
.exn { color: var(--ink); font-weight: 600 } .src { margin-left:auto }
.lv { font-weight:600; text-transform: uppercase; letter-spacing:.1em; font-size: 7.5pt }
.lv.easy::before, .lv.medium::before, .lv.hard::before { content:""; display:inline-block; width:6px; height:6px; border-radius:50%; margin-right:5px; background: var(--ink) }
.lv.easy::before { background: transparent; border:1px solid var(--ink) }
.lv.medium::before { background: linear-gradient(90deg, var(--ink) 50%, transparent 50%); border:1px solid var(--ink) }
.q { padding: 3.5mm 5mm 1mm }
.tip { margin: 0 5mm 2mm; font-size: 9.5pt; color: var(--mut) } .tip b { color: var(--ink); font-weight:600 }
.sol { display:grid; grid-template-columns: 1fr 44mm; gap: 6mm; padding: 2mm 5mm 4mm }
.sol:not(:has(.side)) { grid-template-columns: 1fr }
.step { display:flex; gap:3mm; margin: 2mm 0 } .sn { color: var(--acc); font-weight:600; width: 4mm; flex:none }
.ans { margin-top: 3mm; padding-top: 2mm; border-top: 1px solid var(--rule); color: var(--acc) } .ans b { color: var(--ink) }
.side { border-left: 1px solid var(--rule); padding-left: 4mm; font-size: 9.5pt; align-self:start } .side div + div { margin-top: 2mm }
.try, .mist { margin: 6mm 0; break-inside: avoid; border-top: 1px solid var(--ink); padding-top: 3mm }
.try ol, .mist ul { margin: 0; padding-left: 5mm } .try li, .mist li { margin: 1.5mm 0 }
.idx a { display:flex; gap:6px; color:var(--ink); text-decoration:none; padding:1.6mm 0; border-bottom:1px solid var(--rule); font-size:10pt } .idx .dots{flex:1} .idx .pg{color:var(--mut)}
.key ol { padding-left: 6mm } .key li { margin: 1.5mm 0 }
.rev table { width:100%; border-collapse: collapse } .rev th, .rev td { text-align:left; padding: 2.4mm 3mm; border-bottom: 1px solid var(--rule); vertical-align: top; font-weight: 400 }
.rev th { width: 38mm; font-weight:600; font-size: 9.5pt }
.katex { font-size: 1.04em } .katex-display { margin: 2.5mm 0 }
.sol .katex-display { margin: 2mm 0 }
@font-face { font-family: KaTeX_Main; src: local("KaTeX_Main") }
`;

import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
const katexCss = () => {
  const dir = new URL("./node_modules/katex/dist/", import.meta.url).pathname;
  let c = readFileSync(dir + "katex.min.css", "utf8");
  const base = "file://" + encodeURI(dir).replace(/\)/g, "%29").replace(/\(/g, "%28");
  return c.replace(/url\(fonts\/([^)]+)\)/g, (_, f) => `url("${base}fonts/${f}")`);
};
export const fullCss = () => katexCss();
