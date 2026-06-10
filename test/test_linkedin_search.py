from src.collectors.linkedin.linkedin_collector import (
    LinkedInCollector
)


def main():

    collector = LinkedInCollector()

    job = collector.search_jobs(
        keyword="QA Automation Engineer",
        location="Canada"
    )

    print("\n=== LINKEDIN COLLECTOR TEST ===\n")

    print(job)


if __name__ == "__main__":
    main()