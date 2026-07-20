from bs4 import BeautifulSoup


class WorkableParser:
    """
    Converts raw Workable jobs into TJMI's unified schema.
    """

    def parse(self, job: dict, company: str) -> dict:

        description = BeautifulSoup(
            job["description"],
            "html.parser"
        ).get_text(" ", strip=True)

        city = job.get("city") or ""
        country = job.get("country") or ""

        location = ", ".join(
            part for part in [city, country] if part
        )

        return {
            # "external_id": job["shortcode"],
            # "company": company,
            # "title": job["title"],
            # "location": location,
            # "description": description,
            # "employment_type": job["employment_type"],
            # "department": job["department"],
            # "url": job["url"],
            # "remote": job["telecommuting"],
            # "published_at": job["published_on"],

            "external_id": job["shortcode"],
            "company": company,
            "title": job["title"],
            "location": location,
            "description": description,
            "department": job.get("department"),
            "employment_type": job.get("employment_type"),
            "posted_date": job.get("published_on"),
            "url": job["url"],
            "ats": "Workable",
        }