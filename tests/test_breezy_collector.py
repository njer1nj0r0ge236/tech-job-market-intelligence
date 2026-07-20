from src.collectors.breezy.collector import BreezyCollector

collector = BreezyCollector()

jobs = collector.collect("synnefa")

print(f"Found {len(jobs)} jobs")

for job in jobs:
    print(job["title"])
    print(job["location"])
    print(job["url"])
    print("-" * 50)