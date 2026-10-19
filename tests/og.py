import asyncio
from playwright.async_api import async_playwright
HTML = """<!doctype html><html><head><meta charset=utf-8><link rel=stylesheet href="http://localhost:8765/assets/style.css">
<style>body{margin:0;width:1200px;height:630px;overflow:hidden}
.og{position:relative;width:1200px;height:630px;display:grid;grid-template-columns:1fr 400px;gap:56px;align-items:center;padding:0 72px;box-sizing:border-box}
.og .plan{opacity:.9}.og .bgw{position:absolute;inset:0;-webkit-mask-image:linear-gradient(90deg,transparent 35%,#000 75%)}
.og h1{font-family:var(--serif);font-size:92px;line-height:.98;letter-spacing:-.02em;font-weight:500;margin:0 0 22px}
.og .k{font-size:22px;color:var(--ink-2);margin:0 0 18px;font-weight:500}
.og .s{font-family:var(--serif);font-style:italic;font-size:32px;line-height:1.25;margin:0 0 26px;max-width:22ch}
.og .c{display:flex;gap:10px;font-weight:600;font-size:18px;color:var(--acc)}
.og .ph .mono::before{inset:30px;border-width:3px}.og .ph{position:relative;width:400px;height:500px;border-radius:24px;overflow:hidden;box-shadow:var(--shadow-3)}
.og .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 30%}
.pl-bar path,.pl-dep path{stroke-dashoffset:0!important;animation:none!important}.pl-dia{opacity:1!important;animation:none!important}.pl-drift,.pl-status{animation:none!important}
</style></head><body><div class=og><div class=bgw>PLAN</div>
<div style="position:relative"><p class=k>PMO Manager · Portfolio &amp; Program Management</p><h1>Ayman<br>Alawwad</h1>
<p class=s>Bridging strategy and execution through portfolio governance.</p><p class=c>PMP® · P3O® · PMI-RMP® &nbsp;·&nbsp; Riyadh</p></div>
<div class=ph style="display:grid;place-items:center;background:var(--ink)"><span class="mono" style="width:200px;height:200px"><span style="font-size:56px;color:var(--paper)">AA</span></span></div></div></body></html>"""
import sys; sys.path.insert(0,'.')
from build import plan_svg
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1200,"height":630})
        await pg.goto("http://localhost:8765/index.html")
        await pg.set_content(HTML.replace("PLAN", plan_svg(seed=11)), wait_until="networkidle")
        await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(500)
        await pg.screenshot(path="assets/img/og.png")
        await b.close()
asyncio.run(main())
