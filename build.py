#!/usr/bin/env python3
"""Builds Ayman Alawwad's static multi-page site into ./docs (served by GitHub Pages)

    python3 build.py

Texts live in content.py. Styles in assets/style.css, behaviour in assets/site.js.
"""
import html
import json
import random
import shutil
from pathlib import Path

from content import (ABOUT, CAREER, CASCADE, CONFIG, CORE_CERTS, EDUCATION, ENVIRONMENTS, FAQ,
                     FEATURED_WORK, FIGURES, FOCUS, HEADLINE, HIPO, INSTITUTIONS, INTRO, MORE_CERTS,
                     PILLARS, QUOTE, RECOGNITION, STATEMENT, WORK)

ROOT = Path(__file__).parent
OUT = ROOT / "docs"   # GitHub Pages serves /docs on main
E = html.escape
C = CONFIG
WORK_BY = {w["slug"]: w for w in WORK}
VERSION = "1"
CUR = ' aria-current="page"'

# ---------------------------------------------------------------------------
# Icons — one stroke set (24 grid, 1.6 stroke, round joins)
# ---------------------------------------------------------------------------
ICONS = {
    "home": '<path d="M3.5 10.5 12 3.8l8.5 6.7"/><path d="M5.8 9v11h12.4V9"/><path d="M10 20v-5.5h4V20"/>',
    "compass": '<circle cx="12" cy="12" r="8.6"/><path d="m15.4 8.6-2.1 4.7-4.7 2.1 2.1-4.7 4.7-2.1Z"/>',
    "career": '<rect x="3.4" y="7.2" width="17.2" height="12.6" rx="2.2"/><path d="M9 7.2V5.6a1.8 1.8 0 0 1 1.8-1.8h2.4A1.8 1.8 0 0 1 15 5.6v1.6"/><path d="M3.4 12.6h17.2"/>',
    "layers": '<path d="m12 3.6 8.6 4.7L12 13 3.4 8.3 12 3.6Z"/><path d="m3.4 12.4 8.6 4.7 8.6-4.7"/><path d="m3.4 16.4 8.6 4 8.6-4"/>',
    "award": '<circle cx="12" cy="9.2" r="5.6"/><path d="m8.6 13.8-1.5 6.6 4.9-2.7 4.9 2.7-1.5-6.6"/>',
    "mail": '<rect x="3.2" y="5.2" width="17.6" height="13.6" rx="2.2"/><path d="m3.6 7.2 8.4 6 8.4-6"/>',
    "linkedin": '<rect x="3.4" y="3.4" width="17.2" height="17.2" rx="3"/><path d="M8.2 10.4v6.4"/><path d="M8.2 7.4v.01"/><path d="M11.8 16.8v-6.4"/><path d="M11.8 13.2a2.6 2.6 0 0 1 5.2 0v3.6"/>',
    "pin": '<path d="M12 20.8s-6.6-5.8-6.6-11A6.6 6.6 0 0 1 18.6 9.8c0 5.2-6.6 11-6.6 11Z"/><circle cx="12" cy="9.8" r="2.4"/>',
    "arrow-r": '<path d="M5 12h13.6"/><path d="m13 6.4 5.6 5.6-5.6 5.6"/>',
    "arrow-l": '<path d="M19 12H5.4"/><path d="M11 6.4 5.4 12l5.6 5.6"/>',
    "sun": '<circle cx="12" cy="12" r="3.8"/><path d="M12 2.8v1.8M12 19.4v1.8M4.9 4.9l1.3 1.3M17.8 17.8l1.3 1.3M2.8 12h1.8M19.4 12h1.8M4.9 19.1l1.3-1.3M17.8 6.2l1.3-1.3"/>',
    "moon": '<path d="M19.6 14.6A7.9 7.9 0 1 1 9.4 4.4a6.3 6.3 0 0 0 10.2 10.2Z"/>',
    "chev": '<path d="m6.6 9.4 5.4 5.4 5.4-5.4"/>',
    "target": '<circle cx="12" cy="12" r="8.6"/><circle cx="12" cy="12" r="4.8"/><circle cx="12" cy="12" r="1.1"/>',
    "shield": '<path d="M12 3.4 5 6.2v5.2c0 4.4 3 8 7 9.2 4-1.2 7-4.8 7-9.2V6.2l-7-2.8Z"/><path d="m9.2 12 2 2 3.8-3.8"/>',
    "report": '<rect x="3.4" y="4" width="17.2" height="12" rx="1.8"/><path d="M12 16v4M8.4 20h7.2"/><path d="m7.4 12.2 3-3 2.6 2 3.6-3.6"/>',
    "check": '<rect x="5" y="4.2" width="14" height="16.6" rx="2"/><path d="M9.2 4.2V3h5.6v1.2"/><path d="m9 12.8 2.1 2.1 4-4"/>',
    "network": '<rect x="9" y="3.4" width="6" height="4.8" rx="1.1"/><rect x="3.4" y="15.8" width="6" height="4.8" rx="1.1"/><rect x="14.6" y="15.8" width="6" height="4.8" rx="1.1"/><path d="M12 8.2v3.8M6.4 15.8V13.4c0-.8.6-1.4 1.4-1.4h8.4c.8 0 1.4.6 1.4 1.4v2.4"/>',
    "chart": '<path d="M4 20V4"/><path d="M4 20h16"/><path d="M8.4 16.4v-4.6M12.6 16.4V8.2M16.8 16.4v-6.6"/>',
    "present": '<path d="M3.4 4.4h17.2"/><path d="M4.8 4.4v9.4a1.6 1.6 0 0 0 1.6 1.6h11.2a1.6 1.6 0 0 0 1.6-1.6V4.4"/><path d="m9 20.2 3-4.8 3 4.8"/>',
    "cap": '<path d="m2.6 9.2 9.4-4.8 9.4 4.8-9.4 4.8-9.4-4.8Z"/><path d="M6.4 11.2v4.6c0 1.4 2.5 2.8 5.6 2.8s5.6-1.4 5.6-2.8v-4.6"/><path d="M21.4 9.2v5"/>',
    "medal": '<circle cx="12" cy="14.6" r="5.2"/><path d="M8.6 10.6 6.2 3.4h3.6l2.2 4.8 2.2-4.8h3.6l-2.4 7.2"/>',
    "send": '<path d="M20.6 3.4 10.4 13.6"/><path d="m20.6 3.4-6.4 17.2-3.8-7-7-3.8 17.2-6.4Z"/>',
    "ext": '<path d="M14 4h6v6"/><path d="M20 4l-8.6 8.6"/><path d="M18 13.6v5a1.4 1.4 0 0 1-1.4 1.4H5.4A1.4 1.4 0 0 1 4 18.6V7.4A1.4 1.4 0 0 1 5.4 6h5"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "users": '<circle cx="9" cy="8.4" r="3.4"/><path d="M2.8 19.6a6.2 6.2 0 0 1 12.4 0"/><path d="M15.6 5.2a3.3 3.3 0 0 1 0 6.4"/><path d="M21.2 19.6a6.2 6.2 0 0 0-3.8-5.7"/>',
}


