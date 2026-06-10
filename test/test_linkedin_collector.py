from src.collectors.linkedin.linkedin_collector import (
    LinkedInCollector
)


collector = LinkedInCollector()

jobs = collector.collect()

print(jobs)