"""All site content for Ayman Alawwad's site (English only) — executive edition.

Every fact here traces back to brief.md (LinkedIn profile and posts, collected 2026-10-19).
Wording that interprets his own words (principles, bio) is marked DRAFT in REVIEW below
so Ayman can confirm it before launch.
Edit texts here, then run:  python3 build.py
"""

# ---------------------------------------------------------------------------
# CONFIG — empty values stay hidden on the site
# ---------------------------------------------------------------------------
CONFIG = {
    "NAME": "Ayman Alawwad",
    "NAME_AR": "أيمن العواد",
    "EMAIL": "",                      # hidden until Ayman approves showing it (AymanAlawwad95@gmail.com on LinkedIn)
    "PHONE": "",                      # left empty on purpose — add only with Ayman's OK
    "WHATSAPP": "",
    "LINKEDIN": "https://www.linkedin.com/in/ayman-alawwad-0b9724185/",
    "LOCATION": "Riyadh, Saudi Arabia",
    "PHOTO": "",                      # public GitHub preview: AA monogram card. Set "assets/img/ayman.jpg" to show his portrait
    "PHOTO_WEBP": "assets/img/ayman.webp",
    "BASE_URL": "https://nouraldeentofi.github.io/ayman-alawwad",  # change to the final domain at launch
    "MAKER": "https://nouraldeentofi.com",
    "PREVIEW": True,                  # True = preview: noindex + robots Disallow. Set False after approval.
    "CF_GATE": False,                 # True = add the Cloudflare password gate (_worker.js) to the build
}

HEADLINE = "PMO Manager · Portfolio & Program Governance"
STATEMENT = "Turning strategy into governed delivery leaders can see."
INTRO = ("More than ten years across technology, infrastructure, construction and government environments "
         "in Saudi Arabia, from a national-scale technology rollout to building a firm's Center of Excellence.")

FIGURES = [
    {"pre": "SAR ", "num": 500, "suf": "M+", "label": "Projects and portfolios managed and delivered"},
    {"pre": "", "num": 10, "suf": "+", "label": "Years across portfolio governance and delivery"},
    {"pre": "Top ", "num": 5, "suf": "%", "label": "Selected 60 of 1,200 for an eight-month leadership program"},
    {"pre": "", "num": 4, "suf": "", "label": "Executive-education modules from MIT, NUS, ESCP and Kellogg"},
]

ABOUT = [
    "I am a PMO and project/program management professional with more than ten years of experience across "
    "portfolio governance, strategic initiatives, technology, infrastructure, construction and government "
    "environments in Saudi Arabia.",
    "My work combines hands-on project delivery with portfolio-level governance, bridging strategy and "
    "execution, strengthening accountability, improving executive visibility and supporting effective "
    "decision-making.",
    "I have managed and delivered projects and portfolios exceeding SAR 500M, working with government "
    "stakeholders, executives, multidisciplinary teams and more than 28 suppliers across complex delivery "
    "environments.",
]

# How I lead — DRAFT principles, each built from his About or his own posts
PRINCIPLES = [
    {"title": "Bridge strategy and execution",
     "text": "I combine hands-on delivery with portfolio-level governance, so the priorities set by leadership reach the teams doing the work.",
     "proof": "Kept business requirements and technical delivery aligned on national-level systems."},
    {"title": "Give leaders a clear view",
     "text": "Executive reporting and governance exist to support decisions. I build the visibility that lets leadership decide with confidence.",
     "proof": "Executive reporting, RAID management and risk registers with regular reporting."},
    {"title": "Structure + flexibility = results",
     "text": "Not every project fits one box. I run Agile, Waterfall or hybrid delivery according to what the work needs.",
     "proof": "5+ hybrid projects delivered, and Product Owner on 2+ Agile projects."},
    {"title": "Make accountability shared",
     "text": "Government stakeholders, executives, teams and suppliers each own part of delivery. Governance makes that ownership clear.",
     "proof": "Multi-vendor environments managed for performance and compliance; 28+ suppliers evaluated."},
]