def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


def diamond(cls="dm"):
    return f'<svg class="{cls}" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M6 .8 11.2 6 6 11.2.8 6Z"/></svg>'


# ---------------------------------------------------------------------------
# Concept background: a portfolio roadmap drafted in ink on linen
# ---------------------------------------------------------------------------
def plan_svg(seed=7, lanes=7, w=1200, h=660, cls="plan"):
    rnd = random.Random(seed)
    parts = []
    # drafting grid
    grid = []
    for x in range(0, w + 1, 60):
        grid.append(f'<path d="M{x} 0V{h}"/>')
    for y in range(0, h + 1, 60):
        grid.append(f'<path d="M0 {y}H{w}"/>')
    parts.append(f'<g class="pl-grid">{"".join(grid)}</g>')
    # lanes
    top, gap = 90, (h - 150) / (lanes - 1)
    x1 = rnd.randint(40, 120)
    bars, dias, deps, bases = [], [], [], []
    prev = None
    for i in range(lanes):
        y = round(top + i * gap)
        ln = rnd.randint(230, 430)
        if x1 + ln > w - 60:
            x1 = rnd.randint(60, 260)
        x2 = x1 + ln
        bases.append(f'<path d="M0 {y}H{w}"/>')
        d = i * 0.22
        bars.append(f'<path d="M{x1 + 6} {y - 6}H{x2 - 6}a6 6 0 0 1 0 12H{x1 + 6}a6 6 0 0 1 0-12Z" pathLength="1" style="--d:{d:.2f}s"/>')
        filled = " is-f" if i % 3 != 1 else ""
        dias.append(f'<path class="pl-dia{filled}" d="M{x2 + 22} {y - 8}l8 8-8 8-8-8Z" style="--d:{d + 0.9:.2f}s;--b:{rnd.uniform(0, 4):.2f}s"/>')
        if prev:
            px2, py = prev
            deps.append(f'<path d="M{px2 + 22} {py + 9}V{y - 18}H{x1 - 14}V{y - 8}" pathLength="1" style="--d:{d + 0.6:.2f}s"/>')
        prev = (x2, y)
        x1 = x1 + rnd.randint(90, 230)
    parts.append(f'<g class="pl-base">{"".join(bases)}</g>')
    parts.append(f'<g class="pl-dep">{"".join(deps)}</g>')
    parts.append(f'<g class="pl-bar">{"".join(bars)}</g>')
    parts.append(f'<g class="pl-dias">{"".join(dias)}</g>')
    sx = int(w * 0.62)
    parts.append(f'<g class="pl-status"><path d="M{sx} 34V{h - 20}"/><path class="pl-flag" d="M{sx} 22l7 7-7 7-7-7Z"/></g>')
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" '
            f'focusable="false"><g class="pl-drift">{"".join(parts)}</g></svg>')


def corner_marks():
    return ('<span class="cm cm-tl" aria-hidden="true"></span><span class="cm cm-tr" aria-hidden="true"></span>'
            '<span class="cm cm-bl" aria-hidden="true"></span><span class="cm cm-br" aria-hidden="true"></span>')


# ---------------------------------------------------------------------------
# Shared chrome
# ---------------------------------------------------------------------------
NAV = [
    ("index", "Home", "home", ""),
    ("leadership", "Leadership", "compass", "leadership.html"),
    ("career", "Career", "career", "career.html"),
    ("work", "Work", "layers", "work.html"),
    ("credentials", "Credentials", "award", "credentials.html"),
]


def url(path):
    base = C["BASE_URL"].rstrip("/")
    return f"{base}/{path}" if base else ""


def person_ld():
    alt = ["Ayman Alawwad", "Ayman Al-Awwad", "Ayman AlAwwad", "Ayman Al Awwad", "Ayman Alawad", "Ayman Al-Awad",
           "Aiman Alawwad", "Ayman Alowad", "أيمن العواد", "ايمن العواد", "أيمن عواد"]
    creds = [{"@type": "EducationalOccupationalCredential", "name": f'{c["name"]} ({c["abbr"]})',
              "credentialCategory": "Professional certification",
              "recognizedBy": {"@type": "Organization", "name": c["issuer"]}} for c in CORE_CERTS]
    creds += [{"@type": "EducationalOccupationalCredential", "name": c["name"],
               "credentialCategory": "Certificate", "recognizedBy": {"@type": "Organization", "name": c["issuer"]}}
              for c in MORE_CERTS]
    creds += [{"@type": "EducationalOccupationalCredential", "name": m["name"],
               "credentialCategory": "Executive education", "recognizedBy": {"@type": "CollegeOrUniversity", "name": m["inst"]}}
              for m in HIPO["modules"]]
    occ = [{"@type": "Occupation", "name": n, "occupationLocation": {"@type": "Country", "name": "Saudi Arabia"}}
           for n in ["PMO Manager", "Portfolio Manager", "Program Manager", "Project Manager",
                     "مدير مكتب إدارة المشاريع", "مدير المحافظ", "مدير البرامج", "مدير مشاريع"]]
    d = {
        "@context": "https://schema.org", "@type": "Person", "name": C["NAME"], "alternateName": alt,
        "jobTitle": "PMO Manager", "description": f"{HEADLINE}. {STATEMENT} {INTRO}",
        "hasOccupation": occ,
        "knowsAbout": ["PMO establishment", "PMO governance", "Portfolio management", "Program management",
                       "Project management", "Strategy execution", "Strategic alignment", "Prioritization",
                       "Executive reporting", "RAID management", "Risk management", "Stakeholder management",
                       "Hybrid project delivery", "Agile", "Waterfall", "Vendor management", "OKR", "KPI",
                       "Saudi Building Code", "Infrastructure projects", "Government projects",
                       "إدارة المحافظ", "حوكمة المشاريع", "مكتب إدارة المشاريع"],
        "hasCredential": creds,
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Imam Mohammad Ibn Saud Islamic University",
                     "alternateName": ["IMSIU", "جامعة الإمام محمد بن سعود الإسلامية"]},
        "knowsLanguage": ["ar", "en"],
        "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"},
        "sameAs": [C["LINKEDIN"]],
    }
    if C["EMAIL"]:
        d["email"] = f'mailto:{C["EMAIL"]}'
    if C["PHOTO"] and C["BASE_URL"]:
        d["image"] = url(C["PHOTO"])
    if C["BASE_URL"]:
        d["url"] = url("")
    return d


