import requests


class GreenhouseClient:
    """
    Handles communication with the Greenhouse Job Board API.
    """

    BASE_URL = "https://boards-api.greenhouse.io/v1/boards"

    def get_jobs(self, board_token: str) -> list:
        """
        Fetch all public jobs from a Greenhouse board.
        """

        url = f"{self.BASE_URL}/{board_token}/jobs"

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        data = response.json()

        return data["jobs"]