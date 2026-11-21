"""Shared builder for CP unit notes. Unicode TTF fonts only (no ZapfDingbats/Symbol),
every character is checked against the font cmap, every `run=True` C snippet is compiled
(-Wall -Wextra) and executed so the printed Output is real."""
import re, os, subprocess, tempfile, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    Table, TableStyle, KeepTogether, XPreformatted, PageBreak, CondPageBreak, Flowable)

FD = '/usr/share/fonts/noto/'
FONTS = {'Math': 'NotoSansMath-Regular.ttf', 'Sans': 'NotoSans-Regular.ttf', 'Sans-B': 'NotoSans-Bold.ttf', 'Sans-I': 'NotoSans-Italic.ttf',
         'Sans-BI': 'NotoSans-BoldItalic.ttf', 'Mono': 'NotoSansMono-Regular.ttf', 'Mono-B': 'NotoSansMono-Bold.ttf'}
CMAPS = {}
for k, f in FONTS.items():
    pdfmetrics.registerFont(TTFont(k, FD + f))
    CMAPS[k] = set(TTFont(k, FD + f).face.charToGlyph.keys())
pdfmetrics.registerFontFamily('Sans', normal='Sans', bold='Sans-B', italic='Sans-I', boldItalic='Sans-BI')
pdfmetrics.registerFontFamily('Mono', normal='Mono', bold='Mono-B', italic='Mono', boldItalic='Mono-B')

THEME = {'c': colors.HexColor('#5b3fd6')}   # accent, set by build()
INK = colors.HexColor('#1c1c28'); GREY = colors.HexColor('#5f6368')
W = A4[0] - 36 * mm
PROBLEMS = []

def check(text, fonts, where=''):
    for ch in text:
        if ch in '\n\t\r': continue
        if not all(ord(ch) in CMAPS[f] for f in fonts):
            PROBLEMS.append(f'missing glyph U+{ord(ch):04X} {ch!r} in: {where or text[:50]!r}')

TAGS = r'</?(?:b|i|u|sub|super|br/?)>'
def _fb(t):
    """chars missing from Noto Sans but present in Noto Sans Mono (arrows, >=, <=, sqrt...) get Mono; anything else is a problem."""
    out = ''
    for ch in t:
        o = ord(ch)
        if ch in '\n\t\r' or o in CMAPS['Sans'] and o in CMAPS['Sans-B'] and o in CMAPS['Sans-I']: out += ch
        elif o in CMAPS['Math']: out += f'<font name="Math">{ch}</font>'
        elif o in CMAPS['Mono'] and o in CMAPS['Mono-B']: out += f'<font name="Mono">{ch}</font>'
        else: PROBLEMS.append(f'missing glyph U+{o:04X} {ch!r} near: {t[:50]!r}'); out += '?'
    return out

