"""Stick-figure generator for yoga postures -> inline SVG strings.
Planar articulated figure: y up, figure faces +x in side views. Limbs positioned by
2-bone IK (ankle / wrist targets) or forward kinematics (absolute angles)."""
import math

LT, LN, RH = 0.55, 0.075, 0.085          # torso, neck, head radius
UA, FA = 0.30, 0.27                      # upper arm, forearm
TH, SH, FT = 0.40, 0.40, 0.13            # thigh, shin, foot
DARK, LIGHT, ACC = "#1d2330", "#97a3b8", "#1f5fd6"

def pol(p, ang, L):
    a = math.radians(ang)
    return (p[0] + L*math.cos(a), p[1] + L*math.sin(a))

def ik(P, T, l1, l2, bend):
    dx, dy = T[0]-P[0], T[1]-P[1]
    d = math.hypot(dx, dy)
    base = math.atan2(dy, dx)
    d = max(abs(l1-l2)+1e-3, min(d, l1+l2-1e-4))
    c = (l1*l1 + d*d - l2*l2)/(2*l1*d)
    c = max(-1, min(1, c))
    a = base + bend*math.acos(c)
    j = (P[0]+l1*math.cos(a), P[1]+l1*math.sin(a))
    # end point clamped along the base direction
    e = (P[0]+d*math.cos(base), P[1]+d*math.sin(base))
    return j, e

def limb(P, spec, l1, l2):
    kind = spec[0]
    if kind == 'ik':
        _, T, bend = spec
        j, e = ik(P, T, l1, l2, bend)
        return j, e
    if kind == 'fk':
        _, a1, a2 = spec
        j = pol(P, a1, l1)
        return j, pol(j, a2, l2)
    if kind == 'pts':
        _, j, e = spec
        return j, e
    raise ValueError(kind)

def build(p):
    H = p['H']; wh = p.get('wh', 0.0); ws = p.get('ws', 0.0)
    if 'S' in p: S = p['S']
    else: S = pol(H, p['tor'], LT)
    ta = math.degrees(math.atan2(S[1]-H[1], S[0]-H[0]))
    hd = p.get('hd', ta)
    N = pol(S, hd, LN)
    HC = pol(N, hd, RH)
    pr = (math.cos(math.radians(ta-90)), math.sin(math.radians(ta-90)))   # "right" of torso
    hips = [(H[0]-wh, H[1]), (H[0]+wh, H[1])]
    shs = [(S[0]-pr[0]*ws, S[1]-pr[1]*ws), (S[0]+pr[0]*ws, S[1]+pr[1]*ws)]
    legs = []
    for i in (0, 1):
        k, a = limb(hips[i], p['legs'][i], TH, SH)
        fa = p.get('ft', [0, 0])[i]
        legs.append((hips[i], k, a, pol(a, fa, FT)))
    arms = []
    for i in (0, 1):
        e, w = limb(shs[i], p['arms'][i], UA, FA)
        arms.append((shs[i], e, w))
    return dict(H=H, S=S, N=N, HC=HC, hips=hips, shs=shs, legs=legs, arms=arms, wh=wh, ws=ws, p=p)

