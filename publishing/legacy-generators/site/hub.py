import re, os, math
fav=open('/home/claude/favicon.svg').read()
globe_d=re.search(r'<path fill="#f7f7f2" fill-rule="evenodd" d="([^"]+)"',fav).group(1)

def ball(cx,cy,R):
    rc=R*.33; D=R*.92
    pent=lambda x,y,r,rot:[(x+r*math.cos(math.radians(rot+72*k)),y+r*math.sin(math.radians(rot+72*k))) for k in range(5)]
    P=lambda pts:"M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)+" Z"
    out=f'<clipPath id="bc{cx}"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath><circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff"/><g clip-path="url(#bc{cx})" fill="#14213d"><path d="{P(pent(cx,cy,rc,-90))}"/>'
    for k in range(5):
        a=math.radians(-90+72*k); out+=f'<path d="{P(pent(cx+D*math.cos(a),cy+D*math.sin(a),rc,-90+72*k+180))}"/>'
    return out+f'</g><circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#14213d" stroke-width="2"/>'

zz_top=" ".join(f"L{8+i*7.13:.1f} {40 if i%2==0 else 46}" for i in range(31))
zz_bot=" ".join(f"L{222-i*7.13:.1f} {282 if i%2==0 else 276}" for i in range(31))
PACKPATH=f"M8 46 {zz_top} L222 276 {zz_bot} Z"
BURST="M"+" L".join(f"{(24 if k%2==0 else 17)*math.cos(math.radians(k*15)):.1f} {(24 if k%2==0 else 17)*math.sin(math.radians(k*15)):.1f}" for k in range(24))+" Z"
PASSPORT=f'''<svg viewBox="0 0 230 300" role="img" aria-label="Beer passport">
  <defs><linearGradient id="pc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8a2338"/><stop offset="1" stop-color="#5b1324"/></linearGradient></defs>
  <rect x="12" y="8" width="210" height="288" rx="12" fill="#e9dfc6"/><rect x="10" y="6" width="210" height="288" rx="12" fill="#f4ecd8"/>
  <rect x="2" y="3" width="208" height="284" rx="10" fill="#f3ead4" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg0" x="2" y="3" width="208" height="284" rx="10" fill="#f6efdc" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg1" x="2" y="3" width="208" height="284" rx="10" fill="#f6efdc" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg2" x="2" y="3" width="208" height="284" rx="10" fill="#f6efdc" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg3" x="2" y="3" width="208" height="284" rx="10" fill="#f6efdc" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg4" x="2" y="3" width="208" height="284" rx="10" fill="#f6efdc" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg5" x="2" y="3" width="208" height="284" rx="10" fill="#f6efdc" stroke="#d8cba8" stroke-width="1"/>
  <g class="cv-inside"><rect x="0" y="0" width="214" height="290" rx="12" fill="#5b1324"/><rect x="8" y="8" width="198" height="274" rx="8" fill="#f4ecd8"/><rect x="24" y="34" width="60" height="76" rx="4" fill="#e3d7b8"/><g stroke="#cbbd99" stroke-width="3"><line x1="98" y1="42" x2="190" y2="42"/><line x1="98" y1="56" x2="190" y2="56"/><line x1="98" y1="70" x2="190" y2="70"/><line x1="98" y1="84" x2="190" y2="84"/><line x1="98" y1="98" x2="190" y2="98"/></g></g>
  <g class="cv-front">
  <rect x="0" y="0" width="214" height="290" rx="12" fill="url(#pc)"/>
  <rect x="12" y="12" width="190" height="266" rx="6" fill="none" stroke="#d9b45a" stroke-width="1.2" stroke-dasharray="3 3" opacity=".7"/>
  <g fill="#d9b45a" font-family="Bebas Neue, Impact, sans-serif" text-anchor="middle">
    <text x="107" y="44" font-size="14" letter-spacing="3" textLength="120" lengthAdjust="spacingAndGlyphs">UNITED KINGDOM</text>
    <text x="107" y="60" font-size="14" letter-spacing="3" textLength="58" lengthAdjust="spacingAndGlyphs">OF ALES</text>
  </g>
  <g fill="none" stroke="#d9b45a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="107" cy="134" r="44"/>
    <path d="M91 108 L123 108 L119 162 L95 162 Z"/><path d="M90 108 Q92 98 101 101 Q107 93 114 100 Q124 97 124 108"/>
    <path d="M101 122 L101 150" stroke-width="2"/>
    <path d="M63 160 Q52 134 64 108" stroke-width="2"/><path d="M151 160 Q162 134 150 108" stroke-width="2"/>
  </g>
  <g fill="#d9b45a">{''.join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="2.6" transform="rotate({r} {x} {y})"/>' for x,y,r in [(58,150,-60),(56,134,-85),(58,118,-110),(156,150,60),(158,134,85),(156,118,110)])}</g>
  <g fill="#d9b45a" font-family="Bebas Neue, Impact, sans-serif" text-anchor="middle">
    <text x="107" y="222" font-size="36" letter-spacing="3" textLength="172" lengthAdjust="spacingAndGlyphs">BEER PASSPORT</text>
    <text x="107" y="240" font-size="11" letter-spacing="2" opacity=".85" textLength="104" lengthAdjust="spacingAndGlyphs">PASSEPORT DE BIÈRE</text>
  </g>
  <g fill="none" stroke="#d9b45a" stroke-width="1.6"><rect x="94" y="252" width="26" height="17" rx="2"/><circle cx="107" cy="260.5" r="4"/><path d="M94 260.5h9M111 260.5h9"/></g>
</g>
</svg>'''