def M(s):
    """mini markup: `code`, <b> <i> <u> <sub> <super> allowed; everything else escaped."""
    parts = s.split('`')
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            check(p, ['Mono'], p)
            e = p.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            out.append(f'<font name="Mono" size="8.6" color="#9c2b2b">{e}</font>')
        else:
            keep = re.findall(TAGS, p)
            ph = re.split(TAGS, p)
            seg = ''
            for j, t in enumerate(ph):
                seg += _fb(t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
                if j < len(keep): seg += keep[j]
            out.append(seg)
    if len(parts) % 2 == 0: PROBLEMS.append(f'unbalanced backtick: {s[:60]!r}')
    return ''.join(out)

def S(name, **kw):
    base = dict(fontName='Sans', fontSize=9.6, leading=14, textColor=INK, spaceAfter=4)
    base.update(kw); return ParagraphStyle(name, **base)
ST = {
 'p': S('p'), 'pj': S('pj'),
 'h2': S('h2', fontName='Sans-B', fontSize=11, leading=14, spaceBefore=8, spaceAfter=3),
 'h3': S('h3', fontName='Sans-B', fontSize=9.8, leading=13, spaceBefore=5, spaceAfter=2),
 'b': S('b', leftIndent=14, bulletIndent=4, spaceAfter=2),
 'b2': S('b2', leftIndent=28, bulletIndent=18, spaceAfter=1.5, fontSize=9.3, leading=13),
 'cell': S('cell', fontSize=8.8, leading=12, spaceAfter=0),
 'cellh': S('cellh', fontName='Sans-B', fontSize=8.8, leading=12, spaceAfter=0, textColor=colors.white),
 'q': S('q', fontName='Sans-B', fontSize=9.4, leading=13, spaceAfter=0),
 'sol': S('sol', fontSize=9.2, leading=13, spaceAfter=0, leftIndent=0),
}

def P(t, style='p'): return Paragraph(M(t), ST[style])
def H2(t): return Paragraph(M(t), ST['h2'])
def H3(t): return Paragraph(M(t), ST['h3'])
def SP(h=4): return Spacer(1, h)

def H1(t):
    c = THEME['c']
    tb = Table([[Paragraph(M(t), S('h1', fontName='Sans-B', fontSize=14.5, leading=18, spaceAfter=0))]],
               colWidths=[W - 4])
    tb.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 8), ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3), ('LINEBEFORE', (0, 0), (0, 0), 4, c)]))
    tb.keepWithNext = True
    return [CondPageBreak(60 * mm), SP(8), tb, SP(5)]

def BUL(items, depth=0):
    out = []
    for it in items:
        if isinstance(it, (list, tuple)):
            out += BUL(it, depth + 1)
        else:
            out.append(Paragraph(M(it), ST['b'] if depth == 0 else ST['b2'], bulletText='•' if depth == 0 else '–'))
    return out

def NUM(items):
    return [Paragraph(M(t), ST['b'], bulletText=f'{i}.') for i, t in enumerate(items, 1)]

def _box(label, lcolor, bg, body_items):
    rows = [[Paragraph(f'<font name="Sans-B" size="8" color="{lcolor}">{label}</font>', S('bl', spaceAfter=0))]]
    for it in body_items:
        rows.append([it])
    t = Table(rows, colWidths=[W])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(bg)),
        ('LINEBEFORE', (0, 0), (0, -1), 3, colors.HexColor(lcolor)),
        ('LEFTPADDING', (0, 0), (-1, -1), 9), ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, 0), 5), ('BOTTOMPADDING', (0, -1), (-1, -1), 5)]))
    return [t, SP(6)]

def NOTE(t, label='NOTE'): return _box(label, '#c25e00', '#fff4e5', [Paragraph(M(t), ST['sol'])])
def WARN(t): return _box('COMMON MISTAKE', '#b3261e', '#fdecea', [Paragraph(M(t), ST['sol'])])
def TIP(t): return _box('EXAM TIP', '#1b7a43', '#e9f7ef', [Paragraph(M(t), ST['sol'])])
def SYNTAX(t): return _box('SYNTAX', '#0b6fa4', '#e8f3fa', [Paragraph(M(t), ST['sol'])])
def FORMULA(t): return _box('FORMULA', '#6a1b9a', '#f4eafa', [Paragraph(M(t), ST['sol'])])
def RECALL(items):
    return _box('QUICK RECALL', '#444444', '#f1f1f4', [Paragraph(M(t), ST['sol'], bulletText='•') for t in items])

def TABLE(rows, widths=None, head=True, zebra=True, small=False):
    c = THEME['c']
    cs, hs = ST['cell'], ST['cellh']
    data = []
    for r, row in enumerate(rows):
        data.append([Paragraph(M(str(x)), hs if (head and r == 0) else cs) for x in row])
    n = len(rows[0])
    widths = widths or [1] * n
    tot = float(sum(widths)); cw = [W * w / tot for w in widths]
    t = Table(data, colWidths=cw, repeatRows=1 if head else 0)
    sty = [('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#c9c9d3')), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
           ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
           ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
    if head: sty.append(('BACKGROUND', (0, 0), (-1, 0), c))
    if zebra:
        for r in range(1 if head else 0, len(rows)):
            if r % 2 == 0: sty.append(('BACKGROUND', (0, r), (-1, r), colors.HexColor('#f4f4f8')))
    t.setStyle(TableStyle(sty))
    return [t, SP(7)]

