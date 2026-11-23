import { chromium } from '/home/sleepy/.local/share/mise/installs/node/26.5.0/lib/node_modules/omniroute/node_modules/playwright-core/index.mjs';
const b = await chromium.launch({ executablePath: '/usr/bin/brave' });
const p = await b.newPage();
await p.goto('file://' + process.argv[2], { waitUntil: 'load' });
await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, displayHeaderFooter: true,
  margin: { top: '12mm', bottom: '14mm', left: '13mm', right: '13mm' },
  headerTemplate: '<span></span>',
  footerTemplate: '<div style="font-family:Noto Sans,sans-serif;font-size:7.5pt;color:#8a92a3;width:100%;padding:0 13mm;display:flex;justify-content:space-between"><span>Yoga · Study Notes · Sem-1</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>' });
await b.close();
