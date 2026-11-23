#!/usr/bin/env python3
"""Assemble Yoga_Notes.html from the unit data + figures. Run: python3 build.py"""
import os, html
import figs
from data_u2 import INTRO_U2, U2, COMPARE_U2
from data_u3 import INTRO_U3, U3, REVISION_U3
from data_u4 import INTRO_U4, U4, REVISION_U4
from data_u5 import INTRO_U5, STEPS_U5, ROUND_U5, ROUND_NOTE, BREATH_NOTE, BENEFITS_U5, BENEFITS_NOTE
from data_u6 import INTRO_U6, GROUPS_U6, U6, REVISION_U6

HERE = os.path.dirname(os.path.abspath(__file__))
def read(n): return open(os.path.join(HERE, n), encoding='utf-8').read()

def ul(items, cls=''):
    return f'<ul class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def ol(items, cls=''):
    return f'<ol class="{cls}">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'

def fig(key, scale=0.9):
    return figs.svg(figs.P[key], scale=scale, name=key)

def card(a, with_start=True):
    breath = a.get('breath')
    if isinstance(breath, list): breath = ' · '.join(breath)
    parts = [f'<div class="asana"><div class="fig-col">{fig(a["key"])}<div class="fno">{a["n"]}</div></div><div class="body">']
    parts.append(f'<div class="ah"><b>{a["name"]}</b><span class="en">{a["en"]}</span>' + (f'<em>{a["cat"]}</em>' if a.get('cat') else '') + '</div>')
    parts.append(f'<p class="mean">{a["meaning"]}</p>')
    if a.get('start'): parts.append(f'<p class="start"><b>Start:</b> {a["start"]}</p>')
    parts.append(f'<ol class="steps2">' + ''.join(f'<li>{s}</li>' for s in a['steps']) + '</ol>')
    meta = []
    if breath: meta.append(f'<span><b>Breathing:</b> {breath}</span>')
    if a.get('dur'): meta.append(f'<span><b>Hold:</b> {a["dur"]}</span>')
    if meta: parts.append('<div class="meta">' + ''.join(meta) + '</div>')
    parts.append('</div><div class="bottom">')
    cols = [('Benefits', a['benefits'], 'ben'), ('Precautions', a['prec'], 'pre')]
    if a.get('mist'): cols.append(('Common mistakes', a['mist'], 'mis'))
    parts.append(f'<div class="grid{len(cols)}">' + ''.join(f'<div class="col {c}"><h5>{t}</h5>{ul(items)}</div>' for t, items, c in cols) + '</div>')
    if a.get('teach'): parts.append(f'<p class="teach"><b>Teaching point:</b> {a["teach"]}</p>')
    parts.append('</div></div>')
    return ''.join(parts)

def table(headers, rows, cls='', widths=None):
    h = '<table class="%s"><tr>' % cls + ''.join(f'<th>{x}</th>' for x in headers) + '</tr>'
    for r in rows: h += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return h + '</table>'

# ------------------------------------------------------------------ Unit II
def unit2():
    I = INTRO_U2
    o = [f'<section class="unit" id="u2"><div class="unit-head"><span>UNIT II</span><h2>{I["title"]}</h2><em>{I["hours"]}</em></div>']
    o.append(f'<p>{I["about"]}</p><div class="short"><b>{I["list"]}</b></div>')
    o.append('<h3>General rules for standing asanas</h3><table class="inline wide">' + ''.join(
        f'<tr><td><b>{k}</b></td><td>{v}</td></tr>' for k, v in I['rules']) + '</table>')
    o.append(f'<p class="small">{I["note"]}</p>')
    for a in U2: o.append(card(a))
    o.append('<h3>11. Comparison of the ten standing asanas</h3>')
    o.append(table(['Asana', 'Main movement', 'Learning focus', 'Common modification'], [(f'<b>{a}</b>', b, c, d) for a, b, c, d in COMPARE_U2]))
    o.append('</section>')
    return ''.join(o)

