from src.utils.tech_filter import is_tech_job

titles = [
    "Software Engineer",
    "Data Scientist",
    "Machine Learning Engineer",
    "Backend Developer",
    "Finance Manager",
    "Chef",
    "Driver",
    "HR Officer",
    "Marketing Executive",
]

for title in titles:
    print(title, "->", is_tech_job(title))