import asyncio, sys
from playwright.async_api import async_playwright
BASE="http://localhost:8765/"
OUT="/home/claude/ayman-alawwad/tests/shots/"
# (name, path, selector-to-scroll-to or None, offset)
PHONE=[("p1","index.html",None,0),("p2","index.html",".figs",-70),("p3","index.html",".grid-3",-150),
       ("p4","career.html",".tl",-90),("p5","credentials.html",".seals",-170),("p6","work/infrastructure-rehabilitation-28m.html",None,0),
       ("p7","leadership.html",".cascade",-150),("p8","contact.html",".routes",-110)]
DESK=[("d1","index.html",None,0),("d2","leadership.html",".cascade",-260),("d3","credentials.html",".hipo",-330),("d4","work/violation-detection-nationwide-rollout.html",None,0),("d5","index.html",".seals",-260),("d6","career.html",None,0)]
async def shoot(b, items, w, h, mob, theme, prefix, dpr):
    ctx=await b.new_context(viewport={"width":w,"height":h}, is_mobile=mob, has_touch=mob, device_scale_factor=dpr)
    await ctx.add_init_script(f"try{{localStorage.setItem('aa-theme','{theme}')}}catch(e){{}}")
    pg=await ctx.new_page()
    for name,path,sel,off in items:
        await pg.goto(BASE+path, wait_until="networkidle")
        await pg.evaluate("document.fonts.ready")
        await pg.evaluate("""async()=>{document.documentElement.style.scrollBehavior='auto';for(let y=0;y<document.documentElement.scrollHeight;y+=350){scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,50));}}""")
        if sel:
            await pg.evaluate(f"""(()=>{{const e=document.querySelector('{sel}');scrollTo({{top:e.getBoundingClientRect().top+scrollY+({off}),behavior:'instant'}})}})()""")
        else:
            await pg.evaluate("scrollTo({top:0,behavior:'instant'})")
        if name=="p4":
            await pg.evaluate("document.querySelector('.more-btn').click()")
        await pg.wait_for_timeout(3200)
        await pg.screenshot(path=f"{OUT}{prefix}-{name}-{theme}.png")
    await ctx.close()
async def main():
    theme=sys.argv[1] if len(sys.argv)>1 else "light"
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--no-sandbox"])
        await shoot(b, PHONE, 390, 844, True, theme, "vp", 2)
        await shoot(b, DESK, 1440, 900, False, theme, "vd", 1)
        await b.close()
asyncio.run(main())
