"""Minimalist black-and-white guide builder for ESS notes.
Fonts: Noto Sans (text) + Noto Sans Math (arrows, >=, ~) + Noto Sans Mono (working blocks).
Every character is checked against the font tables; any missing glyph is reported before the PDF is accepted."""
import re, os, io, hashlib
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether, XPreformatted, CondPageBreak, Image as RLImage, PageBreak)

FD = '/usr/share/fonts/noto/'
FONTS = {'Math': 'NotoSansMath-Regular.ttf', 'Sans': 'NotoSans-Regular.ttf', 'Sans-B': 'NotoSans-Bold.ttf', 'Sans-I': 'NotoSans-Italic.ttf',
         'Sans-BI': 'NotoSans-BoldItalic.ttf', 'Mono': 'NotoSansMono-Regular.ttf', 'Mono-B': 'NotoSansMono-Bold.ttf'}
CMAPS = {}
for k, f in FONTS.items():
    pdfmetrics.registerFont(TTFont(k, FD + f)); CMAPS[k] = set(TTFont(k, FD + f).face.charToGlyph.keys())
pdfmetrics.registerFontFamily('Sans', normal='Sans', bold='Sans-B', italic='Sans-I', boldItalic='Sans-BI')
pdfmetrics.registerFontFamily('Mono', normal='Mono', bold='Mono-B', italic='Mono', boldItalic='Mono-B')
PROBLEMS = []
from reportlab.platypus import Flowable
class Story(list):
    def __iadd__(self, x):
        if isinstance(x, Flowable): self.append(x)
        else: self.extend(x)
        return self
INK = colors.black; W = A4[0] - 44 * mm
TAGS = r'</?(?:b|i|u|sub|super|br/?)>'

def _fb(t):
    out = ''
    for ch in t:
        o = ord(ch)
        if ch in '\n\t\r' or (o in CMAPS['Sans'] and o in CMAPS['Sans-B'] and o in CMAPS['Sans-I']): out += ch
        elif o in CMAPS['Math']: out += f'<font name="Math">{ch}</font>'
        else: PROBLEMS.append(f'missing glyph U+{o:04X} {ch!r} near {t[:50]!r}'); out += '?'
    return out

