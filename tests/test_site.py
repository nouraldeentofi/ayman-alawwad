"""Full QA pass for the site (Playwright, Chromium).

    cd docs && python3 -m http.server 8765 &
    python3 tests/test_site.py            # all checks
    python3 tests/test_site.py quick      # fewer widths
"""
import asyncio
import json
import sys
from pathlib import Path

from playwright.async_api import async_playwright

BASE = "http://localhost:8765/"
HERE = Path(__file__).parent
AXE = (HERE / "axe.min.js").read_text()
QUICK = "quick" in sys.argv

PAGES = ["index.html", "leadership.html", "career.html", "work.html", "credentials.html", "contact.html"] + [
    "work/" + p.name for p in sorted((HERE.parent / "docs/work").glob("*.html"))]
SIZES = [("320", 320, 700, True), ("360", 360, 760, True), ("390", 390, 844, True), ("412", 412, 900, True),
         ("430", 430, 932, True), ("land", 844, 390, True), ("768", 768, 1024, True), ("1024", 1024, 768, False),
         ("1366", 1366, 800, False), ("1440", 1440, 900, False)]
if QUICK:
    SIZES = [s for s in SIZES if s[0] in ("320", "390", "768", "1440")]
THEMES = ["light", "dark"]

fails = []
notes = []


def fail(msg):
    fails.append(msg)
    print("  FAIL", msg)


SCROLL_ALL = """async () => { document.documentElement.style.scrollBehavior='auto';
  for (let y=0; y<document.documentElement.scrollHeight; y+=350){ scrollTo({top:y,behavior:'instant'}); await new Promise(r=>setTimeout(r,60)); }
  await new Promise(r=>setTimeout(r,1300)); scrollTo({top:0,behavior:'instant'}); await new Promise(r=>setTimeout(r,200)); }"""

BASIC = """() => {
  const out = {};
  out.hscroll = document.documentElement.scrollWidth - innerWidth;
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && !el.closest('[aria-hidden="true"]') && !el.classList.contains('skip'); };
  out.small = [];
  document.querySelectorAll('a, button, summary, input, textarea, select').forEach(el => {
    if (!vis(el)) return;
    const r = el.getBoundingClientRect();
    if (r.width < 43.5 || r.height < 43.5) out.small.push((el.className || el.tagName) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height) + ' "' + (el.textContent || '').trim().slice(0, 30) + '"');
  });
  out.inputs = [...document.querySelectorAll('input, textarea, select')].filter(vis).map(el => parseFloat(getComputedStyle(el).fontSize)).filter(f => f < 16);
  out.underline = [...document.querySelectorAll('a, button')].filter(el => getComputedStyle(el).textDecorationLine !== 'none').map(el => el.className);
  // overflow of children past their card
  out.stick = [];
  document.querySelectorAll('.card').forEach(c => { if (!vis(c)) return; const cr = c.getBoundingClientRect();
    c.querySelectorAll('*').forEach(ch => { if (!vis(ch)) return; const r = ch.getBoundingClientRect();
      if (r.left < cr.left - 1 || r.right > cr.right + 1) out.stick.push(c.className.split(' ').slice(0,2).join('.') + ' > ' + (ch.className.baseVal ?? ch.className)); }); });
  out.hidden_rv = [...document.querySelectorAll('.rv')].filter(el => getComputedStyle(el).opacity === '0').length;
  return out; }"""