GUIDE=f'''<svg viewBox="0 0 230 300" role="img" aria-label="Travel guides">
  <rect x="14" y="6" width="208" height="290" rx="4" fill="#efe6cf"/>
  <rect x="2" y="3" width="208" height="284" rx="4" fill="#f6f1e2" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg0" x="2" y="3" width="208" height="284" rx="4" fill="#fbf7ec" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg1" x="2" y="3" width="208" height="284" rx="4" fill="#fbf7ec" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg2" x="2" y="3" width="208" height="284" rx="4" fill="#fbf7ec" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg3" x="2" y="3" width="208" height="284" rx="4" fill="#fbf7ec" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg4" x="2" y="3" width="208" height="284" rx="4" fill="#fbf7ec" stroke="#d8cba8" stroke-width="1"/><rect class="pg pg5" x="2" y="3" width="208" height="284" rx="4" fill="#fbf7ec" stroke="#d8cba8" stroke-width="1"/>
  <g class="cv-inside"><rect x="0" y="0" width="214" height="290" rx="6" fill="#0a4a4d"/><rect x="8" y="8" width="198" height="274" rx="4" fill="#fbf7ec"/><g stroke="#cbbd99" stroke-width="3"><line x1="24" y1="50" x2="190" y2="50"/><line x1="24" y1="68" x2="190" y2="68"/><line x1="24" y1="86" x2="190" y2="86"/><line x1="24" y1="104" x2="190" y2="104"/><line x1="24" y1="122" x2="190" y2="122"/><line x1="24" y1="140" x2="190" y2="140"/><line x1="24" y1="158" x2="190" y2="158"/><line x1="24" y1="176" x2="190" y2="176"/><line x1="24" y1="194" x2="190" y2="194"/><line x1="24" y1="212" x2="190" y2="212"/><line x1="24" y1="230" x2="190" y2="230"/><line x1="24" y1="248" x2="190" y2="248"/></g></g>
  <g class="cv-front">
  <rect x="0" y="0" width="214" height="290" rx="6" fill="#f6edd6"/>
  <rect x="0" y="0" width="20" height="290" rx="6" fill="#0f6f73"/><rect x="18" y="0" width="3" height="290" fill="#0b5558"/>
  <rect x="21" y="0" width="193" height="62" fill="#0f6f73"/>
  <text x="118" y="42" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="34" letter-spacing="3" fill="#ffcd00" textLength="168" lengthAdjust="spacingAndGlyphs">TRAVEL GUIDES</text>
  <path d="M42 196 Q118 266 196 170" fill="none" stroke="#0f6f73" stroke-width="2" stroke-dasharray="5 5"/>
  <svg x="58" y="74" width="120" height="120" viewBox="190 157 700 700"><circle cx="540" cy="507" r="345" fill="#0a1838"/><path fill="#f7f7f2" fill-rule="evenodd" d="{globe_d}"/></svg>
  <path d="M196 170 l-14 -2 l3 5 l-6 4 l4 1 l6 -3 l2 6 l3 -1 z" fill="#0a1838" transform="rotate(-30 190 172)"/>
  <text x="118" y="232" text-anchor="middle" font-family="DM Serif Display, Georgia, serif" font-style="italic" font-size="17" fill="#0a1838" textLength="136" lengthAdjust="spacingAndGlyphs">one beer at a time</text>
  <text x="118" y="270" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="15" letter-spacing="4" fill="#0f6f73" textLength="108" lengthAdjust="spacingAndGlyphs">ROB CALLERY</text>
</g>
</svg>'''

BOOK=f'''<svg viewBox="0 0 230 300" role="img" aria-label="Football: Tales of a Leeds Fan">
  <defs><clipPath id="bk"><rect x="0" y="0" width="214" height="290" rx="6"/></clipPath></defs>
  <rect x="14" y="6" width="208" height="290" rx="4" fill="#efe9dc"/>
  <g clip-path="url(#bk)">
    <rect x="0" y="0" width="214" height="290" fill="#fbfaf5"/>
    <path d="M0 230 L80 290 L0 290 Z" fill="#1d4ed8"/><path d="M0 200 L120 290 L94 290 L0 220 Z" fill="#ffcd00"/>
    <path d="M214 60 L150 0 L214 0 Z" fill="#1d4ed8"/><path d="M214 92 L118 0 L140 0 L214 72 Z" fill="#ffcd00"/>
    <rect x="0" y="0" width="22" height="290" fill="#0a1838"/><rect x="20" y="0" width="3" height="290" fill="#06102a"/>
  </g>
  <text x="120" y="76" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="56" letter-spacing="2" fill="#0a1838" textLength="162" lengthAdjust="spacingAndGlyphs">FOOTBALL</text>
  <rect x="38" y="88" width="164" height="26" fill="#0a1838"/>
  <text x="120" y="106" text-anchor="middle" font-family="DM Serif Display, Georgia, serif" font-style="italic" font-size="15.5" fill="#ffcd00" textLength="144" lengthAdjust="spacingAndGlyphs">Tales of a Leeds Fan</text>
  {ball(120,172,36)}
  <path d="M86 214 q34 10 68 0" fill="none" stroke="#c9c3b3" stroke-width="3" stroke-linecap="round"/>
  <text x="120" y="262" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="16" letter-spacing="4" fill="#0a1838" textLength="108" lengthAdjust="spacingAndGlyphs">ROB CALLERY</text>
  <path d="M176 290 L176 312 L183 305 L190 312 L190 290 Z" fill="#ffcd00"/>
</svg>'''