def M(s):
    for m in re.finditer(r'<(/?)([A-Za-z][A-Za-z0-9]*)', s):
        if m.group(2).lower() not in ('b', 'i', 'u', 'sub', 'super', 'br'): PROBLEMS.append(f'unsupported tag <{m.group(1)}{m.group(2)}> in: {s[:60]!r}')
    parts = s.split('`'); out = []
    for i, p in enumerate(parts):
        if i % 2:
            for ch in p:
                if ord(ch) not in CMAPS['Mono']: PROBLEMS.append(f'missing mono glyph {ch!r}')
            out.append('<font name="Mono" size="9">' + p.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;') + '</font>')
        else:
            keep = re.findall(TAGS, p); ph = re.split(TAGS, p); seg = ''
            for j, t in enumerate(ph):
                seg += _fb(t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
                if j < len(keep): seg += keep[j]
            out.append(seg)
    if len(parts) % 2 == 0: PROBLEMS.append(f'unbalanced backtick: {s[:60]!r}')
    return ''.join(out)

def S(name, **kw):
    b = dict(fontName='Sans', bulletFontName='Sans', fontSize=10, leading=14.6, textColor=INK, spaceAfter=5); b.update(kw); return ParagraphStyle(name, **b)
ST = {'p': S('p'), 'b': S('b', leftIndent=14, bulletIndent=3, spaceAfter=2.5), 'b2': S('b2', leftIndent=28, bulletIndent=17, spaceAfter=2, fontSize=9.6, leading=13.6),
      'cell': S('cell', fontSize=9, leading=12.4, spaceAfter=0), 'cellh': S('cellh', fontName='Sans-B', fontSize=9, leading=12.4, spaceAfter=0),
      'cap': S('cap', fontName='Sans-I', fontSize=8.6, leading=11.5, spaceBefore=3, spaceAfter=10, alignment=1, textColor=colors.HexColor('#333333')),
      'h2': S('h2', fontName='Sans-B', fontSize=11.5, leading=15, spaceBefore=11, spaceAfter=4, keepWithNext=1), 'h3': S('h3', fontName='Sans-B', fontSize=10, leading=14, spaceBefore=6, spaceAfter=2, keepWithNext=1),
      'q': S('q', fontName='Sans-B', spaceAfter=3, spaceBefore=0), 'sol': S('sol', leftIndent=12, spaceAfter=3.5),
      'solstep': S('solstep', leftIndent=26, bulletIndent=12, spaceAfter=2.5), 'tag': S('tag', fontName='Sans-B', fontSize=8, leading=10, spaceAfter=2, spaceBefore=9, keepWithNext=1)}
def P(t, style='p'): return Paragraph(M(t), ST[style])
def H2(t): return Paragraph(M(t), ST['h2'])
def H3(t): return Paragraph(M(t), ST['h3'])
def SP(h=5): return Spacer(1, h)
def H1(t):
    p = Paragraph(M(t), S('h1', fontName='Sans-B', fontSize=15, leading=19, spaceAfter=0))
    tb = Table([[p]], colWidths=[W]); tb.setStyle(TableStyle([('LINEBELOW', (0, 0), (-1, -1), 1.1, INK), ('LEFTPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 4), ('TOPPADDING', (0, 0), (-1, -1), 0)]))
    return [CondPageBreak(55 * mm), SP(12), tb, SP(8)]
def BUL(items, depth=0):
    out = []
    for it in items:
        if isinstance(it, (list, tuple)): out += BUL(it, depth + 1)
        else: out.append(Paragraph(M(it), ST['b'] if depth == 0 else ST['b2'], bulletText='•' if depth == 0 else '–'))
    return out
def NUM(items): return [Paragraph(M(t), ST['b'], bulletText=f'{i}.') for i, t in enumerate(items, 1)]
def TABLE(rows, widths=None):
    data = [[Paragraph(M(str(x)), ST['cellh'] if r == 0 else ST['cell']) for x in row] for r, row in enumerate(rows)]
    n = len(rows[0]); widths = widths or [1] * n; tot = float(sum(widths))
    t = Table(data, colWidths=[W * w / tot for w in widths], repeatRows=1)
    t.setStyle(TableStyle([('LINEABOVE', (0, 0), (-1, 0), 1, INK), ('LINEBELOW', (0, 0), (-1, 0), 0.7, INK), ('LINEBELOW', (0, 1), (-1, -1), 0.3, colors.HexColor('#9a9a9a')),
        ('LINEBELOW', (0, -1), (-1, -1), 1, INK), ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5)]))
    return [t, SP(8)]
def BOX(label, body):
    items = [Paragraph(f'<font name="Sans-B" size="8">{M(label)}</font>', S('bl', spaceAfter=2))] + [Paragraph(M(x), S('bb', fontSize=9.6, leading=13.8, spaceAfter=2)) for x in (body if isinstance(body, list) else [body])]
    t = Table([[items]], colWidths=[W]); t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.8, INK), ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8), ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
    return [KeepTogether([t]), SP(8)]
def KEY(t): return BOX('KEY POINT', t)
def FORMULA(t): return BOX('FORMULA', t)
def RECALL(items):
    flow = [Paragraph('<font name="Sans-B" size="8">QUICK RECALL</font>', S('bl', spaceAfter=3))] + [Paragraph(M(x), S('rb', fontSize=9.6, leading=13.8, leftIndent=12, bulletIndent=2, spaceAfter=2.5), bulletText='•') for x in items]
    t = Table([[flow]], colWidths=[W]); t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 0.8, INK), ('LEFTPADDING', (0, 0), (-1, -1), 8), ('RIGHTPADDING', (0, 0), (-1, -1), 8), ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    return [KeepTogether([t]), SP(8)]

_cache = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.imgcache'); os.makedirs(_cache, exist_ok=True)
def FIG(path, caption, maxw=15.5, maxh=9.2):
    """maxw / maxh in cm. Photos are re-saved as JPEG (q=88, <=1600px); diagrams stay PNG."""
    im = Image.open(path)
    if im.mode in ('RGBA', 'LA', 'P'):
        bg = Image.new('RGB', im.size, 'white'); rgba = im.convert('RGBA'); bg.paste(rgba, mask=rgba.split()[3]); im = bg
    else: im = im.convert('RGB')
    if max(im.size) > 1600: im.thumbnail((1600, 1600), Image.LANCZOS)
    key = hashlib.md5(open(path, 'rb').read()).hexdigest()[:10]; out = os.path.join(_cache, key + '.jpg'); im.save(out, 'JPEG', quality=90, optimize=True)
    w, h = im.size; sc = min(maxw * 10 * mm / w, maxh * 10 * mm / h)
    tw, th = w * sc, h * sc
    cap = Paragraph(M(caption), ST['cap'])
    t = Table([[RLImage(out, width=tw, height=th)]], colWidths=[W]); t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0), ('BOX', (0, 0), (-1, -1), 0.4, colors.HexColor('#999999'))]))
    t._argW = [W]
    return [KeepTogether([SP(3), t, cap])]

