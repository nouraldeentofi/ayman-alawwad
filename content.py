"""All site content for Ayman Alawwad's site (English only).

Every fact here traces back to brief.md (LinkedIn, collected 2026-10-19).
Edit texts here, then run:  python3 build.py
"""

# ---------------------------------------------------------------------------
# CONFIG — empty values stay hidden on the site
# ---------------------------------------------------------------------------
CONFIG = {
    "NAME": "Ayman Alawwad",
    "NAME_AR": "أيمن العواد",
    "EMAIL": "",                      # hidden on the public preview — add after Ayman approves
    "PHONE": "",                      # left empty on purpose — add only with Ayman's OK
    "WHATSAPP": "",
    "LINKEDIN": "https://www.linkedin.com/in/ayman-alawwad-0b9724185/",
    "LOCATION": "Riyadh, Saudi Arabia",
    "PHOTO": "assets/img/ayman.jpg",  # set "" to show the monogram instead
    "PHOTO_WEBP": "assets/img/ayman.webp",
    "BASE_URL": "https://nouraldeentofi.github.io/ayman-alawwad",  # change when a custom domain is added
    "MAKER": "https://nouraldeentofi.com",
    "PREVIEW": True,                  # True = private preview: noindex + robots Disallow. Set False after approval.
}

HEADLINE = "PMO Manager · Portfolio & Program Management"
STATEMENT = "Bridging strategy and execution through portfolio governance."
INTRO = ("Ten-plus years leading projects, programs and portfolios across technology, "
         "infrastructure, construction and government environments in Saudi Arabia.")

FIGURES = [
    {"pre": "", "num": 10, "suf": "+", "label": "Years in project, program & portfolio management"},
    {"pre": "SAR ", "num": 500, "suf": "M+", "label": "Projects and portfolios managed and delivered"},
    {"pre": "", "num": 28, "suf": "+", "label": "Suppliers evaluated and approved"},
    {"pre": "", "num": 17, "suf": "+", "label": "Cross-functional team members led"},
]

ABOUT = [
    "I am a PMO and project/program management professional with more than ten years of experience across "
    "portfolio governance, strategic initiatives, technology, infrastructure, construction and government "
    "environments in Saudi Arabia.",
    "My work combines hands-on project delivery with portfolio-level governance — bridging strategy and "
    "execution, strengthening accountability, improving executive visibility and supporting effective "
    "decision-making.",
    "I have managed and delivered projects and portfolios exceeding SAR 500M, working with government "
    "stakeholders, executives, multidisciplinary teams and more than 28 suppliers across complex delivery "
    "environments.",
]

# Six capability pillars — description from his About, "in practice" from his experience
PILLARS = [
    {"icon": "network", "title": "PMO establishment & governance",
     "text": "Establishing PMO governance frameworks that make accountability, standards and decisions visible.",
     "proof": "Launched a Center of Excellence that standardized processes and supported a 3rd-to-1st grade classification upgrade."},
    {"icon": "layers", "title": "Portfolio & program management",
     "text": "Managing and delivering projects and portfolios exceeding SAR 500M across multiple sectors.",
     "proof": "Directed giga-scale infrastructure and technology deployments across 3+ concurrent projects."},
    {"icon": "target", "title": "Strategy execution & prioritization",
     "text": "Strategic alignment and prioritization that keep delivery tied to what the organization set out to achieve.",
     "proof": "Ensured alignment between business requirements and technical delivery on national-level systems."},
    {"icon": "shield", "title": "Risk & RAID management",
     "text": "Risks, assumptions, issues and dependencies tracked and reported — PMI-RMP® certified.",
     "proof": "Monitored risks and maintained risk registers with regular reporting."},
    {"icon": "report", "title": "Executive reporting & stakeholders",
     "text": "Executive reporting and stakeholder management with government entities, executives and multidisciplinary teams.",
     "proof": "Managed stakeholders across government and private sector entities."},
    {"icon": "check", "title": "Vendor & supply governance",
     "text": "Multi-vendor environments managed for performance and compliance.",
     "proof": "Evaluated and approved 28+ suppliers; material rejection rates reduced by 40%."},
]

ENVIRONMENTS = ["Portfolio governance", "Strategic initiatives", "Technology", "Infrastructure",
                "Construction", "Government"]
