from src.collectors.greenhouse.client import GreenhouseClient

client = GreenhouseClient()

jobs = client.get_jobs("jumo")

print(f"Found {len(jobs)} jobs")

# print(jobs[0])

for job in jobs:
    print(job["location"]["name"])