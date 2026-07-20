from dataclasses import dataclass


@dataclass
class Job:
    title: str
    company: str
    location: str
    description: str
    department: str
    employment_type: str
    posted_date: str
    url: str
    ats: str