PACK=f"""<svg viewBox="0 0 230 300" role="img" aria-label="Football Tales trading card pack">
  <defs>
    <linearGradient id="foil" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2e63e6"/><stop offset=".45" stop-color="#1238a8"/><stop offset=".55" stop-color="#2a5ad8"/><stop offset="1" stop-color="#0a1f66"/></linearGradient>
    <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <clipPath id="packClip"><path d="{PACKPATH}"/></clipPath>
  </defs>
  <!-- cards peeking out the top -->
  <g transform="rotate(-9 70 40)"><rect x="40" y="2" width="96" height="130" rx="6" fill="#fbfaf5" stroke="#ffcd00" stroke-width="4"/><rect x="50" y="12" width="76" height="60" rx="3" fill="#1d4ed8"/><circle cx="88" cy="36" r="10" fill="#ffcd00"/><rect x="74" y="48" width="28" height="22" rx="8" fill="#ffcd00"/></g>
  <g transform="rotate(7 150 40)"><rect x="104" y="6" width="96" height="130" rx="6" fill="#fbfaf5" stroke="#1d4ed8" stroke-width="4"/><rect x="114" y="16" width="76" height="60" rx="3" fill="#ffcd00"/><circle cx="152" cy="40" r="10" fill="#1d4ed8"/><rect x="138" y="52" width="28" height="22" rx="8" fill="#1d4ed8"/></g>
  <!-- foil pack -->
  <path d="{PACKPATH}" fill="url(#foil)"/>
  <g clip-path="url(#packClip)">
    <path d="M-20 300 L110 60 L140 60 L10 300 Z" fill="#fff" opacity=".07"/><path d="M60 300 L190 60 L205 60 L75 300 Z" fill="#fff" opacity=".06"/>
    <rect class="sheen" x="-120" y="40" width="90" height="270" fill="url(#sheen)" transform="skewX(-20)"/>
    <rect x="8" y="232" width="214" height="34" fill="#ffcd00"/>
    <rect x="8" y="228" width="214" height="3" fill="#fff" opacity=".8"/>
  </g>
  <path d="M8 48 L222 48" stroke="#0a1f66" stroke-width="2" opacity=".5"/><path d="M8 274 L222 274" stroke="#0a1f66" stroke-width="2" opacity=".5"/>
  <!-- starburst -->
  <g transform="translate(176 196) rotate(12)"><path d="{BURST}" fill="#ffcd00"/><text y="-2" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="10" fill="#0a1838">SERIES</text><text y="12" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="17" fill="#0a1838">1</text></g>
  <text x="115" y="104" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="48" letter-spacing="1" fill="#ffffff" textLength="150" lengthAdjust="spacingAndGlyphs" style="paint-order:stroke" stroke="#0a1838" stroke-width="3">FOOTBALL</text>
  <text x="115" y="138" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="40" letter-spacing="1" fill="#ffcd00" textLength="110" lengthAdjust="spacingAndGlyphs" style="paint-order:stroke" stroke="#0a1838" stroke-width="3">TALES</text>
  <text x="115" y="160" text-anchor="middle" font-family="DM Serif Display, Georgia, serif" font-style="italic" font-size="13" fill="#fff" textLength="128" lengthAdjust="spacingAndGlyphs">of a Leeds Fan</text>
  {ball(84,192,20)}
  <text x="115" y="255" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="15" letter-spacing="2" fill="#0a1838" textLength="170" lengthAdjust="spacingAndGlyphs">TRADING CARDS · 5 PER PACK</text>
  <text x="115" y="226" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="8" letter-spacing="3" fill="#fff" opacity=".75">ROB CALLERY COLLECTION</text>
</svg>"""

TWITCH_URL="https://www.twitch.tv/robcallery"
YOUTUBE_URL="https://www.youtube.com/@calz88"
TV=f"""<svg viewBox="0 0 230 210" role="img" aria-label="Old TV - watch live on Twitch">
  <defs>
    <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a5a32"/><stop offset="1" stop-color="#5e3a1d"/></linearGradient>
    <radialGradient id="crt" cx=".5" cy=".45" r=".7"><stop offset="0" stop-color="#3b2a6e"/><stop offset=".7" stop-color="#1b1236"/><stop offset="1" stop-color="#0a0716"/></radialGradient>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="2" fill="#000" opacity=".28"/></pattern>
    <filter id="noise"><feTurbulence class="noiseSeed" type="fractalNoise" baseFrequency=".9" numOctaves="1" seed="2"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .5 0"/></filter>
    <clipPath id="scr"><rect x="22" y="58" width="140" height="112" rx="22"/></clipPath>
  </defs>
  <line x1="98" y1="44" x2="62" y2="2" stroke="#9aa1ad" stroke-width="3" stroke-linecap="round"/><line x1="112" y1="44" x2="150" y2="6" stroke="#9aa1ad" stroke-width="3" stroke-linecap="round"/>
  <circle cx="62" cy="2" r="3.5" fill="#c9ced6"/><circle cx="150" cy="6" r="3.5" fill="#c9ced6"/>
  <path d="M86 46 Q105 30 124 46 Z" fill="#2b2b2b"/>
  <rect x="4" y="44" width="222" height="146" rx="16" fill="url(#wood)"/>
  <g stroke="#4c2e16" stroke-width="1" opacity=".35" fill="none"><path d="M10 70 Q60 64 120 72 T224 66"/><path d="M8 110 Q70 104 130 112 T224 106"/><path d="M8 160 Q80 154 140 162 T224 156"/></g>
  <rect x="14" y="52" width="156" height="126" rx="26" fill="#1a1a1a"/>
  <rect x="22" y="58" width="140" height="112" rx="22" fill="url(#crt)" class="screen"/>
  <g clip-path="url(#scr)">
    <rect x="22" y="58" width="140" height="112" filter="url(#noise)" opacity=".22" class="static"/>
    <rect x="22" y="58" width="140" height="112" fill="url(#scan)"/>
    <circle cx="58" cy="96" r="5" fill="#ff3b3b" class="recdot"/>
    <text x="68" y="101" font-family="Bebas Neue, Impact, sans-serif" font-size="15" letter-spacing="2" fill="#fff">LIVE</text>
    <text x="92" y="134" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="25" letter-spacing="2" fill="#c9a8ff" textLength="104" lengthAdjust="spacingAndGlyphs" style="filter:drop-shadow(0 0 6px #9146ff)">ON TWITCH</text>
    <rect x="22" y="58" width="140" height="18" fill="#fff" opacity=".05" class="roll"/>
  </g>
  <path d="M30 66 Q60 60 92 64" stroke="#fff" stroke-width="3" opacity=".18" fill="none" stroke-linecap="round"/>
  <rect x="178" y="58" width="40" height="112" rx="6" fill="#4a2d16"/>
  <g><circle cx="198" cy="80" r="11" fill="#d6d0c4"/><rect x="196" y="70" width="4" height="10" rx="2" fill="#6b6459"/><circle cx="198" cy="110" r="9" fill="#d6d0c4"/><rect x="196.5" y="102" width="3" height="8" rx="1.5" fill="#6b6459"/></g>
  <g fill="#2b1a0c">{''.join(f'<rect x="186" y="{y}" width="24" height="2.5" rx="1"/>' for y in range(132,164,6))}</g>
  <rect x="24" y="190" width="26" height="14" rx="3" fill="#2b2b2b"/><rect x="180" y="190" width="26" height="14" rx="3" fill="#2b2b2b"/>
</svg>"""
VCR=f"""<svg viewBox="0 0 230 74" role="img" aria-label="Video recorder - watch on YouTube">
  <defs><linearGradient id="vcr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a3d44"/><stop offset="1" stop-color="#1c1e22"/></linearGradient></defs>
  <rect x="2" y="4" width="226" height="56" rx="6" fill="url(#vcr)"/>
  <rect x="2" y="4" width="226" height="5" rx="3" fill="#5a5e68"/>
  <rect x="16" y="20" width="96" height="14" rx="3" fill="#0b0c0e"/>
  <g class="tape"><rect x="22" y="12" width="84" height="16" rx="2" fill="#1a1a1a"/><rect x="30" y="14" width="68" height="10" rx="1.5" fill="#f2efe6"/><text x="64" y="22" text-anchor="middle" font-family="Bebas Neue, Impact, sans-serif" font-size="8.5" fill="#c4302b" textLength="60" lengthAdjust="spacingAndGlyphs">HIGHLIGHTS · YOUTUBE</text></g>
  <rect x="16" y="40" width="96" height="3" rx="1.5" fill="#55595f"/>
  <rect x="126" y="18" width="62" height="22" rx="3" fill="#081008"/>
  <text x="157" y="34.5" text-anchor="middle" font-family="'Courier New', monospace" font-weight="700" font-size="15" fill="#4dff88" class="clock" style="filter:drop-shadow(0 0 3px #4dff88)">12:00</text>
  <g fill="#8d929c">{''.join(f'<rect x="{x}" y="46" width="14" height="7" rx="1.5"/>' for x in (126,142,158,174))}</g>
  <path d="M130 47.5 l5 2 l-5 2 z" fill="#1c1e22"/>
  <rect x="198" y="20" width="18" height="18" rx="9" fill="#1a1c20" stroke="#55595f" stroke-width="2"/><circle cx="207" cy="29" r="2.5" fill="#ff3b3b"/>
  <rect x="14" y="60" width="20" height="6" rx="2" fill="#111"/><rect x="196" y="60" width="20" height="6" rx="2" fill="#111"/>
</svg>"""

