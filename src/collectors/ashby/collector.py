from src.collectors.ashby.client import AshbyClient
from src.collectors.ashby.parser import AshbyParser

from src.utils.location import is_kenya_job


class AshbyCollector:
    """
    Coordinates data collection from Ashby.
    """

    def __init__(self):
        self.client = AshbyClient()
        self.parser = AshbyParser()

    def collect(self, organization_slug: str):

        raw_jobs = self.client.get_jobs(organization_slug)

        parsed_jobs = []

        for job in raw_jobs:

            parsed_job = self.parser.parse(job)

            if is_kenya_job(parsed_job["location"]):
                parsed_jobs.append(parsed_job)

        return parsed_jobs