def svg(p, scale=0.55, pad=0.18, name=''):
    g = build(p)
    pts = [g['H'], g['S'], g['HC']]
    for hp, k, a, f in g['legs']: pts += [hp, k, a, f]
    for sp, e, w in g['arms']: pts += [sp, e, w]
    for extra in p.get('pts', []): pts.append(extra)
    xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
    x0, x1 = min(xs)-pad-RH, max(xs)+pad+RH
    y0 = min(min(ys)-pad*0.3, -0.06) if p.get('mat') != 'top' else min(ys)-pad
    y1 = max(ys)+pad+RH
    if p.get('mat') == 'top':
        x0 = min(x0, -0.75); x1 = max(x1, 0.75)
    W, Hh = (x1-x0), (y1-y0)
    X = lambda x: round((x-x0)*100, 1)
    Y = lambda y: round((y1-y)*100, 1)
    o = []
    # mat / floor
    if p.get('mat') == 'top':
        o.append(f'<rect x="{X(x0+0.08)}" y="{Y(y1-0.05)}" width="{round((W-0.16)*100,1)}" height="{round((Hh-0.1)*100,1)}" rx="10" fill="#eef1f6" stroke="#d3d9e4"/>')
    else:
        o.append(f'<rect x="{X(x0+0.04)}" y="{Y(0)}" width="{round((W-0.08)*100,1)}" height="3.4" rx="1.7" fill="#c9d1de"/>')
    # props
    for pr in p.get('props', []):
        if pr[0] == 'block':
            _, bx, bw, bh = pr
            o.append(f'<rect x="{X(bx)}" y="{Y(bh)}" width="{bw*100}" height="{bh*100}" rx="2" fill="#f3d9a4" stroke="#caa55c"/>')
        if pr[0] == 'wall':
            o.append(f'<rect x="{X(pr[1])}" y="{Y(y1)}" width="4" height="{round(Hh*100,1)}" fill="#c9d1de"/>')
    far = set(p.get('far', []))      # entries like 'L0','A1'
    def col(tag): return LIGHT if tag in far else DARK
    def line(a, b, c, w=7.5):
        o.append(f'<path d="M{X(a[0])} {Y(a[1])} L{X(b[0])} {Y(b[1])}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" fill="none"/>')
    def poly(pts_, c, w=7.5):
        d = 'M' + ' L'.join(f'{X(q[0])} {Y(q[1])}' for q in pts_)
        o.append(f'<path d="{d}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>')
    order = p.get('order', ['L0', 'A0', 'T', 'L1', 'A1'])
    for item in order:
        if item[0] == 'L':
            i = int(item[1]); hp, k, a, f = g['legs'][i]; poly([hp, k, a, f], col(item))
        elif item[0] == 'A':
            i = int(item[1]); sp, e, w = g['arms'][i]; poly([sp, e, w], col(item), 6.5)
        elif item == 'T':
            line(g['H'], g['S'], DARK, 10)
            if g['wh']: line(g['hips'][0], g['hips'][1], DARK, 7)
            if g['ws']: line(g['shs'][0], g['shs'][1], DARK, 7)
            line(g['S'], g['N'], DARK, 6)
    # head
    o.append(f'<circle cx="{X(g["HC"][0])}" cy="{Y(g["HC"][1])}" r="{RH*100}" fill="#fff" stroke="{DARK}" stroke-width="5"/>')
    for d in p.get('decor', []):
        if d[0] == 'hand_under':
            cx, cy = d[1]
            o.append(f'<ellipse cx="{X(cx)}" cy="{Y(cy)}" rx="9" ry="3.5" fill="{ACC}" opacity=".35"/>')
        if d[0] == 'twist':
            cx, cy = d[1]
            o.append(f'<path d="M{X(cx-0.17)} {Y(cy)} A 17 8 0 1 1 {X(cx+0.17)} {Y(cy)}" fill="none" stroke="{ACC}" stroke-width="2.4" stroke-dasharray="4 3"/>'
                     f'<path d="M{X(cx+0.17)-5} {Y(cy)-6} L{X(cx+0.17)} {Y(cy)} L{X(cx+0.17)+6} {Y(cy)-6}" fill="none" stroke="{ACC}" stroke-width="2.4"/>')
    w_px = round(W*100*scale, 1); h_px = round(Hh*100*scale, 1)
    return (f'<svg class="fig" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {round(W*100,1)} {round(Hh*100,1)}" '
            f'width="{w_px}" height="{h_px}" role="img" aria-label="{name}">{"".join(o)}</svg>')

# --------------------------------------------------------------------------------------------
# POSES  (angles: 0=right, 90=up; legs: ('ik', ankle, bend) / ('fk', thigh, shin) / ('pts', knee, ankle))
# --------------------------------------------------------------------------------------------
def standing_front(**kw):
    d = dict(H=(0, .80), tor=90, wh=.05, ws=.13, ft=[180, 0])
    d.update(kw); return d

P = {}
P['tadasana'] = standing_front(legs=[('ik', (-.06, 0), 1), ('ik', (.06, 0), 1)],
                               arms=[('ik', (-.20, .80), -1), ('ik', (.20, .80), 1)])
P['vrikshasana'] = standing_front(legs=[('ik', (-.05, 0), 1), ('ik', (-.02, .62), 1)],
                               arms=[('ik', (-.02, 1.22), -1), ('ik', (.02, 1.22), 1)], ft=[180, 270])
P['utkatasana'] = dict(H=(-.24, .56), tor=70, legs=[('ik', (.06, 0), 1), ('ik', (.09, 0), 1)], ft=[0, 0],
                       arms=[('fk', 82, 82), ('fk', 78, 78)], far=['L0', 'A0'], hd=82)
P['trikonasana'] = dict(H=(0, .70), tor=20, wh=.05, ws=0, ft=[180, 0], hd=62,
                        legs=[('ik', (-.45, 0), 1), ('ik', (.45, 0), 1)],
                        arms=[('ik', (.517, 1.46), -1), ('ik', (.25, .40), -1)], order=['L0', 'L1', 'A0', 'T', 'A1'])
