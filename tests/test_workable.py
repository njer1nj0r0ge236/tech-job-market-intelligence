from src.collectors.workable.collector import WorkableCollector

collector = WorkableCollector()

jobs = collector.collect(
    "cloudfactory",
    "CloudFactory"
)

print(f"Found {len(jobs)} jobs")

for job in jobs:
    print(job["title"])
    print(job["location"])
    print(job["url"])
    print("-" * 50)