# ------------------------------------------------------------------ Unit III
def unit3():
    I = INTRO_U3
    o = [f'<section class="unit" id="u3"><div class="unit-head"><span>UNIT III</span><h2>{I["title"]}</h2></div>']
    o.append(f'<p>{I["about"]}</p><div class="remember"><b>General precautions:</b>' + ul(I['precautions'], 'cols2 tight') + '</div>')
    for a in U3: o.append(card(a))
    o.append('<h3>Quick revision</h3>' + table(['No.', 'Asana', 'Category', 'Primary focus'], [(n, f'<b>{a}</b>', c, f) for n, a, c, f in REVISION_U3]))
    o.append('</section>')
    return ''.join(o)

# ------------------------------------------------------------------ Unit IV
def unit4():
    I = INTRO_U4
    o = [f'<section class="unit" id="u4"><div class="unit-head"><span>UNIT IV</span><h2>{I["title"]}</h2></div>']
    o.append(f'<p>{I["about"]}</p>')
    o.append('<table class="inline wide">' + ''.join(f'<tr><td><b>{k}</b></td><td>{v}</td></tr>' for k, v in I['classes']) + '</table>')
    o.append('<div class="remember"><b>General precautions:</b>' + ul(I['precautions'], 'cols2 tight') + '</div>')
    last = None
    for a in U4:
        if a['group'] != last:
            o.append(f'<h3 class="grp">{a["group"]}</h3>'); last = a['group']
        o.append(card(a))
    o.append('<h3>Quick revision</h3>' + table(['No.', 'Asana', 'Classification', 'Main focus'], [(n, f'<b>{a}</b>', c, f) for n, a, c, f in REVISION_U4]))
    o.append('</section>')
    return ''.join(o)

# ------------------------------------------------------------------ Unit V
def unit5():
    I = INTRO_U5
    o = ['<section class="unit" id="u5"><div class="unit-head"><span>UNIT V</span><h2>Surya Namaskar</h2><em>Sun Salutation</em></div>']
    o.append(f'<p>{I["about"]}</p>')
    o.append('<div class="two"><div><b>Objectives</b>' + ul(I['objectives'], 'tight') + '</div><div><b>Preparation before practice</b>' + ol(I['prep'], 'tight') + '</div></div>')
    o.append(f'<p><b>Why it is important:</b> {I["importance"]}</p><div class="remember"><b>Precautions:</b> {I["precautions"]}</div>')
    o.append('<h3>The 12 steps</h3><p class="small">A commonly taught traditional form: 12 positions in a continuous sequence, each matched with an inhale, exhale or brief natural pause.</p>')
    o.append('<div class="sgrid">')
    for s in STEPS_U5:
        o.append(f'<div class="step"><div class="sfig">{fig(s["fig"], 0.62)}</div><div class="sbody">'
                 f'<div class="sh"><span class="sn">{s["n"]}</span><b>{s["name"]}</b><span class="en">{s["en"]}</span></div>'
                 f'<div class="sbr">{s["breath"]}</div><p>{s["how"]}</p><p class="sb"><b>Benefits:</b> {s["ben"]}</p>' +
                 (f'<p class="sn2">{s["note"]}</p>' if s['note'] else '') + '</div></div>')
    o.append('</div>')
    o.append('<h3>How to complete a full round</h3><p>In the 12-step sequence above, Step 4 takes the right leg back and Step 9 brings that same leg forward. To balance both sides:</p>' + ol(ROUND_U5, 'tight') + f'<p class="small">{ROUND_NOTE}</p>')
    o.append('<h3>Breathing pattern</h3>' + table(['Step', 'Asana', 'Breathing'], [(s['n'], f'<b>{s["name"]}</b>', s['breath']) for s in STEPS_U5], 'inline wide'))
    o.append(f'<p class="small">{BREATH_NOTE}</p>')
    o.append('<h3>Benefits of Surya Namaskar</h3>' + ul(BENEFITS_U5, 'cols2 tight') + f'<div class="remember">{BENEFITS_NOTE}</div>')
    o.append('</section>')
    return ''.join(o)

