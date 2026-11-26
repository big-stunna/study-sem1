import { essentials, chapter, h, p, rule, fig, ex, tryit, mistakes, revision } from "./lib.mjs";
const R = String.raw;

export const meta = {
  eyebrow: "Unit 4 · Vector Calculus",
  title: "Differential Calculus: Unit 4",
  subtitle: "Vector-valued functions, arc length, gradient, divergence and curl, tangent and normal vectors, curvature, velocity and acceleration. Every problem of typed notes pp. 56 to 58 is solved inside its topic.",
  foot: "Adani University · Semester 1 · Dr Ankit Sharma's course",
  header: "Differential Calculus · Unit 4",
};

// ---------- figures (thin line art) ----------
const AR = id => `<defs><marker id="${id}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1,1 L9,5 L1,9" fill="none" stroke="currentColor" stroke-width="1.2"/></marker></defs>`;
const S = (w, inner) => `<svg width="${w}" viewBox="0 0 360 220" fill="none" stroke="currentColor" stroke-width="1.3" font-family="serif" font-size="20" xmlns="http://www.w3.org/2000/svg">${inner}</svg>`;

const figTangent = S(205, AR("a1") + `
<path d="M30,180 C90,60 170,40 330,70" />
<circle cx="140" cy="68" r="2.6" fill="currentColor"/>
<line x1="140" y1="68" x2="228" y2="62" marker-end="url(#a1)" stroke-width="1.8"/>
<line x1="30" y1="205" x2="140" y2="68" stroke-dasharray="3 4" stroke-width="1"/>
<line x1="30" y1="205" x2="150" y2="204" stroke-dasharray="3 4" stroke-width="1"/>
<text x="150" y="92">r(t)</text><text x="205" y="48">r'(t)</text><text x="10" y="150">C</text>`);

const figGrad = S(205, AR("a2") + `
<circle cx="150" cy="115" r="30"/><circle cx="150" cy="115" r="60"/><circle cx="150" cy="115" r="90"/>
<circle cx="236.4" cy="89" r="2.6" fill="currentColor"/>
<line x1="236.4" y1="89" x2="290" y2="73" marker-end="url(#a2)" stroke-width="1.8"/>
<text x="296" y="72">grad f</text><text x="226" y="112">P</text><text x="135" y="218">f=c</text>`);

const figPlane = S(205, AR("a3") + `
<path d="M70,150 L250,150 L300,100 L120,100 Z"/>
<path d="M60,175 C140,200 230,185 320,165" />
<circle cx="185" cy="125" r="2.6" fill="currentColor"/>
<line x1="185" y1="125" x2="185" y2="30" marker-end="url(#a3)" stroke-width="1.8"/>
<text x="195" y="45">n</text><text x="197" y="145">P</text><text x="110" y="140">plane</text>`);

const figVA = S(205, AR("a5") + `
<path d="M30,190 C70,80 190,40 330,100"/>
<circle cx="150" cy="75" r="2.6" fill="currentColor"/>
<line x1="150" y1="75" x2="235" y2="78" marker-end="url(#a5)" stroke-width="1.8"/>
<line x1="150" y1="75" x2="150" y2="150" marker-end="url(#a5)" stroke-width="1.8"/>
<line x1="10" y1="205" x2="150" y2="75" stroke-dasharray="3 4" stroke-width="1"/>
<text x="238" y="72">v</text><text x="158" y="148">a</text><text x="158" y="68">P</text>`);

const figOsc2 = S(205, AR("a4") + `
<path d="M60,30 Q180,230 300,30"/>
<circle cx="180" cy="73" r="48" stroke-dasharray="4 4" stroke-width="1"/>
<circle cx="180" cy="130" r="2.6" fill="currentColor"/><circle cx="180" cy="73" r="2.2" fill="currentColor"/>
<line x1="180" y1="73" x2="180" y2="128" stroke-width="1"/>
<line x1="180" y1="130" x2="240" y2="130" marker-end="url(#a4)" stroke-width="1.8"/>
<text x="246" y="134">T</text><text x="188" y="100">1/k</text><text x="188" y="70">C</text><text x="188" y="150">P</text>`);

// ---------- essentials ----------
const ess = essentials("Rules you need for this unit", [
  rule("Vector algebra", [
    R`$\vec a=\langle a_1,a_2,a_3\rangle,\quad |\vec a|=\sqrt{a_1^2+a_2^2+a_3^2},\quad \hat a=\dfrac{\vec a}{|\vec a|}$`,
    R`$\vec a\cdot\vec b=a_1b_1+a_2b_2+a_3b_3=|\vec a||\vec b|\cos\theta$`,
    R`$\vec a\times\vec b=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix},\quad \vec a\times\vec a=\vec 0$`,
  ]),
  rule("Derivatives to remember", [
    R`$(e^{kt})'=ke^{kt},\ (\sin t)'=\cos t,\ (\cos t)'=-\sin t,\ (\ln t)'=\tfrac1t,\ (\cosh t)'=\sinh t,\ (\sinh t)'=\cosh t$`,
    R`$\cosh^2t-\sinh^2t=1,\qquad \cosh^2t+\sinh^2t=\cosh 2t$`,
    R`$\dfrac{d}{dx}\arctan\dfrac yx$ w.r.t. $x$ is $\dfrac{-y}{x^2+y^2}$, w.r.t. $y$ is $\dfrac{x}{x^2+y^2}$`,
  ]),
  rule("Line and plane through a point", [
    R`Plane through $(x_0,y_0,z_0)$ with normal $\langle A,B,C\rangle$: $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$`,
    R`Line through the point with direction $\langle A,B,C\rangle$: $\dfrac{x-x_0}{A}=\dfrac{y-y_0}{B}=\dfrac{z-z_0}{C}$`,
  ]),
]);

