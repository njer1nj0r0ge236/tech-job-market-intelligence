from src.collectors.breezy.client import BreezyClient
from src.collectors.breezy.parser import BreezyParser

from src.utils.location import is_kenya_job
from src.utils.tech_filter import is_tech_job


class BreezyCollector:
    """
    Coordinates data collection from BreezyHR.
    """

    def __init__(self):
        self.client = BreezyClient()
        self.parser = BreezyParser()

    def collect(self, company_slug: str):

        raw_jobs = self.client.get_jobs(company_slug)

        parsed_jobs = []

        for job in raw_jobs:

            parsed_job = self.parser.parse(job)

            if (
                is_kenya_job(parsed_job["location"])
                and
                is_tech_job(parsed_job["title"])
            ):
                parsed_jobs.append(parsed_job)

        return parsed_jobs