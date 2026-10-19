# موقع أيمن العواد — Ayman Alawwad

موقع شخصي تنفيذي (Executive Personal Branding) بالإنجليزي، مبني من معلومات لينكدإن المنشورة.
الحالة الآن: **نسخة معاينة** — كل الصفحات عليها `noindex` لحتى الموافقة النهائية.

الموقع: https://nouraldeentofi.github.io/ayman-alawwad/ — الملفات الجاهزة بمجلد `docs/` (منه بيشتغل GitHub Pages)، والسورس بالجذر.

## الفكرة
"Drafted on linen" — لون الكتان والحبر من بانر لينكدإن تبعه، وخلفية حية عبارة عن خارطة طريق محفظة مشاريع بتنرسم لحالها بالحبر (أشرطة، تبعيات، ومعالم milestones على شكل ◆ وهي رمز الـ milestone بالـ Gantt)، وخط "status date" أحمر بيتحرك ببطء. الأحمر الغامق (garnet) مأخوذ من الشماغ. الخطوط: Newsreader (عناوين) و Public Sans (نص) — مستضافة داخل الموقع.

## الصفحات
| الصفحة | الملف | شو فيها |
|---|---|---|
| الرئيسية | `index.html` | الهيرو مع الصورة، 4 أرقام بتعد، نبذة، 6 مجالات قيادة، مسار مهني مختصر، 3 أعمال مختارة، الشهادات، اقتباس من بوسته عن الـ hybrid، دعوة للتواصل |
| Leadership | `leadership.html` | نبذة كاملة، نموذج الحوكمة (Strategy → Portfolio → Program → Project → Operations) المستوحى من P3O، المجالات الستة، البيئات ومحاور التركيز |
| Career | `career.html` | خط زمني لكل الشركات والمناصب بالنقاط (على الموبايل مطوية خلف Show details) + التعليم |
| Work | `work.html` + `work/*.html` | 7 مشاريع، لكل مشروع صفحة: النطاق، الدور، الفترة، النتائج، رقم أساسي، والمشروع السابق/التالي |
| Credentials | `credentials.html` | PMP / PMI-RMP / P3O، برنامج HiPo (60 من 1,200) بوحداته من MIT و NUS و ESCP و Kellogg، باقي الشهادات، التعليم والتكريم |
| Contact | `contact.html` | الإيميل ولينكدإن والمدينة، فورم بيفتح رسالة جاهزة بتطبيق الإيميل، وأسئلة شائعة |

## وين بتعدّل
- **كل النصوص:** `content.py` (كل رقم وجملة فيه مصدره بـ `brief.md`).
- **CONFIG** أول `content.py`:
  - `EMAIL` (فاضي بالنسخة العامة لحد ما يوافق — لما تحطه بيرجع الإيميل وفورم التواصل)، `LINKEDIN`، `LOCATION`
  - `PHONE` فاضي عن قصد — ما بينحط رقمه إلا بموافقته. الفاضي ما بيظهر.
  - `PHOTO` — إذا فضّيتها بيطلع مونوغرام AA بدل الصورة.
  - `BASE_URL` — حطّ رابط الموقع النهائي (مثلاً `https://aymanalawwad.com`) ليطلع canonical و sitemap و og:image بروابط كاملة.
  - `PREVIEW` — خليه `True` لحد الموافقة النهائية. بعدها `False` بيشيل الـ noindex وبيفتح robots.txt لمحركات البحث وبوتات الذكاء الاصطناعي (GPTBot, ClaudeBot, PerplexityBot, Google-Extended…).
  - `MAKER` — رابطك بالفوتر.
- **الألوان والخطوط والمسافات:** أول `assets/style.css` (tokens للفاتح والغامق).
- **الحركة والسلوك:** `assets/site.js`.

بعد أي تعديل:
```
python3 build.py        # بيطلع الموقع جاهز بمجلد docs/
```

## الذكاء الاصطناعي ومحركات البحث
- كل المحتوى مكتوب جوا الـ HTML (ما بيحتاج JavaScript).
- JSON-LD بكل صفحة: Person (مع كل كتابات الاسم بالعربي والإنجليزي، المسميات، الشهادات، الجامعة، المهارات)، ProfilePage، BreadcrumbList بصفحات المشاريع، FAQPage بصفحة التواصل.
- `llms.txt` و `llms-full.txt` و `robots.txt` و `sitemap.xml` (الأخير بيطلع لما تحط BASE_URL).

## الدومين والنشر
- GitHub Pages (الحالي): Settings → Pages → Branch `main` / folder `docs`. بعد الموافقة: `PREVIEW = False` وأعد البناء وارفع `docs/`.
- إذا بدو الكود خاص: Cloudflare Pages (مجاني، `*.pages.dev`، ودومين خاص لاحقاً).
- دومين خاص: ضيف الدومين بإعدادات Pages وحط سجلات DNS اللي بيعطيك ياها، وبعدين حدّث `BASE_URL`.

## الاختبارات
```
cd docs && python3 -m http.server 8765 &
python3 tests/test_site.py          # كل الفحوصات (عرض 320 → 1440، فاتح وغامق)
```
بتفحص: ما في سكرول أفقي، ما في أخطاء JS، axe-core، أهداف اللمس ≥ 44px، الحقول ≥ 16px، ما في underline، الكروت المتجاورة متساوية، ما في أي قفزة بالصفحة، الحركة وreduced motion، والسلاسة مع إبطاء المعالج 4×.