# Mandates — the kinds of work he leads (from About + experience)
PILLARS = [
    {"icon": "network", "title": "Establishing PMO governance",
     "text": "PMO governance frameworks that make accountability, standards and decisions visible.",
     "proof": "Launched a Center of Excellence that standardized processes and documentation."},
    {"icon": "layers", "title": "Portfolio & program management",
     "text": "Projects and portfolios exceeding SAR 500M, managed and delivered across sectors.",
     "proof": "Giga-scale infrastructure and technology deployments for public and private clients."},
    {"icon": "target", "title": "Strategy execution & prioritization",
     "text": "Strategic alignment and prioritization that keep delivery tied to the organization's objectives.",
     "proof": "Prioritized conflicting deadlines across 3+ concurrent projects."},
    {"icon": "shield", "title": "Risk & RAID management",
     "text": "Risks, assumptions, issues and dependencies tracked and reported. PMI-RMP® earned in 2022.",
     "proof": "Monitored risks and maintained risk registers with regular reporting."},
    {"icon": "report", "title": "Executive reporting & stakeholders",
     "text": "Reporting and stakeholder management with government entities, executives and multidisciplinary teams.",
     "proof": "Managed stakeholders across government and private sector entities."},
    {"icon": "check", "title": "Vendor & supply governance",
     "text": "Multi-vendor environments managed for performance and compliance.",
     "proof": "Supplier evaluation frameworks; 28+ suppliers evaluated and approved."},
]

# P3O-style cascade — every phrase taken from his About
CASCADE = [
    {"level": "Strategy", "text": "Strategic alignment and prioritization"},
    {"level": "Portfolio", "text": "Portfolio governance and executive reporting"},
    {"level": "Program", "text": "Program management and cross-functional delivery"},
    {"level": "Project", "text": "Agile, Waterfall and hybrid delivery, with risk, cost and schedule under control"},
    {"level": "Operations", "text": "Operational readiness and business value"},
]

QUOTE = {
    "lines": ["Not every project fits one box.", "In real world delivery, hybrid project management wins."],
    "punch": "structure + flexibility = results",
    "cite": "Ayman Alawwad, on hybrid delivery",
}

# In my words — verbatim from his LinkedIn posts
WORDS = [
    {"text": "This journey has been far more than a set of courses. It has been a transformative experience that expanded my leadership perspective.",
     "src": "On graduating from the HiPo leadership program", "when": "Dec 2025"},
    {"text": "This experience has not only broadened my perspective on leadership, but also reinforced the importance of self-awareness, adaptability, and authenticity in leading with purpose.",
     "src": "On the MIT leadership-strengths module", "when": "Jul 2025"},
]

# ---------------------------------------------------------------------------
# Leadership journey — three chapters (past employers only)
# ---------------------------------------------------------------------------
CHAPTERS = [
    {"num": "I", "title": "Foundations", "years": "2016 – 2021",
     "orgs": "Khazaz Engineering Office",
     "text": [
         "I started in quality assurance, auditing projects against quality and safety standards, then moved into project management.",
         "As Assistant Project Manager I launched the firm's Center of Excellence, prepared bids for public infrastructure tenders and contributed to raising the firm's classification from 3rd to 1st grade. By 2020 I was managing projects end to end and reporting performance to senior management.",
         "In 2018 I also trained with The Royal Commission for Riyadh City on the Al-Ddoho revival project, with an overview of the Riyadh Metro.",
     ],
     "roles": [
         ("Quality Assurance Specialist", "Khazaz Engineering Office", "2016 – 2017"),
         ("Assistant Project Manager", "Khazaz Engineering Office", "2017 – 2020"),
         ("Trainee Civil Engineer", "The Royal Commission for Riyadh City", "2018"),
         ("Project Manager", "Khazaz Engineering Office", "2020 – 2021"),
     ]},
    {"num": "II", "title": "Delivery at scale", "years": "2021 – 2022",
     "orgs": "Tatweer Buildings Company",
     "text": [
         "I led the full lifecycle of a SAR 28M infrastructure reconstruction project for the Ministry of Education, coordinating internal teams, contractors and the client, and resolving technical and contractual issues along the way.",
         "It was delivered two weeks ahead of schedule and within budget, in full compliance with quality and safety standards.",
     ],
     "roles": [
         ("Project Manager", "Tatweer Buildings Company", "2021 – 2022"),
     ]},
    {"num": "III", "title": "National programs", "years": "2022 – 2026",
     "orgs": "TAHAKOM",
     "text": [
         "At TAHAKOM I moved from engineering into leading national-level technology programs. As Project Engineer I worked on the standards behind delivery, evaluating suppliers, writing technical guidelines and system designs, and keeping risk registers current.",
         "As Project Manager I led the end-to-end delivery of smart traffic violation detection systems across multiple Saudi cities, with cross-functional teams of 17+, multi-vendor environments and hybrid delivery.",
         "I was honoured for the accomplishment of 2023 targets, and in 2025 I was selected among 60 of 1,200 candidates for the company's High Potential leadership program.",
     ],
     "roles": [
         ("Project Engineer", "TAHAKOM", "2022 – 2024"),
         ("Project Manager", "TAHAKOM", "2024 – 2026"),
     ]},
]

