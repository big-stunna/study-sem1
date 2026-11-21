import { chromium } from '/home/sleepy/.local/share/mise/installs/node/26.5.0/lib/node_modules/omniroute/node_modules/playwright-core/index.mjs';
const b = await chromium.launch({ executablePath: '/usr/bin/brave' });
const p = await b.newPage();
await p.goto('file://' + process.argv[2], { waitUntil: 'networkidle' });
await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, displayHeaderFooter: true,
  margin: { top: '16mm', bottom: '18mm', left: '15mm', right: '15mm' },
  headerTemplate: '<span></span>',
  footerTemplate: '<div style="font-family:Inter,sans-serif;font-size:7.5pt;color:#8a92a3;width:100%;padding:0 15mm;display:flex;justify-content:space-between"><span>Unit 5 · Feedback Amplifiers &amp; Electronic Systems · Fundamentals of Electronics</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>' });
await b.close();
