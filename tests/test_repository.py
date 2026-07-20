from src.repositories.job_repository import JobRepository

repository = JobRepository()

# Create the table if it doesn't exist
repository.create_table()

# Dummy job
job = {
    "title": "Software Engineer",
    "company": "Test Company",
    "location": "Nairobi, Kenya",
    "description": "Python SQL PostgreSQL",
    "department": "Engineering",
    "employment_type": "Full-time",
    "posted_date": "2026-07-20",
    "url": "https://example.com/job1",
    "ats": "Greenhouse",
}

repository.insert_job(job)

print("✅ Test completed successfully!")