SIBLINGS = """() => {
  const groups = ['.grid-3 .swipe-row', '.wgrid', '.seals', '.certs', '.mods', '.pn-in', '.fcs', '.two', '.figs-in', '.ctrack', '.routes'];
  const foot = '.pl-p, .wc-meta, .seal-y, .mod-i, .cert-y';
  const out = [];
  groups.forEach(sel => document.querySelectorAll(sel).forEach(g => {
    const kids = [...g.children].filter(k => getComputedStyle(k).display !== 'none');
    if (getComputedStyle(g).overflowX === 'auto') return; // swipe row on phones: checked separately
    const rows = {};
    kids.forEach(k => { const r = k.getBoundingClientRect(); const key = Math.round(r.top); (rows[key] = rows[key] || []).push(k); });
    // merge rows within 2px
    Object.values(rows).forEach(row => {
      if (row.length < 2) return;
      const hs = row.map(k => k.getBoundingClientRect().height);
      if (Math.max(...hs) - Math.min(...hs) > 1) out.push(sel + ' heights ' + hs.map(Math.round).join('/'));
      const fs = row.map(k => k.querySelector(foot)).filter(Boolean).map(f => f.getBoundingClientRect().bottom);
      if (fs.length === row.length && Math.max(...fs) - Math.min(...fs) > 1.5) out.push(sel + ' footers ' + fs.map(Math.round).join('/'));
    });
  }));
  return out; }"""


async def basic_pass(b):
    print("== basic: overflow, errors, targets, inputs, underline, sticking-out ==")
    for name, w, h, mob in SIZES:
        for theme in THEMES:
            ctx = await b.new_context(viewport={"width": w, "height": h}, is_mobile=mob, has_touch=mob)
            await ctx.add_init_script(f"try{{localStorage.setItem('aa-theme','{theme}')}}catch(e){{}}")
            pg = await ctx.new_page()
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
            for path in PAGES:
                await pg.goto(BASE + path, wait_until="networkidle")
                await pg.evaluate(SCROLL_ALL)
                r = await pg.evaluate(BASIC)
                tag = f"{path} @{name} {theme}"
                if r["hscroll"] > 0: fail(f"{tag}: horizontal scroll {r['hscroll']}px")
                if r["small"]: fail(f"{tag}: small targets {r['small'][:4]}")
                if r["inputs"]: fail(f"{tag}: input font < 16 {r['inputs']}")
                if r["underline"]: fail(f"{tag}: underline on {r['underline'][:3]}")
                if r["stick"]: fail(f"{tag}: child sticks out {r['stick'][:3]}")
                if r["hidden_rv"]: fail(f"{tag}: {r['hidden_rv']} reveal elements still hidden")
                if errs: fail(f"{tag}: JS errors {errs[:2]}"); errs.clear()
                if name in ("1440", "1024", "768", "390", "320") and theme == "light":
                    s = await pg.evaluate(SIBLINGS)
                    if s: fail(f"{tag}: siblings {s[:3]}")
            await ctx.close()
        print(f"  {name} done")


async def axe_pass(b):
    print("== axe-core ==")
    for name, w, h, mob in [("390", 390, 844, True), ("1440", 1440, 900, False)]:
        for theme in THEMES:
            ctx = await b.new_context(viewport={"width": w, "height": h}, is_mobile=mob, has_touch=mob, reduced_motion="reduce")
            await ctx.add_init_script(f"try{{localStorage.setItem('aa-theme','{theme}')}}catch(e){{}}")
            pg = await ctx.new_page()
            for path in PAGES:
                await pg.goto(BASE + path, wait_until="networkidle")
                await pg.evaluate(SCROLL_ALL)
                await pg.add_script_tag(content=AXE)
                res = await pg.evaluate("""async () => { const r = await axe.run(document, {resultTypes:['violations']});
                    return r.violations.filter(v => ['serious','critical'].includes(v.impact)).map(v => v.id + ': ' + v.nodes.slice(0,3).map(n => n.target.join(' ')).join(' | ')); }""")
                if res: fail(f"axe {path} @{name} {theme}: {res}")
            await ctx.close()


UNDERLINE_HOVER = """async () => { const bad = []; const els = [...document.querySelectorAll('a, button')].filter(e => e.getBoundingClientRect().width > 0);
  for (const el of els) { el.focus(); if (getComputedStyle(el).textDecorationLine !== 'none') bad.push('focus ' + el.className); }
  return bad; }"""


