#!/usr/bin/env python3
"""The Window Seat (/aviation/): rebuild every page from aviation/flights.json.

    python3 _tools/aviation.py add  flight.json   # add one flight (see README), then rebuild
    python3 _tools/aviation.py build              # rebuild all six pages from flights.json
    python3 _tools/aviation.py check              # rebuild in memory, report any page that would change

Only the parts of each page that come from the data are rewritten; the layout, styles, scripts and
map artwork stay as they are. New routes need a map arc, which this script does not draw: it stops
and says so rather than guessing.
"""
import json, re, sys, os, datetime as dt
from collections import Counter, OrderedDict
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AV = os.path.join(ROOT, 'aviation')
PAGES = {k: os.path.join(AV, v) for k, v in {
    'dash': 'index.html', 'log': 'flight-log/index.html', 'map': 'map/index.html',
    'aircraft': 'aircraft/index.html', 'stats': 'statistics/index.html', 'passport': 'passport/index.html'}.items()}
EQUATOR = 24901
INKS = ['#1d428a', '#b3263a', '#1f6b45', '#6a2a8a', '#8a5a12']
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def d(iso):
    return dt.date.fromisoformat(iso)


def dshort(iso):  # 7 Nov
    x = d(iso); return f'{x.day} {MON[x.month - 1]}'


def dlong(iso):  # 7 Nov 2026
    x = d(iso); return f'{x.day} {MON[x.month - 1]} {x.year}'


def n(x):
    return f'{x:,}'


def hm(mins):
    return f'{mins // 60}h {mins % 60:02d}m'


def sgn(x):
    return f'+{x} min' if x > 0 else f'{x} min'


def avg(xs):
    return round(sum(xs) / len(xs)) if xs else 0


def pct(a, b):
    return round(100 * a / b) if b else 0


def ontime(f):
    return f['arr_delay'] is not None and f['arr_delay'] <= 15


def first_order(items):
    """Unique values in order of first appearance."""
    seen = OrderedDict()
    for i in items: seen.setdefault(i, None)
    return list(seen)


def ranked(counter, order):
    """Most first; ties keep order of first appearance."""
    return sorted(order, key=lambda k: (-counter[k], order.index(k)))


def bars(rows):
    top = max((v for _, v in rows), default=0) or 1
    out = []
    for label, v in rows:
        w = 100 * v / top
        style = f'width:{w:.1f}%' + (';min-width:0' if v == 0 else '')
        out.append(f'<li title="{esc(label)}: {v}"><span class="bl">{esc(label)}</span><span class="bt" aria-hidden="true">'
                   f'<span class="bf" style="{style}"></span></span><span class="bv">{v}</span></li>')
    return '<ul class="bars">' + ''.join(out) + '</ul>'


def stat(v, note, label, sm=False):
    return (f'<div class="stat"><div><div class="v{" sm" if sm else ""}">{v}</div><div class="n">{note}</div></div>'
            f'<div class="l">{label}</div></div>')


def sub(page, pattern, new, count=1):
    fn = new if callable(new) else (lambda m: new)
    out, k = re.subn(pattern, fn, page, count=count, flags=re.S)
    if k != count: raise SystemExit(f'Could not find {pattern[:60]!r} on the page; the layout has changed.')
    return out