def head(title, desc, path, root, extra_ld=None):
    ld = [person_ld()] + (extra_ld or [])
    robots = '<meta name="robots" content="noindex, nofollow">' if C["PREVIEW"] else '<meta name="robots" content="index, follow, max-image-preview:large">'
    canon = f'<link rel="canonical" href="{url(path)}">' if C["BASE_URL"] else ""
    og_img = f'<meta property="og:image" content="{url("assets/img/og.jpg")}">' if C["BASE_URL"] else \
        f'<meta property="og:image" content="{root}assets/img/og.jpg">'
    og_url = f'<meta property="og:url" content="{url(path)}">' if C["BASE_URL"] else ""
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f"""<!doctype html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{robots}
{canon}
<meta name="theme-color" content="#F1ECE4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121417" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="profile">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
{og_url}
{og_img}
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{root}assets/fonts/newsreader-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}assets/fonts/public-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/style.css?v={VERSION}">
<script>try{{var t=localStorage.getItem('aa-theme');if(t==='dark'||t==='light')document.documentElement.dataset.theme=t}}catch(e){{}}document.documentElement.classList.add('js')</script>
{lds}
</head>"""


def header(active, root):
    links = "".join(
        f'<a class="nav-a{" is-on" if k == active else ""}" href="{root}{h or "index.html"}"'
        f'{CUR if k == active else ""}>{E(lbl)}</a>'
        for k, lbl, _, h in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"><span></span></div>
<header class="hdr" id="hdr">
  <div class="hdr-in wrap">
    <a class="brand" href="{root}index.html" aria-label="{E(C['NAME'])} — home">
      <span class="mono" aria-hidden="true"><span>AA</span></span>
      <span class="brand-t"><span class="brand-n">{E(C['NAME'])}</span><span class="brand-r">PMO &amp; Portfolio Leadership</span></span>
    </a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <div class="hdr-act">
      <button class="icon-btn theme-btn" type="button" aria-label="Switch to dark theme" data-theme-toggle>
        <span class="swap">{icon("moon", "ic t-moon")}{icon("sun", "ic t-sun")}</span>
      </button>
      <a class="btn btn-ink btn-sm hdr-cta{" is-on" if active == "contact" else ""}" href="{root}contact.html">Contact</a>
      <a class="icon-btn hdr-mail" href="{root}contact.html" aria-label="Contact">{icon("mail")}</a>
    </div>
  </div>
</header>"""


def detail_bar(title, root, back_href, back_label):
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"><span></span></div>
<header class="hdr hdr-detail" id="hdr">
  <div class="hdr-in wrap">
    <a class="back" href="{back_href}" aria-label="Back to {E(back_label)}">{icon("arrow-l")}<span>{E(back_label)}</span></a>
    <span class="bar-title" aria-hidden="true">{E(title)}</span>
    <a class="brand brand-d" href="{root}index.html" aria-label="{E(C['NAME'])} — home">
      <span class="mono" aria-hidden="true"><span>AA</span></span>
      <span class="brand-t"><span class="brand-n">{E(C['NAME'])}</span><span class="brand-r">PMO &amp; Portfolio Leadership</span></span>
    </a>
    <div class="hdr-act">
      <button class="icon-btn theme-btn" type="button" aria-label="Switch to dark theme" data-theme-toggle>
        <span class="swap">{icon("moon", "ic t-moon")}{icon("sun", "ic t-sun")}</span>
      </button>
      <a class="btn btn-ink btn-sm hdr-cta" href="{root}contact.html">Contact</a>
    </div>
  </div>
</header>"""


def dock(active, root):
    items = "".join(
        f'<a class="dock-a{" is-on" if k == active else ""}" href="{root}{h or "index.html"}"'
        f'{CUR if k == active else ""}>{icon(ic)}<span>{E(lbl)}</span></a>'
        for k, lbl, ic, h in NAV)
    return f'<nav class="dock" aria-label="Main (mobile)"><div class="dock-in">{items}</div></nav>'


def footer(root):
    cards = []
    if C["EMAIL"]:
        cards.append(f'<a class="fc" href="mailto:{E(C["EMAIL"])}"><span class="fc-i">{icon("mail")}</span>'
                     f'<span class="fc-t"><span class="fc-k">Email</span><span class="fc-v" dir="ltr">{email_wbr()}</span></span></a>')
    if C["LINKEDIN"]:
        cards.append(f'<a class="fc" href="{E(C["LINKEDIN"])}" target="_blank" rel="noopener"><span class="fc-i">{icon("linkedin")}</span>'
                     f'<span class="fc-t"><span class="fc-k">LinkedIn</span><span class="fc-v" dir="ltr">ayman-alawwad</span></span></a>')
    if C["PHONE"]:
        cards.append(f'<a class="fc" href="tel:{E(C["PHONE"])}"><span class="fc-i">{icon("send")}</span>'
                     f'<span class="fc-t"><span class="fc-k">Phone</span><span class="fc-v" dir="ltr">{E(C["PHONE"])}</span></span></a>')
    cards.append(f'<div class="fc fc-static"><span class="fc-i">{icon("pin")}</span>'
                 f'<span class="fc-t"><span class="fc-k">Based in</span><span class="fc-v">{E(C["LOCATION"])}</span></span></div>')
    preview = '<span class="ft-note">Private preview · not indexed</span>' if C["PREVIEW"] else ""
    return f"""<footer class="ftr">
  <div class="wrap">
    <div class="ft-top">
      <div class="ft-id">
        <span class="mono mono-lg" aria-hidden="true"><span>AA</span></span>
        <div><p class="ft-n">{E(C['NAME'])}</p><p class="ft-r">{E(HEADLINE)}</p></div>
      </div>
      <div class="fcs">{''.join(cards)}</div>
    </div>
    <div class="ft-bot">
      <span>© <span dir="ltr">2026</span> {E(C['NAME'])}</span>
      {preview}
      <span class="maker">Design &amp; development · <a href="{C['MAKER']}" target="_blank" rel="noopener"><span lang="ar" dir="rtl">نور الدين طفي</span></a> · <a href="{C['MAKER']}" target="_blank" rel="noopener">Nour Aldeen Tofi</a></span>
    </div>
  </div>
</footer>"""


def page(key, title, desc, path, body, root="", detail=None, extra_ld=None):
    top = detail_bar(*detail) if detail else header(key, root)
    return f"""{head(title, desc, path, root, extra_ld)}
<body class="pg-{key}{' is-detail' if detail else ''}">
{top}
<main id="main">
{body}
</main>
{footer(root)}
{dock(key if not detail else "work", root)}
<script src="{root}assets/site.js?v={VERSION}" defer></script>
</body>
</html>
"""


def portrait(root, cls="portrait", eager=True):
    if C["PHOTO"]:
        load = 'fetchpriority="high"' if eager else 'loading="lazy"'
        return (f'<picture class="{cls}"><source srcset="{root}{C["PHOTO_WEBP"]}" type="image/webp">'
                f'<img src="{root}{C["PHOTO"]}" width="630" height="630" alt="Portrait of {E(C["NAME"])}" {load} decoding="async"></picture>')
    return f'<div class="{cls} portrait-mono" role="img" aria-label="{E(C["NAME"])}"><span>AA</span></div>'


def email_wbr():
    return E(C["EMAIL"]).replace("@", "@<wbr>")


def kicker(text):
    return f'<p class="kick">{diamond()}<span>{E(text)}</span></p>'


def page_head(kick, title, lead, seed):
    return f"""<section class="phead">
  <div class="phead-bg" aria-hidden="true">{plan_svg(seed=seed, lanes=6, h=520, cls="plan plan-sm")}</div>
  <div class="wrap phead-in">
    {kicker(C["NAME"])}
    <h1 class="ptitle">{title}</h1>
    <p class="plead rv">{E(lead)}</p>
  </div>
</section>"""


def figure_html(f):
    return (f'<div class="fig rv"><p class="fig-n" aria-label="{E(f["pre"])}{f["num"]}{E(f["suf"])}">'
            f'<span class="fig-pre">{E(f["pre"])}</span><span class="count" data-to="{f["num"]}" '
            f'style="--w:{len(str(f["num"]))}ch">{f["num"]}</span><span class="fig-suf">{E(f["suf"])}</span></p>'
            f'<p class="fig-l">{E(f["label"])}</p></div>')


def work_card(w, root, cls=""):
    return f"""<a class="card wcard {cls} rv" href="{root}work/{w['slug']}.html">
  <span class="wc-fig"><span class="wc-n">{E(w['fig'])}</span><span class="wc-l">{E(w['fig_label'])}</span></span>
  <span class="wc-t">{E(w['title'])}</span>
  <span class="wc-s">{E(w['summary'])}</span>
  <span class="wc-meta"><span>{E(w['org'])}</span><span dir="ltr">{E(w['years'])}</span></span>
  <span class="wc-go" aria-hidden="true">{icon("arrow-r")}</span>
</a>"""


def seal(c):
    return f"""<div class="card seal rv">
  <div class="seal-mark" aria-hidden="true">
    <svg viewBox="0 0 120 120"><circle class="s-o" cx="60" cy="60" r="56"/><circle class="s-i" cx="60" cy="60" r="47"/>
    <path class="s-d" d="M60 7l3 3-3 3-3-3Z"/><path class="s-d" d="M60 107l3 3-3 3-3-3Z"/></svg>
    <span class="seal-a">{E(c['abbr'])}<sup>®</sup></span>
  </div>
  <p class="seal-n">{E(c['name'])}</p>
  <p class="seal-i">{E(c['issuer'])}</p>
  <p class="seal-y"><span dir="ltr">{E(c['year'])}</span></p>
</div>"""


def swipe(items_html, cls, label):
    return (f'<div class="swipe {cls}" data-swipe aria-label="{E(label)}" role="region">'
            f'<div class="swipe-row">{items_html}</div><div class="dots" aria-hidden="true"></div></div>')


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def home():
    r = ""
    figs = "".join(figure_html(f) for f in FIGURES)
    pillars = "".join(
        f'<article class="card pillar rv"><span class="tile">{icon(p["icon"])}</span>'
        f'<h3 class="pl-t">{E(p["title"])}</h3><p class="pl-x">{E(p["text"])}</p>'
        f'<p class="pl-p"><span class="pl-pk">In practice</span>{E(p["proof"])}</p></article>'
        for p in PILLARS)
    order = sorted(CAREER, key=lambda c: c["years"][:4])
    def track(c):
        rs = c["roles"]
        return rs[0]["title"] if len(rs) == 1 else f'{rs[-1]["title"]} → {rs[0]["title"]}'
    stops = "".join(
        f'<li class="ct-stop rv"><span class="ct-dot">{diamond()}</span><span class="ct-y" dir="ltr">{E(c["years"])}</span>'
        f'<span class="ct-o">{E(c["org"])}</span><span class="ct-r">{E(track(c))}</span></li>'
        for c in order)
    featured = "".join(work_card(WORK_BY[s], r) for s in FEATURED_WORK)
    seals = "".join(seal(c) for c in CORE_CERTS)
    inst = "".join(f'<li>{E(i)}</li>' for i in INSTITUTIONS)
    body = f"""
<section class="hero">
  <div class="hero-bg" aria-hidden="true">{plan_svg(seed=11)}</div>
  <div class="wrap hero-in">
    <div class="hero-txt">
      <p class="hero-k e1">{E(HEADLINE)}</p>
      <h1 class="hero-n e2 ptitle">{E(C['NAME'])}</h1>
      <p class="hero-s e3">{E(STATEMENT)}</p>
      <p class="hero-p e4">{E(INTRO)}</p>
      <div class="hero-cta e5">
        <a class="btn btn-ink btn-shine" href="career.html">Explore the career {icon("arrow-r")}</a>
        <a class="btn btn-ghost" href="contact.html">Get in touch</a>
      </div>
      <p class="hero-loc e6">{icon("pin")}<span>{E(C['LOCATION'])}</span></p>
    </div>
    <div class="hero-media e3">
      <div class="frame">
        {corner_marks()}
        <div class="frame-img">{portrait(r)}</div>
      </div>
      <div class="glass gcard gc-a">
        <span class="gc-i">{icon("award")}</span>
        <span><span class="gc-t">PMP® · P3O® · PMI-RMP®</span><span class="gc-s">Project, portfolio &amp; risk</span></span>
      </div>
      <div class="glass gcard gc-b">
        <span class="gc-n">SAR 500M+</span><span class="gc-s">Projects &amp; portfolios delivered</span>
      </div>
    </div>
  </div>
</section>

<section class="figs" aria-label="Signature figures">
  <div class="wrap figs-in">{figs}</div>
</section>

<section class="sec">
  <div class="wrap intro">
    <div class="intro-h">
      {kicker("Profile")}
      <h2 class="h2 rv">Hands-on delivery, governed at portfolio level.</h2>
    </div>
    <div class="intro-b">
      <p class="lead rv">{E(ABOUT[1])}</p>
      <p class="rv">{E(ABOUT[2])}</p>
      <a class="tlink rv" href="leadership.html">How Ayman leads {icon("arrow-r")}</a>
    </div>
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap">
    <div class="sec-h">
      {kicker("Capabilities")}
      <h2 class="h2 rv">Where Ayman adds the most value.</h2>
    </div>
    {swipe(pillars, "grid-3", "Capabilities")}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h sec-h-row">
      <div>{kicker("Career")}<h2 class="h2 rv">A decade, from site quality to portfolio governance.</h2></div>
      <a class="tlink rv" href="career.html">Full career {icon("arrow-r")}</a>
    </div>
    <ol class="ctrack">{stops}</ol>
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap">
    <div class="sec-h sec-h-row">
      <div>{kicker("Selected work")}<h2 class="h2 rv">Delivery with measurable outcomes.</h2></div>
      <a class="tlink rv" href="work.html">All engagements {icon("arrow-r")}</a>
    </div>
    {swipe(featured, "grid-3", "Selected work")}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h sec-h-row">
      <div>{kicker("Credentials")}<h2 class="h2 rv">Certified across project, portfolio and risk.</h2></div>
      <a class="tlink rv" href="credentials.html">All credentials {icon("arrow-r")}</a>
    </div>
    <div class="seals">{seals}</div>
    <div class="exec rv">
      <p class="exec-k">Executive education</p>
      <ul class="exec-l">{inst}</ul>
    </div>
  </div>
</section>

{quote_block()}
{cta_block(r)}
"""
    return page("index", f"{C['NAME']} — PMO Manager · Portfolio & Program Management",
                f"{C['NAME']} — {HEADLINE}. {STATEMENT} PMP®, P3O®, PMI-RMP® certified, based in Riyadh.",
                "", body, extra_ld=[website_ld()])


def quote_block():
    lines = "".join(f'<span class="q-l">{E(l)}</span>' for l in QUOTE["lines"])
    return f"""<section class="qsec">
  <div class="wrap">
    <figure class="quote rv">
      <svg class="q-mark" viewBox="0 0 48 36" aria-hidden="true"><path d="M0 36V22C0 9 7 2 19 0l2 5c-7 2-10 7-10 13h9v18H0Zm27 0V22c0-13 7-20 19-22l2 5c-7 2-10 7-10 13h9v18H27Z"/></svg>
      <blockquote><p>{lines}<span class="q-p">{E(QUOTE["punch"])}</span></p></blockquote>
      <figcaption>— {E(QUOTE["cite"])}</figcaption>
    </figure>
  </div>
</section>"""


def cta_block(root):
    return f"""<section class="sec cta-sec">
  <div class="cta-bg" aria-hidden="true">{plan_svg(seed=31, lanes=6, h=520, cls="plan plan-sm")}</div>
  <div class="wrap">
    <div class="cta glass rv">
      <div class="cta-in">
        <h2 class="h2">Start a conversation.</h2>
        <p>The most direct route to Ayman is email or LinkedIn.</p>
        <div class="cta-b">
          <a class="btn btn-ink btn-shine" href="{root}contact.html">Get in touch {icon("arrow-r")}</a>
          <a class="btn btn-ghost" href="{E(C['LINKEDIN'])}" target="_blank" rel="noopener">{icon("linkedin")} LinkedIn</a>
        </div>
      </div>
    </div>
  </div>
</section>"""


def website_ld():
    d = {"@context": "https://schema.org", "@type": "ProfilePage", "name": f"{C['NAME']} — official site",
         "mainEntity": {"@type": "Person", "name": C["NAME"]}, "inLanguage": "en"}
    if C["BASE_URL"]:
        d["url"] = url("")
    return d


def leadership():
    about = "".join(f'<p class="rv{" lead" if i == 0 else ""}">{E(p)}</p>' for i, p in enumerate(ABOUT))
    casc = "".join(
        f'<li class="cs rv" style="--i:{i}"><span class="cs-n" dir="ltr">{i + 1:02d}</span>'
        f'<span class="cs-l">{E(c["level"])}</span><span class="cs-t">{E(c["text"])}</span></li>'
        for i, c in enumerate(CASCADE))
    pillars = "".join(
        f'<article class="card pillar rv"><span class="tile">{icon(p["icon"])}</span>'
        f'<h3 class="pl-t">{E(p["title"])}</h3><p class="pl-x">{E(p["text"])}</p>'
        f'<p class="pl-p"><span class="pl-pk">In practice</span>{E(p["proof"])}</p></article>'
        for p in PILLARS)
    env = "".join(f'<li>{E(x)}</li>' for x in ENVIRONMENTS)
    foc = "".join(f'<li>{E(x)}</li>' for x in FOCUS)
    body = f"""{page_head("Leadership", "Leadership", "Hands-on project delivery combined with portfolio-level governance — bridging strategy and execution.", 21)}
<section class="sec">
  <div class="wrap intro">
    <div class="intro-h">
      <div class="frame frame-sm rv">{corner_marks()}<div class="frame-img">{portrait("", eager=False)}</div></div>
    </div>
    <div class="intro-b">{about}</div>
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap">
    <div class="sec-h">
      {kicker("Governance architecture")}
      <h2 class="h2 rv">From strategy to operational readiness.</h2>
      <p class="sec-p rv">How the work connects across portfolio, program and project offices — the model behind Ayman's P3O® practice.</p>
    </div>
    <ol class="cascade">{casc}</ol>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h">
      {kicker("Capabilities")}
      <h2 class="h2 rv">Six areas of leadership.</h2>
    </div>
    {swipe(pillars, "grid-3", "Capabilities")}
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap two">
    <div class="card lst rv">
      <span class="tile">{icon("network")}</span>
      <h3 class="pl-t">Environments</h3>
      <ul class="chips">{env}</ul>
    </div>
    <div class="card lst rv">
      <span class="tile">{icon("target")}</span>
      <h3 class="pl-t">Focus in every engagement</h3>
      <ul class="chips">{foc}</ul>
    </div>
  </div>
</section>

{quote_block()}
{cta_block("")}
"""
    return page("leadership", f"Leadership — {C['NAME']}",
                f"How {C['NAME']} leads: PMO governance, portfolio and program management, strategy execution, RAID management and executive reporting.",
                "leadership.html", body)


def career():
    blocks = []
    for ci, c in enumerate(CAREER):
        roles = []
        for ri, ro in enumerate(c["roles"]):
            pts = "".join(f"<li>{E(p)}</li>" for p in ro["points"])
            rid = f"r{ci}{ri}"
            roles.append(f"""<div class="role">
  <div class="role-h"><h4 class="role-t">{E(ro['title'])}</h4><span class="role-y" dir="ltr">{E(ro['years'])}</span></div>
  <button class="more-btn" type="button" aria-expanded="false" aria-controls="{rid}"><span class="mb-sw"><span class="mb-a">Show details</span><span class="mb-b">Hide details</span></span>{icon("chev")}</button>
  <div class="more" id="{rid}"><div class="more-in"><ul class="pts">{pts}</ul></div></div>
</div>""")
        honour = (f'<p class="honour">{icon("medal")}<span>{E(c["honour"])}</span></p>' if c.get("honour") else "")
        blocks.append(f"""<li class="tl-i rv">
  <span class="tl-dot" aria-hidden="true">{diamond()}</span>
  <article class="card tl-c">
    <header class="tl-h">
      <div><h3 class="tl-o">{E(c['org'])}</h3><p class="tl-s">{E(c['summary'])}</p></div>
      <p class="tl-y"><span dir="ltr">{E(c['years'])}</span><span class="tl-p">{E(c['place'])}</span></p>
    </header>
    {''.join(roles)}
    {honour}
  </article>
</li>""")
    ed = EDUCATION
    body = f"""{page_head("Career", "Career", "Ten years of progression — from quality assurance on site to project management, PMO foundations and national-scale programs.", 41)}
<section class="sec">
  <div class="wrap">
    <ol class="tl">{''.join(blocks)}</ol>
    <div class="card edu rv">
      <span class="tile">{icon("cap")}</span>
      <div><h3 class="pl-t">{E(ed['degree'])}</h3><p class="edu-s">{E(ed['school'])}</p></div>
      <p class="edu-y" dir="ltr">{E(ed['years'])}</p>
    </div>
  </div>
</section>
{cta_block("")}
"""
    return page("career", f"Career — {C['NAME']}",
                f"{C['NAME']}'s career: TAHAKOM, Tatweer Buildings Company, Khazaz Engineering Office and The Royal Commission for Riyadh City.",
                "career.html", body)


def work_index():
    cards = "".join(work_card(w, "") for w in WORK)
    body = f"""{page_head("Work", "Selected work", "Programs, projects and PMO initiatives — each with its scope, role and outcomes.", 51)}
<section class="sec">
  <div class="wrap">
    <div class="wgrid">{cards}</div>
  </div>
</section>
{cta_block("")}
"""
    return page("work", f"Selected work — {C['NAME']}",
                f"Selected programs and projects led by {C['NAME']}: nationwide violation detection rollout, SAR 28M infrastructure rehabilitation, supplier standardization and more.",
                "work.html", body)


def work_detail(i, w):
    root = "../"
    prev_w = WORK[(i - 1) % len(WORK)]
    next_w = WORK[(i + 1) % len(WORK)]
    outs = "".join(f'<li class="rv">{diamond()}<span>{E(o)}</span></li>' for o in w["outcomes"])
    tags = "".join(f'<li>{E(t)}</li>' for t in w["tags"])
    body = f"""<section class="phead phead-d">
  <div class="phead-bg" aria-hidden="true">{plan_svg(seed=60 + i, lanes=6, h=520, cls="plan plan-sm")}</div>
  <div class="wrap phead-in">
    {kicker(w['org'])}
    <h1 class="ptitle rv">{E(w['title'])}</h1>
    <dl class="facts rv">
      <div><dt>Period</dt><dd dir="ltr">{E(w['years'])}</dd></div>
      <div><dt>Role</dt><dd>{E(w['role'])}</dd></div>
      <div><dt>Organization</dt><dd>{E(w['org'])}</dd></div>
    </dl>
  </div>
</section>
<section class="sec sec-first">
  <div class="wrap det">
    <div class="det-main">
      <h2 class="h3 rv">Scope</h2>
      <p class="lead rv">{E(w['summary'])}</p>
      <h2 class="h3 rv">Outcomes</h2>
      <ul class="outs">{outs}</ul>
    </div>
    <aside class="det-side">
      <div class="inkcard keyfig rv">
        <p class="kf-n">{E(w['fig'])}</p>
        <p class="kf-l">{E(w['fig_label'])}</p>
      </div>
      <div class="card det-tags rv">
        <h2 class="h4">Capabilities applied</h2>
        <ul class="chips">{tags}</ul>
      </div>
    </aside>
  </div>
</section>
<nav class="sec pn" aria-label="More work">
  <div class="wrap pn-in">
    <a class="card pn-a rv" href="{prev_w['slug']}.html">{icon("arrow-l")}<span><span class="pn-k">Previous</span><span class="pn-t">{E(prev_w['short'])}</span></span></a>
    <a class="card pn-a pn-next rv" href="{next_w['slug']}.html"><span><span class="pn-k">Next</span><span class="pn-t">{E(next_w['short'])}</span></span>{icon("arrow-r")}</a>
  </div>
</nav>
"""
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", **({"item": url("")} if C["BASE_URL"] else {})},
        {"@type": "ListItem", "position": 2, "name": "Work", **({"item": url("work.html")} if C["BASE_URL"] else {})},
        {"@type": "ListItem", "position": 3, "name": w["title"]}]}
    return page("work", f"{w['title']} — {C['NAME']}", f"{w['summary']}", f"work/{w['slug']}.html", body,
                root=root, detail=(w["short"], root, "../work.html", "Work"), extra_ld=[crumbs])