FOCUS = ["Governance", "Business value", "Risk", "Cost", "Schedule", "Stakeholder management",
         "Operational readiness"]

# P3O-style cascade — every phrase taken from his About
CASCADE = [
    {"level": "Strategy", "text": "Strategic alignment and prioritization"},
    {"level": "Portfolio", "text": "Portfolio governance and executive reporting"},
    {"level": "Program", "text": "Program management and cross-functional delivery"},
    {"level": "Project", "text": "Agile, Waterfall and hybrid delivery — risk, cost and schedule under control"},
    {"level": "Operations", "text": "Operational readiness and business value"},
]

QUOTE = {
    "lines": ["Not every project fits one box.", "In real world delivery, hybrid project management wins."],
    "punch": "structure + flexibility = results",
    "cite": "Ayman Alawwad, on hybrid delivery",
}

# ---------------------------------------------------------------------------
# Career (past employers only — no current employer details)
# ---------------------------------------------------------------------------
CAREER = [
    {"org": "TAHAKOM", "place": "Riyadh", "years": "2022 – 2026",
     "summary": "Smart traffic enforcement and technology programs delivered for national-level operations.",
     "roles": [
         {"title": "Project Manager", "years": "2024 – 2026", "points": [
             "Led end-to-end delivery of smart traffic violation detection systems, from concept to operation",
             "Delivered high-impact national-level systems supporting traffic enforcement operations",
             "Managed stakeholders across government and private sector entities",
             "Delivered 5+ hybrid (Agile/Waterfall) projects and acted as Product Owner for 2+ Agile projects",
             "Led cross-functional teams of 17+ members",
             "Managed multi-vendor environments, ensuring performance and compliance",
             "Ensured alignment between business requirements and technical delivery",
         ]},
         {"title": "Project Engineer", "years": "2022 – 2024", "points": [
             "Reduced system rejection and missing rates by 40% through advanced technologies",
             "Evaluated and approved 28+ suppliers for civil and power materials",
             "Authored 2+ technical guidelines and 7+ engineering designs",
             "Led cross-functional collaboration between engineering and project teams",
             "Conducted testing, diagnostics and validation for new technologies",
             "Monitored risks and maintained risk registers with regular reporting",
         ]},
     ],
     "honour": "Honoured for the accomplishment of 2023 targets"},
    {"org": "Tatweer Buildings Company", "place": "Riyadh", "years": "2021 – 2022",
     "summary": "Infrastructure reconstruction for the Ministry of Education.",
     "roles": [
         {"title": "Project Manager", "years": "2021 – 2022", "points": [
             "Delivered an infrastructure reconstruction project valued at SAR 28M for the Ministry of Education, on schedule and within budget",
             "Managed the full project lifecycle — planning, execution, monitoring and closure",
             "Led stakeholder communication across internal teams, contractors and clients",
             "Resolved technical and contractual issues to keep delivery on track",
             "Ensured adherence to quality standards and project timelines",
         ]},
     ]},
    {"org": "Khazaz Engineering Office", "place": "Riyadh", "years": "2016 – 2021",
     "summary": "From quality assurance to project management — and a firm upgraded to 1st grade.",
     "roles": [
         {"title": "Project Manager", "years": "2020 – 2021", "points": [
             "Managed project planning, bidding and execution aligned with organizational strategy",
             "Prepared bidding documents and evaluated project opportunities",
             "Led stakeholder meetings and reported performance to senior management",
         ]},
         {"title": "Assistant Project Manager", "years": "2017 – 2020", "points": [
             "Contributed to raising the company classification from 3rd to 1st grade",
             "Established a Center of Excellence to standardize processes and improve efficiency",
             "Prepared BOQs for government project bidding",
         ]},
         {"title": "Quality Assurance Specialist", "years": "2016 – 2017", "points": [
             "Managed QA programs and HSE compliance across projects",
             "Conducted audits and prepared quality reports",
         ]},
     ]},
    {"org": "The Royal Commission for Riyadh City", "place": "Riyadh", "years": "2018",
     "summary": "Early exposure to city-scale programs.",
     "roles": [
         {"title": "Trainee Civil Engineer", "years": "Jun – Sep 2018", "points": [
             "Al-Ddoho project — revival of an old area of Riyadh through different design approaches on infrastructure and substructure",
             "Overview of the Riyadh Metro project from civil, mechanical and electrical perspectives",
         ]},
     ]},
]