WSTY = ParagraphStyle('work', fontName='Mono', fontSize=8.6, leading=12, textColor=INK, backColor=colors.HexColor('#f2f2f2'), borderPadding=(4, 6, 4, 6), leftIndent=22, rightIndent=8, spaceBefore=3, spaceAfter=9)
TAGNAME = {'e': 'EASY', 'm': 'MEDIUM', 'h': 'HARD'}
def QA(level, q, sol):
    """sol items: str paragraph | ('steps',[...]) numbered | ('lines',[...]) | ('work', text) monospace block"""
    items = [sol] if isinstance(sol, (str, tuple)) else sol
    flow = [Paragraph(f'[ {TAGNAME[level]} ]', ST['tag']), Paragraph(M(q), ST['q'])]
    lab = '<font name="Sans-BI">Answer.</font> '
    for n, it in enumerate(items):
        if isinstance(it, str):
            flow.append(Paragraph((lab if n == 0 else '') + M(it), ST['sol'])); continue
        if n == 0: flow.append(Paragraph(lab, ST['sol']))
        kind, data = it
        if kind == 'steps':
            for k, x in enumerate(data, 1): flow.append(Paragraph(M(x), ST['solstep'], bulletText=f'{k}.'))
        elif kind == 'lines':
            for x in data: flow.append(Paragraph(M(x), ST['solstep'], bulletText='•'))
        elif kind == 'work':
            w = data.strip('\n')
            for ch in w:
                if ch != '\n' and ord(ch) not in CMAPS['Mono']: PROBLEMS.append(f'missing mono glyph {ch!r} in work block')
            for ln in w.split('\n'):
                if len(ln) > 86: PROBLEMS.append(f'work line too long: {ln[:40]}')
            flow.append(XPreformatted(w.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), WSTY))
    flow.append(SP(2))
    return [KeepTogether(flow)]

def build(path, unit, title, intro, story):
    def deco(cv, doc):
        cv.saveState(); cv.setFont('Sans', 8); cv.setFillColor(colors.HexColor('#444444'))
        cv.drawString(22 * mm, 11 * mm, f'Environmental Science & Sustainability  ·  Unit {unit}')
        cv.drawRightString(A4[0] - 22 * mm, 11 * mm, str(doc.page)); cv.setStrokeColor(colors.HexColor('#888888')); cv.setLineWidth(0.4)
        cv.line(22 * mm, 15 * mm, A4[0] - 22 * mm, 15 * mm); cv.restoreState()
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=22 * mm, rightMargin=22 * mm, topMargin=20 * mm, bottomMargin=22 * mm, title=f'ESS Unit {unit} Study Guide', author='ESS study notes')
    doc.addPageTemplates([PageTemplate(id='p', frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f', leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)], onPage=deco)])
    head = [Paragraph(f'UNIT {unit}', S('u', fontName='Sans-B', fontSize=10, spaceAfter=2)), Paragraph(M(title), S('t', fontName='Sans-B', fontSize=24, leading=29, spaceAfter=4)),
            Paragraph('Environmental Science &amp; Sustainability (ESS)  ·  Exam Study Guide', S('st', fontSize=11, spaceAfter=7))]
    tb = Table([[head]], colWidths=[W]); tb.setStyle(TableStyle([('LINEBELOW', (0, 0), (-1, -1), 1.4, INK), ('LEFTPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 8)]))
    flat = []
    for x in story: flat += x if isinstance(x, list) else [x]
    from functools import partial
    from reportlab.pdfgen.canvas import Canvas
    doc.build([tb, SP(8)] + [P(intro)] + flat, canvasmaker=partial(Canvas, initialFontName='Sans', initialFontSize=10))
    if PROBLEMS:
        print('PROBLEMS:'); [print(' -', p) for p in dict.fromkeys(PROBLEMS)]; return False
    return True

def FIGROW(items, maxw=7.6, maxh=5.6):
    """items: [(path, caption), ...] placed side by side in one row (2 per row)."""
    cells = []; n = len(items)
    cw = W / n
    for path, caption in items:
        im = Image.open(path)
        if im.mode in ('RGBA', 'LA', 'P'):
            bg = Image.new('RGB', im.size, 'white'); rgba = im.convert('RGBA'); bg.paste(rgba, mask=rgba.split()[3]); im = bg
        else: im = im.convert('RGB')
        if max(im.size) > 1400: im.thumbnail((1400, 1400), Image.LANCZOS)
        key = hashlib.md5(open(path, 'rb').read()).hexdigest()[:10]; out = os.path.join(_cache, key + '.jpg'); im.save(out, 'JPEG', quality=90, optimize=True)
        w, h = im.size; sc = min(maxw * 10 * mm / w, maxh * 10 * mm / h)
        cells.append([RLImage(out, width=w * sc, height=h * sc), Paragraph(M(caption), ST['cap'])])
    t = Table([cells], colWidths=[cw] * n)
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 3), ('RIGHTPADDING', (0, 0), (-1, -1), 3)]))
    return [KeepTogether([SP(3), t])]