def credentials():
    seals = "".join(seal(c) for c in CORE_CERTS)
    more = "".join(
        f'<article class="card cert rv"><span class="tile">{icon(c["icon"])}</span>'
        f'<div class="cert-b"><h3 class="cert-n">{E(c["name"])}</h3><p class="cert-i">{E(c["issuer"])}</p></div>'
        f'<p class="cert-y" dir="ltr">{E(c["year"])}</p></article>' for c in MORE_CERTS)
    mods = "".join(
        f'<li class="card mod rv"><span class="mod-w" dir="ltr">{E(m["when"])}</span>'
        f'<h4 class="mod-n">{E(m["name"])}</h4><p class="mod-i">{E(m["inst"])}</p></li>' for m in HIPO["modules"])
    ed = EDUCATION
    body = f"""{page_head("Credentials", "Credentials", "Professional certifications, executive education and recognition.", 71)}
<section class="sec">
  <div class="wrap">
    <div class="sec-h">{kicker("Professional certifications")}<h2 class="h2 rv">Project, risk and portfolio offices.</h2></div>
    <div class="seals">{seals}</div>
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap">
    <div class="sec-h">{kicker("Leadership development")}<h2 class="h2 rv">{E(HIPO['title'])}</h2>
      <p class="sec-p rv">{E(HIPO['selected'])}</p></div>
    <div class="hipo">
      <div class="inkcard hipo-k rv">
        <p class="hk-n"><span dir="ltr">60</span><span class="hk-of">of</span><span dir="ltr">1,200</span></p>
        <p class="hk-l">candidates selected</p>
        <p class="hk-g">{icon("cap")}<span>{E(HIPO['graduated'])}</span></p>
      </div>
      <ol class="mods">{mods}</ol>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h">{kicker("Further certifications")}<h2 class="h2 rv">Performance, data and communication.</h2></div>
    <div class="certs">{more}</div>
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap two">
    <div class="card lst rv">
      <span class="tile">{icon("cap")}</span>
      <h3 class="pl-t">Education</h3>
      <p class="lst-v">{E(ed['degree'])}</p>
      <p class="lst-s">{E(ed['school'])} · <span dir="ltr">{E(ed['years'])}</span></p>
    </div>
    <div class="card lst rv">
      <span class="tile">{icon("medal")}</span>
      <h3 class="pl-t">Recognition</h3>
      <p class="lst-v">{E(RECOGNITION.split(' — ')[0])}</p>
      <p class="lst-s">{E(RECOGNITION.split(' — ')[1])}</p>
    </div>
  </div>
</section>
{cta_block("")}
"""
    return page("credentials", f"Credentials — {C['NAME']}",
                f"{C['NAME']}'s credentials: PMP®, PMI-RMP®, P3O®, OKR and KPI certifications, and executive education from MIT, NUS, ESCP and Kellogg.",
                "credentials.html", body)


