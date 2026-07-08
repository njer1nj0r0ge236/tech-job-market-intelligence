# from src.collectors.greenhouse.collector import GreenhouseCollector

# collector = GreenhouseCollector()

# jobs = collector.collect("stripe")

# print(f"Kenyan jobs found: {len(jobs)}")

# for job in jobs:
#     print(job)

from src.collectors.greenhouse.collector import GreenhouseCollector

collector = GreenhouseCollector()

jobs = collector.collect("stripe")

print(jobs)
print(type(jobs))