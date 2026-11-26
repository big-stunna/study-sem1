// Usage: bun build.mjs <content.mjs> <out.pdf>   (content exports meta, blocks)
import puppeteer from "puppeteer-core";
import { render } from "./lib.mjs";
import { writeFileSync } from "node:fs";
import { execSync } from "node:child_process";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";

const [, , contentPath, outPath] = process.argv;
const { meta, blocks } = await import(pathToFileURL(resolve(contentPath)).href);
const browser = await puppeteer.launch({ executablePath: "/usr/bin/brave", headless: "new", args: ["--no-sandbox", "--allow-file-access-from-files"] });

async function pdf(pages) {
  const html = render(meta, blocks, pages);
  const tmp = resolve(outPath + ".html");
  writeFileSync(tmp, html);
  const page = await browser.newPage();
  await page.goto(pathToFileURL(tmp).href, { waitUntil: "networkidle0" });
  await page.evaluateHandle("document.fonts.ready");
  await page.pdf({
    path: outPath, format: "A4", printBackground: true, displayHeaderFooter: true,
    margin: { top: "20mm", bottom: "20mm", left: "20mm", right: "20mm" },
    headerTemplate: `<div style="font:8px sans-serif;color:#6b6b70;width:100%;padding:0 20mm;display:flex;justify-content:space-between"><span>${meta.header}</span><span>${meta.eyebrow}</span></div>`,
    footerTemplate: `<div style="font:8px sans-serif;color:#6b6b70;width:100%;padding:0 20mm;display:flex;justify-content:space-between"><span>Adani University · Differential Calculus</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
  });
  await page.close();
}

// pass 1: no page numbers; locate headings via pdftotext; pass 2: with numbers
await pdf({});
const n = +execSync(`pdfinfo "${outPath}" | awk '/Pages/{print $2}'`).toString();
const pages = {};
for (let i = 1; i <= n; i++) {
  const tx = execSync(`pdftotext -f ${i} -l ${i} "${outPath}" -`).toString();
  for (const m of tx.matchAll(/@@([A-Za-z0-9]+)@@/g)) if (!(m[1] in pages)) pages[m[1]] = i;
}
await pdf(pages);
await browser.close();
console.log("built", outPath, n, "pages");