KW = set('auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while'.split())
_tok = re.compile(r'(?P<cm>//[^\n]*|/\*.*?\*/)|(?P<st>"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])\')|(?P<pp>^[ \t]*#[ \t]*\w+)|(?P<nu>\b0[xX][0-9a-fA-F]+\b|\b\d+\.?\d*(?:[eE][+-]?\d+)?[fFuUlL]*\b)|(?P<id>[A-Za-z_]\w*)', re.S | re.M)
def _esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def hl(src):
    out, pos = [], 0
    for m in _tok.finditer(src):
        out.append(_esc(src[pos:m.start()])); pos = m.end(); g = m.lastgroup; t = _esc(m.group())
        if g == 'cm': out.append(f'<font color="#6a737d">{t}</font>')
        elif g == 'st': out.append(f'<font color="#1a7f37">{t}</font>')
        elif g == 'pp': out.append(f'<font color="#8250df">{t}</font>')
        elif g == 'nu': out.append(f'<font color="#b35900">{t}</font>')
        elif g == 'id' and m.group() in KW: out.append(f'<b><font color="#0550ae">{t}</font></b>')
        else: out.append(t)
    out.append(_esc(src[pos:]))
    return ''.join(out)

CSTY = ParagraphStyle('code', fontName='Mono', fontSize=8.2, leading=11.2, textColor=INK, backColor=colors.HexColor('#f3f4f8'),
    borderColor=colors.HexColor('#d5d7e2'), borderWidth=0.5, borderPadding=(5, 6, 5, 6), leftIndent=6, rightIndent=6,
    spaceBefore=4, spaceAfter=9)
OSTY = ParagraphStyle('out', parent=CSTY, backColor=colors.HexColor('#1e1f2b'), textColor=colors.HexColor('#e8e8f0'),
    borderColor=colors.HexColor('#1e1f2b'), spaceBefore=0, spaceAfter=9)
MAXCOL = 88
WSTY = ParagraphStyle('work', fontName='Mono', fontSize=8.2, leading=11.4, textColor=INK, backColor=colors.HexColor('#eef0f7'), borderPadding=(4, 6, 4, 6), leftIndent=20, rightIndent=8, spaceBefore=3, spaceAfter=8)

def run_c(src, stdin='', warn_ok=False):
    with tempfile.TemporaryDirectory() as d:
        cf, ex = os.path.join(d, 'a.c'), os.path.join(d, 'a.out')
        open(cf, 'w').write(src)
        r = subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-o', ex, cf, '-lm'], capture_output=True, text=True)
        if r.returncode != 0 or (r.stderr.strip() and not warn_ok):
            PROBLEMS.append('COMPILE: ' + r.stderr[:600] + '\n--- in ---\n' + src[:300]); return None
        p = subprocess.run([ex], input=stdin, capture_output=True, text=True, timeout=5, cwd=d)
        return p.stdout

def CODE(src, run=False, stdin='', out=None, label=None, warn_ok=False):
    """src is dedented source. run=True: compile with -Wall -Wextra and show real output."""
    src = src.strip('\n')
    check(src, ['Mono'], 'code: ' + src[:40])
    for ln in src.split('\n'):
        if len(ln) > MAXCOL: PROBLEMS.append(f'code line too long ({len(ln)}): {ln[:60]}')
    items = []
    if label:
        items.append(Paragraph(f'<font name="Sans-B" size="8" color="#555555">{M(label)}</font>', S('cl', spaceAfter=0, spaceBefore=3)))
    items.append(XPreformatted(hl(src), CSTY))
    if run:
        o = run_c(src, stdin, warn_ok)
        if o is None: o = '<<COMPILE FAILED>>'
        out = o
    if out is not None:
        check(out, ['Mono'], 'output')
        o = out.expandtabs(8).rstrip('\n')
        if stdin: o = ('[input] ' + stdin.strip().replace('\n', ' ⏎ ') + '\n' + o) if False else o
        items.append(Paragraph('<font name="Sans-B" size="7.5" color="#8a8fa8">OUTPUT</font>', S('ol', spaceAfter=0, leftIndent=6)))
        items.append(XPreformatted(_esc(o) if o else '(no output)', OSTY))
        # pull label+code+output together when short
    if len(src.split('\n')) < 30: return [KeepTogether(items)]
    return items