P['konasana'] = dict(H=(0, .80), tor=105, wh=.05, ws=0, ft=[180, 0], hd=100,
                     legs=[('ik', (-.12, 0), 1), ('ik', (.12, 0), 1)],
                     arms=[('ik', (-.18, .80), -1), ('ik', (-.46, 1.74), -1)])
P['parshvakonasana'] = dict(H=(0, .62), tor=28, wh=.05, ws=0, ft=[180, 0], hd=45,
                            legs=[('ik', (-.555, 0), 1), ('ik', (.42, 0), 1)],
                            arms=[('ik', (.98, 1.14), 1), ('ik', (.28, .46), 1)], order=['L0', 'A0', 'T', 'L1', 'A1'])
P['ardha_chandrasana'] = dict(H=(0, .80), tor=345, wh=.05, ws=0, ft=[180, 0], hd=330,
                              legs=[('ik', (-.85, .86), 1), ('ik', (.05, 0), 1)],
                              arms=[('ik', (.53, 1.24), 1), ('ik', (.53, .08), 1)], order=['L0', 'A0', 'T', 'L1', 'A1'])
P['hastapadasana'] = dict(H=(-.35, .72), tor=335, hd=305, legs=[('ik', (-.02, 0), 1), ('ik', (.0, 0), 1)], ft=[0, 0],
                          arms=[('ik', (.02, .05), -1), ('ik', (.06, .03), -1)], far=['L0', 'A0'])
P['padahastasana'] = dict(H=(-.30, .70), tor=322, hd=292, legs=[('ik', (-.02, 0), 1), ('ik', (.0, 0), 1)], ft=[0, 0],
                          arms=[('ik', (.0, .03), -1), ('ik', (.06, .02), -1)], far=['L0', 'A0'],
                          decor=[('hand_under', (.04, .02))])
P['garudasana'] = standing_front(H=(0, .70), ft=[180, 270],
                          legs=[('ik', (-.03, 0), -1), ('ik', (-.10, .20), -1)],
                          arms=[('ik', (0, 1.62), -1), ('ik', (0, 1.62), 1)])

def sit_front(legs, arms, tor=90, **kw):
    d = dict(H=(0, .07), tor=tor, wh=.06, ws=.13, legs=legs, arms=arms, ft=[180, 0])
    d.update(kw); return d
P['sukhasana'] = sit_front(legs=[('pts', (-.38, .12), (.12, .04)), ('pts', (.38, .12), (-.12, .04))],
                           arms=[('ik', (-.40, .16), -1), ('ik', (.40, .16), 1)], order=['L0', 'L1', 'A0', 'T', 'A1'], ft=[0, 0])
P['vajrasana'] = dict(H=(-.12, .20), tor=90, legs=[('pts', (.26, .05), (-.14, .04)), ('pts', (.26, .05), (-.14, .04))],
                      ft=[180, 180], arms=[('ik', (.06, .21), -1), ('ik', (.10, .20), -1)], far=['A0'])
P['padmasana'] = sit_front(legs=[('pts', (-.40, .07), (.16, .15)), ('pts', (.40, .07), (-.16, .15))],
                           arms=[('ik', (-.40, .13), -1), ('ik', (.40, .13), 1)], ft=[90, 90], order=['L0', 'L1', 'A0', 'T', 'A1'])
P['ardha_padmasana'] = sit_front(legs=[('pts', (-.38, .09), (.14, .15)), ('pts', (.40, .08), (-.12, .03))],
                           arms=[('ik', (-.38, .15), -1), ('ik', (.40, .14), 1)], ft=[90, 0], order=['L0', 'L1', 'A0', 'T', 'A1'])
P['baddha_konasana'] = sit_front(legs=[('pts', (-.40, .11), (-.04, .04)), ('pts', (.40, .11), (.04, .04))],
                           arms=[('ik', (-.12, .06), -1), ('ik', (.12, .06), 1)], ft=[0, 0], order=['L0', 'L1', 'A0', 'T', 'A1'])
P['gomukhasana'] = sit_front(legs=[('pts', (-.03, .24), (.30, .04)), ('pts', (.03, .15), (-.30, .04))],
                           arms=[('ik', (.02, 1.03), 1), ('ik', (-.02, .95), 1)], ft=[0, 180], order=['L0', 'L1', 'A0', 'T', 'A1'])
