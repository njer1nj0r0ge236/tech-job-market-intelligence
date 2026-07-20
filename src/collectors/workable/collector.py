from src.collectors.workable.client import WorkableClient
from src.collectors.workable.parser import WorkableParser

from src.utils.location import is_kenya_job
from src.utils.tech_filter import is_tech_job


class WorkableCollector:
    """
    Coordinates data collection from Workable.
    """

    def __init__(self):
        self.client = WorkableClient()
        self.parser = WorkableParser()

    def collect(self, account_slug: str, company_name: str):

        raw_jobs = self.client.get_jobs(account_slug)

        parsed_jobs = []

        for job in raw_jobs:

            parsed_job = self.parser.parse(
                job,
                company_name
            )

            if (
                is_kenya_job(parsed_job["location"])
                and is_tech_job(parsed_job["title"])
            ):
                parsed_jobs.append(parsed_job)

        return parsed_jobs