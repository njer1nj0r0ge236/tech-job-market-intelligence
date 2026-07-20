class BreezyParser:
    """
    Converts BreezyHR jobs into TJMI's unified schema.
    """

    def parse(self, job: dict) -> dict:

        location = job.get("location", {})

        city = location.get("city", "")

        country = location.get("country", {}).get("name", "")

        return {

            # "external_id": job["id"],

            # "company": job["company"]["name"],

            # "title": job["name"],

            # "location": ", ".join(
            #     part for part in [city, country] if part
            # ),

            # "description": None,

            # "employment_type": job["type"]["name"],

            # "department": job.get("department"),

            # "salary": job.get("salary"),

            # "url": job["url"],

            # "remote": location.get("is_remote", False),

            # "published_at": job["published_date"],

            "external_id": job["id"],
            "company": job["company"]["name"],
            "title": job["name"],
            "location": ", ".join(
                part for part in [city, country] if part
            ),
            "description": None,
            "department": job.get("department"),
            "employment_type": job["type"]["name"],
            "posted_date": job["published_date"],
            "url": job["url"],
            "ats": "BreezyHR",
        }
    