# ---------------------------------------------------------------------------
# Impact — four flagship engagements, told as mandate / complexity / how / result
# ---------------------------------------------------------------------------
IMPACT = [
    {"slug": "national-violation-detection-rollout",
     "title": "Nationwide rollout of smart violation detection systems",
     "short": "National violation detection rollout",
     "org": "TAHAKOM", "years": "2024 – 2026", "role": "Project Manager",
     "fig": "5+", "fig_label": "hybrid projects delivered",
     "card": "End-to-end delivery of national-level traffic enforcement systems across multiple Saudi cities.",
     "mandate": "Lead the delivery of new smart traffic violation detection systems across multiple cities in Saudi Arabia, from concept to operation.",
     "complexity": "National-level systems supporting traffic enforcement operations, with government and private-sector stakeholders, multiple engineering streams and a multi-vendor environment. Alongside it, giga-scale infrastructure and technology deployments for high-profile public and private clients, with conflicting deadlines across 3+ concurrent projects.",
     "how": ["Ran delivery in a hybrid Agile/Waterfall model, acting as Product Owner on 2+ Agile projects",
             "Led cross-functional teams of 17+ members",
             "Kept business requirements and technical delivery aligned",
             "Managed vendors for performance and compliance, and prioritized conflicting deadlines"],
     "result": ["5+ hybrid projects delivered",
                "Site operations launched on time nationwide",
                "Solutions implemented on time, with resource and budget optimization"],
     "tags": ["Program & portfolio management", "Hybrid delivery", "Government stakeholders", "Multi-vendor governance"]},
    {"slug": "supplier-and-design-standards",
     "title": "Raising quality through supplier and design standards",
     "short": "Supplier and design standards",
     "org": "TAHAKOM", "years": "2022 – 2024", "role": "Project Engineer",
     "fig": "40%", "fig_label": "lower material rejection rates",
     "card": "Supplier evaluation frameworks, technical guidelines and system designs for mega infrastructure and technology projects.",
     "mandate": "Bring consistency to the materials and designs behind mega infrastructure and smart traffic enforcement projects.",
     "complexity": "Civil and power materials from many suppliers, engineering teams that needed a shared design approach, and government stakeholders to keep informed throughout.",
     "how": ["Established supplier evaluation frameworks and approved 28+ suppliers for civil and power materials",
             "Authored two technical guidelines and seven system designs that standardized the design approach",
             "Tested, diagnosed and validated new technologies",
             "Maintained risk registers with regular reporting"],
     "result": ["Material rejection rates reduced by 40%",
                "Shorter procurement cycle time and better vendor quality",
                "Less rework and stronger quality assurance"],
     "tags": ["Vendor governance", "Standards", "Quality assurance", "Risk registers"]},
    {"slug": "moe-infrastructure-rehabilitation",
     "title": "SAR 28M infrastructure rehabilitation for the Ministry of Education",
     "short": "SAR 28M Ministry of Education project",
     "org": "Tatweer Buildings Company", "years": "2021 – 2022", "role": "Project Manager",
     "fig": "2 weeks", "fig_label": "ahead of schedule, within budget",
     "card": "Full-lifecycle delivery of a government infrastructure project, from planning to handover.",
     "mandate": "Deliver a SAR 28M infrastructure reconstruction project for the Ministry of Education, covering site reconstruction, MEP systems and handover documentation.",
     "complexity": "A full project lifecycle with contractors, internal teams and a government client, and the technical and contractual issues that reconstruction work brings.",
     "how": ["Managed the full lifecycle, from planning and execution to monitoring and closure",
             "Led communication across internal teams, contractors and the client",
             "Resolved technical and contractual issues to keep delivery moving",
             "Held the project to quality standards and timelines"],
     "result": ["Delivered two weeks ahead of schedule and within budget",
                "Full compliance with quality and safety standards"],
     "tags": ["Full-lifecycle delivery", "Government client", "Contractor management", "Saudi Building Code"]},
    {"slug": "center-of-excellence",
     "title": "A Center of Excellence that helped lift a firm to 1st grade",
     "short": "Center of Excellence and 1st-grade upgrade",
     "org": "Khazaz Engineering Office", "years": "2017 – 2020", "role": "Assistant Project Manager",
     "fig": "3rd → 1st", "fig_label": "grade classification",
     "card": "Standardized processes, documentation and bidding behind the firm's upgrade in classification.",
     "mandate": "Standardize how the firm ran its projects, documentation and bids, and align them with its strategic plan.",
     "complexity": "Public infrastructure tenders that demanded accurate bills of quantities, and a firm working toward a higher contractor classification.",
     "how": ["Launched the internal Center of Excellence to standardize processes and documentation",
             "Prepared BOQs and bidding packages for public infrastructure tenders",
             "Led training, documentation and audit preparation"],
     "result": ["Contributed to the firm's upgrade from 3rd to 1st-grade classification",
                "Better bid alignment with project goals, with higher contract win rates and budget accuracy"],
     "tags": ["PMO foundations", "Standardization", "Bidding & cost estimation", "Strategic alignment"]},
]