async def interaction_pass(b):
    print("== interactions: hover/focus underline, theme, nav, swipe, details, form, layout shift ==")
    # desktop hover + focus underline
    ctx = await b.new_context(viewport={"width": 1440, "height": 900})
    pg = await ctx.new_page()
    for path in PAGES[:6] + PAGES[6:7]:
        await pg.goto(BASE + path, wait_until="networkidle")
        bad = await pg.evaluate(UNDERLINE_HOVER)
        links = await pg.query_selector_all("a:visible, button:visible")
        for el in links[:60]:
            try:
                await el.hover(timeout=800)
                td = await el.evaluate("e => getComputedStyle(e).textDecorationLine")
                if td != "none": bad.append("hover " + (await el.get_attribute("class") or ""))
            except Exception:
                pass
        if bad: fail(f"{path}: underline on hover/focus {bad[:3]}")
    await ctx.close()

    # touch context
    ctx = await b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
    pg = await ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    await pg.goto(BASE + "index.html", wait_until="networkidle")
    # dock navigation
    for label, expect in [("Leadership", "leadership.html"), ("Career", "career.html"), ("Work", "work.html"),
                          ("Credentials", "credentials.html"), ("Home", "index.html")]:
        async with pg.expect_navigation():
            await pg.locator(".dock-a", has_text=label).tap()
        await pg.wait_for_load_state("networkidle")
        if not pg.url.endswith(expect): fail(f"dock {label} → {pg.url}")
    # header mail → contact
    async with pg.expect_navigation():
        await pg.locator(".hdr-mail").tap()
    await pg.wait_for_load_state("networkidle")
    if not pg.url.endswith("contact.html"): fail("header mail button did not open contact")
    # theme toggle persists
    await pg.locator("[data-theme-toggle]").first.tap()
    th = await pg.evaluate("document.documentElement.dataset.theme")
    await pg.goto(BASE + "career.html", wait_until="networkidle")
    th2 = await pg.evaluate("document.documentElement.dataset.theme")
    if th != "dark" or th2 != "dark": fail(f"theme toggle/persist: {th} {th2}")
    await pg.locator("[data-theme-toggle]").first.tap()
    # details expand on career (phones)
    btn = pg.locator(".more-btn").first
    await btn.scroll_into_view_if_needed(); await pg.wait_for_timeout(1600)
    y0 = await btn.evaluate("e => e.getBoundingClientRect().top + scrollY")
    await btn.tap(); await pg.wait_for_timeout(700)
    open_ = await pg.evaluate("document.querySelector('.more').classList.contains('is-open')")
    y1 = await btn.evaluate("e => e.getBoundingClientRect().top + scrollY")
    if not open_: fail("career: Show details did not open")
    if abs(y1 - y0) > 0.5: fail(f"career: tapped button moved {y1 - y0}px")
    # swipe rows on home
    await pg.goto(BASE + "index.html", wait_until="networkidle")
    await pg.evaluate(SCROLL_ALL)
    sw = pg.locator("[data-swipe]").first
    await sw.scroll_into_view_if_needed()
    await pg.wait_for_timeout(400)
    c0 = await sw.evaluate("s => [...s.querySelectorAll('.swipe-row > *')].findIndex(e => e.classList.contains('is-c'))")
    dots = await sw.locator(".dots button").count()
    if dots < 2: fail("swipe: dots missing")
    await sw.locator(".dots button").nth(2).tap(); await pg.wait_for_timeout(900)
    c1 = await sw.evaluate("s => [...s.querySelectorAll('.swipe-row > *')].findIndex(e => e.classList.contains('is-c'))")
    if c1 != 2: fail(f"swipe: dot tap → centred {c1}")
    # manual swipe
    await sw.evaluate("s => s.querySelector('.swipe-row').scrollBy({left: 330, behavior: 'instant'})"); await pg.wait_for_timeout(500)
    c2 = await sw.evaluate("s => [...s.querySelectorAll('.swipe-row > *')].findIndex(e => e.classList.contains('is-c'))")
    if c2 != 3: fail(f"swipe: scroll → centred {c2}")
    # auto-rotate (after pause expires)
    await pg.wait_for_timeout(15500)
    c3 = await sw.evaluate("s => [...s.querySelectorAll('.swipe-row > *')].findIndex(e => e.classList.contains('is-c'))")
    if c3 == c2: fail("swipe: auto-rotate did not advance")
    # hover must not stick on touch: tap a work card's neighbour area then check translate
    stuck = await pg.evaluate("() => [...document.querySelectorAll('.card')].filter(c => { const t = getComputedStyle(c).translate; return t && t !== 'none' && t !== '0px' && t !== '0px 0px'; }).length")
    if stuck: fail(f"touch: {stuck} cards keep a hover offset")
    # contact form
    await pg.goto(BASE + "contact.html", wait_until="networkidle")
    has_form = await pg.locator("#cform").count()
    if has_form:
        await pg.evaluate("window.__nav = []")
        await pg.locator("#cform button[type=submit]").tap()
        msg = await pg.locator("#f-err").text_content()
        if not msg: fail("form: empty submit gave no message")
        await pg.fill("#f-name", "Test Person"); await pg.fill("#f-org", "Org"); await pg.fill("#f-msg", "Hello Ayman")
        await pg.evaluate("document.getElementById('cform').addEventListener('submit', e => {}, {once:true})")
        try:
            await pg.locator("#cform button[type=submit]").tap(timeout=2000)
        except Exception:
            pass
        await pg.wait_for_timeout(300)
        href = await pg.evaluate("document.getElementById('cform') && document.getElementById('cform').dataset.lastHref")
        if not href or "?subject=Message%20from%20Test%20Person" not in href:
            fail(f"form: bad mailto {href}")
        else:
            notes.append("form mailto: " + href[:90] + "…")
    # FAQ open/close
    await pg.goto(BASE + "contact.html", wait_until="networkidle")
    s = pg.locator(".qa summary").first
    await s.tap(); await pg.wait_for_timeout(500)
    if not await pg.evaluate("document.querySelector('.qa').open"): fail("faq: did not open")
    if errs: fail(f"touch: JS errors {errs[:2]}")
    await ctx.close()


