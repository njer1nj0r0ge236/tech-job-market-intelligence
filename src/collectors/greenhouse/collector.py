from src.collectors.greenhouse.client import GreenhouseClient
from src.collectors.greenhouse.parser import GreenhouseParser

from src.utils.location import is_kenya_job


class GreenhouseCollector:
    """
    Coordinates data collection from Greenhouse.
    """

    def __init__(self):
        self.client = GreenhouseClient()
        self.parser = GreenhouseParser()

    def collect(self, board_token: str):
        raw_jobs = self.client.get_jobs(board_token)

        parsed_jobs = []

        for job in raw_jobs:
            parsed_job = self.parser.parse(job)
            
            if is_kenya_job(parsed_job["location"]):
                parsed_jobs.append(parsed_job)


        return parsed_jobs