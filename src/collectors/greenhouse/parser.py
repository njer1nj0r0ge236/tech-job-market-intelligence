class GreenhouseParser:
    """
    Converts raw Greenhouse jobs into TJMI's unified schema.
    """

    def parse(self, job: dict) -> dict:
        return {
            "external_id": job["id"],
            "company": job["company_name"],
            "title": job["title"],
            "location": job["location"]["name"],
            "url": job["absolute_url"],
            "updated_at": job["updated_at"],
        }