def contact():
    faq = "".join(
        f'<details class="card qa rv"><summary><span>{E(q)}</span>{icon("plus", "ic qa-i")}</summary><div class="qa-a"><p>{E(a)}</p></div></details>'
        for q, a in FAQ)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    routes = []
    if C["EMAIL"]:
        routes.append(f'<a class="card route rv" href="mailto:{E(C["EMAIL"])}"><span class="tile">{icon("mail")}</span>'
                      f'<span class="rt-b"><span class="rt-k">Email</span><span class="rt-v" dir="ltr">{email_wbr()}</span></span>{icon("arrow-r", "ic rt-go")}</a>')
    if C["LINKEDIN"]:
        routes.append(f'<a class="card route rv" href="{E(C["LINKEDIN"])}" target="_blank" rel="noopener"><span class="tile">{icon("linkedin")}</span>'
                      f'<span class="rt-b"><span class="rt-k">LinkedIn</span><span class="rt-v">Message Ayman on LinkedIn</span></span>{icon("ext", "ic rt-go")}</a>')
    routes.append(f'<div class="card route route-s rv"><span class="tile">{icon("pin")}</span>'
                  f'<span class="rt-b"><span class="rt-k">Based in</span><span class="rt-v">{E(C["LOCATION"])}</span></span></div>')
    form = ""
    if C["EMAIL"]:
        form = f"""<form class="card form rv" id="cform" data-email="{E(C['EMAIL'])}" novalidate>
  <h2 class="h3">Write to Ayman</h2>
  <p class="form-p">Your message opens in your email app, ready to send.</p>
  <div class="fld"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" enterkeyhint="next" required></div>
  <div class="fld"><label for="f-org">Organization <span class="opt">(optional)</span></label><input id="f-org" name="org" type="text" autocomplete="organization" enterkeyhint="next"></div>
  <div class="fld"><label for="f-msg">Message</label><textarea id="f-msg" name="msg" rows="5" required></textarea></div>
  <p class="form-err" id="f-err" role="alert" aria-live="polite"></p>
  <button class="btn btn-ink btn-shine btn-full" type="submit">{icon("send")} Compose email</button>
</form>"""
    body = f"""{page_head("Contact", "Contact", "The most direct route to Ayman is email or LinkedIn.", 81)}
<section class="sec">
  <div class="wrap ct-grid">
    <div class="routes">{''.join(routes)}</div>
    {form}
  </div>
</section>
<section class="sec sec-tint">
  <div class="wrap faq-w">
    <div class="sec-h">{kicker("At a glance")}<h2 class="h2 rv">Frequently asked</h2></div>
    <div class="faq">{faq}</div>
  </div>
</section>
"""
    return page("contact", f"Contact — {C['NAME']}",
                f"Contact {C['NAME']}, PMO Manager in Riyadh — by email or LinkedIn.", "contact.html", body,
                extra_ld=[faq_ld])


