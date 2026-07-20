# TECH_KEYWORDS = {

#     "data",
#     "software",
#     "developer",
#     "engineer",
#     "machine learning",
#     "ml",
#     "ai",
#     "artificial intelligence",
#     "backend",
#     "frontend",
#     "full stack",
#     "fullstack",
#     "devops",
#     "cloud",
#     "security",
#     "cyber",
#     "gis",
#     "database",
#     "sql",
#     "analytics",
#     "analyst",
#     "business intelligence",
#     "bi",
#     "product manager",
#     "qa",
#     "test",
#     "automation",
#     "mobile",
#     "android",
#     "ios",
#     "react",
#     "python",
# }

TECH_KEYWORDS = {

    # Data
    "data",
    "analytics",
    "analyst",
    "scientist",
    "bi",
    "business intelligence",

    # Software
    "software",
    "developer",
    "engineer",
    "backend",
    "frontend",
    "full stack",
    "fullstack",
    "mobile",
    "android",
    "ios",

    # AI
    "machine learning",
    "ml",
    "ai",
    "artificial intelligence",

    # Infrastructure
    "cloud",
    "devops",
    "site reliability",
    "sre",
    "platform",
    "infrastructure",

    # Security
    "security",
    "cyber",
    "application security",
    "DevSecOps",

    # GIS
    "gis",
    "geospatial",

    # QA
    "qa",
    "quality assurance",
    "test automation",

    # Product
    "technical product",
    "product manager",
    "product owner",

    # Architecture
    "solutions architect",
    "architect",

    # Database
    "database",
    "sql",

    # UI/UX
    "ux",
    "ui",
    "designer",

    # Support
    "technical support",
    "support engineer",
    "implementation",

}

def is_tech_job(title: str) -> bool:

    if not title:
        return False

    title = title.lower()

    return any(keyword in title for keyword in TECH_KEYWORDS)