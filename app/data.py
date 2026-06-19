"""
Central place for all portfolio content.

Keeping this data separate from __init__.py means:
- Adding a new job / degree / hobby is just adding one dict to a list.
- The HTML templates loop over these lists with Jinja instead of
  having hardcoded, repeated markup for every entry.
"""

NAV_LINKS = [
    {"name": "Team Home", "endpoint": "index"},
    {"name": "Sri Nidhi", "endpoint": "sri_nidhi"},
    {"name": "Sri Hobbies", "endpoint": "sri_nidhi_hobbies"},
]

TEAM_MEMBERS = [
    {
        "name": "Sri Nidhi Kuchana",
        "role": "B.Tech CSE Student & MLH Fellow",
        "description": (
            "Sri Nidhi is passionate about AI, full-stack development, "
            "data analytics, and building practical technology projects."
        ),
        "portfolio_endpoint": "sri_nidhi",
        "hobbies_endpoint": "sri_nidhi_hobbies",
        "initials": "SN",
    },
    {
        "name": "Aziz Ercoban",
        "role": "Computer Science Student & MLH Fellow",
        "description": (
            "Aziz is interested in backend engineering, AI systems, "
            "production engineering, and building real-world software projects."
        ),
        "portfolio_endpoint": "aziz",
        "hobbies_endpoint": "aziz_hobbies",
        "initials": "AE",
    },
]

ABOUT_ME = (
    "Hi, I'm Sri Nidhi Kuchana — a B.Tech CSE student at Malla Reddy "
    "Engineering College for Women, currently in my 3rd year. I'm passionate "
    "about building practical AI and full-stack projects, from satellite-data "
    "powered crop advisories to voice assistants with emotion recognition. "
    "Outside of code, I serve as my class's Class Representative, I'm a "
    "member of the college Film Club, and I'm genuinely curious about "
    "derivative markets and how trading works. I'm currently an MLH Fellow "
    "on the Site Reliability Engineering track, working alongside Meta "
    "engineers this summer."
)

EXPERIENCES = [
    {
        "title": "AI Engineer Intern",
        "company": "MetaTaaraka AI Innovations Pvt. Ltd.",
        "dates": "Dec 2025 – Mar 2026",
        "location": "",
        "bullets": [
            "Designed and deployed AI-powered solutions including NLP pipelines and ML model integrations for production systems.",
            "Worked on production-grade AI systems using Python, TensorFlow, and cloud-based infrastructure (OCI).",
        ],
    },
    {
        "title": "AI & Data Analytics Intern",
        "company": "Edunet Foundation",
        "dates": "Oct 2025 – Nov 2025",
        "location": "Virtual",
        "bullets": [
            "Built an end-to-end AI & Data Analytics project (EV Type Predictor) covering data collection, cleaning, preprocessing, and EDA.",
            "Performed exploratory data analysis to identify patterns and correlations in electric vehicle datasets.",
        ],
    },
    {
        "title": "Full Stack Developer Intern",
        "company": "Thiranex",
        "dates": "Apr 2026 – May 2026",
        "location": "Remote",
        "bullets": [
            "Developed and maintained full stack web applications using React.js, Node.js, and REST APIs in a remote agile environment.",
            "Collaborated with cross-functional teams to design and implement scalable front-end interfaces and back-end services.",
            "Contributed to code reviews, bug fixes, and feature delivery across the full development lifecycle.",
        ],
    },
    {
        "title": "Python Full Stack Development Intern",
        "company": "RVNS Solutions Pvt. Ltd.",
        "dates": "June 2026",
        "location": "",
        "bullets": [
            "Developed full-stack web applications using Python, Flask, HTML, CSS, and JavaScript, implementing responsive front-end and back-end functionality.",
            "Designed and managed MySQL databases and integrated front-end with back-end services on real-world projects.",
        ],
    },
]

EDUCATION = [
    {
        "school": "Malla Reddy Engineering College for Women",
        "degree": "B.Tech in Computer Science & Engineering",
        "dates": "2024 – 2028",
        "details": "CGPA: 9.32 · Class Representative · Film Club Member",
    },
]

HOBBIES = [
    {
        "name": "Film Club",
        "description": "Active member of my college Film Club, exploring storytelling through film and screenings.",
        "image": "film-club.svg",
    },
    {
        "name": "Derivative Markets & Trading",
        "description": "Following options, futures, and swaps markets — fascinated by how risk and pricing work.",
        "image": "trading.svg",
    },
    {
        "name": "Competitive Programming",
        "description": "Solving DSA problems across HackerRank, CodeChef, and LeetCode.",
        "image": "coding.svg",
    },
    {
        "name": "Building AI Side Projects",
        "description": "Hackathon and demo projects like AgriSat, voice assistants, and chatbots — coding for fun outside of class.",
        "image": "ai-projects.svg",
    },
]

TRAVEL_PLACES = [
    {"name": "Singapore", "lat": 1.352083, "lng": 103.819836},
]


AZIZ_ABOUT_ME = (
    "Hi, I'm Aziz Ercoban, a Computer Science student at Trinity College Dublin. "
    "I enjoy building backend systems, AI-powered applications, and practical software "
    "projects using Python, Flask, Django, SQL, Docker, and JavaScript. I am especially "
    "interested in backend engineering, production engineering, reliability, and turning "
    "ideas into real working products."
)

AZIZ_EXPERIENCES = [
    {
        "title": "Backend & AI Engineer",
        "company": "Propylon – AI-Native Legislative Research Platform",
        "dates": "Dec 2025 – Mar 2026",
        "location": "Remote",
        "bullets": [
            "Worked on backend and AI features for a legislative research platform.",
            "Built workflows for Congress.gov data ingestion, legal-text chunking, embedding generation, semantic retrieval, reranking, caching, and citation validation.",
            "Used Python, FastAPI-style backend patterns, search/retrieval systems, and AI tooling to support reliable legal research features.",
        ],
    },
    {
        "title": "Software Development Intern",
        "company": "Cocoon Creations",
        "dates": "Summer 2026",
        "location": "Cyprus",
        "bullets": [
            "Working as a software development intern on real company projects.",
            "Contributing to backend and web development tasks while improving practical engineering skills.",
        ],
    },
    {
        "title": "Production Engineering Fellow",
        "company": "MLH Fellowship",
        "dates": "Summer 2026",
        "location": "Remote",
        "bullets": [
            "Selected for the Meta Production Engineering Fellowship through MLH.",
            "Learning and applying production engineering and site reliability engineering concepts through hands-on technical work.",
        ],
    },
]

AZIZ_EDUCATION = [
    {
        "school": "Trinity College Dublin",
        "degree": "Integrated Computer Science",
        "dates": "2024 – 2028",
        "details": (
            "Completed Year 1 with First Class Honours. Relevant areas include programming, "
            "data structures and algorithms, computer systems, statistics, databases, and software engineering."
        ),
    },
]

AZIZ_TRAVEL_PLACES = [
    {"name": "Dublin, Ireland", "lat": 53.3498, "lng": -6.2603},
    {"name": "Nicosia, Cyprus", "lat": 35.1856, "lng": 33.3823},
    {"name": "Kyrenia, Cyprus", "lat": 35.3403, "lng": 33.3192},
    {"name": "Berlin, Germany", "lat": 52.5200, "lng": 13.4050},
    {"name": "Athens, Greece", "lat": 37.9838, "lng": 23.7275},
]