// ---------- chapters ----------
const raw = [
  ess,

  // ===================== 1 =====================
  chapter("Vector-valued functions", { glance: {
    formula: R`$\vec r(t)=\langle x(t),y(t),z(t)\rangle$; limit, continuity, derivative act on each component; length $L=\int_a^b|\vec r'(t)|\,dt$.`,
    use: "A curve is given by a parameter $t$ and you need its length or a limit.",
    trap: R`Length needs $|\vec r'|$ (speed), not $|\vec r|$.` } }),
  rule("Limit and continuity", [
    R`$\displaystyle\lim_{t\to a}\vec r(t)=\Big\langle \lim x(t),\ \lim y(t),\ \lim z(t)\Big\rangle$ (exists iff all three exist)`,
    R`$\vec r$ is continuous at $a$ iff $\displaystyle\lim_{t\to a}\vec r(t)=\vec r(a)$, i.e. $x,y,z$ are all continuous at $a$.`,
  ]),
  rule("Length of a curve", [
    R`$L=\displaystyle\int_a^b|\vec r'(t)|\,dt=\int_a^b\sqrt{x'^2+y'^2+z'^2}\,dt$`,
  ]),
  ex({ n: 1, level: "Easy", src: "Book · Thomas §13.1",
    q: R`Find $\displaystyle\lim_{t\to0}\vec r(t)$ for $\vec r(t)=\Big\langle \dfrac{\sin 2t}{t},\ e^{t},\ \dfrac{1-\cos t}{t}\Big\rangle$ and decide whether $\vec r$ is continuous at $0$ if $\vec r(0)=\langle 2,1,0\rangle$.`,
    steps: [R`Componentwise: $\dfrac{\sin 2t}{t}\to2$, $e^t\to1$, $\dfrac{1-\cos t}{t}\to0$.`],
    answer: R`Limit $=\langle 2,1,0\rangle=\vec r(0)$, so $\vec r$ is continuous at $0$.`,
    formula: [R`$\lim\vec r=\langle\lim x,\lim y,\lim z\rangle$`] }),
  ex({ n: 2, level: "Medium", src: "Prof · Typed p.56 · Q1",
    q: R`Find the length of $\vec r(t)=4t\,\mathbf i-2t^3\mathbf j+(1-t^3)\mathbf k$ for $0\le t\le1$.`,
    tip: R`"Length on an interval" means $\int|\vec r'|\,dt$. Here the root does not simplify, so a numerical value is expected.`,
    steps: [R`$\vec r'=\langle4,-6t^2,-3t^2\rangle$, so $|\vec r'|^2=16+36t^4+9t^4=16+45t^4$.`,
      R`$L=\displaystyle\int_0^1\sqrt{16+45t^4}\,dt$. The integrand is not elementary; Simpson's rule gives the value.`],
    answer: R`$L=\displaystyle\int_0^1\sqrt{16+45t^4}\,dt\approx4.88$`,
    formula: [R`$L=\int_a^b|\vec r'|\,dt$`] }),
  ex({ n: 3, level: "Medium", src: "Prof · Typed p.56 · Q2",
    q: R`Find the length of $\vec r(t)=\langle 9-2t,\ 4+2t,\ \sqrt2\,t^2\rangle$ for $0\le t\le1$.`,
    tip: R`Check whether $|\vec r'|^2$ factors as a constant times $(1+t^2)$ or a perfect square.`,
    steps: [R`$\vec r'=\langle-2,2,2\sqrt2\,t\rangle$, $|\vec r'|^2=4+4+8t^2=8(1+t^2)$.`,
      R`$L=2\sqrt2\displaystyle\int_0^1\sqrt{1+t^2}\,dt=2\sqrt2\Big[\tfrac t2\sqrt{1+t^2}+\tfrac12\ln\big(t+\sqrt{1+t^2}\big)\Big]_0^1$.`,
      R`$=2\sqrt2\cdot\tfrac12\big(\sqrt2+\ln(1+\sqrt2)\big)$.`],
    answer: R`$L=2+\sqrt2\,\ln(1+\sqrt2)\approx3.246$`,
    formula: [R`$\int\sqrt{1+t^2}\,dt=\tfrac t2\sqrt{1+t^2}+\tfrac12\ln(t+\sqrt{1+t^2})$`] }),
  ex({ n: 4, level: "Hard", src: "Prof · Typed p.56 · Q3",
    q: R`Find the length of $\vec r(t)=2t\,\mathbf i+\tfrac12t^2\mathbf j+\ln(t^2)\,\mathbf k$ for $1\le t\le3$.`,
    tip: R`A sum like $4+t^2+\dfrac4{t^2}$ is the expansion of a perfect square, so the root disappears.`,
    steps: [R`$\vec r'=\langle2,\ t,\ \tfrac2t\rangle$, so $|\vec r'|^2=4+t^2+\dfrac4{t^2}=\Big(t+\dfrac2t\Big)^2$.`,
      R`$|\vec r'|=t+\dfrac2t$ since $t>0$, so $L=\displaystyle\int_1^3\Big(t+\dfrac2t\Big)dt=\Big[\tfrac{t^2}2+2\ln t\Big]_1^3$.`],
    answer: R`$L=4+2\ln3\approx6.197$`,
    formula: [R`$(a+b)^2=a^2+2ab+b^2$`, R`$\ln(t^2)=2\ln t$`] }),
  tryit([
    { q: R`Find the length of $\vec r(t)=\langle\cos t,\sin t,t\rangle$ for $0\le t\le2\pi$.`, a: R`$2\sqrt2\,\pi$` },
    { q: R`Find $\displaystyle\lim_{t\to0}\Big\langle \dfrac{\tan t}{t},\ \dfrac{e^{t}-1}{t},\ \cos t\Big\rangle$.`, a: R`$\langle1,1,1\rangle$` },
  ]),
  mistakes([
    R`Using $|\vec r(t)|$ instead of $|\vec r'(t)|$ in the length integral.`,
    R`Forgetting that $\sqrt{(t+2/t)^2}=t+2/t$ only because $t>0$ on the interval.`,
  ]),

  // ===================== 2 =====================
  chapter("Arc length and arc-length function", { glance: {
    formula: R`$s(t)=\displaystyle\int_{t_0}^{t}|\vec r'(u)|\,du$, so $\dfrac{ds}{dt}=|\vec r'(t)|$.`,
    use: "You must measure distance along a curve from a starting parameter, or reparametrise by $s$.",
    trap: R`Use a dummy variable $u$ inside the integral, and fix the lower limit $t_0$ (here $t_0=0$).` } }),
  rule("Arc-length function", [
    R`$s(t)=\displaystyle\int_0^t|\vec r'(u)|\,du$ (distance travelled from $t=0$)`,
    R`Curve is parametrised by arc length when $|\vec r'(s)|=1$.`,
  ]),
  ex({ n: 5, level: "Easy", src: "Prof · Typed p.56 · Q4",
    q: R`Find the arc-length function of $\vec r(t)=\langle8t,\ 6+t,\ -7t\rangle$.`,
    steps: [R`$\vec r'=\langle8,1,-7\rangle$, $|\vec r'|=\sqrt{64+1+49}=\sqrt{114}$ (constant).`, R`$s(t)=\displaystyle\int_0^t\sqrt{114}\,du$.`],
    answer: R`$s(t)=\sqrt{114}\;t$`,
    formula: [R`$s(t)=\int_0^t|\vec r'|\,du$`] }),
  ex({ n: 6, level: "Medium", src: "Prof · Typed p.56 · Q5",
    q: R`Find the arc-length function of $\vec r(t)=\langle8t,\ 4t^{3/2},\ 3\rangle$ (take $t\ge0$).`,
    tip: R`Under the root you get $a+bt$, a linear expression, which integrates as a power.`,
    steps: [R`$\vec r'=\langle8,\ 6t^{1/2},\ 0\rangle$, $|\vec r'|=\sqrt{64+36t}=2\sqrt{16+9t}$.`,
      R`$s(t)=\displaystyle\int_0^t2\sqrt{16+9u}\,du=2\cdot\tfrac{2}{27}\big[(16+9u)^{3/2}\big]_0^t$.`],
    answer: R`$s(t)=\dfrac4{27}\Big[(16+9t)^{3/2}-64\Big]$`,
    formula: [R`$\int\sqrt{a+bu}\,du=\tfrac{2}{3b}(a+bu)^{3/2}$`] }),
  ex({ n: 7, level: "Hard", src: "Prof · Typed p.56 · Q6",
    q: R`Find the arc-length function of $\vec r(t)=\langle e^{4t}\sin t,\ e^{4t}\cos t,\ 2\rangle$.`,
    tip: R`Exponential times trig: after the product rule the sines and cosines combine into $\sin^2+\cos^2=1$.`,
    steps: [R`$x'=e^{4t}(4\sin t+\cos t)$, $y'=e^{4t}(4\cos t-\sin t)$, $z'=0$.`,
      R`$x'^2+y'^2=e^{8t}\big[(4s+c)^2+(4c-s)^2\big]=e^{8t}\cdot17(s^2+c^2)=17e^{8t}$.`,
      R`$s(t)=\displaystyle\int_0^t\sqrt{17}\,e^{4u}\,du$.`],
    answer: R`$s(t)=\dfrac{\sqrt{17}}{4}\big(e^{4t}-1\big)$`,
    formula: [R`$\sin^2t+\cos^2t=1$`] }),
  ex({ n: 8, level: "Medium", src: "Prof · Typed p.56 · Q7",
    q: R`For $\vec r(t)=t^2\mathbf i+t^3\mathbf j+t\,\mathbf k$, $0\le t\le1$, find the arc-length function and the length of the curve.`,
    tip: R`The statement lists only the interval, so we give $s(t)$ and the length $s(1)$.`,
    steps: [R`$\vec r'=\langle2t,3t^2,1\rangle$, $|\vec r'|=\sqrt{1+4t^2+9t^4}$ (does not simplify).`,
      R`$s(t)=\displaystyle\int_0^t\sqrt{1+4u^2+9u^4}\,du$; the length is $s(1)$, found numerically.`],
    answer: R`$s(t)=\displaystyle\int_0^t\sqrt{1+4u^2+9u^4}\,du$, length $s(1)\approx1.863$`,
    formula: [R`$s(t)=\int_0^t|\vec r'|\,du$`] }),
  tryit([
    { q: R`Find $s(t)$ for (a) $\vec r=\langle3\cos t,3\sin t,4t\rangle$; (b) $\vec r=\langle2t,3t,6t\rangle$.`, a: R`(a) $s=5t$; (b) $s=7t$` },
  ]),
  mistakes([
    R`Writing $s=\int|\vec r'|\,dt$ without limits, which leaves a stray constant.`,
    R`Dropping the factor $2$ in $\sqrt{64+36t}=2\sqrt{16+9t}$ before integrating.`,
  ]),

  // ===================== 3 =====================
  chapter("Derivative of a vector function", { glance: {
    formula: R`$\vec r'(t)=\displaystyle\lim_{h\to0}\dfrac{\vec r(t+h)-\vec r(t)}{h}=\langle x',y',z'\rangle$, tangent to the curve.`,
    use: "You need a tangent direction, a rate of change, or a derivative of a dot or cross product.",
    trap: R`$\dfrac{d}{dt}(\vec u\times\vec v)=\vec u'\times\vec v+\vec u\times\vec v'$; the order of the cross product matters.` } }),
  fig(figTangent, R`The tangent vector $\vec r'(t)$ at a point of the curve $C$.`),
  rule("Differentiation rules", [
    R`$(\vec u\pm\vec v)'=\vec u'\pm\vec v',\qquad (f\vec u)'=f'\vec u+f\vec u'$`,
    R`$(\vec u\cdot\vec v)'=\vec u'\cdot\vec v+\vec u\cdot\vec v',\qquad (\vec u\times\vec v)'=\vec u'\times\vec v+\vec u\times\vec v'$`,
    R`$\vec r'(t)$ is tangent to the curve; $\vec T=\vec r'/|\vec r'|$; if $|\vec r|$ is constant then $\vec r\cdot\vec r'=0$`,
  ]),
  ex({ n: 9, level: "Easy", src: "Book · Thomas §13.1",
    q: R`If $\vec r(t)=\langle t,\ t^2,\ t^3\rangle$, find $\vec r'(1)$, $\vec r''(1)$ and the unit tangent at $t=1$.`,
    steps: [R`$\vec r'=\langle1,2t,3t^2\rangle\Rightarrow\vec r'(1)=\langle1,2,3\rangle$; $\vec r''=\langle0,2,6t\rangle\Rightarrow\vec r''(1)=\langle0,2,6\rangle$.`,
      R`$|\vec r'(1)|=\sqrt{14}$.`],
    answer: R`$\vec T(1)=\dfrac1{\sqrt{14}}\langle1,2,3\rangle$`,
    formula: [R`$\vec T=\vec r'/|\vec r'|$`] }),
  ex({ n: 10, level: "Medium", src: "Book · Thomas §13.1",
    q: R`If $\vec u=\langle t,\ t^2,\ 1\rangle$ and $\vec v=\langle \sin t,\ \cos t,\ t\rangle$, find $\dfrac{d}{dt}(\vec u\cdot\vec v)$ at $t=0$.`,
    tip: R`A derivative of a dot product of two vector functions: use the product rule, or expand the dot first.`,
    steps: [R`$\vec u\cdot\vec v=t\sin t+t^2\cos t+t$.`,
      R`$\dfrac{d}{dt}=\sin t+t\cos t+2t\cos t-t^2\sin t+1$, and at $t=0$ this is $0+0+0-0+1$.`],
    answer: R`$1$`,
    formula: [R`$(\vec u\cdot\vec v)'=\vec u'\cdot\vec v+\vec u\cdot\vec v'$`] }),
  tryit([
    { q: R`Find $\vec r'(t)$ for $\vec r=\langle e^{2t},\ \ln(1+t),\ t\cos t\rangle$.`, a: R`$\vec r'=\langle2e^{2t},\tfrac1{1+t},\cos t-t\sin t\rangle$` },
    { q: R`If $|\vec r(t)|=3$ for all $t$, show $\vec r\perp\vec r'$.`, a: R`$\vec r\cdot\vec r=9\Rightarrow2\vec r\cdot\vec r'=0$` },
  ]),
  mistakes([
    R`Differentiating $|\vec r|$ as if it were a vector: $|\vec r|'\ne|\vec r'|$.`,
    R`Swapping the order in $\vec u'\times\vec v+\vec u\times\vec v'$, which changes the sign.`,
  ]),

  // ===================== 4 =====================
  chapter("Gradient and directional derivative", { glance: {
    formula: R`$\nabla f=\langle f_x,f_y,f_z\rangle$; $D_{\hat u}f=\nabla f\cdot\hat u$; max rate $=|\nabla f|$ in direction $\nabla f$.`,
    use: "You need the rate of change of $f$ in a direction, or the direction of steepest ascent.",
    trap: R`The direction vector must be a **unit** vector before dotting with $\nabla f$.` } }),
  rule("Gradient and directional derivative", [
    R`$\nabla f=\langle f_x,f_y,f_z\rangle$`,
    R`$D_{\hat u}f=\nabla f\cdot\hat u=|\nabla f|\cos\theta$, with $\hat u=\dfrac{\vec v}{|\vec v|}$`,
    R`Maximum rate $=|\nabla f|$ along $\nabla f$; minimum $-|\nabla f|$ along $-\nabla f$; zero along level curves.`,
  ]),
  fig(figGrad, R`$\nabla f$ at $P$ is perpendicular to the level curve $f=c$ and points towards increasing $f$.`),
  ex({ n: 11, level: "Easy", src: "Prof · Typed p.57 · Q1, Q2",
    q: R`Find $\nabla f$ at the given point. (a) $f=xy^2-yz^2,\ P(-1,1)$. (b) $f=xe^y-\ln x,\ P(-3,0)$.`,
    tip: R`(a) The point has two coordinates, so the printed $z$ must be a misprint for $x$: we use $f=xy^2-yx^2$. (b) $\ln x$ is undefined at $x=-3$; we read it as $\ln|x|$, whose derivative is $1/x$.`,
    steps: [R`(a) $f_x=y^2-2xy=1+2=3$, $f_y=2xy-x^2=-2-1=-3$.`,
      R`(b) $f_x=e^y-\dfrac1x=1+\dfrac13=\dfrac43$, $f_y=xe^y=-3$.`],
    answer: R`(a) $\nabla f=\langle3,-3\rangle$. (b) $\nabla f=\langle\tfrac43,-3\rangle$.`,
    formula: [R`$\nabla f=\langle f_x,f_y\rangle$`, R`$(\ln|x|)'=1/x$`] }),
  ex({ n: 12, level: "Medium", src: "Prof · Typed p.57 · Q3, Q4",
    q: R`(a) $f=xy-\ln z$ at $P(2,-2,2)$. (b) $f=x\sqrt{y^2+z^2}$ at $P(-2,-1,-1)$.`,
    tip: R`Three variables: write all three partial derivatives before substituting.`,
    steps: [R`(a) $\nabla f=\langle y,\ x,\ -\tfrac1z\rangle=\langle-2,2,-\tfrac12\rangle$.`,
      R`(b) $\nabla f=\Big\langle\sqrt{y^2+z^2},\ \dfrac{xy}{\sqrt{y^2+z^2}},\ \dfrac{xz}{\sqrt{y^2+z^2}}\Big\rangle$; with $\sqrt{y^2+z^2}=\sqrt2$ this is $\langle\sqrt2,\ \tfrac2{\sqrt2},\ \tfrac2{\sqrt2}\rangle$.`],
    answer: R`(a) $\langle-2,\,2,\,-\tfrac12\rangle$. (b) $\langle\sqrt2,\sqrt2,\sqrt2\rangle$.`,
    formula: [R`$\dfrac{\partial}{\partial y}\sqrt{y^2+z^2}=\dfrac{y}{\sqrt{y^2+z^2}}$`] }),
  ex({ n: 13, level: "Easy", src: "Prof · Typed p.57 · Q6",
    q: R`Find the directional derivative of $f=x^2y+yz^2+z^3$ at $(1,2,1)$ in the direction $\vec v=2\mathbf i+3\mathbf j+6\mathbf k$.`,
    steps: [R`$\nabla f=\langle2xy,\ x^2+z^2,\ 2yz+3z^2\rangle=\langle4,2,7\rangle$ at $(1,2,1)$.`,
      R`$|\vec v|=7$, $\hat u=\tfrac17\langle2,3,6\rangle$, so $D_{\hat u}f=\tfrac17(8+6+42)$.`],
    answer: R`$D_{\hat u}f=8$`,
    formula: [R`$D_{\hat u}f=\nabla f\cdot\dfrac{\vec v}{|\vec v|}$`] }),
  ex({ n: 14, level: "Easy", src: "Prof · Typed p.57 · Q7",
    q: R`Find the directional derivative of $f=x^2yz^2$ at $(1,2,1)$ in the direction $\mathbf i+\mathbf j+\mathbf k$.`,
    steps: [R`$\nabla f=\langle2xyz^2,\ x^2z^2,\ 2x^2yz\rangle=\langle4,1,4\rangle$.`,
      R`$\hat u=\tfrac1{\sqrt3}\langle1,1,1\rangle$, so $D_{\hat u}f=\tfrac9{\sqrt3}$.`],
    answer: R`$3\sqrt3$`,
    formula: [R`$D_{\hat u}f=\nabla f\cdot\hat u$`] }),
  ex({ n: 15, level: "Medium", src: "Prof · Typed p.57 · Q5",
    q: R`$f=x^2+xy+y^2$ at $(-5,-4)$: find the directional derivative in the direction of most rapid increase.`,
    tip: R`The phrase "increases most rapidly" tells you to use $\nabla f$ itself, and the answer is $|\nabla f|$.`,
    steps: [R`$\nabla f=\langle2x+y,\ x+2y\rangle=\langle-14,-13\rangle$.`, R`$|\nabla f|=\sqrt{196+169}=\sqrt{365}$.`],
    answer: R`$D_{\hat u}f=\sqrt{365}$, along $\dfrac{\langle-14,-13\rangle}{\sqrt{365}}$`,
    formula: [R`$D_{\max}=|\nabla f|$`] }),
  ex({ n: 16, level: "Medium", src: "Prof · Typed p.57 · Q8, Q9",
    q: R`(a) $f=e^{xy}$ at $(6,7)$. (b) $f=\arctan\!\big(\tfrac yx\big)$ at $(-9,9)$.`,
    tip: R`Same phrase, so find $\nabla f$ and its magnitude. In (b) use $\partial_x\arctan\frac yx=\dfrac{-y}{x^2+y^2}$.`,
    steps: [R`(a) $\nabla f=e^{xy}\langle y,x\rangle=e^{42}\langle7,6\rangle$, $|\nabla f|=e^{42}\sqrt{85}$.`,
      R`(b) $x^2+y^2=162$: $\nabla f=\Big\langle\dfrac{-y}{162},\dfrac{x}{162}\Big\rangle=\langle-\tfrac1{18},-\tfrac1{18}\rangle$, $|\nabla f|=\dfrac{\sqrt2}{18}$.`],
    answer: R`(a) $e^{42}\sqrt{85}$ along $\langle7,6\rangle/\sqrt{85}$. (b) $\dfrac{\sqrt2}{18}$ along $\langle-1,-1\rangle/\sqrt2$.`,
    formula: [R`$\partial_x\arctan\frac yx=\frac{-y}{x^2+y^2}$`, R`$\partial_y\arctan\frac yx=\frac{x}{x^2+y^2}$`] }),
  ex({ n: 17, level: "Hard", src: "Prof · Typed p.57 · Q10, Q11",
    q: R`(a) $f=\ln(xy+yz+zx)$ at $(-9,-18,-27)$. (b) $f=\dfrac xy+\dfrac yz+\dfrac zx$ at $(5,-5,5)$. Direction of most rapid increase.`,
    tip: R`Three variables and a messy point: simplify the inside first, then evaluate each partial. In (b) the typed text is garbled; the page image shows the three fractions $\frac xy,\frac yz,\frac zx$.`,
    steps: [R`(a) $xy+yz+zx=162+486+243=891$. $\nabla f=\dfrac{\langle y+z,\ x+z,\ x+y\rangle}{891}=\dfrac{\langle-45,-36,-27\rangle}{891}=\dfrac{\langle-5,-4,-3\rangle}{99}$, $|\nabla f|=\dfrac{\sqrt{50}}{99}$.`,
      R`(b) $f_x=\tfrac1y-\tfrac z{x^2}=-\tfrac15-\tfrac15=-\tfrac25$, $f_y=-\tfrac x{y^2}+\tfrac1z=-\tfrac15+\tfrac15=0$, $f_z=-\tfrac y{z^2}+\tfrac1x=\tfrac15+\tfrac15=\tfrac25$.`],
    answer: R`(a) $\dfrac{5\sqrt2}{99}$ along $\langle-5,-4,-3\rangle/(5\sqrt2)$. (b) $\dfrac{2\sqrt2}{5}$ along $\langle-1,0,1\rangle/\sqrt2$.`,
    formula: [R`$\partial\ln u=\dfrac{\partial u}{u}$`] }),
  ex({ n: 18, level: "Easy", src: "Prof · Typed p.57 · Q10 (max-rate list)",
    q: R`Find the maximum rate of change of $f=x^2+3y^2$ at $(-1,1)$ and its direction.`,
    steps: [R`$\nabla f=\langle2x,6y\rangle=\langle-2,6\rangle$, $|\nabla f|=\sqrt{40}$.`],
    answer: R`Max rate $2\sqrt{10}$ in direction $\dfrac{\langle-1,3\rangle}{\sqrt{10}}$`,
    formula: [R`$\text{max rate}=|\nabla f|$`] }),
  ex({ n: 19, level: "Medium", src: "Prof · Typed p.57 · Q11 (max-rate list)",
    q: R`Find the maximum rate of change of $f=\sqrt{x^2+2y}$ at $(4,10)$ and its direction.`,
    tip: R`Evaluate the root first: $\sqrt{16+20}=6$.`,
    steps: [R`$\nabla f=\Big\langle\dfrac{x}{\sqrt{x^2+2y}},\ \dfrac1{\sqrt{x^2+2y}}\Big\rangle=\langle\tfrac46,\tfrac16\rangle$.`,
      R`$|\nabla f|=\dfrac{\sqrt{16+1}}6$.`],
    answer: R`Max rate $\dfrac{\sqrt{17}}6$ in direction $\dfrac{\langle4,1\rangle}{\sqrt{17}}$`,
    formula: [R`$\partial_y\sqrt u=\dfrac{u_y}{2\sqrt u}$`] }),
  ex({ n: 20, level: "Medium", src: "Prof · Typed p.57 · Q12 (max-rate list)",
    q: R`Find the maximum rate of change of $f=\cos(3x+2y)$ at $\big(\tfrac\pi6,-\tfrac\pi8\big)$ and its direction.`,
    tip: R`First compute the angle: $3x+2y=\tfrac\pi2-\tfrac\pi4=\tfrac\pi4$.`,
    steps: [R`$\nabla f=-\sin(3x+2y)\langle3,2\rangle=-\tfrac{\sqrt2}2\langle3,2\rangle$.`,
      R`$|\nabla f|=\tfrac{\sqrt2}2\sqrt{13}$.`],
    answer: R`Max rate $\dfrac{\sqrt{26}}2$ in direction $-\dfrac{\langle3,2\rangle}{\sqrt{13}}$`,
    formula: [R`$\nabla\cos g=-\sin g\,\nabla g$`] }),
  tryit([
    { q: R`$f=x^2y+z$ at $(1,2,3)$: find $D_{\hat u}f$ along $\langle1,2,2\rangle$ and the maximum rate.`, a: R`$\tfrac83$; $3\sqrt2$` },
    { q: R`$f=xe^{y}$ at $(2,0)$: direction of steepest ascent and rate.`, a: R`rate $\sqrt5$ along $\langle1,2\rangle$` },
  ]),
  mistakes([
    R`Dotting $\nabla f$ with $\vec v$ without dividing by $|\vec v|$ (that would give $56$ instead of $8$ in the $\vec v=\langle2,3,6\rangle$ problem).`,
    R`Substituting the point before differentiating.`,
    R`Quoting the direction without normalising it.`,
  ]),

  // ===================== 5 =====================
  chapter("Tangent plane and normal line to a surface", { glance: {
    formula: R`For $F(x,y,z)=c$ at $P$: normal $\vec n=\nabla F(P)$. Plane: $\nabla F(P)\cdot(\vec x-\vec x_0)=0$.`,
    use: "A surface is given implicitly and you want its plane or line at a point.",
    trap: R`Check the point lies on the surface first; move the constant to the right side before taking $\nabla F$.` } }),
  fig(figPlane, R`$\nabla F(P)$ is normal to the level surface $F=c$, hence to the tangent plane at $P$.`),
  rule("Tangent plane and normal line", [
    R`Plane: $F_x(x-x_0)+F_y(y-y_0)+F_z(z-z_0)=0$, partials evaluated at $P$.`,
    R`Normal line: $\dfrac{x-x_0}{F_x}=\dfrac{y-y_0}{F_y}=\dfrac{z-z_0}{F_z}$, or $\vec r=\vec r_0+t\nabla F(P)$.`,
  ]),
  ex({ n: 21, level: "Medium", src: "Prof · Typed p.57 · Q13",
    q: R`Find the tangent plane and normal line to $x^2+y^2+z^2=0$ at $(1,1,-2)$.`,
    tip: R`First test the point: $1+1+4=6\ne0$, so $(1,1,-2)$ is not on the surface as printed (it is just the origin). The sphere through the point is $x^2+y^2+z^2=6$; we solve that.`,
    steps: [R`$\nabla F=\langle2x,2y,2z\rangle=\langle2,2,-4\rangle\parallel\langle1,1,-2\rangle$.`,
      R`Plane: $(x-1)+(y-1)-2(z+2)=0$.`],
    answer: R`Plane: $x+y-2z=6$. Line: $\dfrac{x-1}{1}=\dfrac{y-1}{1}=\dfrac{z+2}{-2}$.`,
    formula: [R`$\vec n=\nabla F(P)$`] }),
  ex({ n: 22, level: "Easy", src: "Prof · Typed p.57 · Q14",
    q: R`Find the tangent plane and normal line to $xy+yz+zx=3$ at $(1,1,1)$.`,
    steps: [R`$\nabla F=\langle y+z,\ x+z,\ x+y\rangle=\langle2,2,2\rangle$.`, R`Plane: $2(x-1)+2(y-1)+2(z-1)=0$.`],
    answer: R`Plane: $x+y+z=3$. Line: $x-1=y-1=z-1$.`,
    formula: [R`$\vec n=\nabla F(P)$`] }),
  ex({ n: 23, level: "Medium", src: "Prof · Typed p.57 · Q15",
    q: R`Find the tangent plane and normal line to $x^2y-y+z=0$ at $(1,2,0)$.`,
    tip: R`A zero in the normal gives a line with fixed $y$: write it parametrically.`,
    steps: [R`Check: $2-2+0=0$. $\nabla F=\langle2xy,\ x^2-1,\ 1\rangle=\langle4,0,1\rangle$.`,
      R`Plane: $4(x-1)+0(y-2)+1(z-0)=0$.`],
    answer: R`Plane: $4x+z=4$. Line: $x=1+4t,\ y=2,\ z=t$.`,
    formula: [R`$\vec r=\vec r_0+t\nabla F$`] }),
  ex({ n: 24, level: "Medium", src: "Prof · Typed p.57 · Q16",
    q: R`Find the tangent plane and normal line to $xe^y\cos z-z=1$ at $(1,0,0)$.`,
    tip: R`Move the constant: $F=xe^y\cos z-z-1$; the point checks since $1\cdot1\cdot1-0=1$.`,
    steps: [R`$\nabla F=\langle e^y\cos z,\ xe^y\cos z,\ -xe^y\sin z-1\rangle=\langle1,1,-1\rangle$ at $(1,0,0)$.`,
      R`Plane: $(x-1)+y-z=0$.`],
    answer: R`Plane: $x+y-z=1$. Line: $x-1=y=-z$.`,
    formula: [R`$\vec n=\nabla F(P)$`] }),
  tryit([
    { q: R`(a) Tangent plane to $z=x^2+y^2$ at $(1,2,5)$. (b) Normal line to $x^2+y^2+z=3$ at $(1,1,1)$.`, a: R`(a) $2x+4y-z=5$; (b) $\langle1,1,1\rangle+t\langle2,2,1\rangle$` },
  ]),
  mistakes([
    R`Using $F=0$ when the surface is $F=c$: move $c$ to the left so that $\nabla F$ is unchanged but the point check is correct.`,
    R`Writing the plane with the normal components swapped, or leaving the point out.`,
  ]),

  // ===================== 6 =====================
  chapter("Divergence and curl", { glance: {
    formula: R`$\operatorname{div}\vec F=\nabla\cdot\vec F=P_x+Q_y+R_z$; $\operatorname{curl}\vec F=\nabla\times\vec F$.`,
    use: "Test whether a field is solenoidal ($\\operatorname{div}=0$) or irrotational ($\\operatorname{curl}=\\vec0$).",
    trap: R`Divergence is a scalar, curl is a vector; watch the sign of the $\mathbf j$ component.` } }),
  rule("Divergence and curl", [
    R`For $\vec F=P\mathbf i+Q\mathbf j+R\mathbf k$: $\ \operatorname{div}\vec F=\dfrac{\partial P}{\partial x}+\dfrac{\partial Q}{\partial y}+\dfrac{\partial R}{\partial z}$`,
    R`$\operatorname{curl}\vec F=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ \partial_x&\partial_y&\partial_z\\ P&Q&R\end{vmatrix}=\langle R_y-Q_z,\ P_z-R_x,\ Q_x-P_y\rangle$`,
    R`Solenoidal: $\nabla\cdot\vec F=0$. Irrotational: $\nabla\times\vec F=\vec 0$.`,
  ]),
  ex({ n: 25, level: "Easy", src: "Prof · Typed p.58 · Q1",
    q: R`Compute $\operatorname{div}\vec F$ and $\operatorname{curl}\vec F$ for $\vec F=x^2y\,\mathbf i-(z^3-3x)\mathbf j+4y^2\mathbf k$.`,
    steps: [R`$P=x^2y,\ Q=3x-z^3,\ R=4y^2$. $\operatorname{div}\vec F=2xy+0+0$.`,
      R`$R_y-Q_z=8y+3z^2$, $\ P_z-R_x=0$, $\ Q_x-P_y=3-x^2$.`],
    answer: R`$\operatorname{div}\vec F=2xy$, $\ \operatorname{curl}\vec F=\langle8y+3z^2,\ 0,\ 3-x^2\rangle$`,
    formula: [R`$\operatorname{curl}\vec F=\langle R_y-Q_z,P_z-R_x,Q_x-P_y\rangle$`] }),
  ex({ n: 26, level: "Medium", src: "Prof · Typed p.58 · Q2",
    q: R`Compute $\operatorname{div}\vec F$ and $\operatorname{curl}\vec F$ for $\vec F=(3x+2z^2)\mathbf i+\dfrac{x^3y^2}{z}\mathbf j-(z-7x)\mathbf k$.`,
    tip: R`A fraction with $z$ in the denominator: derivative in $z$ gives $-\dfrac{1}{z^2}$ factor.`,
    steps: [R`$P=3x+2z^2,\ Q=\dfrac{x^3y^2}{z},\ R=7x-z$. $\operatorname{div}\vec F=3+\dfrac{2x^3y}{z}-1$.`,
      R`$R_y-Q_z=0+\dfrac{x^3y^2}{z^2}$, $\ P_z-R_x=4z-7$, $\ Q_x-P_y=\dfrac{3x^2y^2}{z}$.`],
    answer: R`$\operatorname{div}\vec F=2+\dfrac{2x^3y}{z}$, $\ \operatorname{curl}\vec F=\Big\langle\dfrac{x^3y^2}{z^2},\ 4z-7,\ \dfrac{3x^2y^2}{z}\Big\rangle$`,
    formula: [R`$\partial_z(z^{-1})=-z^{-2}$`] }),
  ex({ n: 27, level: "Hard", src: "Prof · Typed p.58 · Q3",
    q: R`Is $\vec F=\Big(4y^2+\dfrac{3x^2y}{z^2}\Big)\mathbf i+\Big(8xy+\dfrac{x^3}{z^2}\Big)\mathbf j+\Big(11-\dfrac{2x^3y}{z^3}\Big)\mathbf k$ irrotational? solenoidal?`,
    tip: R`Long terms: check each curl component pair separately; they cancel in pairs.`,
    steps: [R`$R_y=-\dfrac{2x^3}{z^3}=Q_z$, so the $\mathbf i$ component is $0$.`,
      R`$P_z=-\dfrac{6x^2y}{z^3}=R_x$, so the $\mathbf j$ component is $0$. $\ Q_x=8y+\dfrac{3x^2}{z^2}=P_y$, so the $\mathbf k$ component is $0$.`,
      R`$\operatorname{div}\vec F=\dfrac{6xy}{z^2}+8x+\dfrac{6x^3y}{z^4}\ne0$.`],
    answer: R`Irrotational ($\operatorname{curl}\vec F=\vec0$), but **not** solenoidal.`,
    formula: [R`irrotational: $\nabla\times\vec F=\vec0$`] }),
  ex({ n: 28, level: "Easy", src: "Prof · Typed p.58 · Q4",
    q: R`Is $\vec F=6x\,\mathbf i+(2y-y^2)\mathbf j+(6z-x^3)\mathbf k$ irrotational? solenoidal?`,
    steps: [R`$\operatorname{div}\vec F=6+(2-2y)+6=14-2y\ne0$.`,
      R`$\operatorname{curl}\vec F=\langle0-0,\ 0-(-3x^2),\ 0-0\rangle=\langle0,3x^2,0\rangle\ne\vec0$.`],
    answer: R`Neither solenoidal nor irrotational.`,
    formula: [R`$\nabla\cdot\vec F,\ \nabla\times\vec F$`] }),
  ex({ n: 29, level: "Medium", src: "Prof · Typed p.58 · Q5",
    q: R`Find $a,b,c$ so that $\vec V=(x+2y+az)\mathbf i+(bx-3y-z)\mathbf j+(4x+cy+2z)\mathbf k$ is irrotational.`,
    tip: R`"Find constants so that it is irrotational": set each curl component to $0$.`,
    steps: [R`$\mathbf i$: $R_y-Q_z=c-(-1)=c+1=0$. $\mathbf j$: $P_z-R_x=a-4=0$. $\mathbf k$: $Q_x-P_y=b-2=0$.`],
    answer: R`$a=4,\ b=2,\ c=-1$`,
    formula: [R`$\operatorname{curl}\vec V=\vec0$`] }),
  ex({ n: 30, level: "Medium", src: "Prof · Typed p.58 · Q6",
    q: R`Show $\vec F=(6xy+z^3)\mathbf i+(3x^2-z)\mathbf j+(3xz^2-y)\mathbf k$ is irrotational but not solenoidal.`,
    tip: R`A field of the form $\nabla f$ is irrotational; here $f=3x^2y+xz^3-yz$.`,
    steps: [R`$R_y-Q_z=-1-(-1)=0$, $\ P_z-R_x=3z^2-3z^2=0$, $\ Q_x-P_y=6x-6x=0$.`,
      R`$\operatorname{div}\vec F=6y+0+6xz=6(y+xz)$, not identically $0$.`],
    answer: R`$\operatorname{curl}\vec F=\vec0$ and $\operatorname{div}\vec F=6y+6xz\ne0$.`,
    formula: [R`$\nabla\times\nabla f=\vec0$`] }),
  tryit([
    { q: R`Find $\operatorname{div}\vec F$ and $\operatorname{curl}\vec F$ for $\vec F=xy\mathbf i+yz\mathbf j+zx\mathbf k$.`, a: R`$x+y+z$; $\langle-y,-z,-x\rangle$` },
    { q: R`Show $\vec F=2x\mathbf i+3y\mathbf j-5z\mathbf k$ is both solenoidal and irrotational.`, a: R`$\operatorname{div}=2+3-5=0$; curl $=\vec0$` },
  ]),
  mistakes([
    R`Forgetting the minus sign in the $\mathbf j$ component of the determinant, i.e. writing $R_x-P_z$.`,
    R`Calling a field irrotational after checking only one or two curl components.`,
  ]),

  // ===================== 7 =====================
  chapter("Unit tangent and unit normal vectors", { glance: {
    formula: R`$\vec T=\dfrac{\vec r'}{|\vec r'|}$, $\ \vec N=\dfrac{\vec T'}{|\vec T'|}$, $\ \vec N\perp\vec T$.`,
    use: "You want the direction of motion ($\\vec T$) and the direction the curve bends ($\\vec N$).",
    trap: R`For a straight line $\vec T'=\vec0$, so $\vec N$ is undefined.` } }),
  rule("Unit tangent and unit normal", [
    R`$\vec T(t)=\dfrac{\vec r'(t)}{|\vec r'(t)|}$ (since $|\vec T|=1$, we get $\vec T\cdot\vec T'=0$)`,
    R`$\vec N(t)=\dfrac{\vec T'(t)}{|\vec T'(t)|}$, points to the concave side of the curve`,
  ]),
  ex({ n: 31, level: "Medium", src: "Prof · Typed p.58 · Q1 (tangent and normal)",
    q: R`For $\vec r(t)=\langle t^2,t^3\rangle$ find $\vec T$ and $\vec N$ at $t=1$.`,
    tip: R`In the plane, $\vec N$ is $\vec T$ rotated $90^\circ$ towards the concave side; you can find it without differentiating $\vec T$.`,
    steps: [R`$\vec r'=\langle2t,3t^2\rangle$, so for $t>0$: $\vec T=\dfrac{\langle2,3t\rangle}{\sqrt{4+9t^2}}$, $\ \vec T(1)=\dfrac{\langle2,3\rangle}{\sqrt{13}}$.`,
      R`$\vec N$ is perpendicular to $\vec T$: $\pm\langle-3,2\rangle/\sqrt{13}$. The curve $y=x^{3/2}$ bends upward (concave up), so $\vec N$ has positive $\mathbf j$ part.`],
    answer: R`$\vec T(1)=\dfrac{\langle2,3\rangle}{\sqrt{13}}$, $\ \vec N(1)=\dfrac{\langle-3,2\rangle}{\sqrt{13}}$`,
    formula: [R`$\vec T=\vec r'/|\vec r'|$`, R`$\vec N\perp\vec T$`] }),
  ex({ n: 32, level: "Medium", src: "Prof · Typed p.58 · Q2 (tangent and normal)",
    q: R`For $\vec r(t)=\langle\cos t,\sin t,t\rangle$ find $\vec T$ and $\vec N$ at $t=\pi/4$.`,
    tip: R`Constant $|\vec r'|=\sqrt2$ makes $\vec T'$ easy.`,
    steps: [R`$\vec r'=\langle-\sin t,\cos t,1\rangle$, $|\vec r'|=\sqrt2$, so $\vec T=\tfrac1{\sqrt2}\langle-\sin t,\cos t,1\rangle$.`,
      R`$\vec T'=\tfrac1{\sqrt2}\langle-\cos t,-\sin t,0\rangle$, $|\vec T'|=\tfrac1{\sqrt2}$, so $\vec N=\langle-\cos t,-\sin t,0\rangle$.`],
    answer: R`$\vec T\big(\tfrac\pi4\big)=\big\langle-\tfrac12,\ \tfrac12,\ \tfrac1{\sqrt2}\big\rangle$, $\ \vec N\big(\tfrac\pi4\big)=\big\langle-\tfrac1{\sqrt2},-\tfrac1{\sqrt2},0\big\rangle$`,
    formula: [R`$\vec N=\vec T'/|\vec T'|$`] }),
  ex({ n: 33, level: "Easy", src: "Prof · Typed p.58 · Q3 (tangent and normal)",
    q: R`For $\vec r(t)=\langle2+t,\ -(t+1),\ t\rangle$ find $\vec T$ and $\vec N$ at $t=0$.`,
    tip: R`Every component is linear in $t$, so the curve is a straight line.`,
    steps: [R`$\vec r'=\langle1,-1,1\rangle$ is constant, so $\vec T=\tfrac1{\sqrt3}\langle1,-1,1\rangle$ for all $t$.`,
      R`Hence $\vec T'=\vec0$ and $\vec N=\vec T'/|\vec T'|$ is not defined (a line does not bend).`],
    answer: R`$\vec T=\tfrac1{\sqrt3}\langle1,-1,1\rangle$; $\vec N$ does not exist (curvature $0$).`,
    formula: [R`$\vec T'=\vec0\Rightarrow\vec N$ undefined`] }),
  ex({ n: 34, level: "Medium", src: "Prof · Typed p.58 · Q4",
    q: R`For $\vec r(t)=\langle e^t,\sin t,\cos t\rangle$ find the unit tangent vector at $t=\pi$.`,
    steps: [R`$\vec r'=\langle e^t,\cos t,-\sin t\rangle$, and at $t=\pi$: $\langle e^{\pi},-1,0\rangle$.`,
      R`$|\vec r'(\pi)|=\sqrt{e^{2\pi}+1}$.`],
    answer: R`$\vec T(\pi)=\dfrac{\langle e^{\pi},-1,0\rangle}{\sqrt{e^{2\pi}+1}}$`,
    formula: [R`$\vec T=\vec r'/|\vec r'|$`] }),
  tryit([
    { q: R`(a) $\vec T,\vec N$ of $\langle\cos2t,\sin2t\rangle$ at $t=\pi/4$. (b) $\vec T(0)$ for $\langle t,t^2,t^3\rangle$.`, a: R`(a) $\langle-1,0\rangle,\ \langle0,-1\rangle$; (b) $\langle1,0,0\rangle$` },
  ]),
  mistakes([
    R`Forgetting to divide by $|\vec r'|$, so $\vec T$ is not a unit vector.`,
    R`Computing $\vec N$ as $\vec r''/|\vec r''|$, which is only correct when speed is constant.`,
  ]),

  // ===================== 8 =====================
  chapter("Curvature", { glance: {
    formula: R`$\kappa=\left|\dfrac{d\vec T}{ds}\right|=\dfrac{|\vec T'|}{|\vec r'|}=\dfrac{|\vec r'\times\vec r''|}{|\vec r'|^3}$; radius $\rho=1/\kappa$.`,
    use: "You want how sharply a curve bends at a point.",
    trap: R`Divide by $|\vec r'|^3$, not $|\vec r'|$; and differentiate $\vec T$ with respect to $s$, not $t$, in the definition.` } }),
  fig(figOsc2, R`Osculating circle at $P$: radius $1/\kappa$, centre $C$ on the normal side.`),
  rule("Curvature formulas", [
    R`$\kappa=\dfrac{|\vec T'(t)|}{|\vec r'(t)|}=\dfrac{|\vec r'\times\vec r''|}{|\vec r'|^3}$`,
    R`Plane curve $y=f(x)$: $\ \kappa=\dfrac{|f''|}{\big(1+f'^2\big)^{3/2}}$`,
    R`Circle of radius $a$: $\kappa=\dfrac1a$. Helix $\langle a\cos t,a\sin t,bt\rangle$: $\kappa=\dfrac{a}{a^2+b^2}$.`,
  ]),
  ex({ n: 36, level: "Medium", src: "Prof · Typed p.58 · Q1 (extended)",
    q: R`Find the curvature and radius of curvature of $\vec r(t)=\langle t^2,t^3\rangle$ at $t=1$.`,
    tip: R`Cross-product formula; in the plane the cross product has only a $\mathbf k$ component.`,
    steps: [R`$\vec r'(1)=\langle2,3\rangle$, $\vec r''(1)=\langle2,6\rangle$; $\ |\vec r'\times\vec r''|=|2\cdot6-3\cdot2|=6$.`,
      R`$|\vec r'|^3=13^{3/2}$.`],
    answer: R`$\kappa=\dfrac6{13\sqrt{13}}\approx0.128$, $\ \rho=\dfrac{13\sqrt{13}}6$`,
    formula: [R`$\kappa=\dfrac{|\vec r'\times\vec r''|}{|\vec r'|^3}$`] }),
  ex({ n: 37, level: "Easy", src: "Book · Thomas §13.4",
    q: R`Find the curvature of $y=x^2$ at $x=1$.`,
    steps: [R`$f'=2x=2$, $f''=2$ at $x=1$.`, R`$\kappa=\dfrac{2}{(1+4)^{3/2}}$.`],
    answer: R`$\kappa=\dfrac{2}{5\sqrt5}$`,
    formula: [R`$\kappa=\dfrac{|f''|}{(1+f'^2)^{3/2}}$`] }),
  tryit([
    { q: R`Curvature of (a) $y=e^x$ at $x=0$; (b) the circle $\langle3\cos t,3\sin t\rangle$.`, a: R`(a) $\tfrac1{2\sqrt2}$; (b) $\tfrac13$` },
  ]),
  mistakes([
    R`Using $\kappa=|f''|$ and forgetting the factor $(1+f'^2)^{3/2}$.`,
    R`Dividing by $|\vec r'|$ instead of $|\vec r'|^3$ in the cross-product formula.`,
  ]),

  // ===================== 9 =====================
  chapter("Velocity, acceleration and speed", { glance: {
    formula: R`$\vec v=\vec r'$, $\ \text{speed}=|\vec v|$, $\ \vec a=\vec v'=\vec r''$.`,
    use: "A particle's position is given as a function of time.",
    trap: R`Speed is a scalar, $|\vec v|$; it is not $|\vec r|$.` } }),
  fig(figVA, R`Velocity $\vec v$ is tangent to the path; acceleration $\vec a$ points towards the concave side.`),
  rule("Motion in space", [
    R`$\vec v=\dfrac{d\vec r}{dt},\quad \text{speed}=|\vec v|=\dfrac{ds}{dt},\quad \vec a=\dfrac{d\vec v}{dt}$`,
    R`Polar form: $\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta$, $\ \vec a=(\ddot r-r\dot\theta^2)\vec u_r+(r\ddot\theta+2\dot r\dot\theta)\vec u_\theta$`,
  ]),
  ex({ n: 38, level: "Easy", src: "Prof · Typed p.58 · Q1 (motion)",
    q: R`$\vec r=\langle t^3,2t^2,t\rangle$. Find velocity, speed and acceleration at $t=1$.`,
    steps: [R`$\vec v=\langle3t^2,4t,1\rangle\to\langle3,4,1\rangle$; $\vec a=\langle6t,4,0\rangle\to\langle6,4,0\rangle$.`],
    answer: R`$\vec v=\langle3,4,1\rangle$, speed $\sqrt{26}$, $\vec a=\langle6,4,0\rangle$`,
    formula: [R`$\vec v=\vec r',\ \vec a=\vec r''$`] }),
  ex({ n: 39, level: "Easy", src: "Prof · Typed p.58 · Q2 (motion)",
    q: R`$\vec r=\langle\sin t,\cos t,t^2\rangle$. Find velocity, speed and acceleration at $t=\pi/2$.`,
    steps: [R`$\vec v=\langle\cos t,-\sin t,2t\rangle\to\langle0,-1,\pi\rangle$; $\vec a=\langle-\sin t,-\cos t,2\rangle\to\langle-1,0,2\rangle$.`],
    answer: R`$\vec v=\langle0,-1,\pi\rangle$, speed $\sqrt{1+\pi^2}$, $\vec a=\langle-1,0,2\rangle$`,
    formula: [R`$\text{speed}=|\vec v|$`] }),
  ex({ n: 40, level: "Medium", src: "Prof · Typed p.58 · Q3 (motion)",
    q: R`$\vec r=\langle4e^t,t^2,\ln(1+t)\rangle$. Find $\vec v$, $\vec a$ and speed at $t=0$.`,
    tip: R`Remember $\dfrac{d}{dt}\ln(1+t)=\dfrac1{1+t}$ and its second derivative is $-\dfrac1{(1+t)^2}$.`,
    steps: [R`$\vec v=\langle4e^t,2t,\tfrac1{1+t}\rangle\to\langle4,0,1\rangle$; $\vec a=\langle4e^t,2,-\tfrac1{(1+t)^2}\rangle\to\langle4,2,-1\rangle$.`],
    answer: R`$\vec v=\langle4,0,1\rangle$, speed $\sqrt{17}$, $\vec a=\langle4,2,-1\rangle$`,
    formula: [R`$(\ln(1+t))'=\dfrac1{1+t}$`] }),
  ex({ n: 41, level: "Medium", src: "Prof · Typed p.58 · Q4 (motion)",
    q: R`$\vec r=\langle\cosh t,\sinh t\rangle$. Find velocity, acceleration and speed at $t=1$.`,
    tip: R`Hyperbolic identities: $\cosh^2+\sinh^2=\cosh2t$.`,
    steps: [R`$\vec v=\langle\sinh t,\cosh t\rangle$, $\ \vec a=\langle\cosh t,\sinh t\rangle=\vec r$.`,
      R`Speed $=\sqrt{\sinh^2t+\cosh^2t}=\sqrt{\cosh2t}$.`],
    answer: R`$\vec v=\langle\sinh1,\cosh1\rangle$, $\vec a=\langle\cosh1,\sinh1\rangle$, speed $\sqrt{\cosh2}\approx1.94$`,
    formula: [R`$\cosh^2t+\sinh^2t=\cosh2t$`] }),
  ex({ n: 42, level: "Easy", src: "Prof · Typed p.58 · Q5, Q6 (motion)",
    q: R`(a) $\vec r=t^2\mathbf i+3t\mathbf j+2\mathbf k$: find $\vec v,\vec a$. (b) $\vec r=e^{2t}\mathbf i+\sin t\,\mathbf j+\ln(1+t)\mathbf k$: find $\vec v,\vec a$ at $t=0$.`,
    steps: [R`(a) $\vec v=\langle2t,3,0\rangle$, $\ \vec a=\langle2,0,0\rangle$, speed $\sqrt{4t^2+9}$.`,
      R`(b) $\vec v=\langle2e^{2t},\cos t,\tfrac1{1+t}\rangle\to\langle2,1,1\rangle$; $\ \vec a=\langle4e^{2t},-\sin t,-\tfrac1{(1+t)^2}\rangle\to\langle4,0,-1\rangle$.`],
    answer: R`(a) $\vec v=\langle2t,3,0\rangle$, $\vec a=\langle2,0,0\rangle$. (b) $\vec v(0)=\langle2,1,1\rangle$, $\vec a(0)=\langle4,0,-1\rangle$.`,
    formula: [R`$\vec v=\vec r',\ \vec a=\vec r''$`] }),
  ex({ n: 43, level: "Hard", src: "Book · Thomas Ch. 13 Practice Ex 7",
    q: R`A rod through the origin rotates about it at $3$ rad/min. A beetle starts at $(2,0)$ and crawls along the rod towards the origin at $1$ in/min. (a) Find its velocity and acceleration in polar form when it is $1$ in from the origin. (b) Find the length of its path until it reaches the origin.`,
    tip: R`$\dot r$ and $\dot\theta$ are given: use the polar formulas.`,
    steps: [R`$r=2-t$, $\theta=3t$, so $\dot r=-1$, $\ddot r=0$, $\dot\theta=3$, $\ddot\theta=0$. At $r=1$: $t=1$.`,
      R`$\vec v=\dot r\vec u_r+r\dot\theta\vec u_\theta=-\vec u_r+3\vec u_\theta$.`,
      R`$\vec a=(\ddot r-r\dot\theta^2)\vec u_r+(r\ddot\theta+2\dot r\dot\theta)\vec u_\theta=-9\vec u_r-6\vec u_\theta$.`,
      R`Speed $=\sqrt{\dot r^2+r^2\dot\theta^2}=\sqrt{1+9(2-t)^2}$; with $s=2-t$: length $=\displaystyle\int_0^2\sqrt{1+9s^2}\,ds=\Big[\tfrac s2\sqrt{1+9s^2}+\tfrac16\ln\big(3s+\sqrt{1+9s^2}\big)\Big]_0^2$.`],
    answer: R`(a) $\vec v=-\vec u_r+3\vec u_\theta$, $\ \vec a=-9\vec u_r-6\vec u_\theta$ (in/min and in/min$^2$). (b) $\sqrt{37}+\tfrac16\ln(6+\sqrt{37})\approx6.5$ in.`,
    formula: [R`$\vec v=\dot r\vec u_r+r\dot\theta\vec u_\theta$`, R`$\vec a=(\ddot r-r\dot\theta^2)\vec u_r+(r\ddot\theta+2\dot r\dot\theta)\vec u_\theta$`] }),
  ex({ n: 44, level: "Hard", src: "Book · Thomas Ch. 13 Practice Ex 8",
    q: R`A body of mass $m$ moves under the force $\vec F=-\dfrac{c}{|\vec r|^3}\vec r$ ($c$ constant). Prove that the angular momentum $\vec L=\vec r\times m\vec v$ is constant.`,
    tip: R`Conserved means the derivative is $\vec 0$.`,
    steps: [R`$\dfrac{d\vec L}{dt}=m(\vec v\times\vec v)+m(\vec r\times\vec a)=\vec 0+\vec r\times m\vec a$.`,
      R`By Newton's law $m\vec a=\vec F=-\dfrac{c}{|\vec r|^3}\vec r$, so $\vec r\times m\vec a=-\dfrac{c}{|\vec r|^3}(\vec r\times\vec r)=\vec 0$.`],
    answer: R`$\dfrac{d\vec L}{dt}=\vec0$, hence $\vec L$ is a constant vector.`,
    formula: [R`$(\vec u\times\vec v)'=\vec u'\times\vec v+\vec u\times\vec v'$`, R`$\vec a\times\vec a=\vec0$`] }),
  tryit([
    { q: R`$\vec r=\langle t,t^2,t^3\rangle$: find $\vec v$, $\vec a$ and speed at $t=1$.`, a: R`$\langle1,2,3\rangle$; $\langle0,2,6\rangle$; $\sqrt{14}$` },
    { q: R`A particle moves on $\langle2\cos t,2\sin t\rangle$. Show speed is constant and $|\vec a|$ is constant.`, a: R`Speed $2$, $|\vec a|=2$` },
  ]),
  mistakes([
    R`Taking speed as $|\vec r|$ or as the magnitude of one component.`,
    R`In polar form, dropping the cross term $2\dot r\dot\theta$ in the $\vec u_\theta$ part of $\vec a$.`,
  ]),

  revision("Unit 4: one-page revision", [
    ["Vector function", R`$\vec r(t)=\langle x,y,z\rangle$; limit and continuity componentwise`],
    ["Length", R`$L=\int_a^b|\vec r'|\,dt$`],
    ["Arc-length function", R`$s(t)=\int_0^t|\vec r'|\,du,\ \ ds/dt=|\vec r'|$`],
    ["Derivative rules", R`$(\vec u\cdot\vec v)'=\vec u'\cdot\vec v+\vec u\cdot\vec v'$, $(\vec u\times\vec v)'=\vec u'\times\vec v+\vec u\times\vec v'$`],
    ["Gradient", R`$\nabla f=\langle f_x,f_y,f_z\rangle\perp$ level set`],
    ["Directional derivative", R`$D_{\hat u}f=\nabla f\cdot\hat u$, $\hat u=\vec v/|\vec v|$; max $=|\nabla f|$`],
    ["Tangent plane", R`$\nabla F(P)\cdot(\vec x-\vec x_0)=0$; normal line direction $\nabla F(P)$`],
    ["Div and curl", R`$\nabla\cdot\vec F=P_x+Q_y+R_z$; $\nabla\times\vec F=\langle R_y-Q_z,P_z-R_x,Q_x-P_y\rangle$`],
    ["Types of field", R`Solenoidal: $\nabla\cdot\vec F=0$. Irrotational: $\nabla\times\vec F=\vec 0$`],
    ["Unit tangent, normal", R`$\vec T=\vec r'/|\vec r'|$, $\ \vec N=\vec T'/|\vec T'|$`],
    ["Curvature", R`$\kappa=\dfrac{|\vec r'\times\vec r''|}{|\vec r'|^3}=\dfrac{|f''|}{(1+f'^2)^{3/2}}$, $\rho=1/\kappa$`],
    ["Motion", R`$\vec v=\vec r'$, speed $|\vec v|$, $\vec a=\vec r''$`],
    ["Polar motion", R`$\vec v=\dot r\vec u_r+r\dot\theta\vec u_\theta$, $\ \vec a=(\ddot r-r\dot\theta^2)\vec u_r+(r\ddot\theta+2\dot r\dot\theta)\vec u_\theta$`],
  ]),
];