class Log:
    def __init__(self, data, calz):
        self.data = data
        self.F = data['flights']
        self.A = calz['airports']
        self.arcs = calz['arcs']
        for f in self.F:
            if f['arc'] not in self.arcs:
                raise SystemExit(f"{f['id']}: no map arc for {f['arc']}. A new route needs its arc drawn first.")
        self.airlines = first_order(f['airline'] for f in self.F)
        self.aname = {f['airline']: f['airline_name'] for f in self.F}
        self.acolor = {f['airline']: f['color'] for f in self.F}
        self.ac = Counter(f['airline'] for f in self.F)
        self.air_rank = ranked(self.ac, self.airlines)
        seq = [c for f in self.F for c in (f['dep'], f['arr'])]
        self.apts = first_order(seq)
        self.uses = Counter(seq)
        self.apt_rank = ranked(self.uses, self.apts)
        self.fams = first_order(f['family'] for f in self.F)
        self.fc = Counter(f['family'] for f in self.F)
        self.regs = first_order(f['reg'] for f in self.F)
        self.rc = Counter(f['reg'] for f in self.F)
        self.countries = first_order(self.A[c]['country'] for c in seq)
        self.timed = [f for f in self.F if f['act_arr'] and f['arr_delay'] is not None]

    def calz(self):
        A = {}
        for k, v in self.A.items():
            v = dict(v); v['uses'] = self.uses.get(k, 0); A[k] = v
        return json.dumps({'flights': self.F, 'airports': A, 'arcs': self.arcs}, ensure_ascii=False, separators=(',', ':'))

    def city(self, c):
        return self.A[c]['city']

    def route(self, f):
        return ' ⇄ '.join(sorted([f['dep'], f['arr']]))

    # ---------- dashboard ----------
    def dash(self, p):
        F = self.F; N = len(F); miles = sum(f['miles'] for f in F); mins = sum(f['duration'] for f in F)
        p = sub(p, r'(<p class="lede">)\d+ flights, [\d,]+ miles and \d+ countries',
                f'<p class="lede">{N} flights, {n(miles)} miles and {len(self.countries)} countries')
        rows = []
        for f in reversed(F[-6:]):
            st = 'ON TIME' if ontime(f) else 'LATE'
            rows.append(f'<a class="brow" href="#" data-flight="{f["id"]}"><span>{dshort(f["date"])}</span><span class="r">{esc(f["flight"])}</span>'
                        f'<span>{f["dep"]} → {f["arr"]} <span class="r">{esc(self.city(f["arr"]).upper())}</span></span><span class="st">{st}</span></a>')
        p = sub(p, r'<span aria-hidden="true">✈</span></h2>.*?</div>\n</section>',
                '<span aria-hidden="true">✈</span></h2>' + ''.join(rows) + '</div>\n</section>')
        lng = max(F, key=lambda f: (f['miles'], f['duration'])); sht = min(F, key=lambda f: (f['miles'], f['duration']))
        routes = Counter(self.route(f) for f in F)
        rorder = first_order(self.route(f) for f in F)
        top_r = ranked(routes, rorder)[0]; top_a = self.apt_rank[0]
        s = ''.join([
            stat(N, f'{dlong(F[0]["date"])} to {dlong(F[-1]["date"])}', 'Flights flown'),
            stat(n(miles), f'{miles / EQUATOR:.1f}× round the Equator', 'Miles flown'),
            stat(f'{mins / 60:.1f}', f'{mins / 1440:.1f} days, gate to gate', 'Hours in the air'),
            stat(len(self.countries), 'including home', 'Countries'),
            stat(len(self.apts), '', 'Airports'), stat(len(self.airlines), '', 'Airlines'),
            stat(len(self.fams), '', 'Aircraft types'), stat(len(self.regs), 'by registration', 'Individual aircraft'),
            stat(f'{lng["dep"]} → {lng["arr"]}', f'{n(lng["miles"])} mi · {esc(lng["airline_name"])}', 'Longest flight', True),
            stat(f'{sht["dep"]} → {sht["arr"]}', f'{n(sht["miles"])} mi · {esc(sht["airline_name"])}', 'Shortest flight', True),
            stat(top_a, f'{esc(self.city(top_a))} · {self.uses[top_a]} times', 'Most-used airport', True),
            stat(top_r, f'{routes[top_r]} flights', 'Most-flown route', True)])
        p = sub(p, r'<h2 id="s-h">Lifetime numbers</h2><div class="stats">.*?</div></section>',
                '<h2 id="s-h">Lifetime numbers</h2><div class="stats">' + s + '</div></section>')
        p = sub(p, r'<h2>Flights by airline</h2><ul class="bars">.*?</ul>',
                '<h2>Flights by airline</h2>' + bars([(self.aname[a], self.ac[a]) for a in self.air_rank]))
        p = sub(p, r'<p class="note" style="margin-top:10px">\d+ flights have actual times recorded\. \d+ of them',
                f'<p class="note" style="margin-top:10px">{len(self.timed)} flights have actual times recorded. {sum(map(ontime, self.timed))} of them')
        p = sub(p, r'<span>\d+ types and \d+ individual aircraft, by registration\.</span>',
                f'<span>{len(self.fams)} types and {len(self.regs)} individual aircraft, by registration.</span>')
        return p

    # ---------- flight log and map filters ----------
    def opts(self, values):
        return ''.join(f'<option value="{esc(v)}">{esc(t)}</option>' for v, t in values)

    def years(self, newest_first):
        ys = sorted({f['year'] for f in self.F}, reverse=newest_first)
        return self.opts((y, y) for y in ys)

    def types_opts(self):
        return self.opts((t, t) for t in sorted(self.fams))

    def log(self, p):
        p = self._sel(p, 'f-y', 'All years', self.years(True))
        p = self._sel(p, 'f-a', 'All airlines', self.opts((a, self.aname[a]) for a in self.air_rank))
        p = self._sel(p, 'f-p', 'All airports', self.opts((c, f'{c} · {self.city(c)}') for c in sorted(self.apts)))
        p = self._sel(p, 'f-r', 'All routes', self.opts((r, r) for r in sorted({self.route(f) for f in self.F})))
        p = self._sel(p, 'f-t', 'All aircraft', self.types_opts())
        return p

    def _sel(self, p, i, first, inner):
        return sub(p, rf'<select id="{i}"><option value="">{first}</option>.*?</select>',
                   f'<select id="{i}"><option value="">{first}</option>{inner}</select>')

    def map(self, p):
        p = self._sel(p, 'f-y', 'All years', self.years(False))
        p = self._sel(p, 'f-t', 'All aircraft', self.types_opts())
        leg = ''.join(f'<button type="button" aria-pressed="true" data-air="{esc(a)}"><i style="background:{self.acolor[a]}"></i>'
                      f'{esc(self.aname[a])} <span class="note">{self.ac[a]}</span></button>' for a in self.air_rank)
        return sub(p, r'(<div class="legend" role="group" aria-label="Show or hide airlines">).*?(</div>)',
                   '<div class="legend" role="group" aria-label="Show or hide airlines">' + leg + '</div>')

    # ---------- aircraft ----------
    def aircraft(self, p):
        icons = {name: svg for svg, name in re.findall(r'<article class="type">(<svg.*?</svg>)<span class="badge">×\d+</span><b>([^<]*)</b>', p, flags=re.S)}
        multi = [r for r in self.regs if self.rc[r] > 1]
        if multi:
            names = multi[0] if len(multi) == 1 else ', '.join(multi[:-1]) + ' and ' + multi[-1]
            who = f' {len(multi)} of them Rob’s managed to fly on more than once: {names}.' if len(multi) > 1 else f' One of them Rob’s managed to fly on more than once: {names}.'
        else:
            who = ''
        p = sub(p, r'<p class="lede">\d+ aircraft types and \d+ individual aircraft, each one tracked by its registration\.[^<]*</p>',
                f'<p class="lede">{len(self.fams)} aircraft types and {len(self.regs)} individual aircraft, each one tracked by its registration.{who}</p>')
        arts = []
        for fam in sorted(self.fams, key=lambda t: (-self.fc[t], t)):
            fl = [f for f in self.F if f['family'] == fam]
            if fam not in icons: raise SystemExit(f'No icon for a new aircraft type, {fam}: add one to the aircraft page first.')
            arts.append(f'<article class="type">{icons[fam]}<span class="badge">×{len(fl)}</span><b>{esc(fam)}</b>'
                        f'<p class="note">{esc(", ".join(sorted({f["variant"] for f in fl})))}</p>'
                        f'<p class="note">With {esc(", ".join(sorted({f["airline_name"] for f in fl}, key=str.lower)))} · first flown {dlong(fl[0]["date"])}</p></article>')
        p = sub(p, r'<div class="types">.*?</div></section>', '<div class="types">' + ''.join(arts) + '</div></section>')
        regs = []
        for r in self.regs:
            fl = [f for f in self.F if f['reg'] == r]; f0 = fl[0]
            tw = f'<span class="twice">FLOWN {len(fl)}×</span>' if len(fl) > 1 else ''
            li = ''.join(f'<li><button type="button" data-flight="{f["id"]}">{dlong(f["date"])} · {esc(f["flight"])} · {f["dep"]} → {f["arr"]}</button></li>' for f in fl)
            regs.append(f'<article class="reg" id="{esc(r)}" style="--c:{f0["color"]}"><h3>{esc(r)}{tw}</h3>'
                        f'<p>{esc(f0["airline_name"])} · {esc(f0["family"])} <span class="mono">{esc(f0["variant"])}</span></p><ul>{li}</ul></article>')
        return sub(p, r'<div class="regs">.*?</div>\n</section>', '<div class="regs">' + ''.join(regs) + '</div>\n</section>')

    # ---------- statistics ----------
    def stats(self, p):
        T = self.timed; N = len(self.F)
        allt = 'All ' + str(N) if len(T) == N else str(len(T)) + ' of ' + str(N)
        p = sub(p, r'All \d+ flights have actual times\.|\d+ of \d+ flights have actual times\.', f'{allt} flights have actual times.')
        ot = sum(map(ontime, T))
        bdd = max(T, key=lambda f: f['dep_delay']); ea = min(T, key=lambda f: f['arr_delay'])
        cu = max(T, key=lambda f: f['dep_delay'] - f['arr_delay']); la = max(T, key=lambda f: f['arr_delay'])
        def tag(f): return f'{esc(f["flight"])} {f["dep"]} → {f["arr"]}, {dlong(f["date"])}'
        def early(x): return f'{-x} min early' if x < 0 else f'{x} min late'
        s = ''.join([
            stat(f'{ot}/{len(T)}', f'{pct(ot, len(T))}% within 15 minutes', 'Arrived on time'),
            stat(sgn(avg([f['dep_delay'] for f in T])), 'versus the timetable', 'Average departure'),
            stat(sgn(avg([f['arr_delay'] for f in T])), 'negative means early', 'Average arrival'),
            stat(sum(1 for f in T if f['dep_delay'] > 0 and f['arr_delay'] < 0), 'the pilots made it up', 'Left late, landed early'),
            stat(f'{bdd["dep_delay"]} min', tag(bdd), 'Biggest departure delay'),
            stat(early(ea['arr_delay']), tag(ea), 'Earliest arrival', True),
            stat(f'{cu["dep_delay"] - cu["arr_delay"]} min', f'{esc(cu["flight"])}: left {cu["dep_delay"]} late, {early(cu["arr_delay"])}', 'Best catch-up', True),
            stat(f'{la["arr_delay"]} min', tag(la), 'Latest arrival')])
        p = sub(p, r'<h2 id="p-h">Punctuality</h2><div class="stats">.*?</div></section>',
                '<h2 id="p-h">Punctuality</h2><div class="stats">' + s + '</div></section>')
        rows = []
        for a in self.air_rank:
            fl = [f for f in T if f['airline'] == a]; fa = [f for f in self.F if f['airline'] == a]
            rows.append(f'<tr><th scope="row"><span class="chip"><i style="background:{self.acolor[a]}"></i>{esc(self.aname[a])}</span></th>'
                        f'<td class="num">{len(fa)}</td><td class="num">{n(sum(f["miles"] for f in fa))}</td><td class="num">{hm(sum(f["duration"] for f in fa))}</td>'
                        f'<td class="num">{sgn(avg([f["dep_delay"] for f in fl]))}</td><td class="num">{sgn(avg([f["arr_delay"] for f in fl]))}</td>'
                        f'<td class="num">{pct(sum(map(ontime, fl)), len(fl))}% <span class=note>of {len(fl)}</span></td></tr>')
        p = sub(p, r'(<h2 id="a-h">Airlines compared</h2>.*?<tbody>).*?</tbody>', lambda m: m.group(1) + ''.join(rows) + '</tbody>')
        years = sorted({f['year'] for f in self.F})
        yr = ''.join(f'<tr><th scope="row">{y}</th><td class="num">{sum(1 for f in self.F if f["year"] == y)}</td>'
                     f'<td class="num">{n(sum(f["miles"] for f in self.F if f["year"] == y))}</td>'
                     f'<td class="num">{hm(sum(f["duration"] for f in self.F if f["year"] == y))}</td></tr>' for y in years)
        p = sub(p, r'(<h2>Year by year</h2>.*?<tbody>).*?</tbody>', lambda m: m.group(1) + yr + '</tbody>')
        p = sub(p, r'<p class="note" style="margin-top:8px">\d{4} so far\.</p>', f'<p class="note" style="margin-top:8px">{years[-1]} so far.</p>')
        L = [f for f in T if f['dep'] == 'LBA']; M = [f for f in T if f['dep'] == 'MAN']
        def side(name, fl):
            return f'{name}: average {sgn(avg([f["dep_delay"] for f in fl]))} late leaving, {pct(sum(map(ontime, fl)), len(fl))}% arrived on time ({len(fl)} flights)'
        lt, mt = avg([f['dep_delay'] for f in L]), avg([f['dep_delay'] for f in M])
        verdict = ('On average, Leeds has got Rob away closer to the timetable.' if lt < mt else
                   'On average, Manchester has got Rob away closer to the timetable.' if mt < lt else 'So far it’s a dead heat.')
        p = sub(p, r'<h2>Leeds Bradford or Manchester\?</h2><p>.*?</p><p class="note" style="margin-top:8px">On average.*?</p>',
                f'<h2>Leeds Bradford or Manchester?</h2><p>{side("Leeds", L)} · {side("Manchester", M)}.</p>'
                f'<p class="note" style="margin-top:8px">{verdict} Manchester’s numbers come from {len(M)} long-haul departures, so it’s an early verdict.</p>')
        p = sub(p, r'<h2>Airports used</h2><ul class="bars">.*?</ul>',
                '<h2>Airports used</h2>' + bars([(f'{c} · {self.city(c)}', self.uses[c]) for c in self.apt_rank]))
        p = sub(p, r'<h2>Aircraft types</h2><ul class="bars">.*?</ul>',
                '<h2>Aircraft types</h2>' + bars([(t, self.fc[t]) for t in ranked(self.fc, self.fams)]))
        wd = Counter(DAYS[d(f['date']).weekday()] for f in self.F)
        p = sub(p, r'<h2>Day of the week</h2><ul class="bars">.*?</ul>', '<h2>Day of the week</h2>' + bars([(x, wd[x]) for x in DAYS]))
        def bucket(f):
            h = int(f['sched_dep'][:2])
            return 0 if h < 9 else 1 if h < 17 else 2 if h < 22 else 3
        bk = Counter(bucket(f) for f in self.F)
        names = ['Early morning (before 9am)', 'Daytime (9am–5pm)', 'Evening (5pm–10pm)', 'Late night (after 10pm)']
        return sub(p, r'<h2>Time of departure</h2><ul class="bars">.*?</ul>',
                   '<h2>Time of departure</h2>' + bars([(names[i], bk[i]) for i in range(4)]))

    # ---------- passport ----------
    def passport(self, p):
        F = self.F; last = F[-1]
        p = sub(p, r'Holder: Rob Callery · Issued: [^·]+ · \d+ stamps and counting\.',
                f'Holder: Rob Callery · Issued: {dlong(F[0]["date"])} · {len(F)} stamps and counting.')
        wk = d(last['date']).strftime('%a')
        bp = (f'<div class="m"><small>The Window Seat · latest flight</small><div class="codes">{last["dep"]} ✈ {last["arr"]}</div>'
              f'<p>{wk} {dlong(last["date"])} · {esc(last["airline_name"])}</p><div class="row">'
              f'<div><small>Flight</small><b>{esc(last["flight"])}</b></div><div><small>Aircraft</small><b>{esc(last["family"])} {esc(last["variant"])}</b></div>'
              f'<div><small>Registration</small><b>{esc(last["reg"])}</b></div><div><small>Flight time</small><b>{hm(last["duration"])}</b></div>'
              f'<div><small>Distance</small><b>{n(last["miles"])} mi</b></div></div></div><div class="s"><span>FLOWN</span>'
              f'<button type="button" class="btn" style="margin-top:10px;color:#13203a;background:#fff;border-color:#b9b09a" data-flight="{last["id"]}">Details</button></div>')
        p = sub(p, r'<div class="pass" role="group" aria-label="Latest flight">.*?</div></section>',
                '<div class="pass" role="group" aria-label="Latest flight">' + bp + '</div></section>')
        seen = OrderedDict()
        for f in F:
            for c in (f['dep'], f['arr']): seen.setdefault(self.A[c]['country'], f['date'])
        visas = ''.join(f'<div class="visa"><small>ADMITTED</small><b>{esc(k.upper())}</b>{dlong(v)}</div>' for k, v in seen.items())
        p = sub(p, r'<div class="visas">.*?</div></section>', '<div class="visas">' + visas + '</div></section>')
        st = []
        for i, f in enumerate(reversed(F)):
            cls = 'stamp round' if i % 3 == 1 else 'stamp'
            st.append(f'<button type="button" class="{cls}" style="--ink-c:{INKS[i % 5]};--r:{i % 9 - 4}deg" data-flight="{f["id"]}" '
                      f'aria-label="{esc(f["flight"])}, {esc(self.city(f["dep"]))} to {esc(self.city(f["arr"]))}, {dlong(f["date"])}">'
                      f'<span>{esc(f["airline_name"].upper())}</span><b>{f["dep"]} ✈ {f["arr"]}</b><span>{dlong(f["date"]).upper()}</span>'
                      f'<span>{esc(f["flight"])}</span><span class="fl">FLOWN</span></button>')
        return sub(p, r'<div class="pp-grid">.*?</div></section>', '<div class="pp-grid">' + ''.join(st) + '</div></section>')