# gomukhasana arms: one elbow up, one down - set explicitly below
P['gomukhasana']['arms'] = [('pts', (-.30, 1.55), (-.02, 1.12)), ('pts', (.28, .48), (.02, .95))]
P['paschimottanasana'] = dict(H=(0, .07), tor=28, hd=15, legs=[('ik', (.80, .06), 1), ('ik', (.80, .03), 1)], ft=[90, 90],
                              arms=[('ik', (.76, .14), 1), ('ik', (.78, .12), 1)], far=['L0', 'A0'])
P['janu_shirshasana'] = dict(H=(0, .07), tor=30, hd=18, legs=[('fk', 35, 205), ('ik', (.80, .05), 1)], ft=[270, 90],
                             arms=[('ik', (.74, .14), 1), ('ik', (.76, .12), 1)], far=['L0', 'A0'])
P['yog_mudra'] = dict(H=(0, .07), tor=12, hd=-5, legs=[('fk', 4, 188), ('fk', 9, 192)], ft=[180, 180],
                      arms=[('fk', 125, 150), ('fk', 128, 155)], far=['L0', 'A0'])
P['vakrasana'] = dict(H=(0, .07), tor=90, legs=[('ik', (.80, .06), 1), ('ik', (.46, .03), 1)], ft=[90, 0],
                      arms=[('ik', (-.20, .05), -1), ('ik', (.30, .42), 1)], far=['L0', 'A0'],
                      decor=[('twist', (0, .45))])
P['ardha_matsyendrasana'] = dict(H=(0, .07), tor=90, legs=[('fk', 20, 185), ('ik', (.34, .03), 1)], ft=[180, 0],
                      arms=[('ik', (-.22, .05), -1), ('ik', (.24, .50), 1)], far=['L0', 'A0'],
                      decor=[('twist', (0, .45))])

def lie(**kw):
    d = dict(H=(0, .08), tor=180, ft=[90, 90]); d.update(kw); return d
P['bhujangasana'] = dict(H=(0, .09), tor=145, hd=170, legs=[('ik', (.80, .07), 1), ('ik', (.80, .05), 1)], ft=[270, 270],
                         arms=[('ik', (-.37, .03), 1), ('ik', (-.43, .03), 1)], far=['L0', 'A0'])
P['shalabhasana'] = lie(legs=[('fk', 17, 17), ('fk', 13, 13)], ft=[17, 13], hd=170,
                        arms=[('ik', (.02, .12), 1), ('ik', (.0, .10), 1)], far=['L0', 'A0'])
P['dhanurasana'] = dict(H=(0, .10), tor=140, hd=160, legs=[('fk', 20, 126), ('fk', 16, 122)], ft=[200, 200],
                        arms=[('ik', (.14, .56), 1), ('ik', (.12, .54), 1)], far=['L0', 'A0'])
P['makarasana'] = dict(H=(0, .0), S=(0, .55), hd=90, mat='top', wh=.07, ws=.13,
                       legs=[('ik', (-.17, -.80), 1), ('ik', (.17, -.80), 1)], ft=[270, 270],
                       arms=[('pts', (-.30, .60), (-.04, .62)), ('pts', (.30, .60), (.04, .62))], order=['L0', 'L1', 'A0', 'T', 'A1'])
P['uttan_padasana'] = lie(hd=170, legs=[('fk', 30, 30), ('fk', 28, 28)], ft=[120, 120],
                          arms=[('ik', (.02, .12), 1), ('ik', (0, .10), 1)], far=['L0', 'A0'])
P['pawanmuktasana'] = lie(hd=170, legs=[('fk', 120, 330), ('ik', (.80, .07), 1)], ft=[90, 90],
                          arms=[('ik', (-.02, .34), 1), ('ik', (-.04, .30), 1)], far=['L1', 'A1'])
P['setu_bandhasana'] = dict(H=(0, .40), S=(-.47, .12), hd=195, legs=[('ik', (.52, 0), 1), ('ik', (.55, 0), 1)], ft=[0, 0],
                            arms=[('ik', (.15, .05), 1), ('ik', (.12, .04), 1)], far=['L0', 'A0'])
P['naukasana'] = lie(tor=145, hd=150, legs=[('fk', 35, 35), ('fk', 32, 32)], ft=[100, 100],
                     arms=[('fk', 12, 12), ('fk', 8, 8)], far=['L0', 'A0'])
P['supta_matsyendrasana'] = dict(H=(0, 0), S=(0, .55), hd=90, mat='top', wh=.07, ws=.13,
                       legs=[('pts', (.36, .06), (.07, -.15)), ('pts', (.36, .06), (.07, -.15)) ], ft=[270, 270],
                       arms=[('ik', (-.70, .55), -1), ('ik', (.70, .55), 1)])