# ---------------------------------------------------------------------------
# Credentials
# ---------------------------------------------------------------------------
CORE_CERTS = [
    {"abbr": "PMP", "name": "Project Management Professional", "issuer": "Project Management Institute", "year": "2021"},
    {"abbr": "RMP", "name": "PMI Risk Management Professional", "issuer": "Project Management Institute", "year": "2022"},
    {"abbr": "P3O", "name": "Portfolio, Programme and Project Offices", "issuer": "PeopleCert", "year": "2023"},
]
PERF_CERTS = [
    {"name": "Certified OKR Professional", "issuer": "The KPI Institute", "year": "2022", "icon": "target"},
    {"name": "Key Performance Indicators", "issuer": "The KPI Institute", "year": "2022", "icon": "report"},
]
CONTINUING = [
    ("Power BI", "Money Experts Institute for Training", "2023"),
    ("Introduction to Data Analytics", "Coursera", "2023"),
    ("Internet of Things (IoT)", "PwC", "2023"),
    ("Business presentation course", "PwC's Academy", "2023"),
]
HIPO = {
    "title": "High Potential (HiPo) Leadership Development Program",
    "host": "TAHAKOM",
    "selected": "Selected as one of 60 high-potential employees from 1,200 candidates for an eight-month program to develop future leaders.",
    "steps": [
        {"when": "May 2025", "name": "Selected: 60 of 1,200 candidates", "inst": "Eight-month program begins", "kind": "milestone"},
        {"when": "Jul 2025", "name": "Discovering and Implementing Your Leadership Strengths", "inst": "Massachusetts Institute of Technology"},
        {"when": "Sep 2025", "name": "Customer Centric Solutions with Design Thinking & Innovation", "inst": "National University of Singapore"},
        {"when": "Oct 2025", "name": "Smart Work Strategies for Collaboration", "inst": "ESCP Business School, London"},
        {"when": "Oct 2025", "name": "AI Strategies for Business Transformation", "inst": "Northwestern University, Kellogg School of Management"},
        {"when": "2025", "name": "Driving Strategy Innovation", "inst": "HiPo program module"},
        {"when": "Dec 2025", "name": "Graduated", "inst": "High Potential Development Program", "kind": "milestone"},
    ],
}
HIPO_MODULES = [s for s in HIPO["steps"] if s.get("kind") != "milestone"]
INSTITUTIONS = ["MIT", "National University of Singapore", "ESCP Business School", "Kellogg School of Management"]
EDUCATION = {"degree": "Bachelor's degree, Civil Engineering",
             "school": "Imam Mohammad Ibn Saud Islamic University (IMSIU)", "years": "2014 – 2019"}
