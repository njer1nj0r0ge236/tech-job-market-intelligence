class AshbyParser:
    """
    Converts raw Ashby jobs into TJMI's unified schema.
    """

    def parse(self, job: dict) -> dict:

        return {
            "external_id": job["id"],
            "company": None,      # We'll improve this later
            "title": job["title"],
            "location": job["location"],
            "url": None,          # We'll improve this later
            "updated_at": None    # Ashby endpoint doesn't expose this here
        }