# ---------------------------------------------------------------------------
# Machine-readable files
# ---------------------------------------------------------------------------
def llms_txt():
    base = C["BASE_URL"].rstrip("/")
    def u(p):
        return f"{base}/{p}" if base else p
    lines = [f"# {C['NAME']}", "", f"> {HEADLINE}. {STATEMENT} {INTRO}", "",
             "Also written: Ayman Al-Awwad, Ayman AlAwwad, Ayman Alawad, أيمن العواد.", "",
             "## Pages",
             f"- [Home]({u('index.html')}): overview, signature figures, capabilities, career, selected work, credentials",
             f"- [Leadership]({u('leadership.html')}): approach, governance architecture, six capability areas",
             f"- [Career]({u('career.html')}): roles at TAHAKOM, Tatweer Buildings Company, Khazaz Engineering Office, Royal Commission for Riyadh City",
             f"- [Work]({u('work.html')}): selected programs and projects"]
    for w in WORK:
        lines.append(f"  - [{w['title']}]({u('work/' + w['slug'] + '.html')})")
    lines += [f"- [Credentials]({u('credentials.html')}): PMP, PMI-RMP, P3O, executive education",
              f"- [Contact]({u('contact.html')})", "", f"- [Full text]({u('llms-full.txt')})", ""]
    return "\n".join(lines)


