// Unit 1 content: Limits, Continuity, Differentiability, MVT, Indeterminate forms.
import { essentials, chapter, h, p, rule, fig, ex, tryit, mistakes, revision } from "./lib.mjs";

// String.raw, with any \uXXXX escape that the transpiler inserted for non-ASCII text turned back into the character.
const r = (s, ...v) => String.raw(s, ...v).replace(/\\u([0-9A-Fa-f]{4})/g, (_, h) => String.fromCharCode(parseInt(h, 16)));
let N = 0;
const E = o => ex({ n: ++N, ...o });
// Group of short lettered questions in one card; items: [{q, s (one-line solution), a}]
const G = ({ items, ...o }) => E({ ...o,
  q: items.map((it, i) => `(${"abcdefghijkl"[i]}) ${it.q}`).join(String.raw`$\qquad$`),
  steps: items.map((it, i) => `(${"abcdefghijkl"[i]}) ${it.s}`),
  answer: items.map((it, i) => `(${"abcdefghijkl"[i]}) ${it.a}`).join("; ") });

export const meta = {
  eyebrow: "Differential Calculus · Unit 1",
  title: "Function of a Single Variable",
  subtitle: "Limits, continuity, differentiability, mean value theorems and L'Hôpital's rule",
  foot: "Adani University · CSAM (Sem-I)",
  header: "Differential Calculus · Unit 1 Notes",
};

// ---------- figures (computed so the tangent really is parallel / horizontal) ----------
function bez(P, t) {
  const u = 1 - t;
  return [0, 1].map(i => u ** 3 * P[0][i] + 3 * u * u * t * P[1][i] + 3 * u * t * t * P[2][i] + t ** 3 * P[3][i]);
}
function dbez(P, t) {
  const u = 1 - t;
  return [0, 1].map(i => 3 * u * u * (P[1][i] - P[0][i]) + 6 * u * t * (P[2][i] - P[1][i]) + 3 * t * t * (P[3][i] - P[2][i]));
}
function figure(P, label) {
  const A = P[0], B = P[3];
  const sl = (B[1] - A[1]) / (B[0] - A[0]);
  let best = 0.5, bd = 1e9;
  for (let t = 0.05; t < 0.95; t += 0.001) { const d = dbez(P, t); const e = Math.abs(d[1] / d[0] - sl); if (e < bd) { bd = e; best = t; } }
  const C = bez(P, best), s = sl;
  const L = 70;
  const f = v => v.toFixed(1);
  const y0 = 150;
  return `<svg viewBox="0 0 380 175" width="300" style="max-width:100%" fill="none" stroke="currentColor" stroke-width="1.3">
  <line x1="20" y1="${y0}" x2="365" y2="${y0}" stroke-width="0.8"/>
  <path d="M${P[0][0]} ${P[0][1]} C${P[1][0]} ${P[1][1]} ${P[2][0]} ${P[2][1]} ${P[3][0]} ${P[3][1]}"/>
  <line x1="${f(A[0])}" y1="${f(A[1])}" x2="${f(B[0])}" y2="${f(B[1])}" stroke-dasharray="4 3" stroke-width="1"/>
  <line x1="${f(C[0] - L)}" y1="${f(C[1] - s * L)}" x2="${f(C[0] + L)}" y2="${f(C[1] + s * L)}"/>
  <line x1="${f(A[0])}" y1="${f(A[1])}" x2="${f(A[0])}" y2="${y0}" stroke-width="0.6" stroke-dasharray="2 3"/>
  <line x1="${f(B[0])}" y1="${f(B[1])}" x2="${f(B[0])}" y2="${y0}" stroke-width="0.6" stroke-dasharray="2 3"/>
  <line x1="${f(C[0])}" y1="${f(C[1])}" x2="${f(C[0])}" y2="${y0}" stroke-width="0.6" stroke-dasharray="2 3"/>
  <circle cx="${f(C[0])}" cy="${f(C[1])}" r="2.6" fill="currentColor"/>
  <g fill="currentColor" stroke="none" font-size="12" font-family="serif" font-style="italic" text-anchor="middle">
  <text x="${f(A[0])}" y="${y0 + 14}">a</text><text x="${f(B[0])}" y="${y0 + 14}">b</text><text x="${f(C[0])}" y="${y0 + 14}">c</text></g>
  </svg>`;
}
const figRolle = figure([[50, 110], [110, 10], [230, 10], [330, 110]]);
const figMVT = figure([[50, 120], [120, 10], [230, 130], [330, 50]]);