# ---------------------------------------------------------------------------
# Selected work — one page each
# ---------------------------------------------------------------------------
WORK = [
    {"slug": "violation-detection-nationwide-rollout",
     "title": "Violation Detection System — Nationwide Rollout",
     "short": "Nationwide violation detection rollout",
     "org": "TAHAKOM", "years": "2024 – 2026", "role": "Project Manager",
     "fig": "5+", "fig_label": "hybrid projects delivered",
     "summary": "Led full-cycle delivery of new violation detection systems across multiple cities in Saudi Arabia — stakeholder alignment, technical execution and delivery from concept to operation.",
     "outcomes": ["Delivered 5+ hybrid-methodology projects",
                  "Oversaw government and private sector coordination",
                  "Ensured timely launch of site operations nationwide"],
     "tags": ["Program & Portfolio Management", "Hybrid delivery", "Government stakeholders"]},
    {"slug": "giga-multi-sector-deployments",
     "title": "Giga Project Management for Multi-Sector Deployments",
     "short": "Giga-scale multi-sector deployments",
     "org": "TAHAKOM", "years": "2024 – 2026", "role": "Project Manager",
     "fig": "3+", "fig_label": "concurrent projects prioritized",
     "summary": "Directed giga-scale infrastructure and technology deployments for high-profile public and private clients.",
     "outcomes": ["Coordinated multiple engineering streams and stakeholder groups",
                  "Prioritized conflicting deadlines across 3+ concurrent projects",
                  "Implemented solutions on time, ensuring resource and budget optimization"],
     "tags": ["Program & Portfolio Management", "Saudi Building Code", "Prioritization"]},
    {"slug": "supplier-evaluation-standardization",
     "title": "Supplier Evaluation and Standardization Program",
     "short": "Supplier evaluation & standardization",
     "org": "TAHAKOM", "years": "2022 – 2024", "role": "Project Engineer",
     "fig": "40%", "fig_label": "lower material rejection rates",
     "summary": "Evaluated and approved more than 28 suppliers for civil and power materials across mega infrastructure and technology projects.",
     "outcomes": ["Established supplier evaluation frameworks",
                  "Reduced material rejection rates by 40%",
                  "Improved procurement cycle time and vendor quality"],
     "tags": ["Vendor governance", "Quality", "Procurement"]},
    {"slug": "guidelines-and-designs-technology-projects",
     "title": "Guideline & Design Creation for Technology Projects",
     "short": "Technical guidelines & system designs",
     "org": "TAHAKOM", "years": "2022 – 2024", "role": "Project Engineer",
     "fig": "2 · 7", "fig_label": "guidelines · system designs",
     "summary": "Authored two technical guidelines and developed seven system designs for smart traffic enforcement projects.",
     "outcomes": ["Standardized the design approach across engineering teams",
                  "Reduced rework and improved quality assurance"],
     "tags": ["Standards", "Saudi Building Code", "Quality assurance"]},
    {"slug": "infrastructure-rehabilitation-28m",
     "title": "Infrastructure Rehabilitation Project — SAR 28M",
     "short": "SAR 28M infrastructure rehabilitation",
     "org": "Tatweer Buildings Company", "years": "2021 – 2022", "role": "Project Manager",
     "fig": "2 weeks", "fig_label": "ahead of schedule",
     "summary": "Delivered a SAR 28M infrastructure project for the Ministry of Education, covering site reconstruction, MEP systems and handover documentation.",
     "outcomes": ["Delivered two weeks ahead of schedule, within budget",
                  "Maintained full compliance with quality and safety standards",
                  "Facilitated contractor coordination and stakeholder reporting"],
     "tags": ["Full lifecycle delivery", "Saudi Building Code", "Government client"]},
    {"slug": "center-of-excellence-strategic-plan",
     "title": "Center of Excellence & Strategic Plan",
     "short": "Center of Excellence & strategic plan",
     "org": "Khazaz Engineering Office", "years": "2017 – 2020", "role": "Assistant Project Manager",
     "fig": "3rd → 1st", "fig_label": "grade classification",
     "summary": "Launched the firm's internal Center of Excellence to standardize processes, documentation and strategic alignment.",
     "outcomes": ["Contributed to the firm's upgrade from 3rd to 1st-grade classification",
                  "Led training, documentation and audit preparation"],
     "tags": ["PMO foundations", "Program & Portfolio Management", "Standardization"]},
    {"slug": "boq-and-bidding-government-projects",
     "title": "BOQ & Bidding Documents for Government Projects",
     "short": "BOQ & bidding for public tenders",
     "org": "Khazaz Engineering Office", "years": "2017 – 2020", "role": "Assistant Project Manager",
     "fig": "Public", "fig_label": "infrastructure tenders",
     "summary": "Prepared comprehensive bills of quantities and bidding packages for public infrastructure tenders.",
     "outcomes": ["Improved bid alignment with project goals",
                  "Increased contract win rates and budget accuracy"],
     "tags": ["Cost estimation", "Saudi Building Code", "Bidding"]},
]
FEATURED_WORK = ["violation-detection-nationwide-rollout", "infrastructure-rehabilitation-28m",
                 "center-of-excellence-strategic-plan"]