def llms_full():
    L = [f"# {C['NAME']}", "", HEADLINE, STATEMENT, INTRO, f"Location: {C['LOCATION']}", ""]
    L += ["## Profile"] + ABOUT + [""]
    L += ["## Signature figures"] + [f"- {f['pre']}{f['num']}{f['suf']}: {f['label']}" for f in FIGURES] + [""]
    L += ["## Capabilities"] + [f"- {p['title']}: {p['text']} In practice: {p['proof']}" for p in PILLARS] + [""]
    L += ["## Governance architecture"] + [f"- {c['level']}: {c['text']}" for c in CASCADE] + [""]
    L += ["## Career"]
    for c in CAREER:
        L.append(f"### {c['org']} ({c['years']}, {c['place']})")
        for r in c["roles"]:
            L.append(f"- {r['title']} ({r['years']})")
            L += [f"  - {p}" for p in r["points"]]
        if c.get("honour"):
            L.append(f"- {c['honour']}")
    L += ["", "## Selected work"]
    for w in WORK:
        L += [f"### {w['title']}", f"{w['org']} · {w['years']} · {w['role']}", w["summary"]] + [f"- {o}" for o in w["outcomes"]] + [""]
    L += ["## Certifications"] + [f"- {c['abbr']}® — {c['name']}, {c['issuer']} ({c['year']})" for c in CORE_CERTS]
    L += [f"- {c['name']}, {c['issuer']} ({c['year']})" for c in MORE_CERTS] + [""]
    L += ["## Leadership development", HIPO["title"], HIPO["selected"], HIPO["graduated"]]
    L += [f"- {m['name']} — {m['inst']} ({m['when']})" for m in HIPO["modules"]] + [""]
    L += ["## Education", f"{EDUCATION['degree']} — {EDUCATION['school']} ({EDUCATION['years']})", ""]
    L += ["## FAQ"] + [f"Q: {q}\nA: {a}" for q, a in FAQ] + [""]
    L += ["## Contact", f"Email: {C['EMAIL']}" if C["EMAIL"] else "", f"LinkedIn: {C['LINKEDIN']}", ""]
    return "\n".join(L)


