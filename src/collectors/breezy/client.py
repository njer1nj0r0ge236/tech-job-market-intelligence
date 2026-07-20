import requests


class BreezyClient:
    """
    Handles communication with the BreezyHR public API.
    """

    def get_jobs(self, company_slug: str) -> list:
        url = f"https://{company_slug}.breezy.hr/json"

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        return response.json()