SHIFT = """async (ops) => {
  window.__cls = 0;
  new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) window.__cls += e.value; }).observe({type: 'layout-shift', buffered: false});
  const anchors = [...document.querySelectorAll('section, .figs, footer')].map(el => el);
  const pos = () => anchors.map(a => Math.round((a.getBoundingClientRect().top + scrollY) * 10) / 10);
  const before = pos();
  const moved = [];
  for (const op of ops) {
    if (op === 'theme') { document.querySelector('[data-theme-toggle]').click(); await new Promise(r => setTimeout(r, 700)); }
    if (op === 'dots') { for (const b of document.querySelectorAll('.dots button')) { b.click(); await new Promise(r => setTimeout(r, 350)); } }
    if (op === 'count') { await new Promise(r => setTimeout(r, 2200)); }
    if (op === 'wait') { await new Promise(r => setTimeout(r, 6000)); }
    const now = pos();
    now.forEach((v, i) => { if (Math.abs(v - before[i]) > 0.5) moved.push(op + ':' + anchors[i].className + ' ' + before[i] + '→' + v); });
  }
  return {cls: window.__cls, moved}; }"""


async def shift_pass(b):
    print("== nothing jumps ==")
    for name, w, h, mob in [("390", 390, 844, True), ("1440", 1440, 900, False), ("768", 768, 1024, True)]:
        ctx = await b.new_context(viewport={"width": w, "height": h}, is_mobile=mob, has_touch=mob)
        pg = await ctx.new_page()
        for path in ["index.html", "leadership.html", "credentials.html", "career.html", "contact.html", PAGES[6]]:
            await pg.goto(BASE + path, wait_until="networkidle")
            await pg.evaluate("document.fonts.ready")
            await pg.evaluate(SCROLL_ALL)
            await pg.evaluate("scrollTo(0, 0)")
            r = await pg.evaluate(SHIFT, ["count", "theme", "dots", "theme", "wait"])
            if r["cls"] > 0 or r["moved"]:
                fail(f"jump {path} @{name}: cls={r['cls']:.4f} moved={r['moved'][:3]}")
        await ctx.close()