// =====================================================================
export const blocks = [
  essentials("Rules used throughout Unit 1", [
    rule("Derivative table", [
      r`$(x^n)'=nx^{n-1},\quad (e^x)'=e^x,\quad (a^x)'=a^x\ln a,\quad (\ln x)'=\tfrac1x$`,
      r`$(\sin x)'=\cos x,\ (\cos x)'=-\sin x,\ (\tan x)'=\sec^2x,\ (\cot x)'=-\csc^2x$`,
      r`$(\sec x)'=\sec x\tan x,\ (\csc x)'=-\csc x\cot x,\ (\sinh x)'=\cosh x,\ (\cosh x)'=\sinh x$`,
      r`$(\tan^{-1}x)'=\dfrac{1}{1+x^2},\quad (\sin^{-1}x)'=\dfrac{1}{\sqrt{1-x^2}}$`,
    ]),
    rule("Differentiation rules", [
      r`Product: $(uv)'=u'v+uv'$ $\qquad$ Quotient: $\left(\dfrac uv\right)'=\dfrac{u'v-uv'}{v^2}$`,
      r`Chain: $\dfrac{d}{dx}f(g(x))=f'(g(x))\,g'(x)$`,
    ]),
    rule("Standard limits", [
      r`$\displaystyle\lim_{x\to0}\frac{\sin x}{x}=\lim_{x\to0}\frac{\tan x}{x}=\lim_{x\to0}\frac{\ln(1+x)}{x}=\lim_{x\to0}\frac{e^x-1}{x}=1,\qquad \lim_{x\to0}\frac{1-\cos x}{x^2}=\frac12$`,
      r`$\displaystyle\lim_{x\to0}\frac{a^x-1}{x}=\ln a,\qquad \lim_{x\to\infty}\Big(1+\frac kx\Big)^{x}=e^{k},\qquad \lim_{x\to0}(1+x)^{1/x}=e$`,
    ]),
    rule("Maclaurin series (for limits)", [
      r`$\sin x=x-\dfrac{x^3}{6}+\cdots,\quad \cos x=1-\dfrac{x^2}{2}+\cdots,\quad \tan x=x+\dfrac{x^3}{3}+\cdots$`,
      r`$e^x=1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6}+\cdots,\quad \ln(1+x)=x-\dfrac{x^2}{2}+\cdots,\quad \sinh x=x+\dfrac{x^3}{6}+\cdots$`,
    ]),
    rule("Log trick for powers", [
      r`$y=f(x)^{g(x)}\ \Rightarrow\ \ln y=g(x)\ln f(x)$; find $\lim\ln y=L$, then $\lim y=e^{L}$.`,
    ]),
  ]),

  // =============================== CH 1 ===============================
  chapter("Limits", { glance: {
    formula: r`$\displaystyle\lim_{x\to a}f(x)=L$ exists iff left limit $=$ right limit $=L$`,
    use: "to see what a function approaches near a point, even where it is undefined",
    trap: r`direct substitution giving $\tfrac00$ is not an answer: simplify first, or use a standard limit`,
  } }),
  h("Domain and range"),
  rule("Domain checklist", [
    r`Fraction $\frac1{g}$: $g\ne0$. $\quad$ Even root $\sqrt{g}$: $g\ge0$. $\quad$ $\ln g$: $g>0$. $\quad$ $\sin^{-1}g$: $-1\le g\le1$.`,
    r`Several conditions: take all of them together. Range: put $y=f(x)$, solve for $x$, and see which $y$ are allowed.`,
  ]),
  E({ level: "Easy", src: "Prof · Typed p.4 · Ex 1",
    q: r`Find domain and range: (1) $\dfrac1{x-3}$, (2) $\sqrt{4-x^2}$, (3) $\sqrt{x-2}+1$, (4) $\dfrac{\sqrt{x+1}}{x-2}$, (5) $\dfrac{x^2-4}{x-2}$, (6) $\log(x^2-9)$, (7) $\sin^{-1}(2x-1)$.`,
    steps: [
      r`(1) $x\ne3$; $\frac1{x-3}$ is never $0$, so range $\mathbb R\setminus\{0\}$.`,
      r`(2) $4-x^2\ge0\Rightarrow[-2,2]$; the root takes values from $0$ (at $x=\pm2$) to $2$ (at $x=0$): range $[0,2]$.`,
      r`(3) $x\ge2$; $\sqrt{x-2}\ge0$ so range $[1,\infty)$.`,
      r`(4) $x+1\ge0$ and $x\ne2$: domain $[-1,2)\cup(2,\infty)$; range $\mathbb R$.`,
      r`(5) $x\ne2$; for $x\ne2$ the function equals $x+2$, so $y=4$ is missed: range $\mathbb R\setminus\{4\}$.`,
      r`(6) $x^2>9\Rightarrow(-\infty,-3)\cup(3,\infty)$; $\log$ takes every real value: range $\mathbb R$.`,
      r`(7) $-1\le2x-1\le1\Rightarrow[0,1]$; range $[-\frac\pi2,\frac\pi2]$.`,
    ],
    answer: r`Domains: $\mathbb R\setminus\{3\}$, $[-2,2]$, $[2,\infty)$, $[-1,2)\cup(2,\infty)$, $\mathbb R\setminus\{2\}$, $(-\infty,-3)\cup(3,\infty)$, $[0,1]$.`,
    formula: [r`Domain checklist`] }),

  h("Meaning and laws of limits"),
  p(r`$\lim_{x\to a}f(x)=L$ means $f(x)$ gets as close to $L$ as we like when $x$ is close to $a$ (but $x\ne a$). It exists only if the **left limit** $\lim_{x\to a^-}f$ and **right limit** $\lim_{x\to a^+}f$ are equal.`),
  rule("Limit laws", [
    r`If $\lim f=l$ and $\lim g=m$ (finite): $\lim(f\pm g)=l\pm m,\ \lim(fg)=lm,\ \lim kf=kl$,`,
    r`$\lim\dfrac fg=\dfrac lm$ provided $m\ne0$. Also $\lim_{x\to a}c=c$ and $\lim_{x\to a}x=a$.`,
  ]),
  rule("Techniques for 0/0 and inf/inf limits", [
    r`Factor and cancel; rationalise surds; divide by the highest power of $x$ (as $x\to\infty$); rewrite with a standard limit.`,
  ]),
  G({ level: "Medium", src: "Prof · Typed p.5-6 · Ex 2-7",
    tip: r`Match each limit to a standard form (sine, tangent, exponential, log, $e^k$), a factorisation, or a division by the highest power. A cube in the denominator (part i) needs a series.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0}\frac{\sin3x}{x}$`, s: r`$=3\cdot\frac{\sin3x}{3x}\to3$.`, a: r`$3$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{1-\cos2x}{x^2}$`, s: r`$1-\cos2x=2\sin^2x$, so $2\left(\frac{\sin x}{x}\right)^2\to2$.`, a: r`$2$` },
      { q: r`$\displaystyle\lim_{x\to\infty}\frac{3x^2+5}{2x^2-x}$`, s: r`Divide by $x^2$: $\frac{3+5/x^2}{2-1/x}\to\frac32$.`, a: r`$\frac32$` },
      { q: r`$\displaystyle\lim_{x\to1}\frac{x^3-1}{x-1}$`, s: r`$x^3-1=(x-1)(x^2+x+1)$; cancel, put $x=1$.`, a: r`$3$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{e^x-1}{x}$`, s: r`Standard limit.`, a: r`$1$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{\tan5x}{x}$`, s: r`$=5\cdot\frac{\tan5x}{5x}\to5$.`, a: r`$5$` },
    ],
    formula: [r`$\frac{\sin u}{u},\frac{\tan u}{u},\frac{e^u-1}{u},\frac{\ln(1+u)}{u}\to1$`, r`$a^3-b^3=(a-b)(a^2+ab+b^2)$`] }),
  G({ level: "Medium", src: "Prof · Typed p.5-6 · Ex 8-11 · Tut 1 · P1(i)",
    tip: r`Exponent-type limits match $\left(1+\frac kx\right)^x\to e^k$; a cube in the denominator (part c) needs a series; $\tan^2-\sin^2$ factors.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to\infty}\Big(1+\frac2x\Big)^{x}$`, s: r`Form $\left(1+\frac kx\right)^x$ with $k=2$.`, a: r`$e^2$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{\ln(1+x)}{x}$`, s: r`Standard limit.`, a: r`$1$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{\sin x-x}{x^3}$`, s: r`$\sin x=x-\frac{x^3}6+\cdots$, so numerator $=-\frac{x^3}6+\cdots$; divide by $x^3$.`, a: r`$-\frac16$` },
      { q: r`$\displaystyle\lim_{x\to\infty}\frac{\sqrt{x^2+1}}{x}$`, s: r`For $x>0$ it is $\sqrt{1+\frac1{x^2}}\to1$.`, a: r`$1$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{\tan^2x-\sin^2x}{x^2}$`, s: r`$\tan^2x-\sin^2x=\sin^2x\tan^2x$, so ratio $=\left(\frac{\sin x}x\right)^2\tan^2x\to0$.`, a: r`$0$` },
    ],
    formula: [r`$\frac{\sin u}{u},\frac{\tan u}{u},\frac{e^u-1}{u},\frac{\ln(1+u)}{u}\to1$`, r`$\left(1+\frac kx\right)^x\to e^k$`, r`$a^3-b^3=(a-b)(a^2+ab+b^2)$`] }),
  tryit([
    { q: r`$\displaystyle\lim_{x\to0}\frac{\sin7x}{\sin3x}$`, a: r`$\frac73$` },
    { q: r`$\displaystyle\lim_{x\to\infty}\Big(1+\frac3x\Big)^{2x}$`, a: r`$e^6$` },
    { q: r`$\displaystyle\lim_{x\to\infty}\big(\sqrt{x^2+x}-x\big)$ (multiply and divide by the conjugate)`, a: r`$\frac12$` },
  ]),
  mistakes([
    r`Cancelling a factor that is zero at the point *before* factoring: $\frac{x^2-1}{x-1}$ must be factored first.`,
    r`Using $\frac{\sin u}{u}\to1$ when $u\not\to0$, or forgetting the factor $k$ in $\frac{\sin kx}{x}\to k$.`,
    r`Treating $\infty-\infty$ or $\frac\infty\infty$ as $0$ or $1$; these need work.`,
  ]),

  // =============================== CH 2 ===============================
  chapter("Continuity", { glance: {
    formula: r`$f$ continuous at $a$ $\iff$ $\lim_{x\to a^-}f=\lim_{x\to a^+}f=f(a)$`,
    use: "to find unknown constants that make a piecewise function join up, and to classify breaks",
    trap: r`checking only that the limit exists: $f(a)$ must be defined and equal to it`,
  } }),
  rule("Continuity at a point", [
    r`$f$ is continuous at $x=a$ if (i) $f(a)$ is defined, (ii) $\lim_{x\to a}f(x)$ exists, (iii) $\lim_{x\to a}f(x)=f(a)$.`,
    r`Left-continuous: $\lim_{x\to a^-}f=f(a)$. Right-continuous: $\lim_{x\to a^+}f=f(a)$. Continuous on $[a,b]$: continuous inside and one-sided at the ends.`,
  ]),
  rule("Types of discontinuity", [
    r`Removable: $\lim$ exists but $\ne f(a)$ or $f(a)$ undefined. Jump: both one-sided limits finite but different. Infinite: a one-sided limit is $\pm\infty$.`,
    r`Polynomials, $\sin$, $\cos$, $e^x$ are continuous everywhere; sums, products, quotients (denominator $\ne0$) and compositions of continuous functions are continuous.`,
  ]),
  E({ level: "Medium", src: "Tut 1 · P8",
    q: r`Find where $f$ is discontinuous and whether it is continuous from the right, left or neither:$$f(x)=\begin{cases}1+x^2,&x\le0\\ 2-x,&0<x\le2\\ (x-2)^2,&x>2\end{cases}$$`,
    tip: r`Each piece is continuous by itself; trouble can only occur at the **break points** $x=0$ and $x=2$.`,
    steps: [
      r`At $x=0$: $f(0)=1$, left limit $=1+0=1$, right limit $=2-0=2$. Left limit $=f(0)$ but right limit $\ne f(0)$.`,
      r`At $x=2$: $f(2)=0$, left limit $=2-2=0$, right limit $=(x-2)^2\to0$. All three agree.`,
    ],
    answer: r`Discontinuous only at $x=0$ (jump); there it is continuous from the left, not from the right.`,
    formula: [r`Continuity at a point`] }),
  E({ level: "Hard", src: "Tut 1 · P9",
    q: r`Find $a,b$ so that $f$ is continuous everywhere:$$f(x)=\begin{cases}\dfrac{x^2-4}{x-2},&x<2\\ ax^2-bx+3,&2\le x<3\\ 2x-a+b,&x\ge3\end{cases}$$`,
    tip: r`Piecewise with two unknowns: write one equation per break point (left value $=$ right value) and solve the pair.`,
    steps: [
      r`For $x<2$: $\frac{x^2-4}{x-2}=x+2\to4$ as $x\to2^-$.`,
      r`At $x=2$: $4a-2b+3=4\Rightarrow 4a-2b=1$.`,
      r`At $x=3$: $9a-3b+3=6-a+b\Rightarrow10a-4b=3$.`,
      r`From the first, $b=\frac{4a-1}2$; then $10a-2(4a-1)=3\Rightarrow2a=1$.`,
    ],
    answer: r`$a=\tfrac12,\ b=\tfrac12$.`,
    formula: [r`left value $=$ right value at each break`] }),
  E({ level: "Easy", src: "Extra · standard",
    q: r`Find $k$ so that $f(x)=\dfrac{\sin x}{x}$ for $x\ne0$, $f(0)=k$ is continuous at $0$.`,
    steps: [r`$\lim_{x\to0}\frac{\sin x}{x}=1$, so need $f(0)=k=1$.`],
    answer: r`$k=1$ (the break at $0$ was removable).`, formula: [r`$\lim\dfrac{\sin x}{x}=1$`] }),
  tryit([
    { q: r`Find $k$: $f(x)=\dfrac{x^2-9}{x-3}$ for $x\ne3$, $f(3)=k$, continuous at $3$.`, a: r`$k=6$` },
    { q: r`Find $k$: $f(x)=x+1$ for $x<1$, $f(x)=kx^2$ for $x\ge1$, continuous at $1$.`, a: r`$k=2$` },
  ]),
  mistakes([
    r`Checking only the limit and forgetting $f(a)$ (a hole is still a discontinuity).`,
    r`Matching only one break point when there are two unknowns and two break points.`,
    r`Writing $\le$ and $<$ carelessly: the piece containing the equality sign gives $f(a)$.`,
  ]),

  // =============================== CH 3 ===============================
  chapter("Differentiability", { glance: {
    formula: r`$f'(a)=\lim_{h\to0}\dfrac{f(a+h)-f(a)}{h}$ exists $\iff$ LHD $=$ RHD`,
    use: "to test corners, cusps and break points, and to justify the hypothesis of MVT",
    trap: r`differentiable $\Rightarrow$ continuous, but continuous does not give differentiable ($|x|$ at $0$)`,
  } }),
  rule("Derivative at a point", [
    r`$f'(a)=\displaystyle\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$. LHD: $h\to0^-$. RHD: $h\to0^+$. $f'(a)$ exists iff LHD $=$ RHD (both finite).`,
  ]),
  rule("Link with continuity", [
    r`Differentiable at $a$ $\Rightarrow$ continuous at $a$. The converse is false. So: not continuous $\Rightarrow$ not differentiable.`,
  ]),
  E({ level: "Medium", src: "Tut 1 · P10",
    q: r`Discuss differentiability at $x=1,2$:$$f(x)=\begin{cases}x,&x<1\\2-x,&1\le x\le2\\-2+3x-x^2,&x>2\end{cases}$$`,
    tip: r`Piecewise with matching formulas: check continuity at each join first, then compare the slopes of the two pieces.`,
    steps: [
      r`At $x=1$: $f(1)=1$; left limit $=1$, right limit $=2-1=1$, continuous. LHD $=(x)'=1$, RHD $=(2-x)'=-1$.`,
      r`LHD $\ne$ RHD, so not differentiable at $1$ (corner).`,
      r`At $x=2$: $f(2)=0$; right limit $=-2+6-4=0$, continuous. LHD $=(2-x)'=-1$, RHD $=(3-2x)'\big|_{x=2}=-1$.`,
      r`LHD $=$ RHD $=-1$.`,
    ],
    answer: r`Not differentiable at $x=1$; differentiable at $x=2$ with $f'(2)=-1$.`,
    formula: [r`Derivative at a point`] }),
  E({ level: "Easy", src: "Tut 1 · P11",
    q: r`Prove $f(x)=|x-5|$ is continuous but not differentiable at $x=5$.`,
    steps: [
      r`$f(5)=0$ and $\lim_{x\to5}|x-5|=0$, so continuous.`,
      r`LHD $=\lim_{h\to0^-}\dfrac{|h|}{h}=\dfrac{-h}{h}=-1$; RHD $=\lim_{h\to0^+}\dfrac{|h|}{h}=1$.`,
      r`LHD $\ne$ RHD.`,
    ],
    answer: r`Continuous at $5$, not differentiable (corner, slopes $-1$ and $1$).`,
    formula: [r`$|h|=-h$ for $h<0$, $=h$ for $h>0$`] }),
  E({ level: "Hard", src: "Extra · standard",
    q: r`Is $f(x)=x^2\sin\frac1x$ ($x\ne0$), $f(0)=0$, differentiable at $0$?`,
    tip: r`Formula undefined at the point: go back to the definition of the derivative, not the product rule.`,
    steps: [
      r`$\dfrac{f(h)-f(0)}{h}=h\sin\frac1h$.`,
      r`$|h\sin\frac1h|\le|h|\to0$ (squeeze), so the limit is $0$.`,
    ],
    answer: r`Yes, $f'(0)=0$.`, formula: [r`$-|h|\le h\sin\frac1h\le|h|$`] }),
  tryit([
    { q: r`Is $f(x)=x|x|$ differentiable at $0$? Find $f'(0)$.`, a: r`yes, $f'(0)=0$` },
    { q: r`Where is $f(x)=|x-1|+|x-2|$ not differentiable?`, a: r`$x=1$ and $x=2$` },
  ]),
  mistakes([
    r`Using the formula for $f'$ of one piece at the join point: compute LHD and RHD from the two pieces separately.`,
    r`Concluding differentiable just because the function is continuous.`,
    r`Differentiating each piece and comparing only the *values* of the pieces, not their *slopes*.`,
  ]),

  // =============================== CH 4 ===============================
  chapter("Mean Value Theorems", { glance: {
    formula: r`$f'(c)=\dfrac{f(b)-f(a)}{b-a}$ for some $c\in(a,b)$`,
    use: "to locate a point where the tangent is parallel to the chord, or to prove an inequality",
    trap: r`check both hypotheses first: continuous on $[a,b]$ **and** differentiable on $(a,b)$`,
  } }),
  h("Rolle's theorem"),
  rule("Rolle's theorem", [
    r`If $f$ is (i) continuous on $[a,b]$, (ii) differentiable on $(a,b)$, (iii) $f(a)=f(b)$, then $f'(c)=0$ for some $c\in(a,b)$.`,
  ]),
  fig(figRolle, r`Rolle: equal heights at $a$ and $b$, horizontal tangent at $c$.`),
  h("Lagrange's mean value theorem (MVT)"),
  rule("Lagrange MVT", [
    r`If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there is $c\in(a,b)$ with $f'(c)=\dfrac{f(b)-f(a)}{b-a}$.`,
    r`Geometric meaning: some tangent is parallel to the chord joining $(a,f(a))$ and $(b,f(b))$. Rolle is the case $f(a)=f(b)$.`,
  ]),
  fig(figMVT, r`MVT: the tangent at $c$ is parallel to the chord (dashed) through $a$ and $b$.`),
  h("Cauchy's mean value theorem"),
  rule("Cauchy MVT", [
    r`If $f,g$ are continuous on $[a,b]$, differentiable on $(a,b)$ and $g'\ne0$ there, then for some $c\in(a,b)$: $\dfrac{f'(c)}{g'(c)}=\dfrac{f(b)-f(a)}{g(b)-g(a)}$.`,
    r`Taking $g(x)=x$ gives Lagrange's MVT.`,
  ]),
  rule("Method to find c", [
    r`1. Check the hypotheses. 2. Compute the slope $\frac{f(b)-f(a)}{b-a}$. 3. Solve $f'(c)=$ slope. 4. Keep only roots with $a<c<b$.`,
  ]),
  E({ level: "Medium", src: "Tut 1 · P12(i)",
    q: r`Check Rolle's theorem for $f(x)=5-2x+3x^2$ on $[1,3]$; find $c$.`,
    tip: r`Always compute $f(a)$ and $f(b)$: condition (iii) decides whether Rolle applies at all.`,
    steps: [
      r`$f$ is a polynomial: continuous and differentiable. $f(1)=6$, $f(3)=26$.`,
      r`$f(1)\ne f(3)$, so **Rolle's hypotheses fail** (the problem as printed has a typo; e.g. $5-4x+x^2$ would have $f(1)=f(3)=2$, $c=2$).`,
      r`MVT does apply: $6c-2=\frac{26-6}{2}=10\Rightarrow c=2$.`,
    ],
    answer: r`Rolle not applicable; the MVT point is $c=2$.`,
    formula: [r`Rolle's theorem`, r`Lagrange MVT`] }),
  E({ level: "Medium", src: "Tut 1 · P12(ii)",
    q: r`Verify Rolle's theorem for $f(x)=\cos2x$ on $[\frac\pi8,\frac{7\pi}8]$ and find $c$.`,
    tip: r`Equal end values come from symmetry of $\cos$: check them numerically, then solve $f'(c)=0$.`,
    steps: [
      r`$\cos 2x$ is continuous and differentiable everywhere.`,
      r`$f(\frac\pi8)=\cos\frac\pi4=\frac{\sqrt2}2$ and $f(\frac{7\pi}8)=\cos\frac{7\pi}4=\frac{\sqrt2}2$: equal.`,
      r`$f'(x)=-2\sin2x=0\Rightarrow2x=\pi\Rightarrow x=\frac\pi2\in(\frac\pi8,\frac{7\pi}8)$.`,
    ],
    answer: r`$c=\dfrac\pi2$.`, formula: [r`Rolle's theorem`] }),
  G({ level: "Easy", src: "Tut 1 · P13(i),(ii) · Prof · Typed p.13 · Ex 23",
    items: [
      { q: r`$f=2x^2-3x+1$ on $[0,2]$`, s: r`Polynomial. $f(0)=1,\ f(2)=3$, slope $1$; $4c-3=1\Rightarrow c=1$.`, a: r`$c=1$` },
      { q: r`$f=\ln x$ on $[1,4]$`, s: r`Continuous, differentiable for $x>0$. Slope $\frac{\ln4}{3}$; $\frac1c=\frac{\ln4}3\Rightarrow c=\frac3{\ln4}\approx2.16$.`, a: r`$c=\frac{3}{\ln4}$` },
      { q: r`$f=1-x^2$ on $[0,2]$`, s: r`$f(2)=-3,\ f(0)=1$, slope $-2$; $-2c=-2\Rightarrow c=1$.`, a: r`$c=1$` },
    ], formula: [r`Lagrange MVT`] }),
  E({ level: "Medium", src: "Prof · Typed p.14 · Ex 24",
    q: r`Verify MVT for $f(x)=x^{2/3}$ on $[1,8]$.`,
    tip: r`A fractional power fails to be differentiable at $x=0$; check that $0\notin(a,b)$ before applying MVT.`,
    steps: [
      r`Continuous on $[1,8]$; $f'(x)=\frac23x^{-1/3}$ exists on $(1,8)$ (bad point $0$ is outside).`,
      r`Slope $=\frac{8^{2/3}-1}{7}=\frac37$, so $\frac23c^{-1/3}=\frac37\Rightarrow c^{1/3}=\frac{14}9$.`,
    ],
    answer: r`$c=\left(\frac{14}9\right)^3=\frac{2744}{729}\approx3.76\in(1,8)$.`, formula: [r`Lagrange MVT`] }),
  G({ level: "Easy", src: "Prof · Typed p.16 · Q1-Q5",
    items: [
      { q: r`$x^2+2x$ on $[1,3]$`, s: r`$f(3)=15,\ f(1)=3$, slope $6$; $2c+2=6\Rightarrow c=2$.`, a: r`$c=2$` },
      { q: r`$x^2$ on $[1,3]$`, s: r`Slope $\frac{9-1}2=4$; $2c=4$.`, a: r`$c=2$` },
      { q: r`$\sin x$ on $[0,\pi]$`, s: r`Applicable (smooth). Slope $0$; $\cos c=0$.`, a: r`$c=\frac\pi2$` },
      { q: r`$e^x$ on $[0,2]$`, s: r`Slope $\frac{e^2-1}2$; $e^c=\frac{e^2-1}2$, $c\approx1.161\in(0,2)$.`, a: r`$c=\ln\frac{e^2-1}2$` },
      { q: r`$\ln x$ on $[1,e]$`, s: r`Slope $\frac1{e-1}$; $\frac1c=\frac1{e-1}$.`, a: r`$c=e-1\approx1.718$` },
    ], formula: [r`Lagrange MVT`] }),
  G({ level: "Medium", src: "Prof · Typed p.15 · Ex 25 · p.16 · Q6",
    tip: r`Absolute value inside the interval: the corner lies in $(a,b)$, so differentiability on the open interval is suspect.`,
    items: [
      { q: r`$f=|x|$ on $[-1,1]$`, s: r`Continuous. At $0$: LHD $=\lim_{h\to0^-}\frac{-h}h=-1$, RHD $=+1$: not differentiable on $(-1,1)$.`, a: r`MVT not applicable` },
      { q: r`$f=|x-2|$ on $[0,4]$`, s: r`Corner at $x=2\in(0,4)$. Chord slope $0$ but $f'=\pm1\ne0$: the conclusion truly fails.`, a: r`MVT not applicable` },
    ], formula: [r`Derivative at a point`] }),
  E({ level: "Medium", src: "Prof · Typed p.16 · Q7, Q8",
    q: r`Verify MVT and find $c$: (7) $f=x^3-3x+1$ on $[-2,2]$ (all $c$); (8) $f=\tan^{-1}x$ on $[0,1]$.`,
    tip: r`A quadratic in $c$ can give two roots: test each against the open interval. For $\frac1{1+c^2}=k$, invert then take the positive root.`,
    steps: [
      r`(7) $f(2)=3,\ f(-2)=-1$, slope $1$; $3c^2-3=1\Rightarrow c=\pm\frac2{\sqrt3}\approx\pm1.155$, both in $(-2,2)$.`,
      r`(8) slope $=\frac\pi4$; $\frac1{1+c^2}=\frac\pi4\Rightarrow c^2=\frac4\pi-1$.`,
    ],
    answer: r`(7) $c=\pm\frac2{\sqrt3}$; (8) $c=\sqrt{\frac4\pi-1}\approx0.523$.`, formula: [r`Lagrange MVT`, r`$(\tan^{-1}x)'=\frac1{1+x^2}$`] }),
  E({ level: "Hard", src: "Prof · Typed p.16 · Q9",
    q: r`For $f(x)=x^2\sin x$ on $[0,\pi]$ show $\exists\,c\in(0,\pi)$ with $f'(c)=\frac{f(\pi)-f(0)}{\pi}$; find $c$ approximately.`,
    tip: r`The slope is $0$ so the equation is $f'(c)=0$ with no closed form: reduce to $\tan c=-\frac c2$ and solve numerically.`,
    steps: [
      r`Smooth, and $f(0)=f(\pi)=0$: slope $0$ (the Rolle case).`,
      r`$f'(x)=x(2\sin x+x\cos x)=0$, $x\ne0$, so $\tan c=-\frac c2$; a root lies in $(\frac\pi2,\pi)$ where $\tan<0$. Newton gives $c\approx2.289$.`,
    ],
    answer: r`$c\approx2.289$.`, formula: [r`Rolle's theorem`] }),
  E({ level: "Hard", src: "Prof · Typed p.16 · Q10",
    q: r`For $f(x)=x^p$ ($p>0$) on $[a,b]$, $a>0$, find $c$ in terms of $a,b,p$.`,
    tip: r`General parameters: run the standard method symbolically, ending with $c^{p-1}=\dots$.`,
    steps: [
      r`$x^p$ is continuous on $[a,b]$, differentiable on $(a,b)$ since $a>0$.`,
      r`$pc^{p-1}=\frac{b^p-a^p}{b-a}\Rightarrow c^{p-1}=\frac{b^p-a^p}{p(b-a)}$.`,
    ],
    answer: r`$c=\left[\frac{b^p-a^p}{p(b-a)}\right]^{\frac1{p-1}}$ for $p\ne1$ (for $p=1$ every $c$ works).`, formula: [r`Lagrange MVT`] }),
  h("Cauchy MVT and uses"),
  E({ level: "Medium", src: "Extra · standard",
    q: r`Find $c$ of Cauchy's MVT for $f(x)=x^2$, $g(x)=x^3$ on $[1,2]$.`,
    tip: r`Two functions and a ratio of derivatives: compare $f'/g'$ with the ratio of increments.`,
    steps: [
      r`$\dfrac{f'(c)}{g'(c)}=\dfrac{2c}{3c^2}=\dfrac2{3c}$ and $\dfrac{f(2)-f(1)}{g(2)-g(1)}=\dfrac{3}{7}$.`,
      r`$\dfrac2{3c}=\dfrac37\Rightarrow c=\dfrac{14}9\approx1.556\in(1,2)$.`,
    ],
    answer: r`$c=\dfrac{14}{9}$.`, formula: [r`Cauchy MVT`] }),
  E({ level: "Hard", src: "Extra · standard",
    q: r`Use MVT to prove $\ln(1+x)<x$ for $x>0$.`,
    tip: r`Inequality with a function of $x$ and its derivative: apply MVT on $[0,x]$ and bound $f'(c)$.`,
    steps: [
      r`Take $f(t)=\ln(1+t)$ on $[0,x]$; $f(x)-f(0)=x\,f'(c)=\dfrac{x}{1+c}$ with $0<c<x$.`,
      r`Since $1+c>1$, $\dfrac{x}{1+c}<x$.`,
    ],
    answer: r`$\ln(1+x)<x$ for all $x>0$.`, formula: [r`Lagrange MVT`] }),
  tryit([
    { q: r`Find $c$ for $f(x)=x^3$ on $[0,2]$.`, a: r`$c=\frac{2}{\sqrt3}$` },
    { q: r`Find $c$ for $f(x)=\sqrt x$ on $[1,4]$.`, a: r`$c=\frac94$` },
    { q: r`Verify Rolle's theorem for $f(x)=x^2-4x+3$ on $[1,3]$.`, a: r`$f(1)=f(3)=0$; $c=2$` },
  ]),
  mistakes([
    r`Applying Rolle when $f(a)\ne f(b)$; compute both end values first.`,
    r`Giving a root $c$ outside the open interval $(a,b)$: always reject it.`,
    r`Ignoring a corner or a vertical tangent inside $(a,b)$ ($|x|$, $x^{2/3}$ at $0$): hypothesis (ii) fails.`,
  ]),

  // =============================== CH 5 ===============================
  chapter("Indeterminate Forms and L'Hôpital's Rule", { glance: {
    formula: r`$\displaystyle\lim\frac{f}{g}=\lim\frac{f'}{g'}$ when the limit is $\frac00$ or $\frac\infty\infty$`,
    use: String.raw`limits that become $\frac00,\ \frac\infty\infty,\ 0\cdot\infty,\ \infty-\infty,\ 0^0,\ 1^\infty,\ \infty^0$`,
    trap: r`differentiate top and bottom **separately**, never the quotient; check the form each time`,
  } }),
  rule("L'Hôpital's rule", [
    r`If $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)}$ is $\dfrac00$ or $\dfrac\infty\infty$, then $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$ (if the right side exists). Repeat while the form persists.`,
  ]),
  rule("Seven indeterminate forms", [
    r`$\dfrac00,\ \dfrac\infty\infty,\ 0\cdot\infty,\ \infty-\infty,\ 0^0,\ 1^\infty,\ \infty^0$.`,
  ]),
  rule("Conversion recipes", [
    r`$0\cdot\infty$: write $f\,g=\dfrac{f}{1/g}$ to get $\frac00$ or $\frac\infty\infty$.`,
    r`$\infty-\infty$: take a common denominator (or $f-g=fg\left(\frac1g-\frac1f\right)$) to get $\frac00$.`,
    r`$0^0,\ 1^\infty,\ \infty^0$: put $y=f^g$, $\ln y=g\ln f$ is a $0\cdot\infty$ form; then $y=e^{\lim\ln y}$.`,
  ]),
  h("0/0 form"),
  G({ level: "Easy", src: "Prof · Typed p.7 · Ex 12 · p.12 · Q3, Q4",
    items: [
      { q: r`$\displaystyle\lim_{x\to0}\frac{e^x-1-x}{x^2}$`, s: r`$\frac00$: $\frac{e^x-1}{2x}$ ($\frac00$) $\to\frac{e^x}{2}\to\frac12$.`, a: r`$\frac12$` },
      { q: r`$\displaystyle\lim_{x\to1}\frac{x^3-1}{x-1}$`, s: r`$\frac00$: $\frac{3x^2}{1}\to3$.`, a: r`$3$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{x}{2x-3\tan x}$`, s: r`$\frac00$: $\frac{1}{2-3\sec^2x}\to\frac1{2-3}$.`, a: r`$-1$` },
    ], formula: [r`L'Hôpital's rule`] }),
  G({ level: "Medium", src: "Prof · Typed p.12 · Q1, Q5, Q6, Q9",
    tip: r`A cubic denominator with a numerator vanishing at $0$: repeat L'Hôpital until the denominator is non-zero, or factor first (part c).`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0}\frac{x-\tan x}{x^3}$`, s: r`$\frac{1-\sec^2x}{3x^2}=-\frac13\left(\frac{\tan x}{x}\right)^2\to-\frac13$.`, a: r`$-\frac13$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{\sinh x-x}{x^3}$`, s: r`$\frac{\cosh x-1}{3x^2}\to\frac{\sinh x}{6x}\to\frac{\cosh x}6$.`, a: r`$\frac16$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{\tan x-\sin x}{x^3}$`, s: r`$\tan x-\sin x=\tan x(1-\cos x)$; ratio $=\frac{\tan x}x\cdot\frac{1-\cos x}{x^2}\to\frac12$.`, a: r`$\frac12$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{e^x-e^{-x}-2x}{x^3}$`, s: r`$\frac{e^x+e^{-x}-2}{3x^2}\to\frac{e^x-e^{-x}}{6x}\to\frac{e^x+e^{-x}}6=\frac26$.`, a: r`$\frac13$` },
    ], formula: [r`L'Hôpital's rule`, r`$\lim\frac{1-\cos x}{x^2}=\frac12$`] }),
  E({ level: "Hard", src: "Prof · Typed p.12 · Q2",
    q: r`$\displaystyle\lim_{x\to0}\frac{2x-x\cos x-\sin x}{x^3}$`,
    tip: r`Mixed $x$, $x\cos x$, $\sin x$ over $x^3$: three rounds of L'Hôpital, using the product rule on $x\cos x$ each time.`,
    steps: [
      r`$\frac00$: numerator$'=2-2\cos x+x\sin x$, denominator$'=3x^2$. Still $\frac00$.`,
      r`Numerator$''=3\sin x+x\cos x$, denominator$''=6x$. Still $\frac00$.`,
      r`Numerator$'''=4\cos x-x\sin x\to4$, denominator$'''=6$.`,
    ],
    answer: r`$\frac23$`, formula: [r`L'Hôpital's rule`, r`$(uv)'=u'v+uv'$`] }),
  E({ level: "Medium", src: "Prof · Typed p.12 · Q7",
    q: r`$\displaystyle\lim_{a\to b}\frac{a^p-b^p}{a^q-b^q}$`,
    tip: r`The variable is $a$ ($b,p,q$ are constants): differentiate with respect to $a$.`,
    steps: [r`At $a=b$: $\frac00$. Differentiate in $a$: $\frac{pa^{p-1}}{qa^{q-1}}$; put $a=b$.`],
    answer: r`$\frac pq\,b^{\,p-q}$`, formula: [r`$(a^n)'=na^{n-1}$`] }),
  E({ level: "Hard", src: "Prof · Typed p.12 · Q8 · Tut 1 · P7",
    q: r`If $\displaystyle\lim_{x\to0}\frac{\sin3x+ax+bx^3}{x^3}=1$, find $a,b$.`,
    tip: r`A finite limit over $x^3$ forces the $x^0$ and $x^1$ parts of the numerator to vanish: match coefficients.`,
    steps: [
      r`$\sin3x=3x-\frac92x^3+\cdots$, so numerator $=(3+a)x+\left(b-\frac92\right)x^3+\cdots$.`,
      r`Finite limit: $3+a=0\Rightarrow a=-3$. Then the limit is $b-\frac92=1\Rightarrow b=\frac{11}2$.`,
    ],
    answer: r`$a=-3,\ b=\frac{11}2$.`, formula: [r`$\sin x=x-\frac{x^3}6+\cdots$`] }),
  G({ level: "Hard", src: "Prof · Typed p.12 · Q10 · Tut 1 · P1(ii)",
    tip: r`Rewrite or expand instead of differentiating: $1-\cos x=2\sin^2\frac x2$, and $\sin^2x=x^2-\frac{x^4}3+\cdots$ exposes the powers of $x$.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0}\frac{x^2\sin x}{1-\cos x}$`, s: r`$=\frac{x^2}{2\sin^2(x/2)}\cdot\sin x=2\left(\frac{x/2}{\sin(x/2)}\right)^2\sin x\to2\cdot0$.`, a: r`$0$` },
      { q: r`$\displaystyle\lim_{x\to0}\frac{\sin^2x-x^2}{x^2\sin^2x}$`, s: r`Numerator $=-\frac{x^4}3+\cdots$, denominator $\approx x^4$.`, a: r`$-\frac13$` },
    ], formula: [r`$1-\cos x=2\sin^2\frac x2$`, r`$\sin x=x-\frac{x^3}6+\cdots$`] }),

  h("Infinity / infinity form"),
  G({ level: "Medium", src: "Prof · Typed p.8 · Ex 13 · Tut 1 · P2(i)",
    tip: r`Both parts blow up: differentiate; for logs of $\tan$ or $\sec$, L'Hôpital turns them into trig quotients.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to\pi/2}\frac{3\sec x}{1+\tan x}$`, s: r`$\frac\infty\infty$: $\frac{3\sec x\tan x}{\sec^2x}=3\sin x\to3$.`, a: r`$3$` },
      { q: r`$\displaystyle\lim_{x\to0^+}\frac{\ln\tan x}{\ln x}$`, s: r`$\frac{-\infty}{-\infty}$: $\frac{\sec^2x/\tan x}{1/x}=\frac{x}{\sin x\cos x}\to1$.`, a: r`$1$` },
    ], formula: [r`L'Hôpital's rule`, r`$(\sec x)'=\sec x\tan x$`] }),

  h("Infinity minus infinity form"),
  G({ level: "Medium", src: "Prof · Typed p.8 · Ex 14 · p.12 · Q11",
    tip: r`A difference of two terms that both blow up: put it over a common denominator to reach $\frac00$.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to1}\left(\frac{x}{x-1}-\frac1{\ln x}\right)$`, s: r`$=\frac{x\ln x-x+1}{(x-1)\ln x}$ ($\frac00$) $\to\frac{\ln x}{\ln x+\frac{x-1}{x}}$ ($\frac00$) $\to\frac{1/x}{\frac1x+\frac1{x^2}}\to\frac12$.`, a: r`$\frac12$` },
      { q: r`$\displaystyle\lim_{x\to2}\left[\frac1{x-2}-\frac1{\ln(x-1)}\right]$`, s: r`$=\frac{\ln(x-1)-(x-2)}{(x-2)\ln(x-1)}$ ($\frac00$) $\to\frac{\frac1{x-1}-1}{\ln(x-1)+\frac{x-2}{x-1}}$ ($\frac00$) $\to\frac{-1/(x-1)^2}{\frac1{x-1}+\frac1{(x-1)^2}}=\frac{-1}{2}$ at $x=2$.`, a: r`$-\frac12$` },
    ], formula: [r`common denominator`] }),
  G({ level: "Medium", src: "Prof · Typed p.12 · Q12, Q13 · Tut 1 · P4(i)",
    tip: r`Two reciprocals both $\to\infty$: common denominator, then $\frac00$.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0}\left(\frac1x-\frac1{e^x-1}\right)$`, s: r`$=\frac{e^x-1-x}{x(e^x-1)}\to\frac{e^x-1}{e^x-1+xe^x}\to\frac{e^x}{2e^x+xe^x}=\frac12$.`, a: r`$\frac12$` },
      { q: r`$\displaystyle\lim_{x\to0}\left(\frac1{\sin x}-\frac1x\right)$`, s: r`$=\frac{x-\sin x}{x\sin x}\to\frac{1-\cos x}{\sin x+x\cos x}\to\frac{\sin x}{2\cos x-x\sin x}=\frac02$.`, a: r`$0$` },
    ], formula: [r`L'Hôpital's rule`] }),
  G({ level: "Hard", src: "Prof · Typed p.12 · Q14 · Tut 1 · P4(ii)",
    tip: r`Substitute $u=\frac xa$ to remove the constant (part a); for $\frac1{x^2}-\cot^2x$ combine and read off the $x^4$ terms with series.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0}\left(\frac ax-\cot\frac xa\right)$`, s: r`$u=\frac xa$: $\frac1u-\cot u=\frac{\sin u-u\cos u}{u\sin u}\to\frac{u\sin u}{\sin u+u\cos u}\to\frac{\sin u+u\cos u}{2\cos u-u\sin u}=\frac02$.`, a: r`$0$` },
      { q: r`$\displaystyle\lim_{x\to0}\left(\frac1{x^2}-\cot^2x\right)$`, s: r`$=\frac{\sin^2x-x^2\cos^2x}{x^2\sin^2x}$; $\sin^2x=x^2-\frac{x^4}3+\cdots$, $x^2\cos^2x=x^2-x^4+\cdots$, numerator $=\frac23x^4$, denominator $\approx x^4$.`, a: r`$\frac23$` },
    ], formula: [r`$\cos^2x=1-x^2+\cdots$`] }),

  h("Zero times infinity form"),
  E({ level: "Hard", src: "Prof · Typed p.9 · Ex 15",
    q: r`$\displaystyle\lim_{x\to\pi/4}(1-\tan2x)\sec2x$`,
    tip: r`Check the factors first: here both blow up, so it is not $0\cdot\infty$ but $\infty\cdot\infty$ with a definite sign.`,
    steps: [
      r`As $x\to\frac\pi4$, $\tan2x\to\pm\infty$ and $\sec2x\to\pm\infty$ with the same sign, so $1-\tan2x$ and $\sec2x$ have opposite signs.`,
      r`The product $\to-\infty$ from both sides (typed notes: $\frac{\sec^22x}{\sin2x}\to-\infty$ after L'Hôpital).`,
    ],
    answer: r`$-\infty$ (no finite limit).`, formula: [r`L'Hôpital's rule`] }),
  G({ level: "Medium", src: "Prof · Typed p.9 · Ex 16 · Tut 1 · P3(i)",
    tip: r`One factor $\to0$, one $\to\infty$: move the infinite factor to the denominator ($\tan=\frac1{\cot}$).`,
    items: [
      { q: r`$\displaystyle\lim_{x\to1}(x^2-1)\tan\frac{\pi x}2$`, s: r`$=\frac{x^2-1}{\cot(\pi x/2)}$ ($\frac00$) $\to\frac{2x}{-\frac\pi2\csc^2(\pi x/2)}\to-\frac4\pi$. (Typed notes print it as a quotient but work it as a product.)`, a: r`$-\frac4\pi$` },
      { q: r`$\displaystyle\lim_{x\to1/2}\left(x^2-\tfrac14\right)\tan\pi x$`, s: r`$=\frac{x^2-1/4}{\cot\pi x}\to\frac{2x}{-\pi\csc^2\pi x}\to\frac{1}{-\pi}$.`, a: r`$-\frac1\pi$` },
    ], formula: [r`$(\cot u)'=-\csc^2u\cdot u'$`] }),
  G({ level: "Medium", src: "Prof · Typed p.12 · Q15, Q16",
    tip: r`Combine into one fraction (part a), or write $\tan x=\frac1{\cot x}$ (part b).`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0}\frac1x(1-x\cot x)$`, s: r`$=\frac{\sin x-x\cos x}{x\sin x}\to\frac{x\sin x}{\sin x+x\cos x}\to\frac{\sin x+x\cos x}{2\cos x-x\sin x}=\frac02$.`, a: r`$0$` },
      { q: r`$\displaystyle\lim_{x\to\pi/2}(1-\sin x)\tan x$`, s: r`$=\frac{1-\sin x}{\cot x}\to\frac{-\cos x}{-\csc^2x}=\cos x\sin^2x\to0$.`, a: r`$0$` },
    ], formula: [r`L'Hôpital's rule`] }),
  E({ level: "Hard", src: "Prof · Typed p.12 · Q17",
    q: r`$\displaystyle\lim_{x\to a}\ln\!\left(2-\frac xa\right)\cot(x-a)$`,
    tip: r`$\ln(\to1)\to0$ times $\cot(\to0)\to\infty$: put the cotangent below as $\tan$.`,
    steps: [
      r`The typed list prints $\ln\frac{2-x}{a}$, which is $0$ at $x=a$ only for $a=1$; the intended function is $\ln(2-\frac xa)$ (same when $a=1$).`,
      r`$=\frac{\ln(2-x/a)}{\tan(x-a)}$ ($\frac00$) $\to\frac{-\frac1a/(2-x/a)}{\sec^2(x-a)}\to-\frac1a$.`,
    ],
    answer: r`$-\frac1a$ (equals $-1$ for $a=1$).`, formula: [r`$\cot u=\frac1{\tan u}$`] }),
  G({ level: "Hard", src: "Tut 1 · P2(ii), P3(ii)",
    tip: r`$0\cdot(-\infty)$: put the vanishing factor in the denominator as a reciprocal to get $\frac\infty\infty$, or use $\lim x^n\ln x=0$.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0^+}x\ln\sin x$`, s: r`$=\frac{\ln\sin x}{1/x}\to\frac{\cot x}{-1/x^2}=-x^2\cot x=-x\cos x\cdot\frac x{\sin x}\to0$.`, a: r`$0$` },
      { q: r`$\displaystyle\lim_{x\to0^+}\sin^2\!\tfrac x2\,\ln x$ (printed $\sin^2x/2\cdot\ln x$ gives the same answer)`, s: r`$\sin^2\frac x2\sim\frac{x^2}4$ and $x^2\ln x=\frac{\ln x}{x^{-2}}\to\frac{1/x}{-2x^{-3}}=-\frac{x^2}2\to0$.`, a: r`$0$` },
    ], formula: [r`$\lim_{x\to0^+}x^n\ln x=0$`] }),

  h("Exponential forms"),
  G({ level: "Medium", src: "Prof · Typed p.10 · Ex 17, 18 · Tut 1 · P6(i)",
    tip: r`Variable in both base and exponent with form $0^0$: take $\ln$ and rewrite the $0\cdot\infty$ as a quotient.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0^+}x^x$`, s: r`$\ln y=\frac{\ln x}{1/x}\to\frac{1/x}{-1/x^2}=-x\to0$.`, a: r`$1$` },
      { q: r`$\displaystyle\lim_{x\to0^+}(\sin x)^{\tan x}$`, s: r`$\ln y=\frac{\ln\sin x}{\cot x}\to\frac{\cot x}{-\csc^2x}=-\sin x\cos x\to0$.`, a: r`$1$` },
      { q: r`$\displaystyle\lim_{x\to\pi/2}(\cos x)^{\cos x}$`, s: r`$t=\cos x\to0^+$: $t^t\to1$ by the first part.`, a: r`$1$` },
    ], formula: [r`Log trick for powers`] }),
  G({ level: "Medium", src: "Prof · Typed p.11 · Ex 19-21 · Tut 1 · P6(ii)",
    tip: r`Base $\to1$ with exponent $\to\infty$ is $1^\infty$; base $\to\infty$ with exponent $\to0$ is $\infty^0$. Take $\ln$ in both.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0}(1+x)^{1/x}$`, s: r`$\ln y=\frac{\ln(1+x)}x\to1$.`, a: r`$e$` },
      { q: r`$\displaystyle\lim_{x\to\infty}\Big(1+\frac1x\Big)^x$`, s: r`$t=\frac1x$: $\ln y=\frac{\ln(1+t)}t\to1$.`, a: r`$e$` },
      { q: r`$\displaystyle\lim_{x\to\infty}\Big(1+\frac2x\Big)^x$`, s: r`$t=\frac1x$: $\ln y=\frac{\ln(1+2t)}t\to\frac{2/(1+2t)}{1}=2$.`, a: r`$e^2$` },
      { q: r`$\displaystyle\lim_{x\to\infty}x^{1/x}$`, s: r`$\ln y=\frac{\ln x}x\to\frac{1/x}1=0$.`, a: r`$1$` },
    ], formula: [r`Log trick for powers`] }),
  E({ level: "Hard", src: "Prof · Typed p.12 · Q18",
    q: r`$\displaystyle\lim_{x\to0}\left(\frac{\tan x}{x}\right)^{1/x}$`,
    tip: r`Base $\to1$, exponent $\to\infty$: $1^\infty$. The $\ln$ of the base is tiny, so use $\tan x=x+\frac{x^3}3+\cdots$.`,
    steps: [
      r`$\ln y=\frac1x\ln\frac{\tan x}x$ with $\frac{\tan x}x=1+\frac{x^2}3+\cdots$.`,
      r`$\ln\left(1+\frac{x^2}3\right)\approx\frac{x^2}3$, so $\ln y\approx\frac x3\to0$.`,
    ],
    answer: r`$1$`, formula: [r`$\tan x=x+\frac{x^3}3+\cdots$`, r`$\ln(1+u)\approx u$`] }),
  G({ level: "Hard", src: "Prof · Typed p.12 · Q19, Q20",
    tip: r`Base $\to\frac{1+1}{2}=1$ (or $\frac44$) with exponent $\to\infty$: $1^\infty$; the answer is a geometric mean.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to0}\left(\frac{a^x+b^x}2\right)^{1/x}$`, s: r`$\ln y=\frac{\ln\frac{a^x+b^x}2}x$ ($\frac00$) $\to\frac{a^x\ln a+b^x\ln b}{a^x+b^x}\to\frac{\ln a+\ln b}2$.`, a: r`$\sqrt{ab}$` },
      { q: r`$\displaystyle\lim_{x\to0}\left(\frac{1^x+2^x+3^x+4^x}4\right)^{1/x}$`, s: r`$\ln y\to\frac{2^x\ln2+3^x\ln3+4^x\ln4}{1+2^x+3^x+4^x}\to\frac{\ln2+\ln3+\ln4}{4}=\frac{\ln24}4$.`, a: r`$24^{1/4}$` },
    ], formula: [r`$(a^x)'=a^x\ln a$`] }),
  G({ level: "Hard", src: "Tut 1 · P5(i), P5(ii)",
    tip: r`(a) is $1^\infty$ with $\tan\frac{\pi x}2$ in the exponent: use $\tan=\frac1{\cot}$. (b) is $0^0$: split $\ln(1-x^2)=\ln(1-x)+\ln(1+x)$.`,
    items: [
      { q: r`$\displaystyle\lim_{x\to1}(2-x)^{\tan(\pi x/2)}$`, s: r`$\ln y=\frac{\ln(2-x)}{\cot(\pi x/2)}$ ($\frac00$) $\to\frac{-1/(2-x)}{-\frac\pi2\csc^2(\pi x/2)}\to\frac{-1}{-\pi/2}=\frac2\pi$.`, a: r`$e^{2/\pi}$` },
      { q: r`$\displaystyle\lim_{x\to1^-}(1-x^2)^{\frac1{\ln(1-x)}}$`, s: r`$\ln y=\frac{\ln(1-x)+\ln(1+x)}{\ln(1-x)}=1+\frac{\ln(1+x)}{\ln(1-x)}\to1+\frac{\ln2}{-\infty}=1$.`, a: r`$e$` },
    ], formula: [r`Log trick for powers`] }),
  tryit([
    { q: r`$\displaystyle\lim_{x\to0}\frac{e^x-e^{-x}}{\sin x}$`, a: r`$2$` },
    { q: r`$\displaystyle\lim_{x\to0^+}x^{\sin x}$`, a: r`$1$` },
    { q: r`$\displaystyle\lim_{x\to0}(1+3x)^{1/x}$`, a: r`$e^3$` },
  ]),
  mistakes([
    r`Differentiating the quotient with the quotient rule instead of top and bottom separately.`,
    r`Using L'Hôpital when the form is not $\frac00$ or $\frac\infty\infty$ (e.g. $\frac{1}{0}$ or $\frac{\cos x}{x}$ at $\frac\pi2$).`,
    r`Forgetting the final step $y=e^{L}$ after finding $\lim\ln y=L$.`,
    r`Missing a simpler route: a standard limit, a factorisation or a series is often shorter than four rounds of L'Hôpital.`,
  ]),

  revision("Unit 1 · one-page revision sheet", [
    ["Limit exists", r`left limit $=$ right limit; standard: $\frac{\sin x}{x},\frac{e^x-1}{x},\frac{\ln(1+x)}{x}\to1$, $\frac{1-\cos x}{x^2}\to\frac12$, $\left(1+\frac kx\right)^x\to e^k$`],
    ["Continuous at $a$", r`$\lim_{x\to a^-}f=\lim_{x\to a^+}f=f(a)$. Types: removable, jump, infinite`],
    ["Differentiable at $a$", r`LHD $=$ RHD $=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$; differentiable $\Rightarrow$ continuous (not conversely)`],
    ["Rolle", r`continuous $[a,b]$, differentiable $(a,b)$, $f(a)=f(b)$ $\Rightarrow$ $f'(c)=0$`],
    ["Lagrange MVT", r`$f'(c)=\dfrac{f(b)-f(a)}{b-a}$, $c\in(a,b)$. Reject roots outside the open interval`],
    ["Cauchy MVT", r`$\dfrac{f'(c)}{g'(c)}=\dfrac{f(b)-f(a)}{g(b)-g(a)}$, $g'\ne0$`],
    ["L'Hôpital", r`$\frac00$ or $\frac\infty\infty$: $\lim\frac fg=\lim\frac{f'}{g'}$; repeat if the form persists`],
    [r`$0\cdot\infty$`, r`$f g=\dfrac{f}{1/g}$`],
    [r`$\infty-\infty$`, r`common denominator, then $\frac00$`],
    [r`$0^0,\ 1^\infty,\ \infty^0$`, r`$\ln y=g\ln f$, find $L=\lim\ln y$, answer $e^L$`],
    ["Handy results", r`$x^x\to1$ ($x\to0^+$), $x^{1/x}\to1$ ($x\to\infty$), $\left(\frac{a^x+b^x}2\right)^{1/x}\to\sqrt{ab}$`],
  ]),
];
