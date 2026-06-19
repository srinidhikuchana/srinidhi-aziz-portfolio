"""
Central place for all portfolio content.

Keeping this data separate from __init__.py means:
- Adding a new job / degree / hobby is just adding one dict to a list.
- The HTML templates loop over these lists with Jinja instead of
  having hardcoded, repeated markup for every entry.
"""

NAV_LINKS = [
    {"name": "Home", "endpoint": "index"},
    {"name": "Hobbies", "endpoint": "hobbies"},
]

ABOUT_ME = (
    "Hi, I'm Sri Nidhi Kuchana \u2014 a B.Tech CSE student at Malla Reddy "
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
        "dates": "Dec 2025 \u2013 Mar 2026",
        "location": "",
        "bullets": [
            "Designed and deployed AI-powered solutions including NLP pipelines and ML model integrations for production systems.",
            "Worked on production-grade AI systems using Python, TensorFlow, and cloud-based infrastructure (OCI).",
        ],
    },
    {
        "title": "AI & Data Analytics Intern",
        "company": "Edunet Foundation",
        "dates": "Oct 2025 \u2013 Nov 2025",
        "location": "Virtual",
        "bullets": [
            "Built an end-to-end AI & Data Analytics project (EV Type Predictor) covering data collection, cleaning, preprocessing, and EDA.",
            "Performed exploratory data analysis to identify patterns and correlations in electric vehicle datasets.",
        ],
    },
    {
        "title": "Full Stack Developer Intern",
        "company": "Thiranex",
        "dates": "Apr 2026 \u2013 May 2026",
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
        "dates": "2024 \u2013 2028",
        "details": "CGPA: 9.32 \u00b7 Class Representative \u00b7 Film Club Member",
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
        "description": "Following options, futures, and swaps markets \u2014 fascinated by how risk and pricing work.",
        "image": "trading.svg",
    },
    {
        "name": "Competitive Programming",
        "description": "Solving DSA problems across HackerRank (5\u2605), CodeChef (485+), and LeetCode (54+).",
        "image": "coding.svg",
    },
    {
        "name": "Building AI Side Projects",
        "description": "Hackathon and demo projects like AgriSat, voice assistants, and chatbots \u2014 coding for fun outside of class.",
        "image": "ai-projects.svg",
    },
]

TRAVEL_PLACES = [
    {"name": "Singapore", "lat": 1.352083, "lng": 103.819836},
]
