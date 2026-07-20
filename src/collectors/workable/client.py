import requests


class WorkableClient:
    """
    Handles communication with the Workable public API.
    """

    BASE_URL = "https://www.workable.com/api/accounts"

    def get_jobs(self, account_slug: str) -> list:
        """
        Fetch all public jobs from a Workable account.
        """

        url = f"{self.BASE_URL}/{account_slug}?details=true"

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        data = response.json()

        return data["jobs"]