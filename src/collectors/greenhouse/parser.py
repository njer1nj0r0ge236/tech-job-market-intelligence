class GreenhouseParser:
    """
    Converts raw Greenhouse jobs into TJMI's unified schema.
    """

    def parse(self, job: dict) -> dict:

        metadata = job.get("metadata") or []
        location = job.get("location") or {}

        department = None

        for item in metadata:
            if item.get("name", "").lower() == "department":
                department = item.get("value")
                break

        return {
            # "external_id": job["id"],
            # "company": job["company_name"],
            # "title": job["title"],
            # "location": job["location"]["name"],
            # "url": job["absolute_url"],
            # "updated_at": job["updated_at"],

            "external_id": job.get("id"),
            "company": job.get("company_name"),
            "title": job.get("title"),
            "location": location.get("name", ""),
            "description": job.get("content") or "",
            "department": department,
            "employment_type": None,
            "posted_date": job.get("updated_at"),
            "updated_at": job.get("updated_at"),
            "url": job.get("absolute_url"),
            "ats": "Greenhouse",
        }