def load():
    data = json.load(open(os.path.join(AV, 'flights.json')))
    pages = {k: open(v, encoding='utf-8').read() for k, v in PAGES.items()}
    t = pages['dash']; c = t[t.index('<script id="calz"'):]; calz = json.loads(c[c.index('>') + 1:c.index('</script>')])
    return data, pages, calz


def render(data, pages, calz):
    L = Log(data, calz)
    out = {}
    for k, p in pages.items():
        p = getattr(L, k)(p)
        p = sub(p, r'<script id="calz" type="application/json">.*?</script>', '<script id="calz" type="application/json">' + L.calz() + '</script>')
        out[k] = p
    return out


def flight_from(spec, data, calz):
    """Fill in the derived fields for a new flight from its local times."""
    A = calz['airports']; F = data['flights']
    f = dict(spec)
    for k in ('date', 'flight', 'dep', 'arr', 'sched_dep', 'act_dep', 'sched_arr', 'act_arr', 'reg', 'variant'):
        if not f.get(k): raise SystemExit(f'Missing {k}')
    like = next((x for x in reversed(F) if x['flight'][:2] == f['flight'][:2]), None) or {}
    for k in ('airline', 'airline_name', 'color'):
        f.setdefault(k, like.get(k))
    fam = next((x for x in F if x['variant'] == f['variant']), None)
    for k in ('maker', 'family', 'type'):
        f.setdefault(k, fam and fam[k])
    if not all(f.get(k) for k in ('airline', 'airline_name', 'color', 'maker', 'family', 'type')):
        raise SystemExit('New airline or aircraft type: give airline, airline_name, color, maker, family and type too.')
    day = d(f['date'])
    tz1, tz2 = ZoneInfo(A[f['dep']]['tz']), ZoneInfo(A[f['arr']]['tz'])
    def at(date, hhmm, tz): h, m = map(int, hhmm.split(':')); return dt.datetime(date.year, date.month, date.day, h, m, tzinfo=tz)
    sd = at(day, f['sched_dep'], tz1); ad = at(day, f['act_dep'], tz1)
    if (ad - sd).total_seconds() < -6 * 3600: ad += dt.timedelta(days=1)
    nxt = f.get('arr_next_day')
    if nxt is None:
        nxt = at(day, f['sched_arr'], tz2) < sd
    aday = day + dt.timedelta(days=1 if nxt else 0)
    sa = at(aday, f['sched_arr'], tz2); aa = at(aday, f['act_arr'], tz2)
    if (aa - sa).total_seconds() < -12 * 3600: aa += dt.timedelta(days=1)
    if (aa - sa).total_seconds() > 12 * 3600: aa -= dt.timedelta(days=1)
    a, b = sorted([f['dep'], f['arr']])
    same = next((x for x in F if x['arc'] == f'{a}-{b}|{f["airline"]}'), None)
    out = OrderedDict([
        ('id', f'{f["date"]}-{f["flight"]}'), ('date', f['date']), ('year', day.year), ('airline', f['airline']),
        ('airline_name', f['airline_name']), ('color', f['color']), ('flight', f['flight']), ('callsign', f.get('callsign')),
        ('dep', f['dep']), ('arr', f['arr']), ('sched_dep', f['sched_dep']), ('act_dep', f['act_dep']),
        ('sched_arr', f['sched_arr']), ('act_arr', f['act_arr']),
        ('dep_delay', round((ad - sd).total_seconds() / 60)), ('arr_delay', round((aa - sa).total_seconds() / 60)),
        ('duration', round((aa - ad).total_seconds() / 60)), ('duration_estimated', False),
        ('miles', f.get('miles') or (same and same['miles'])), ('miles_recorded', f.get('miles_recorded') or (same and same['miles_recorded'])),
        ('maker', f['maker']), ('family', f['family']), ('type', f['type']), ('variant', f['variant']), ('reg', f['reg']),
        ('arr_next_day', bool(nxt)), ('est_arr', None), ('est_arr_delay', None), ('note', f.get('note')),
        ('arc', f'{a}-{b}|{f["airline"]}'), ('rev', f['dep'] != a)])
    if not out['miles']: raise SystemExit('New route: give miles and miles_recorded.')
    return dict(out)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    data, pages, calz = load()
    if cmd == 'add':
        new = flight_from(json.load(open(sys.argv[2])), data, calz)
        if any(x['id'] == new['id'] for x in data['flights']): raise SystemExit(f'{new["id"]} is already in the log.')
        data['flights'].append(new); data['flights'].sort(key=lambda x: (x['date'], x['sched_dep']))
        data['generated'] = dt.date.today().isoformat()
        print(json.dumps(new, ensure_ascii=False))
    out = render(data, pages, calz)
    changed = [k for k in out if out[k] != pages[k]]
    if cmd == 'check':
        print('No page would change.' if not changed else 'Would change: ' + ', '.join(changed)); return
    for k in changed: open(PAGES[k], 'w', encoding='utf-8').write(out[k])
    with open(os.path.join(AV, 'flights.json'), 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print('Rebuilt: ' + (', '.join(changed) or 'nothing'))


if __name__ == '__main__':
    main()