P['shavasana'] = dict(H=(0, 0), S=(0, .55), hd=90, mat='top', wh=.07, ws=.13,
                      legs=[('ik', (-.17, -.80), 1), ('ik', (.17, -.80), 1)], ft=[270, 270],
                      arms=[('ik', (-.32, .0), -1), ('ik', (.32, .0), 1)])
P['halasana'] = dict(H=(.114, .627), S=(0, .09), hd=185, legs=[('ik', (-.52, .13), 1), ('ik', (-.55, .09), 1)], ft=[270, 270],
                     arms=[('ik', (.50, .06), 1), ('ik', (.52, .04), 1)], far=['L0', 'A0'])
P['sarvangasana'] = dict(H=(.10, .64), S=(0, .09), hd=185, legs=[('fk', 88, 88), ('fk', 86, 86)], ft=[180, 180],
                         arms=[('ik', (.08, .40), 1), ('ik', (.06, .42), 1)], far=['L0', 'A0'])

# Surya Namaskar (side view, facing right)
P['s_pranamasana'] = dict(H=(0, .80), tor=90, legs=[('ik', (.0, 0), 1), ('ik', (.03, 0), 1)], ft=[0, 0],
                          arms=[('ik', (.13, 1.22), -1), ('ik', (.15, 1.22), -1)], far=['L0', 'A0'])
P['s_hasta_uttanasana'] = dict(H=(0, .80), tor=96, hd=110, legs=[('ik', (.0, 0), 1), ('ik', (.03, 0), 1)], ft=[0, 0],
                          arms=[('fk', 108, 108), ('fk', 105, 105)], far=['L0', 'A0'])
P['s_padahastasana'] = dict(H=(-.35, .72), tor=335, hd=305, legs=[('ik', (-.02, 0), 1), ('ik', (.0, 0), 1)], ft=[0, 0],
                          arms=[('ik', (.02, .03), -1), ('ik', (.06, .02), -1)], far=['L0', 'A0'])
_ash = dict(H=(-.05, .30), tor=42, hd=60, ft=[0, 0], arms=[('ik', (.45, .03), 1), ('ik', (.48, .03), 1)])
P['s_ashwa_right'] = dict(_ash, legs=[('ik', (.46, 0), 1), ('ik', (-.75, .05), 1)], far=['L0', 'A0'])
P['s_ashwa_left'] = dict(_ash, legs=[('ik', (-.75, .05), 1), ('ik', (.46, 0), 1)], far=['L1', 'A0'])
P['s_dandasana'] = dict(H=(-.504, .376), S=(0, .60), hd=40, legs=[('ik', (-1.24, .06), 1), ('ik', (-1.25, .05), 1)], ft=[90, 90],
                        arms=[('ik', (.0, .03), 1), ('ik', (.02, .03), 1)], far=['L0', 'A0'])
P['s_ashtanga_namaskara'] = dict(H=(-.40, .38), S=(.12, .20), hd=330,
                        legs=[('pts', (-.62, .04), (-1.0, .06)), ('pts', (-.60, .05), (-1.0, .07))], ft=[90, 90],
                        arms=[('ik', (.20, .03), -1), ('ik', (.24, .03), -1)], far=['L0', 'A0'])
P['s_bhujangasana'] = dict(H=(-.50, .10), tor=40, hd=45, legs=[('ik', (-1.30, .08), 1), ('ik', (-1.30, .06), 1)], ft=[270, 270],
                        arms=[('ik', (-.05, .03), -1), ('ik', (-.01, .03), -1)], far=['L0', 'A0'])
P['s_parvatasana'] = dict(H=(-.15, .74), S=(.30, .40), hd=250, legs=[('ik', (-.55, .04), 1), ('ik', (-.58, .02), 1)], ft=[0, 0],
                        arms=[('ik', (.65, .03), -1), ('ik', (.68, .03), -1)], far=['L0', 'A0'])

if __name__ == '__main__':
    import sys
    keys = list(P.keys())
    html = ['<!doctype html><meta charset=utf-8><style>body{font-family:sans-serif;margin:8px}.c{display:inline-block;width:250px;margin:4px;border:1px solid #ddd;text-align:center;vertical-align:top}.c small{display:block;color:#555}</style>']
    for k in keys:
        try:
            html.append(f'<div class=c>{svg(P[k], name=k)}<small>{k}</small></div>')
        except Exception as ex:
            html.append(f'<div class=c><small>{k}: ERROR {ex}</small></div>')
    open(sys.argv[1], 'w').write(''.join(html))
    print(len(keys), 'poses')