DIFF = {'g': ('EASY', '#2e9e48'), 'y': ('MEDIUM', '#e08a1e'), 'r': ('HARD', '#e0434f')}
def QA(level, q, sol, code=None):
    """sol: str or list of str paragraphs. code: list of CODE() flowables (already built)."""
    name, col = DIFF[level]
    badge = Paragraph(f'<font name="Sans-B" size="8" color="white">{name}</font>', S('bd', alignment=1, spaceAfter=0, leading=10))
    head = Table([[Paragraph(M(q), ST['q']), badge]], colWidths=[W - 62, 52])
    head.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#f4f4f8')), ('BACKGROUND', (1, 0), (1, 0), colors.HexColor(col)),
        ('LINEBEFORE', (0, 0), (0, 0), 3, colors.HexColor(col)), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (0, 0), 8), ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5), ('LEFTPADDING', (1, 0), (1, 0), 3), ('RIGHTPADDING', (1, 0), (1, 0), 3)]))
    head.keepWithNext = True
    items = [sol] if isinstance(sol, (str, tuple)) else sol
    solst = ParagraphStyle('solp', parent=ST['sol'], backColor=colors.HexColor('#fafafc'), borderPadding=(3, 6, 3, 6), leftIndent=6, rightIndent=6, spaceAfter=6, spaceBefore=2)
    stepst = ParagraphStyle('stepp', parent=solst, leftIndent=26, bulletIndent=10, spaceAfter=2.5, spaceBefore=0)
    linest = ParagraphStyle('linep', parent=solst, leftIndent=20, spaceAfter=2.5, spaceBefore=0)
    label = '<font name="Sans-B" color="%s">Solution:</font>' % col
    body = []
    for n, it in enumerate(items):
        if isinstance(it, str):
            body.append(Paragraph((label + ' ' if n == 0 else '') + M(it), solst))
            continue
        if n == 0: body.append(Paragraph(label, ParagraphStyle('lab', parent=solst, spaceAfter=3)))
        kind, data = it
        if kind == 'steps':
            for k, x in enumerate(data, 1): body.append(Paragraph(M(x), stepst, bulletText=f'{k}.'))
            body.append(SP(3))
        elif kind == 'lines':
            for x in data:
                nsp = len(x) - len(x.lstrip(' '))
                body.append(Paragraph(M(x.strip()), ParagraphStyle('lp', parent=linest, leftIndent=20 + nsp * 3.3)) if nsp else Paragraph(M(x), linest))
            body.append(SP(3))
        elif kind == 'work':
            w = data.strip('\n'); check(w, ['Mono'], 'work: ' + w[:40])
            for ln in w.split('\n'):
                if len(ln) > MAXCOL - 6: PROBLEMS.append(f'work line too long: {ln[:50]}')
            body.append(XPreformatted(_esc(w), WSTY))
    flow = [SP(5), head, SP(2)] + body
    if code:
        for c in code: flow += c if isinstance(c, list) else [c]
    return flow

