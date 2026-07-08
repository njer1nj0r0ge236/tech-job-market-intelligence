from src.services.registry import CompanyRegistry
from src.services.collector_router import CollectorRouter

class IngestionEngine:
    """
    Coordinates job collection from all supported ATSs.
    """
    def __init__(self):
        self.registry = CompanyRegistry()
        self.router = CollectorRouter()

    def run(self):
        """
        Collect jobs from every supported company.
        """
        companies = self.registry.get_companies()

        all_jobs = []

        for company in companies:

             ats = company["ats"]
             
             collector = self.router.get_collector(ats)

            # Skip ATSs we haven't implemented yet
             if collector is None:
                print(f"Skipping {company['company']} ({ats})")
                continue

             print(f"Collecting jobs from {company['company']}...")

             try:
                jobs = collector.collect(
                    company["company"].lower().replace(" ", "-")
                )

                all_jobs.extend(jobs)

             except Exception as e:
                print(f"Failed to collect {company['company']}: {e}")

        return all_jobs