# ------------------------------------------------------------------ Unit VI
def unit6():
    I = INTRO_U6
    o = ['<section class="unit" id="u6"><div class="unit-head"><span>UNIT VI</span><h2>Pranayama &amp; Breathing Practices</h2></div>']
    o.append(f'<p>{I["about"]}</p><div class="remember"><b>Before practising pranayama</b>' + ol(I['guidelines'], 'cols2 tight') + '</div>')
    for gname, keys in GROUPS_U6:
        o.append(f'<h3 class="grp">{gname}</h3>')
        for k in keys:
            a = U6[k]
            o.append(f'<div class="prana"><div class="ph"><span class="pn">{a["n"]}</span><b>{a["name"]}</b></div>')
            o.append(f'<p class="mean">{a["meaning"]}</p>')
            o.append('<div class="pcols"><div><h5>Technique</h5>' + ol(a['steps'], 'steps2') + '</div><div>')
            o.append(f'<h5>Breathing pattern</h5><p>{a["pattern"]}</p>')
            o.append('<h5>Benefits</h5>' + ul(a['benefits']) + '<h5>Precautions</h5>' + ul(a['prec']))
            if a.get('exam'): o.append('<h5>Practical exam points</h5>' + ul(a['exam']))
            o.append('</div></div>')
            if a.get('diff'):
                o.append('<table class="inline wide">' + ''.join(f'<tr><td><b>{x}</b></td><td>{y}</td></tr>' for x, y in a['diff']) + '</table>')
            o.append('</div>')
    o.append('<h3>Quick revision — practical exam</h3>' + table(['Practice', 'Inhalation', 'Exhalation', 'Main feature'], [(f'<b>{a}</b>', b, c, d) for a, b, c, d in REVISION_U6]))
    o.append('</section>')
    return ''.join(o)

# ------------------------------------------------------------------ cover
UNITS = [
 ('I', 'Foundation of Yoga', 'meaning, history, 8 limbs, benefits, principles, precautions, practical basics, Q&amp;A'),
 ('II', 'Standing &amp; Balancing Asanas', '10 asanas with diagrams'),
 ('III', 'Sitting, Forward-Bending &amp; Twisting Asanas', '11 asanas with diagrams'),
 ('IV', 'Prone, Supine &amp; Relaxation Asanas', '12 asanas with diagrams'),
 ('V', 'Surya Namaskar', '12 steps with diagrams'),
 ('VI', 'Pranayama &amp; Breathing Practices', '13 practices'),
 ('VII', 'Relaxation, Concentration &amp; Meditation', '10 topics'),
 ('VIII', 'Basic Yoga Philosophy &amp; Lifestyle', '13 topics + activity'),
]
def cover():
    rows = ''.join(f'<div class="crow"><span class="cu">Unit {u}</span><b>{t}</b><i>{d}</i></div>' for u, t, d in UNITS)
    return (f'<section class="cover"><h1>Yoga — Study Notes</h1><div class="sub">Sem-1 · Units I–VIII · short, simple, complete</div>'
            f'<div class="contents">{rows}</div>'
            '<div class="legend"><b>How to use these notes</b>'
            '<ul class="tight"><li>Each <b>asana card</b> has: meaning · starting position · steps · breathing · hold time · benefits · precautions · common mistakes · teaching point.</li>'
            '<li><span class="k blue"></span>Blue bar = the idea in one line &nbsp; <span class="k yel"></span>Yellow = remember / precautions &nbsp; <span class="k grey"></span>Grey box = step-by-step procedure.</li>'
            '<li>Diagrams are <b>simplified line drawings</b> for quick revision (shown from the side or front, or from above for lying poses; the lighter limb is the far side). Always follow your instructor\'s demonstration for exact form.</li>'
            '<li>Hold times and repetitions are for <b>beginners</b>. Never force a posture — stop for sharp pain, dizziness, numbness or unusual discomfort.</li></ul></div></section>')