async def motion_pass(b):
    print("== motion + reduced motion ==")
    out = HERE / "shots"
    for theme in THEMES:
        ctx = await b.new_context(viewport={"width": 1440, "height": 900})
        await ctx.add_init_script(f"try{{localStorage.setItem('aa-theme','{theme}')}}catch(e){{}}")
        pg = await ctx.new_page()
        await pg.goto(BASE + "index.html", wait_until="commit")
        await pg.wait_for_timeout(150)
        await pg.screenshot(path=str(out / f"motion-{theme}-0.png"))
        await pg.wait_for_timeout(1000)
        await pg.screenshot(path=str(out / f"motion-{theme}-1s.png"))
        await pg.wait_for_timeout(2000)
        await pg.screenshot(path=str(out / f"motion-{theme}-3s.png"))
        o0 = await pg.evaluate("getComputedStyle(document.querySelector('.hero-n')).opacity")
        st = await pg.evaluate("getComputedStyle(document.querySelector('.pl-drift')).animationName")
        if o0 != "1" or "drift" not in st: fail(f"motion {theme}: hero not settled / drift missing")
        for i, y in enumerate([500, 1400, 2600]):
            await pg.evaluate(f"scrollTo({{top:{y},behavior:'instant'}})")
            await pg.wait_for_timeout(1300)
            await pg.screenshot(path=str(out / f"motion-{theme}-scroll{i}.png"))
        await ctx.close()
    ctx = await b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True, reduced_motion="reduce")
    pg = await ctx.new_page()
    for path in PAGES[:6]:
        await pg.goto(BASE + path, wait_until="networkidle")
        await pg.evaluate(SCROLL_ALL)
        hidden = await pg.evaluate("[...document.querySelectorAll('.rv, .e1, .e2, .e3, .e4, .e5, .e6, .ptitle')].filter(e => !e.closest('.swipe.is-js') && +getComputedStyle(e).opacity < 1).length")
        if hidden: fail(f"reduced motion {path}: {hidden} elements not fully visible")
    await ctx.close()


async def perf_pass(b):
    print("== smoothness (390px touch, 4x CPU throttle) ==")
    ctx = await b.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
    pg = await ctx.new_page()
    cdp = await ctx.new_cdp_session(pg)
    for path in ["index.html", "credentials.html", "career.html"]:
        await pg.goto(BASE + path, wait_until="networkidle")
        await cdp.send("Emulation.setCPUThrottlingRate", {"rate": 4})
        r = await pg.evaluate("""async () => { const frames = []; let last = performance.now(); let run = true;
          const loop = t => { frames.push(t - last); last = t; if (run) requestAnimationFrame(loop); }; requestAnimationFrame(loop);
          const H = document.documentElement.scrollHeight - innerHeight;
          for (let y = 0; y <= H; y += 24) { scrollTo({top: y, behavior: 'instant'}); await new Promise(r => requestAnimationFrame(r)); }
          run = false; frames.shift(); frames.sort((a, b) => a - b);
          const avg = frames.reduce((a, b) => a + b, 0) / frames.length;
          return {n: frames.length, fps: Math.round(1000 / avg), p95: Math.round(frames[Math.floor(frames.length * .95)]), long: frames.filter(f => f > 50).length}; }""")
        await cdp.send("Emulation.setCPUThrottlingRate", {"rate": 1})
        notes.append(f"perf {path}: {r}")
        if r["fps"] < 45: fail(f"perf {path}: {r}")
    await ctx.close()


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--no-sandbox"])
        which = [a for a in sys.argv[1:] if a != "quick"] or ["basic", "axe", "interact", "shift", "motion", "perf"]
        if "basic" in which: await basic_pass(b)
        if "axe" in which: await axe_pass(b)
        if "interact" in which: await interaction_pass(b)
        if "shift" in which: await shift_pass(b)
        if "motion" in which: await motion_pass(b)
        if "perf" in which: await perf_pass(b)
        await b.close()
    print("\n".join(notes))
    print(f"\n{len(fails)} failures")
    (HERE / "report.json").write_text(json.dumps({"fails": fails, "notes": notes}, indent=1))


asyncio.run(main())