RECOGNITION = ("Honoured for the accomplishment of 2023 targets", "TAHAKOM")

# ---------------------------------------------------------------------------
# Executive bio — DRAFT, third person, for organizers, boards and media
# ---------------------------------------------------------------------------
BIO_SHORT = ("Ayman Alawwad is a PMO and portfolio leader based in Riyadh, with more than ten years of experience "
             "bridging strategy and execution across technology, infrastructure and government environments. He has "
             "managed and delivered projects and portfolios exceeding SAR 500 million, and has earned the PMP®, "
             "PMI-RMP® and P3O® certifications.")
BIO_LONG = ("Ayman Alawwad is a PMO and portfolio management leader with more than ten years of experience across "
            "portfolio governance, strategic initiatives, technology, infrastructure, construction and government "
            "environments in Saudi Arabia. He combines hands-on delivery with portfolio-level governance to strengthen "
            "accountability, improve executive visibility and support effective decision-making.\n\n"
            "At TAHAKOM he led the end-to-end delivery of national-level smart traffic violation detection systems across "
            "multiple Saudi cities, working with government and private-sector stakeholders, multi-vendor environments and "
            "cross-functional teams of more than 17. Earlier, he delivered a SAR 28 million infrastructure project for the "
            "Ministry of Education two weeks ahead of schedule, and launched a Center of Excellence that supported his firm's "
            "upgrade from 3rd- to 1st-grade classification.\n\n"
            "He has earned the PMP®, PMI-RMP® and P3O® certifications, and was selected among 60 of 1,200 candidates for an "
            "eight-month High Potential leadership program with modules from MIT, the National University of Singapore, "
            "ESCP Business School and Northwestern University's Kellogg School of Management. He holds a bachelor's degree "
            "in civil engineering from Imam Mohammad Ibn Saud Islamic University.")

FAQ = [
    ("What does Ayman Alawwad specialize in?",
     "PMO governance, portfolio and program management, strategy execution, RAID management and executive reporting, "
     "across technology, infrastructure, construction and government environments in Saudi Arabia."),
    ("Which professional certifications has he earned?",
     "PMP® (Project Management Institute, 2021), PMI-RMP® (2022) and P3O® (PeopleCert, 2023), together with "
     "Certified OKR Professional and Key Performance Indicators certifications from The KPI Institute."),
    ("Which delivery models does he work with?",
     "Agile, Waterfall and hybrid delivery, with a strong focus on governance, business value, risk, cost, "
     "schedule, stakeholder management and operational readiness."),
    ("What executive education has he completed?",
     "An eight-month High Potential leadership program, selected as one of 60 from 1,200 candidates, with modules "
     "from MIT, the National University of Singapore, ESCP Business School and Northwestern University's Kellogg "
     "School of Management."),
    ("Where is he based?", "Riyadh, Saudi Arabia."),
]

# ---------------------------------------------------------------------------
# Points for Ayman to confirm before launch (not shown on the site)
# ---------------------------------------------------------------------------
REVIEW = [
    "PMI-RMP (Jun 2022) and P3O (Apr 2023) show as expired on LinkedIn; PMP (2021) is not in the Licenses section. Site shows the year earned only.",
    "40%: LinkedIn has 'system rejection and missing rates' (experience) and 'material rejection rates' (projects). Site uses the projects wording.",
    "Guidelines and designs: '2+ / 7+' (experience) vs '2 / 7' (projects). Site uses 2 and 7.",
    "TAHAKOM shown as 2022 – 2026 (from his Aug 2026 farewell post); LinkedIn still says Present.",
    "HiPo: module months are taken from post dates; 'Driving Strategy Innovation' has no published date or institution.",
    "DRAFT wording for his review: the four 'How I lead' principles and the executive bio.",
    "Photo and email: GitHub preview shows the AA monogram; email hidden until he approves.",
]