// ---- tighten: drop / merge worked examples, renumber sequentially ----
const DROP = new Set([1, 9, 35, 37]);
const GROUPS = [[5, 6], [11, 12], [13, 14], [15, 16], [18, 19, 20], [21, 22], [23, 24], [25, 26], [27, 28], [29, 30], [31, 32], [33, 34], [38, 39, 40], [41, 42]];
const lvlRank = { Easy: 0, Medium: 1, Hard: 2 }, lvlName = ["Easy", "Medium", "Hard"];
function merge(parts) {
  const tail = o => o.src.split(" · ").pop().match(/^(.*?)( \(.*\))?$/);
  const label = o => tail(o)[1];
  const suf = tail(parts[0])[2] || "";
  const pre = parts[0].src.split(" · ").slice(0, -1).join(" · ");
  const lv = lvlName[Math.max(...parts.map(o => lvlRank[o.level]))];
  const tips = parts.filter(o => o.tip);
  const forms = [...new Set(parts.flatMap(o => o.formula || []))].slice(0, 3);
  return ex({
    n: 0, level: lv, src: pre + " · " + parts.map(label).join(", ") + suf,
    q: parts.map(o => `**${label(o)}.** ${o.q}`).join("  "),
    tip: lv === "Easy" ? undefined : tips.map(o => (tips.length > 1 ? `**${label(o)}.** ` : "") + o.tip).slice(0, 2).join(" "),
    steps: parts.map(o => `**${label(o)}.** ` + o.steps.join(" ")),
    answer: parts.map(o => `**${label(o)}.** ${o.answer}`).join("  "),
    formula: forms,
  });
}
export const blocks = (() => {
  const out = []; let k = 0;
  for (let i = 0; i < raw.length; i++) {
    const b = raw[i];
    if (b.k === "mistakes") { out.push({ ...b, items: b.items.slice(0, 1) }); continue; }
    if (b.k !== "ex") { out.push(b); continue; }
    if (DROP.has(b.n)) continue;
    const g = GROUPS.find(g => g[0] === b.n);
    if (g) {
      const parts = raw.filter(x => x.k === "ex" && g.includes(x.n));
      out.push({ ...merge(parts), n: ++k });
    } else if (GROUPS.some(g => g.includes(b.n))) continue;
    else out.push({ ...b, n: ++k });
  }
  return out;
})();
