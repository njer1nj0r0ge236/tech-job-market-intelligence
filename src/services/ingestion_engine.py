from src.services.registry import CompanyRegistry
from src.services.collector_router import CollectorRouter
from src.repositories.job_repository import JobRepository

class IngestionEngine:
    """
    Coordinates job collection from all supported ATSs.
    """
    def __init__(self):
        self.registry = CompanyRegistry()
        self.router = CollectorRouter()
        self.repository = JobRepository()

    def run(self):
        """
        Collect jobs from every supported company.
        """
        companies = self.registry.get_companies()

        all_jobs = []

        for company in companies:
             # Skip disabled companies
             if company["enabled"].strip().upper() != "TRUE":
                 continue

             ats = company["ats"]
             
             collector = self.router.get_collector(ats)

            # Skip ATSs we haven't implemented yet
             if collector is None:
                print(f"Skipping {company['company']} ({ats})")
                continue

             print(f"Collecting jobs from {company['company']}...")

             try:
                identifier = company["ats_identifier"]
                
                if not identifier:
                       print(f"No ATS identifier for {company['company']}")
                       continue
                
                if ats.lower() == "workable":
                      jobs = collector.collect(
                            identifier,
                            company["company"]
                            )
                else:
                      jobs = collector.collect(identifier)
                
                
                
                # jobs = collector.collect(identifier)
                print(f"Collected {len(jobs)} jobs from {company['company']}")
                
                # jobs = collector.collect(
                #     company["company"].lower().replace(" ", "-")
                # )

                all_jobs.extend(jobs)

             except Exception as e:
                print(f"Failed to collect {company['company']}: {e}")

        print(f"\nSaving {len(all_jobs)} jobs to PostgreSQL...")

        self.repository.insert_many(all_jobs)

        print("Done!")

        return all_jobs
