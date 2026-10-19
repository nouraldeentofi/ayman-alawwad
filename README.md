# موقع أيمن العواد — Ayman Alawwad (النسخة التنفيذية)

موقع Executive Personal Branding بالإنجليزي، مبني من معلومات لينكدإن المنشورة.
الحالة: **معاينة** على GitHub Pages (https://nouraldeentofi.github.io/ayman-alawwad/) والصفحات كلها `noindex`. وفي بوابة كلمة سر جاهزة لـ Cloudflare Pages لما نحتاجها (`CF_GATE = True`).

## الفكرة
"Drafted on linen": لون الكتان والحبر من بانر لينكدإن تبعه، وخلفية حية عبارة عن خارطة طريق محفظة مشاريع بتنرسم لحالها بالحبر، والمعالم (milestones) على شكل ◆. الأحمر الغامق من الشماغ. الخطوط Newsreader و Public Sans، ومستضافة جوا الموقع.

## الصفحات
| الصفحة | الملف | شو فيها |
|---|---|---|
| الرئيسية | `index.html` | جملة التموضع، 4 أرقام تنفيذية، 4 مبادئ قيادية، 4 مشاريع رئيسية، المسيرة بـ 3 فصول، الشهادات، اقتباسه عن الـ hybrid |
| Leadership | `leadership.html` | النبذة، "How I lead"، نموذج الحوكمة (P3O)، الـ Mandates، اقتباسات من بوستاته، نبذة تنفيذية قصيرة وطويلة مع زر نسخ |
| Journey | `journey.html` | 3 فصول: Foundations / Delivery at scale / National programs، وتحت كل فصل المناصب والتواريخ |
| Impact | `impact.html` + `impact/*.html` | 4 مشاريع، كل واحد قصة: The mandate / The complexity / How I led / The result |
| Credentials | `credentials.html` | PMP و PMI-RMP و P3O، الـ OKR والـ KPI، رحلة برنامج HiPo بالتواريخ، التعليم والتكريم، والكورسات بسطر "Continuing development" |
| Contact | `contact.html` | لينكدإن، المدينة، رابط النبذة، وأسئلة شائعة |

## وين بتعدّل
- **كل النصوص:** `content.py`. كل رقم وجملة مصدره بـ `brief.md`.
- **نقاط لازم يأكدها أيمن قبل الإطلاق:** قائمة `REVIEW` آخر `content.py`.
- **CONFIG** أول `content.py`:
  - `PHOTO` — صورته (فاضي = بطاقة AA بدلها، وهيك هي بنسخة GitHub). `EMAIL` فاضي لحد ما يوافق يبين، و`PHONE` فاضي.
  - `BASE_URL` — الدومين النهائي (canonical و sitemap و og:image).
  - `PREVIEW` — `True` بالمعاينة (noindex). عند الإطلاق `False`.
  - `CF_GATE` — `True` بيضيف بوابة كلمة السر لما ترفع على Cloudflare Pages.
- **الألوان والخطوط والمسافات:** أول `assets/style.css`. **الحركة والسلوك:** `assets/site.js`.

```
python3 build.py        # بيطلع الموقع جاهز بمجلد docs/
```

## المعاينة المحمية (Cloudflare Pages)
`cloudflare/_worker.js` بيتنسخ لـ `docs/_worker.js` لما `CF_GATE = True`. هو صفحة كلمة سر بنفس شكل الموقع، وبعد كلمة السر الصحيحة بيضل الزائر داخل 30 يوم. إذا ما في كلمة سر محطوطة، الموقع بيضل مسكّر.

1. Cloudflare → Workers & Pages → Create → Pages → Upload assets → اسم المشروع مثلاً `ayman-alawwad-preview` → ارفع مجلد `docs` → Deploy.
2. Settings → Variables and Secrets → Add → الاسم `PREVIEW_PASSWORD`، النوع Secret، والقيمة كلمة السر اللي بدك تعطيها لأيمن.
3. Deployments → Create deployment → ارفع `docs` مرة تانية لحتى تشتغل كلمة السر.
4. افتح `https://ayman-alawwad-preview.pages.dev` وجرّب كلمة السر، وبعدين ابعت الرابط وكلمة السر لأيمن.

## الإطلاق بعد الموافقة
- أيمن بيعمل حساب Cloudflare مجاني بإيميله، وبيشتري الدومين من جواته (Domain Registration)، وبيضيفك عضو من Manage Account → Members.
- إنت بتعمل مشروع Pages على حسابه، بتربط الدومين، وبتحط `PREVIEW = False` و`BASE_URL` = الدومين، وبتبني وبترفع. وقتها `_worker.js` ما بينضاف والموقع بينفتح لمحركات البحث وبوتات الذكاء الاصطناعي.
- بتسلمه الملفات والكود، وهو بيقدر يشيلك من الحساب.

## الذكاء الاصطناعي ومحركات البحث
- كل المحتوى جوا الـ HTML (ما بيحتاج JavaScript).
- JSON-LD: Person (كل كتابات الاسم، المسميات، الشهادات، التعليم التنفيذي)، ProfilePage، BreadcrumbList، FAQPage.
- `llms.txt` و`llms-full.txt` (فيهن النبذة الكاملة)، `robots.txt`، `sitemap.xml` لما ينحط `BASE_URL`.

## الاختبارات
```
cd docs && python3 -m http.server 8765 &
python3 tests/test_site.py          # كل الفحوصات (320 → 1440، فاتح وغامق)
```