# ---------------------------------------------------------------------------
# Credentials
# ---------------------------------------------------------------------------
CORE_CERTS = [
    {"abbr": "PMP", "name": "Project Management Professional", "issuer": "Project Management Institute", "year": "2021"},
    {"abbr": "RMP", "name": "PMI Risk Management Professional", "issuer": "Project Management Institute", "year": "2022"},
    {"abbr": "P3O", "name": "Portfolio, Programme and Project Offices", "issuer": "PeopleCert", "year": "2023"},
]
MORE_CERTS = [
    {"name": "Certified OKR Professional", "issuer": "The KPI Institute", "year": "2022", "icon": "target"},
    {"name": "Key Performance Indicators", "issuer": "The KPI Institute", "year": "2022", "icon": "report"},
    {"name": "Power BI", "issuer": "Money Experts Institute for Training", "year": "2023", "icon": "chart"},
    {"name": "Introduction to Data Analytics", "issuer": "Coursera", "year": "2023", "icon": "chart"},
    {"name": "Internet of Things (IoT)", "issuer": "PwC", "year": "2023", "icon": "network"},
    {"name": "Powerful Business Presentation", "issuer": "PwC's Academy", "year": "2023", "icon": "present"},
]
HIPO = {
    "title": "High Potential (HiPo) Leadership Development Program",
    "host": "TAHAKOM",
    "selected": "Selected as one of 60 high-potential employees from 1,200 candidates for an eight-month program to develop future leaders.",
    "graduated": "Graduated December 2025",
    "modules": [
        {"name": "Discovering and Implementing Your Leadership Strengths", "inst": "Massachusetts Institute of Technology", "when": "Jul 2025"},
        {"name": "Customer Centric Solutions with Design Thinking & Innovation", "inst": "National University of Singapore", "when": "Sep 2025"},
        {"name": "Smart Work Strategies for Collaboration", "inst": "ESCP Business School, London", "when": "Oct 2025"},
        {"name": "AI Strategies for Business Transformation", "inst": "Northwestern University — Kellogg School of Management", "when": "Oct 2025"},
    ],
}
INSTITUTIONS = ["MIT", "National University of Singapore", "ESCP Business School", "Kellogg School of Management"]
EDUCATION = {"degree": "Bachelor's degree, Civil Engineering",
             "school": "Imam Mohammad Ibn Saud Islamic University (IMSIU)", "years": "2014 – 2019"}
RECOGNITION = "Honoured for the accomplishment of 2023 targets — TAHAKOM"

FAQ = [
    ("What does Ayman Alawwad specialize in?",
     "PMO establishment and governance, portfolio and program management, strategy execution, RAID management "
     "and executive reporting — across technology, infrastructure, construction and government environments in Saudi Arabia."),
    ("Which professional certifications has he earned?",
     "PMP® (Project Management Institute, 2021), PMI-RMP® (2022) and P3O® (PeopleCert, 2023), together with "
     "Certified OKR Professional and Key Performance Indicators certifications from The KPI Institute."),
    ("Which delivery models does he work with?",
     "Agile, Waterfall and hybrid delivery, with a strong focus on governance, business value, risk, cost, "
     "schedule, stakeholder management and operational readiness."),
    ("What executive education has he completed?",
     "An eight-month High Potential leadership program with modules from MIT, the National University of "
     "Singapore, ESCP Business School and Northwestern University's Kellogg School of Management."),
    ("Where is he based?", "Riyadh, Saudi Arabia."),
]
