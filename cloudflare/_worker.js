// Private preview gate for Cloudflare Pages (advanced mode, works with dashboard drag-and-drop).
// 1. In the Pages project: Settings → Variables and Secrets → add PREVIEW_PASSWORD (type: Secret).
// 2. Redeploy (upload the folder again) so the secret is picked up.
// Visitors see a branded password page; after the right password a cookie keeps them signed in for 30 days.
// No password set = the site stays closed (fails closed).

const COOKIE = 'aa_preview';
const MAX_AGE = 60 * 60 * 24 * 30;
const OPEN_PATHS = [/^\/assets\/fonts\//, /^\/assets\/img\/favicon\.svg$/];
const SECURITY_HEADERS = {
  'Cache-Control': 'no-store',
  'X-Robots-Tag': 'noindex, nofollow',
  'Referrer-Policy': 'same-origin',
  'X-Content-Type-Options': 'nosniff',
};

async function tokenFor(secret) {
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode('ayman-alawwad-preview-v1'));
  return [...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

function safeEqual(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string' || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function readCookie(request, name) {
  const raw = request.headers.get('Cookie') || '';
  for (const part of raw.split(';')) {
    const [k, ...v] = part.trim().split('=');
    if (k === name) return v.join('=');
  }
  return '';
}

function safeNext(value) {
  if (typeof value !== 'string' || !value.startsWith('/') || value.startsWith('//')) return '/';
  return value;
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function loginPage(next, error) {
  const msg = error ? '<p class="err" role="alert">That password did not match. Please try again.</p>' : '';
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow"><title>Private preview · Ayman Alawwad</title>
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<style>
@font-face{font-family:"Newsreader";font-weight:200 800;font-display:swap;src:url("/assets/fonts/newsreader-latin-opsz-normal.woff2") format("woff2")}
@font-face{font-family:"Public Sans";font-weight:100 900;font-display:swap;src:url("/assets/fonts/public-sans-latin-wght-normal.woff2") format("woff2")}
:root{--paper:#F1ECE4;--surface:#FAF7F2;--ink:#1C1F24;--ink2:#44484F;--line:rgba(28,31,36,.16);--acc:#8A2C2F;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--paper:#121417;--surface:#1C1F24;--ink:#EDE7DD;--ink2:#C6BFB3;--line:rgba(237,231,221,.16);--acc:#E0948D;color-scheme:dark}}
*{box-sizing:border-box}html,body{height:100%}
body{margin:0;display:grid;place-items:center;padding:24px max(16px,env(safe-area-inset-right)) 24px max(16px,env(safe-area-inset-left));background:var(--paper);color:var(--ink);font:400 17px/1.6 "Public Sans",system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
main{width:100%;max-width:420px;background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:36px 30px;box-shadow:0 2px 4px rgba(40,30,26,.06),0 18px 40px -16px rgba(40,30,26,.22)}
.mono{position:relative;display:grid;place-items:center;width:56px;height:56px;margin-bottom:22px}
.mono:before{content:"";position:absolute;inset:8px;border:1.5px solid var(--acc);border-radius:6px;transform:rotate(45deg)}
.mono span{position:relative;font:600 17px "Newsreader",Georgia,serif;letter-spacing:.03em}
h1{margin:0 0 6px;font:500 1.9rem/1.15 "Newsreader",Georgia,serif;letter-spacing:-.01em}
p{margin:0;color:var(--ink2)}
form{display:grid;gap:10px;margin-top:24px}
label{font-weight:600;font-size:.94rem}
input{width:100%;min-height:52px;padding:12px 16px;border-radius:14px;border:1px solid var(--line);background:var(--paper);color:var(--ink);font:inherit;font-size:17px}
input:focus{outline:none;border-color:var(--acc);box-shadow:0 0 0 4px color-mix(in srgb,var(--acc) 18%,transparent)}
button{min-height:50px;border:0;border-radius:999px;background:var(--ink);color:var(--paper);font:600 .95rem "Public Sans",system-ui,sans-serif;cursor:pointer;touch-action:manipulation;margin-top:6px}
button:active{transform:scale(.98)}
button:focus-visible{outline:2px solid var(--acc);outline-offset:3px}
.err{color:var(--acc);font-weight:500;font-size:.94rem}
.foot{margin-top:22px;font-size:.82rem}
</style></head>
<body><main>
<div class="mono" aria-hidden="true"><span>AA</span></div>
<h1>Private preview</h1>
<p>This site for Ayman Alawwad is in review and not public yet.</p>
<form method="post" action="/__unlock">
<input type="hidden" name="next" value="${escapeHtml(next)}">
<label for="pw">Password</label>
<input id="pw" name="password" type="password" autocomplete="current-password" enterkeyhint="go" required autofocus>
${msg}
<button type="submit">View the site</button>
</form>
<p class="foot">Designed and built by Nour Aldeen Tofi.</p>
</main></body></html>`;
}

function htmlResponse(body, status) {
  return new Response(body, { status, headers: { 'Content-Type': 'text/html; charset=utf-8', ...SECURITY_HEADERS } });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const secret = env.PREVIEW_PASSWORD;
    if (!secret) {
      return new Response('This preview is not open yet.', { status: 503, headers: { 'Content-Type': 'text/plain; charset=utf-8', ...SECURITY_HEADERS } });
    }

    if (OPEN_PATHS.some((re) => re.test(url.pathname))) return env.ASSETS.fetch(request);

    const token = await tokenFor(secret);

    if (url.pathname === '/__unlock' && request.method === 'POST') {
      let password = '';
      let next = '/';
      try {
        const form = await request.formData();
        password = String(form.get('password') || '');
        next = safeNext(String(form.get('next') || '/'));
      } catch (e) { /* malformed body */ }
      if (safeEqual(password, secret)) {
        return new Response(null, {
          status: 303,
          headers: {
            Location: next,
            'Set-Cookie': `${COOKIE}=${token}; Path=/; Max-Age=${MAX_AGE}; HttpOnly; Secure; SameSite=Lax`,
            ...SECURITY_HEADERS,
          },
        });
      }
      return htmlResponse(loginPage(next, true), 401);
    }

    if (!safeEqual(readCookie(request, COOKIE), token)) {
      return htmlResponse(loginPage(url.pathname + url.search, false), 401);
    }

    const res = await env.ASSETS.fetch(request);
    const out = new Response(res.body, res);
    for (const [k, v] of Object.entries(SECURITY_HEADERS)) out.headers.set(k, v);
    return out;
  },
};