def robots():
    if C["PREVIEW"]:
        return "# Private preview — not for indexing yet\nUser-agent: *\nDisallow: /\n"
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot",
            "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "DuckDuckBot"]
    out = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + "User-agent: *\nAllow: /\n"
    if C["BASE_URL"]:
        out += f"\nSitemap: {url('sitemap.xml')}\n"
    return out


def sitemap(paths):
    if not C["BASE_URL"]:
        return None
    items = "".join(f"<url><loc>{url(p)}</loc></url>" for p in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>'


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1C1F24"/><path d="M32 9 55 32 32 55 9 32Z" fill="none" stroke="#C9A9A0" stroke-width="2"/><text x="32" y="39" font-family="Georgia,serif" font-size="20" text-anchor="middle" fill="#F1ECE4">AA</text></svg>"""


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "work").mkdir(parents=True)
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / "assets/img/favicon.svg").write_text(FAVICON)
    pages = {"index.html": home(), "leadership.html": leadership(), "career.html": career(),
             "work.html": work_index(), "credentials.html": credentials(), "contact.html": contact()}
    for i, w in enumerate(WORK):
        pages[f"work/{w['slug']}.html"] = work_detail(i, w)
    for p, h in pages.items():
        (OUT / p).write_text(h, encoding="utf-8")
    (OUT / "llms.txt").write_text(llms_txt(), encoding="utf-8")
    (OUT / "llms-full.txt").write_text(llms_full(), encoding="utf-8")
    (OUT / "robots.txt").write_text(robots(), encoding="utf-8")
    sm = sitemap(["" if p == "index.html" else p for p in pages])
    if sm:
        (OUT / "sitemap.xml").write_text(sm, encoding="utf-8")
    print(f"Built {len(pages)} pages → {OUT}")


if __name__ == "__main__":
    build()