def build(path, unit, title, sub, meta, syllabus, color, story):
    THEME['c'] = colors.HexColor(color)
    def deco(cv, doc):
        cv.saveState(); cv.setFont('Sans', 7.5); cv.setFillColor(GREY)
        cv.drawString(18 * mm, A4[1] - 11 * mm, f'Computer Programming · Unit {unit} · {title}')
        cv.drawCentredString(A4[0] / 2, 9 * mm, f'{doc.page}')
        cv.setStrokeColor(colors.HexColor(color)); cv.setLineWidth(1.2); cv.line(18 * mm, A4[1] - 13 * mm, A4[0] - 18 * mm, A4[1] - 13 * mm)
        cv.restoreState()
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=18 * mm, bottomMargin=16 * mm,
                          title=f'Computer Programming — Unit {unit} Notes', author='CP study notes')
    doc.addPageTemplates([PageTemplate(id='p', frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)], onPage=deco)])
    ttl = Table([[Paragraph(f'<font name="Sans-B" size="19" color="white">Unit {unit} — {M(title)}</font>', S('t', leading=24, spaceAfter=2)),],
                 [Paragraph(f'<font size="9" color="#e9e6ff">{M(meta)}</font>', S('t2', spaceAfter=0))]], colWidths=[W])
    ttl.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(color)), ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, -1), (-1, -1), 11)]))
    head = [ttl, SP(6), Paragraph('<font name="Sans-B">Syllabus:</font> ' + M(syllabus), S('syl', fontSize=8.8, textColor=GREY))]
    flat = []
    for x in story:
        flat += x if isinstance(x, list) else [x]
    doc.build(head + flat)
    if PROBLEMS:
        print('PROBLEMS:'); [print(' -', p) for p in dict.fromkeys(PROBLEMS)]
        return False
    return True

# ---------------------------------------------------------------- flowcharts
from reportlab.graphics.shapes import Drawing, Rect, Polygon, Line, String
import math

def _txt(g, x, y, s, size=7.6, bold=False, col=colors.HexColor('#1c1c28'), anchor='middle'):
    check(s, ['Sans', 'Sans-B'], 'flow:' + s)
    g.add(String(x, y, s, fontName='Sans-B' if bold else 'Sans', fontSize=size, fillColor=col, textAnchor=anchor))