CSS = """
@page { size: A4; margin: 12mm 13mm 14mm 13mm; }
:root { --blue:#1f5fd6; --ink:#1d2330; --mute:#5b6475; --rule:#d9dee7; --grey:#f1f3f7; --yellow:#fff7d6; --lblue:#e8f1ff; --green:#e6f5ea; --red:#fdeceb; }
* { box-sizing:border-box; }
body { font-family:"Noto Sans", Inter, sans-serif; color:var(--ink); font-size:9pt; line-height:1.34; margin:0; background:#fff; }
h1 { font-size:26pt; margin:0 0 4px; line-height:1.15; }
.sub { color:var(--mute); font-size:10pt; margin-bottom:16px; }
p { margin:4px 0; } ul, ol { margin:3px 0 4px; padding-left:17px; } li { margin:1px 0; }
h2 { font-size:15pt; margin:0; }
h3 { font-size:10.8pt; margin:11px 0 5px; padding-bottom:3px; border-bottom:1.2px solid var(--ink); break-after:avoid; }
h3.grp { border:none; background:var(--ink); color:#fff; padding:4px 9px; border-radius:3px; font-size:9.6pt; margin:12px 0 6px; }
h5 { font-size:8.2pt; letter-spacing:.05em; text-transform:uppercase; color:var(--mute); margin:5px 0 2px; }
.unit { break-before:page; }
.unit-head { display:flex; align-items:baseline; gap:10px; border-bottom:2.4px solid var(--blue); padding-bottom:5px; margin-bottom:8px; }
.unit-head span { background:var(--blue); color:#fff; font-weight:700; font-size:8.5pt; padding:2px 8px; border-radius:3px; letter-spacing:.06em; }
.unit-head em { margin-left:auto; color:var(--mute); font-size:8.5pt; }
.short { border-left:3px solid var(--blue); padding:3px 0 3px 10px; margin:6px 0; background:var(--lblue); border-radius:0 3px 3px 0; }
.remember { background:var(--yellow); border-left:3px solid #e0a800; padding:5px 10px; margin:7px 0; border-radius:3px; }
.small { font-size:8.2pt; color:var(--mute); }
.steps-box { background:var(--grey); border-radius:4px; padding:6px 10px; margin:6px 0; }
.steps-box ol { margin:3px 0 0; }
.two { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:4px 0; }
.cols2 { columns:2; column-gap:18px; } .tight li { margin:0.5px 0; }
ol.steps-n { columns:2; column-gap:18px; } ol.steps-n li { break-inside:avoid; }
table { border-collapse:collapse; width:100%; margin:5px 0 7px; font-size:8.5pt; break-inside:auto; }
tr { break-inside:avoid; }
th, td { border-bottom:1px solid var(--rule); padding:3px 6px; text-align:left; vertical-align:top; }
th { background:var(--grey); font-weight:600; }
table.inline th { background:var(--grey); } table.wide td:first-child { white-space:normal; }
table.t8 td, table.t8 th { text-align:center; font-size:7.6pt; padding:3px 3px; }
table.qa td:first-child { width:32%; }
.partb { background:var(--ink); color:#fff; font-weight:700; letter-spacing:.05em; padding:6px 10px; border-radius:3px; margin:12px 0 4px; }
.partb small { display:block; font-weight:400; letter-spacing:0; opacity:.85; }
/* cover */
.cover { padding-top:6mm; }
.contents { margin:6px 0 14px; } .crow { display:grid; grid-template-columns:62px 1fr; gap:2px 10px; padding:6px 0; border-bottom:1px solid var(--rule); }
.crow b { font-size:10.5pt; } .crow i { grid-column:2; color:var(--mute); font-size:8.6pt; font-style:normal; } .cu { color:var(--blue); font-weight:700; font-size:9pt; }
.legend { background:var(--grey); border-radius:5px; padding:9px 14px; font-size:9pt; }
.k { display:inline-block; width:12px; height:9px; border-radius:2px; margin-right:4px; vertical-align:middle; } .k.blue{background:var(--blue)} .k.yel{background:#e0a800} .k.grey{background:#b9c1cf}
/* asana card */
.bottom { grid-column:1 / -1; }
.asana { display:grid; grid-template-columns:40mm 1fr; gap:1.5mm 3mm; border:1px solid var(--rule); border-radius:5px; padding:4px 7px 5px; margin:5px 0; break-inside:avoid; }
.fig-col { position:relative; display:flex; align-items:center; justify-content:center; background:#f7f9fc; border-radius:4px; min-height:24mm; }
.fig-col svg { max-width:100%; height:auto; }
.fno { position:absolute; left:4px; top:3px; background:var(--blue); color:#fff; font-weight:700; font-size:8pt; width:18px; height:18px; border-radius:50%; text-align:center; line-height:18px; }
.ah { display:flex; align-items:baseline; flex-wrap:wrap; gap:3px 8px; border-bottom:1px solid var(--rule); padding-bottom:2px; }
.ah b { font-size:11.2pt; } .ah .en { color:var(--blue); font-weight:600; font-size:9pt; } .ah em { margin-left:auto; font-size:7.6pt; color:var(--mute); font-style:normal; background:var(--grey); padding:1px 6px; border-radius:8px; }
.mean { color:#2b3342; font-size:8.2pt; } .start { font-size:8.2pt; }
ol.steps2 { counter-reset:s; list-style:none; padding-left:0; margin:3px 0; columns:2; column-gap:14px; }
ol.steps2 li { counter-increment:s; position:relative; padding-left:15px; margin:1px 0; break-inside:avoid; font-size:8.1pt; line-height:1.28; }
ol.steps2 li::before { content:counter(s); position:absolute; left:0; top:1px; width:12px; height:12px; border-radius:50%; background:var(--blue); color:#fff; font-size:6.6pt; font-weight:700; text-align:center; line-height:12px; }
.meta { display:flex; flex-wrap:wrap; gap:2px 14px; background:var(--lblue); padding:2px 8px; border-radius:3px; font-size:8pt; margin:2px 0; line-height:1.3; }
.grid3, .grid2 { display:grid; gap:3px 9px; margin:3px 0; } .grid3 { grid-template-columns:1fr 1fr 1fr; } .grid2 { grid-template-columns:1fr 1fr; }
.col { border-radius:3px; padding:2px 6px 3px; } .col.ben { background:var(--green); } .col.pre { background:var(--yellow); } .col.mis { background:var(--red); }
.col ul { padding-left:13px; margin:1px 0; } .col li { font-size:7.8pt; margin:0; line-height:1.26; } .col h5 { margin:1px 0 1px; }
.teach { background:var(--grey); border-left:3px solid var(--ink); padding:1px 8px; margin:2px 0 0; font-size:8pt; line-height:1.3; border-radius:0 3px 3px 0; }
/* surya */
.sgrid { display:grid; grid-template-columns:1fr 1fr; gap:6px 9px; }
.step { display:grid; grid-template-columns:30mm 1fr; gap:2mm; border:1px solid var(--rule); border-radius:5px; padding:5px 6px; break-inside:avoid; }
.sfig { background:#f7f9fc; border-radius:4px; display:flex; align-items:center; justify-content:center; } .sfig svg { max-width:100%; height:auto; }
.sh { display:flex; flex-wrap:wrap; align-items:baseline; gap:1px 6px; } .sn { background:var(--blue); color:#fff; font-weight:700; font-size:7.8pt; min-width:17px; height:17px; border-radius:50%; text-align:center; line-height:17px; }
.sh b { font-size:9.3pt; } .sh .en { color:var(--blue); font-size:8pt; font-weight:600; } .sbr { display:inline-block; background:var(--lblue); font-size:7.6pt; padding:0 6px; border-radius:8px; margin:2px 0; }
.sbody p { font-size:8pt; margin:2px 0; line-height:1.34; } .sb { color:#2b3342; } .sn2 { color:var(--mute); font-style:italic; }
/* pranayama */
.prana { border:1px solid var(--rule); border-radius:5px; padding:5px 9px 6px; margin:6px 0; break-inside:avoid; }
.ph { display:flex; align-items:center; gap:8px; border-bottom:1px solid var(--rule); padding-bottom:2px; } .ph b { font-size:10.5pt; } .pn { background:var(--blue); color:#fff; font-weight:700; font-size:8pt; width:19px; height:19px; border-radius:50%; text-align:center; line-height:19px; }
.pcols { display:grid; grid-template-columns:1.05fr 1fr; gap:4px 14px; } .pcols ul, .pcols ol { margin:1px 0 3px; } .pcols li { font-size:8.3pt; } .pcols p { font-size:8.3pt; }
.fig { display:block; }
"""

def head():
    return ('<!doctype html><html><head><meta charset="utf-8"><title>Yoga — Study Notes</title><style>' + CSS + '</style></head><body>')

def main():
    out = [head(), cover(), read('unit1.html'), unit2(), unit3(), unit4(), unit5(), unit6(), read('unit7.html'), read('unit8.html'), '</body></html>']
    path = os.path.join(HERE, 'yoga.html')
    open(path, 'w', encoding='utf-8').write(''.join(out))
    print('wrote', path, os.path.getsize(path)//1024, 'KB')

if __name__ == '__main__':
    main()