import sys as _sys; _sys.path.insert(0,"/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad/")
from stadium_parts import poster, scoreboard_art, stadium_scene, scoreboard_link, cards_link
POSTER=poster()
ITEMS=[("beer-passport","Beer Passport","Every beer, every bar, stamped and rated.",PASSPORT,-3),
       ("travel-guides","Travel Guides","City guides from a pint-first point of view.",GUIDE,2),
       ("stadium","Elland Road","Through the turnstiles for football tales and the match hub.",POSTER,-2)]

HEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root{{--navy:#0a1838;--navy2:#13285a;--yellow:#ffcd00;--cream:#f7f2e4;--muted:#b8c3dc;--wood1:#7a4b27;--wood2:#5a361b;--wood3:#3b2312}}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{min-height:100vh;background:radial-gradient(ellipse 90% 60% at 50% 0,#2b417e 0,#13285a 45%,#0a1838 100%);color:var(--cream);font-family:Inter,system-ui,sans-serif;line-height:1.55;display:flex;flex-direction:column}}
  a{{color:inherit}}
  header{{display:flex;align-items:center;justify-content:space-between;gap:16px;max-width:1160px;width:100%;margin:0 auto;padding:22px 16px}}
  .brand{{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:"Bebas Neue",Impact,sans-serif;font-size:1.6rem;letter-spacing:.06em}}
  .brand svg{{width:38px;height:38px}}
  .back{{font-size:.92rem;font-weight:600;text-decoration:none;opacity:.85;padding:.45em .9em;border:1.5px solid rgba(247,242,228,.4);border-radius:999px;transition:opacity .15s,border-color .15s}}
  .back:hover,.back:focus-visible{{opacity:1;border-color:var(--yellow)}}
  main{{flex:1;width:100%}}
  .intro{{text-align:center;max-width:720px;margin:0 auto;padding:18px 16px 8px}}
  .intro h1{{font-family:"DM Serif Display",Georgia,serif;font-weight:400;font-size:clamp(2.2rem,5.5vw,3.6rem);line-height:1.05;letter-spacing:-.01em}}
  .intro h1 em{{color:var(--yellow);font-style:italic}}
  .intro p{{color:var(--muted);margin-top:.7rem;font-size:clamp(1rem,2vw,1.12rem)}}
  .bar{{position:relative;margin-top:28px;padding:0 16px 70px}}
  .bar::before{{content:"";position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(180deg,var(--wood1) 0,var(--wood2) 22px,#4a2c16 60%,var(--wood3) 100%);box-shadow:inset 0 3px 0 rgba(255,220,170,.25)}}
  .bar::after{{content:"";position:absolute;left:0;right:0;bottom:150px;height:40px;background:linear-gradient(180deg,transparent,rgba(0,0,0,.25))}}
  .items{{position:relative;z-index:1;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;max-width:1180px;margin:0 auto;align-items:end}}
  .item{{display:flex;flex-direction:column;align-items:center;text-decoration:none;text-align:center;outline:none}}
  .item .art{{width:min(230px,100%);transform:rotate(var(--r));transition:transform .35s cubic-bezier(.2,.8,.2,1.2),filter .35s;filter:drop-shadow(0 18px 18px rgba(0,0,0,.45))}}
  .item .art>svg{{width:100%;height:auto;display:block;overflow:visible}}
  .item:hover .art,.item:focus-visible .art{{transform:rotate(0) translateY(-14px) scale(1.04);filter:drop-shadow(0 30px 24px rgba(0,0,0,.5))}}
  .label{{margin-top:22px;background:var(--cream);color:var(--navy);border-radius:10px;padding:10px 16px 12px;min-width:200px;box-shadow:0 6px 16px rgba(0,0,0,.35);transition:background .2s}}
  .label h2{{font-family:"Bebas Neue",Impact,sans-serif;font-weight:400;font-size:1.7rem;letter-spacing:.05em;line-height:1}}
  .label p{{font-size:.86rem;color:#4a5570;margin-top:3px}}
  .item:hover .label,.item:focus-visible .label{{background:var(--yellow)}}
  .item:focus-visible .label{{outline:3px solid #fff;outline-offset:3px}}
  footer{{text-align:center;padding:22px 16px;color:var(--muted);font-size:.85rem;background:var(--wood3)}}
  .soon{{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:48px;align-items:center;max-width:960px;margin:0 auto;padding:30px 16px 70px}}
  .soon .art{{transform:rotate(var(--r));filter:drop-shadow(0 22px 22px rgba(0,0,0,.45))}}
  .soon .art>svg{{width:100%;height:auto;display:block;overflow:visible}}
  .soon .tag{{display:inline-block;background:var(--yellow);color:var(--navy);font-weight:700;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;padding:.35em .8em;border-radius:6px}}
  .soon h1{{font-family:"DM Serif Display",Georgia,serif;font-weight:400;font-size:clamp(2.2rem,5vw,3.4rem);line-height:1.05;margin:.6rem 0 .8rem}}
  .soon p{{color:var(--muted);font-size:1.08rem;max-width:34rem}}
  .soon .btn{{display:inline-block;margin-top:1.6rem;background:var(--cream);color:var(--navy);font-weight:700;text-decoration:none;padding:.7em 1.4em;border-radius:999px;transition:background .2s}}
  .soon .btn:hover,.soon .btn:focus-visible{{background:var(--yellow)}}
  @media (max-width:820px){{
    .items{{grid-template-columns:1fr;gap:44px;max-width:300px}}
    .bar::before,.bar::after{{display:none}}
    .bar{{padding-bottom:50px}}
    .soon{{grid-template-columns:1fr;text-align:center;gap:28px}}
    .soon .art{{max-width:230px;margin:0 auto}}
    .soon p{{margin:0 auto}}
  }}
  .pg,.cv-front,.cv-inside{{transform-box:view-box;transform-origin:0px 145px}}
  .pg,.cv-inside{{transform:scaleX(0)}}
  .pg{{opacity:0}}
  .flick .art{{transform:rotate(0) translateY(-10px) scale(1.04)!important}}
  .flick .cv-front{{animation:cvF .32s ease-in forwards}}
  .flick .cv-inside{{animation:cvI .32s .32s ease-out forwards}}
  .flick .pg{{animation:pgFlip .26s ease-in-out forwards}}
  .flick .pg0{{animation-delay:.42s}}.flick .pg1{{animation-delay:.52s}}.flick .pg2{{animation-delay:.62s}}.flick .pg3{{animation-delay:.72s}}.flick .pg4{{animation-delay:.82s}}.flick .pg5{{animation-delay:.92s}}
  @keyframes cvF{{to{{transform:scaleX(0)}}}}
  @keyframes cvI{{to{{transform:scaleX(-.72)}}}}
  @keyframes pgFlip{{0%{{opacity:1;transform:scaleX(1)}}100%{{opacity:1;transform:scaleX(-.7)}}}}
  .pg{{animation-fill-mode:forwards}}
  .brand,.back{{white-space:nowrap}}
  .tvstack{{width:min(230px,100%)}}
  .telly .art{{display:block;text-decoration:none;width:100%}}
  .telly .label{{min-width:0;width:min(300px,100%)}}
  .telly .vcr{{margin-top:-2px}}
  .telly:hover .art,.telly .art:hover{{transform:none}}
  .telly .tv:hover,.telly .tv:focus-visible{{transform:translateY(-8px) rotate(-1.5deg) scale(1.03)}}
  .telly .vcr:hover,.telly .vcr:focus-visible{{transform:translateY(-4px) scale(1.03)}}
  .telly .art:focus-visible{{outline:3px solid #fff;outline-offset:4px;border-radius:12px}}
  .telly .tv:hover .screen{{fill:#4b2f9a}}
  .telly .vcr:hover .tape{{transform:translateY(8px)}}
  .tape{{transition:transform .4s ease}}
  .telly .label{{margin-top:22px;padding-bottom:12px}}
  .telly .label h2{{margin-bottom:0}}
  .items>.item{{align-self:end}}
  .label{{min-height:95px;display:flex;flex-direction:column;justify-content:center}}
  .telly .label p{{white-space:nowrap}}
  .telly .label p a{{color:inherit;text-decoration:underline;text-underline-offset:2px}}
  .telly .label p a:hover{{color:#1d4ed8}}
  .static{{animation:flick .15s steps(2) infinite}}
  @keyframes flick{{50%{{opacity:.12}}}}
  .roll{{animation:roll 3.5s linear infinite}}
  @keyframes roll{{from{{transform:translateY(-20px)}}to{{transform:translateY(130px)}}}}
  .recdot,.clock{{animation:blinkit 1.2s steps(2) infinite}}
  @keyframes blinkit{{50%{{opacity:.15}}}}
  @media (max-width:1100px) and (min-width:821px){{.items{{grid-template-columns:repeat(2,minmax(0,1fr));max-width:640px;row-gap:56px}}.bar::before,.bar::after{{display:none}}}}
  .sheen{{transition:transform 1s ease}}
  .item:hover .sheen,.item:focus-visible .sheen{{transform:skewX(-20deg) translateX(420px)}}
  @media (max-width:480px){{.brand{{font-size:1.3rem}}.brand svg{{width:30px;height:30px}}.back{{font-size:.8rem}}}}
  .enter .art{{transition:transform .75s cubic-bezier(.6,0,.4,1),opacity .75s ease;transform:rotate(0) scale(3.2)!important;opacity:0}}
  .enter .label{{opacity:0;transition:opacity .3s}}
  .stadium{{position:relative;max-width:1200px;margin:6px auto 0;padding:0 16px}}
  .stadium>svg{{width:100%;height:auto;display:block;border-radius:14px;box-shadow:0 20px 40px rgba(0,0,0,.45)}}
  .hot{{cursor:pointer;outline:none}}
  .hot rect,.hot g{{transition:transform .3s ease,filter .3s ease}}
  .sb:hover>rect:first-child,.sb:focus-visible>rect:first-child{{filter:drop-shadow(0 0 14px #ffcd00)}}
  .cards{{transition:transform .35s cubic-bezier(.2,.8,.2,1.2)}}
  .cards:hover,.cards:focus-visible{{transform:translateY(-16px)}}
  .hot:focus-visible{{outline:3px solid #fff}}
  .pl .body{{transform-box:fill-box;transform-origin:50% 100%}}
  .pl .body.kick{{animation:kick .35s ease-out}}
  @keyframes kick{{30%{{transform:translateY(-3px) rotate(-6deg)}}100%{{transform:none}}}}
  .tvlink{{transition:transform .3s ease,filter .3s ease;transform-box:fill-box;transform-origin:50% 100%}}
  .tvlink:hover,.tvlink:focus-visible{{transform:translateY(-8px) scale(1.03);filter:drop-shadow(0 0 18px rgba(255,205,0,.55))}}
  .bmsg{{transition:opacity .35s ease,transform .35s ease;transform-box:fill-box}}
  .bmsg.out{{opacity:0;transform:translateY(-14px)}}
  .bbg{{transition:fill .35s ease}}
  .board[href]{{cursor:pointer}}
  .board[href]:hover .bbg,.board[href]:focus-visible .bbg{{filter:brightness(1.25)}}
  .spots{{display:flex;justify-content:center;gap:24px;flex-wrap:wrap;max-width:1200px;margin:26px auto 60px;padding:0 16px}}
  .spot{{text-decoration:none;background:var(--cream);color:var(--navy);border-radius:10px;padding:12px 18px;min-width:260px;max-width:360px;box-shadow:0 6px 16px rgba(0,0,0,.35);transition:background .2s}}
  .spot h2{{font-family:"Bebas Neue",Impact,sans-serif;font-weight:400;font-size:1.7rem;letter-spacing:.05em;line-height:1}}
  .spot p{{font-size:.88rem;color:#4a5570;margin-top:3px}}
  .spot:hover,.spot:focus-visible{{background:var(--yellow)}}
  .spot .tag{{display:inline-block;background:#1e3f9a;color:#fff;font-size:.66rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:.2em .6em;border-radius:4px;margin-left:.4em;vertical-align:.3em}}
  @media (prefers-reduced-motion:reduce){{.item .art{{transition:none}}.static,.roll,.recdot,.clock{{animation:none}}}}
</style>
</head>
<body>
<header>
  <a class="brand" href="/"><svg viewBox="190 157 700 700" aria-hidden="true"><circle cx="540" cy="507" r="345" fill="#f7f2e4"/><path fill="#0a1838" fill-rule="evenodd" d="{globe}"/></svg>Rob Callery</a>
  <a class="back" href="{backhref}">{backtxt}</a>
</header>
'''
FOOT='''<footer>© <span id="yr">2026</span> Rob Callery · callery.co.uk · Drink responsibly</footer>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
</body>
</html>
'''
os.makedirs('/home/claude/site/explore',exist_ok=True)
hub=HEAD.format(title="Explore - Rob Callery",desc="Beer passport, travel guides and football tales from Rob Callery.",globe=globe_d,backhref="/",backtxt="← Back to Elland Road")
hub+='''<main>
  <section class="intro">
    <h1>Pull up a stool, <em>pick a read.</em></h1>
    <p>Beers I've stamped, cities I've drunk my way round, and a lifetime of following Leeds.</p>
  </section>
  <section class="bar" aria-label="Sections">
    <div class="items">
'''
for slug,name,desc,svg,r in ITEMS:
    hub+=f'''      <a class="item item-{slug}" href="/{slug}/" style="--r:{r}deg">
        <div class="art">{svg}</div>
        <div class="label"><h2>{name}</h2><p>{desc}</p></div>
      </a>
'''
hub+=f'''      <div class="item telly" style="--r:0deg"><div class="tvstack">
        <a class="art tv" href="{TWITCH_URL}" target="_blank" rel="noopener" aria-label="Watch live on Twitch">{TV}</a>
        <a class="art vcr" href="{YOUTUBE_URL}" target="_blank" rel="noopener" aria-label="Watch on YouTube">{VCR}</a></div>
        <div class="label"><h2>On the Telly</h2><p><a href="{TWITCH_URL}" target="_blank" rel="noopener">TV: live on Twitch</a> · <a href="{YOUTUBE_URL}" target="_blank" rel="noopener">VCR: YouTube</a></p></div>
      </div>
'''
hub+='''    </div>
  </section>
</main>
'''+'''<script>
// flick through the passport before opening it
(function(){
  document.querySelectorAll('.item-beer-passport,.item-travel-guides').forEach(function(a){
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  a.addEventListener('click',function(e){
    if(reduce||e.metaKey||e.ctrlKey||e.shiftKey||e.button) return;
    e.preventDefault(); a.classList.add('flick');
    setTimeout(function(){location.href=a.href},1350);
  });
  addEventListener('pageshow',function(){a.classList.remove('flick')});
  });
  // walk through the poster into the stadium
  document.querySelectorAll('.item-stadium').forEach(function(a){
    var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
    a.addEventListener('click',function(e){
      if(reduce||e.metaKey||e.ctrlKey||e.shiftKey||e.button) return;
      e.preventDefault(); a.classList.add('enter');
      setTimeout(function(){location.href=a.href},700);
    });
    addEventListener('pageshow',function(){a.classList.remove('enter')});
  });
})();
</script>
'''+FOOT
open('/home/claude/site/explore/index.html','w').write(hub)

def soon_page(slug,title,blurb,art,r,back,backtxt,tagtxt="Coming soon"):
    os.makedirs(f'/home/claude/site/{slug}',exist_ok=True)
    pg=HEAD.format(title=f"{title} - Rob Callery",desc=blurb,globe=globe_d,backhref=back,backtxt=backtxt)
    pg+=f'''<main>
  <section class="soon">
    <div class="art" style="--r:{r}deg">{art}</div>
    <div>
      <span class="tag">{tagtxt}</span>
      <h1>{title}</h1>
      <p>{blurb}</p>
      <a class="btn" href="{back}">{backtxt}</a>
    </div>
  </section>
</main>
'''+FOOT
    open(f'/home/claude/site/{slug}/index.html','w').write(pg)

soon_page("football-tales","Football: Tales of a Leeds Fan","Stories from Elland Road and away days up and down the country, the highs, the lows and the pubs either side, collected one card at a time. The first pack is being printed.",PACK,-2,"/stadium/","← Back to the stadium")
from pub_parts import pub_scene, leeds_tv_art, teletext_page, PUB_CSS, hub_tv_svg, leeds_tv_svg, world_tv_svg, poster_leeds, poster_world, shelf_svg, bar_top_svg
import json as _json, subprocess as _sp
_GC=_json.loads(_sp.run(['node','-e',"global.window={};require('/home/claude/site/travel-guides/guides.js');process.stdout.write(JSON.stringify(window.GUIDES.map(g=>g.city)))"],capture_output=True,text=True).stdout)
soon_page("match-hub/leeds","Leeds United Match Hub","Live scores, fixtures, the table, team news and matchday pubs for Leeds United, all on one telly. It's being wired up now.",leeds_tv_art(),0,"/match-hub/","← Back to the pub")
os.makedirs('/home/claude/site/match-hub/world',exist_ok=True)
open('/home/claude/site/match-hub/world/index.html','w').write(teletext_page(_GC))
mh=HEAD.format(title="Match Hub - Rob Callery",desc="The Match Hub pub: a Leeds United telly and a retro teletext telly showing a random live game somewhere in the world, with the local beer.",globe=globe_d,backhref="/stadium/",backtxt="← Back to the stadium")
mh=mh.replace('</style>\n</head>\n<body>', PUB_CSS+'</style>\n</head>\n<body class="pubpage">\n<div class="lamps" aria-hidden="true"><i></i><i></i><i></i></div>',1)
_pL='<a class="poster tvl" style="--r:-4deg" href="/match-hub/leeds/"><span class="sr">Leeds United match hub (coming soon)</span>'+poster_leeds()+'</a>'
_pW='<a class="poster tvl" style="--r:3deg" href="/match-hub/world/"><span class="sr">Around the World: a random live game and the local beer</span>'+poster_world()+'</a>'
mh+='''<main class="wall">
  <h1 class="sr">The Match Hub</h1>
  <div class="tier top">
    '''+_pL+'''
    <div class="hubtv">'''+hub_tv_svg()+'''</div>
    '''+_pW+'''
  </div>
  <div class="tier low">
    <a class="tvl tv-leeds" id="tvLeeds" href="/match-hub/leeds/"><span class="sr">Leeds United telly: the Leeds match hub (coming soon)</span>'''+leeds_tv_svg()+'''</a>
    <div class="shelf">'''+shelf_svg()+'''</div>
    <a class="tvl tv-world" id="tvWorld" href="/match-hub/world/"><span class="sr">Retro telly: CALFAX 302, a random live game around the world</span>'''+world_tv_svg()+'''</a>
  </div>
  <div class="tier posters">'''+_pL.replace('class="poster tvl"','class="poster tvl" aria-hidden="true" tabindex="-1"')+_pW.replace('class="poster tvl"','class="poster tvl" aria-hidden="true" tabindex="-1"')+'''</div>
</main>
<div class="pbar" aria-hidden="true"><div class="bartop">'''+bar_top_svg()+'''</div><div class="counter"></div><div class="front"></div></div>
<script>
(function(){var c=[].slice.call(document.querySelectorAll('.ttclock,.hubclock'));function t(){try{var s=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',timeZone:'Europe/London'}).format(new Date());c.forEach(function(e){e.textContent=s})}catch(e){}}t();setInterval(t,15000)})();
</script>
'''+FOOT
open('/home/claude/site/match-hub/index.html','w').write(mh)

# the stadium
os.makedirs('/home/claude/site/stadium',exist_ok=True)
st=HEAD.format(title="Elland Road - Rob Callery",desc="Step inside Elland Road: football tales from a lifetime following Leeds United, and the match hub.",globe=globe_d,backhref="/explore/",backtxt="← Back to the bar")
st+='''<main>
  <section class="intro">
    <h1>Welcome to <em>Elland Road.</em></h1>
    <p>Pick up the cards for the stories, or look up at the scoreboard for the match hub.</p>
  </section>
  <section class="stadium" aria-label="Inside the stadium">
    <svg viewBox="0 0 1200 700" role="img" aria-label="Inside Elland Road under the floodlights">
'''+stadium_scene()+scoreboard_link()+cards_link()+'''
    </svg>
  </section>
  <nav class="spots" aria-label="In the stadium">
    <a class="spot" href="/football-tales/"><h2>Football Tales</h2><p>Away days, home days and the pubs either side, one card at a time.</p></a>
    <a class="spot" href="/match-hub/"><h2>Match Hub <span class="tag">Soon</span></h2><p>Scores, fixtures and matchday, up on the big screen.</p></a>
  </nav>
</main>
<script>
(function(){
  var c=document.getElementById('sbClock'),t=document.getElementById('sbTicker'),msgs=['KICK-OFF SOON','MARCHING ON TOGETHER','MATCH HUB COMING SOON'],i=0;
  function tick(){try{c.textContent=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',timeZone:'Europe/London'}).format(new Date())}catch(e){}}
  tick();setInterval(tick,15000);
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches)setInterval(function(){i=(i+1)%msgs.length;t.textContent=msgs[i]},3000);
  // LED advertising hoardings
  var ADS=[
    {t:"MARCHING ON TOGETHER",bg:"#0a1838",fg:"#ffcd00"},
    {t:"FOLLOW ME ON X @CALZ88",bg:"#000000",fg:"#ffffff",href:"https://x.com/calz88"},
    {t:"ALL LEEDS AREN'T WE",bg:"#ffcd00",fg:"#0a1838"},
    {t:"FOLLOW ME ON INSTAGRAM @CALZ88",bg:"#c13584",fg:"#ffffff",href:"https://www.instagram.com/calz88"},
    {t:"SIDE BEFORE SELF EVERY TIME",bg:"#ffffff",fg:"#1e3f9a"},
    {t:"WATCH ON YOUTUBE @CALZ88",bg:"#c4302b",fg:"#ffffff",href:"https://www.youtube.com/@calz88"}];
  var boards=[0,1,2].map(function(k){var b=document.getElementById('board'+k);return {a:b,bg:b.querySelector('.bbg'),g:b.querySelector('.bmsg'),tx:b.querySelector('text')}});
  var step=0;
  function show(b,ad){
    b.bg.setAttribute('fill',ad.bg);b.tx.setAttribute('fill',ad.fg);b.tx.textContent=ad.t;
    b.tx.setAttribute('textLength',Math.min(360,ad.t.length*15));
    if(ad.href){b.a.setAttribute('href',ad.href);b.a.setAttribute('target','_blank');b.a.setAttribute('rel','noopener');b.a.setAttribute('aria-label',ad.t)}
    else{b.a.removeAttribute('href');b.a.removeAttribute('target');b.a.setAttribute('aria-label',ad.t)}
  }
  function paint(anim){
    boards.forEach(function(b,k){
      var ad=ADS[(step+k*2)%ADS.length];
      if(!anim){show(b,ad);return}
      setTimeout(function(){b.g.classList.add('out');setTimeout(function(){show(b,ad);b.g.classList.remove('out')},350)},k*180);
    });
  }
  paint(false);
  var still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  // players knocking the ball about (world metres -> screen, same projection as the drawing)
  (function(){
    if(still) return;
    var F=1408,FH=78565,YH=-185.6,CX=600;
    function proj(x,z,up){return [CX+F*x/z, YH+FH/z-F*(up||0)/z]}
    var host=document.getElementById('players');
    var P=[].map.call(document.querySelectorAll('.pl'),function(el,i){var x=+el.dataset.x,z=+el.dataset.z;
      return {el:el,body:el.querySelector('.body'),x:x,z:z,hx:x,hz:z,tx:x,tz:z,keeper:Math.abs(x)>45,wander:0}});
    var shadow=document.getElementById('ballShadow'),ball=document.getElementById('ballBody');
    var holder=3,recv=-1,t0=0,dur=0,from=null,to=null,loft=0,wait=performance.now()+800,last=performance.now();
    var bx=P[holder].x+.6,bz=P[holder].z,bh=0;
    function place(p){var q=proj(p.x,p.z);p.el.setAttribute('transform','translate('+q[0].toFixed(1)+' '+q[1].toFixed(1)+') scale('+(150/p.z).toFixed(2)+')')}
    function drawBall(){var g=proj(bx,bz),b=proj(bx,bz,bh),k=130/bz;
      shadow.setAttribute('cx',g[0].toFixed(1));shadow.setAttribute('cy',g[1].toFixed(1));shadow.setAttribute('rx',(5*k).toFixed(1));shadow.setAttribute('ry',(2*k).toFixed(1));
      ball.setAttribute('transform','translate('+b[0].toFixed(1)+' '+(b[1]-4*k).toFixed(1)+') scale('+k.toFixed(2)+')')}
    function pick(){var h=P[holder],c=[];
      P.forEach(function(p,i){if(i===holder)return;var d=Math.hypot(p.x-h.x,p.z-h.z);if(d<8||d>48)return;var w=p.keeper?.35:1;c.push([i,w])});
      if(!c.length)return (holder+1)%P.length;var s=c.reduce(function(a,b){return a+b[1]},0),r=Math.random()*s;
      for(var j=0;j<c.length;j++){r-=c[j][1];if(r<=0)return c[j][0]}return c[0][0]}
    function kick(p){p.body.classList.remove('kick');void p.body.getBBox();p.body.classList.add('kick')}
    function order(){var s=P.slice().sort(function(a,b){return b.z-a.z});s.forEach(function(p){host.appendChild(p.el)})}
    function frame(now){
      var dt=Math.min(.05,(now-last)/1000);last=now;
      P.forEach(function(p,i){
        if(i!==recv&&i!==holder&&now>p.wander){var r=p.keeper?2.5:6;p.tx=p.hx+(Math.random()*2-1)*r;p.tz=p.hz+(Math.random()*2-1)*r*.6;p.wander=now+2500+Math.random()*3000}
        var dx=p.tx-p.x,dz=p.tz-p.z,d=Math.hypot(dx,dz),v=(i===recv?5:2.2)*dt;
        if(d>.05){p.x+=dx/d*Math.min(v,d);p.z+=dz/d*Math.min(v,d)}
        place(p)});
      if(recv<0){                       // ball at the holder's feet
        var h=P[holder];bx=h.x+.6;bz=h.z+.2;bh=0;
        if(now>wait){recv=pick();var r=P[recv];from=[bx,bz];
          to=[r.x+(Math.random()*2-1)*1.5,r.z+(Math.random()*2-1)*1.2];r.tx=to[0]-.6;r.tz=to[1]-.2;
          var dist=Math.hypot(to[0]-from[0],to[1]-from[1]);dur=Math.max(.6,dist/15);loft=dist>26?dist*.16:0;t0=now;kick(h)}
      }else{
        var u=Math.min(1,(now-t0)/1000/dur),e=u*(2-u);
        bx=from[0]+(to[0]-from[0])*e;bz=from[1]+(to[1]-from[1])*e;bh=loft*4*u*(1-u);
        if(u>=1){holder=recv;recv=-1;wait=now+500+Math.random()*900;kick(P[holder]);P[holder].tx=P[holder].x;P[holder].tz=P[holder].z}
      }
      drawBall();order();requestAnimationFrame(frame)}
    requestAnimationFrame(frame);
  })();
  setInterval(function(){step=(step+1)%ADS.length;paint(!still)},still?8000:4500);
})();
</script>
'''+FOOT
open('/home/claude/site/stadium/index.html','w').write(st)
print("built")