def FLOW(steps, width=215, acc=None):
    """steps: ('start',txt) ('stop',txt) ('io',txt) ('proc',txt)
              ('if',cond,yes_txt,no_txt)  -> diamond + two branch boxes that rejoin
              ('loop',cond,[body steps])   -> while-style loop (body: io/proc only)"""
    acc = acc or THEME['c']
    cx = width / 2; GAP = 15; LINE = colors.HexColor('#444455'); ops = []
    def box(kind, text, t):
        h = {'t': 20, 'io': 22, 'p': 22}[kind]
        ops.append((kind, cx, t, h, text)); return t + h
    def arrow(x1, t1, x2, t2): ops.append(('arrow', x1, t1, x2, t2))
    def seg(x1, t1, x2, t2): ops.append(('seg', x1, t1, x2, t2))
    kinds = {'start': 't', 'stop': 't', 'io': 'io', 'proc': 'p'}
    t = 4.0; prev_bottom = None
    for st in steps:
        k = st[0]
        if prev_bottom is not None:
            arrow(cx, prev_bottom, cx, prev_bottom + GAP); t = prev_bottom + GAP
        if k in kinds:
            prev_bottom = box(kinds[k], st[1], t)
        elif k == 'if':
            dh = 40; ops.append(('dia', cx, t, dh, st[1])); mid = t + dh / 2
            lx, rx = cx - 52, cx + 52
            seg(cx - 40, mid, lx, mid); arrow(lx, mid, lx, mid + 16); seg(cx + 40, mid, rx, mid); arrow(rx, mid, rx, mid + 16)
            y0 = mid + 16
            ops.append(('bx', lx, y0, 22, st[2], 'Yes')); ops.append(('bx', rx, y0, 22, st[3], 'No'))
            join = y0 + 22 + 10
            seg(lx, y0 + 22, lx, join); seg(rx, y0 + 22, rx, join); seg(lx, join, rx, join)
            prev_bottom = join
        elif k == 'loop':
            dh = 40; ops.append(('dia', cx, t, dh, st[1])); mid = t + dh / 2
            cur = t + dh
            ops.append(('lbl', cx + 4, cur + 10, 'Yes'))
            for b in st[2]:
                arrow(cx, cur, cx, cur + GAP); cur += GAP
                cur = box(kinds[b[0]], b[1], cur)
            back = cur + 10
            seg(cx, cur, cx, back); seg(cx, back, cx - 82, back); seg(cx - 82, back, cx - 82, mid); arrow(cx - 82, mid, cx - 40, mid)
            seg(cx + 40, mid, cx + 82, mid); ops.append(('lbl', cx + 44, mid - 3, 'No'))
            ex = back + 12
            seg(cx + 82, mid, cx + 82, ex); seg(cx + 82, ex, cx, ex)
            prev_bottom = ex
    H = prev_bottom + 6
    d = Drawing(width, H)
    Y = lambda tt: H - tt
    for op in ops:
        o = op[0]
        if o in ('t', 'io', 'p'):
            _, x, tt, h, text = op; top = Y(tt)
            if o == 't':
                d.add(Rect(x - 40, top - h, 80, h, rx=10, ry=10, fillColor=colors.HexColor('#e8e4ff'), strokeColor=acc, strokeWidth=0.9))
            elif o == 'io':
                d.add(Polygon([x - 52, top - h, x - 40, top, x + 52, top, x + 40, top - h], fillColor=colors.HexColor('#e3f2fd'), strokeColor=acc, strokeWidth=0.9))
            else:
                d.add(Rect(x - 52, top - h, 104, h, fillColor=colors.HexColor('#fff6e0'), strokeColor=acc, strokeWidth=0.9))
            _txt(d, x, top - h / 2 - 2.6, text, bold=(o == 't'))
        elif o == 'dia':
            _, x, tt, h, text = op; top = Y(tt)
            d.add(Polygon([x, top, x + 40, top - h / 2, x, top - h, x - 40, top - h / 2], fillColor=colors.HexColor('#e9f7ef'), strokeColor=acc, strokeWidth=0.9))
            _txt(d, x, top - h / 2 - 2.6, text, size=7.2)
        elif o == 'bx':
            _, x, tt, h, text, lab = op; top = Y(tt)
            d.add(Rect(x - 46, top - h, 92, h, fillColor=colors.HexColor('#fff6e0'), strokeColor=acc, strokeWidth=0.9))
            _txt(d, x, top - h / 2 - 2.6, text, size=7.2)
            _txt(d, x + (-4 if lab == 'Yes' else 4), top + 4, lab, size=6.6, bold=True, col=colors.HexColor('#555555'), anchor='end' if lab == 'Yes' else 'start')
        elif o == 'lbl':
            _txt(d, op[1], Y(op[2]), op[3], size=6.6, bold=True, col=colors.HexColor('#555555'), anchor='start')
        elif o == 'seg':
            _, x1, t1, x2, t2 = op; d.add(Line(x1, Y(t1), x2, Y(t2), strokeColor=LINE, strokeWidth=0.9))
        elif o == 'arrow':
            _, x1, t1, x2, t2 = op; d.add(Line(x1, Y(t1), x2, Y(t2), strokeColor=LINE, strokeWidth=0.9))
            ang = math.atan2(Y(t2) - Y(t1), x2 - x1); a = 4.2
            d.add(Polygon([x2, Y(t2), x2 - a * math.cos(ang - 0.45), Y(t2) - a * math.sin(ang - 0.45),
                           x2 - a * math.cos(ang + 0.45), Y(t2) - a * math.sin(ang + 0.45)], fillColor=LINE, strokeColor=LINE, strokeWidth=0.3))
    return d

def ALGO_FLOW(title, algo_lines, flow):
    left = [Paragraph(f'<font name="Sans-B">{M(title)}</font>', ST['h3'])]
    for ln in algo_lines:
        ind = len(ln) - len(ln.lstrip(' '))
        left.append(Paragraph(M(ln.strip()), ParagraphStyle('al', parent=ST['sol'], leftIndent=ind * 3, spaceAfter=1.5)))
    fd = FLOW(flow)
    t = Table([[left, fd]], colWidths=[W - 225, 225])
    t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#d5d7e2')),
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#fafafc')), ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 6)]))
    return [KeepTogether([t]), SP(8)]
