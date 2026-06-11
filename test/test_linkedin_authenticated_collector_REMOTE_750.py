from src.collectors.linkedin.linkedin_authenticated_collector import (
    LinkedInAuthenticatedCollector
)

from src.config.search_profiles import (
    QA_CANADA
)

from src.services.job_enrichment_service import (
    JobEnrichmentService
)


def main():

    collector = (
        LinkedInAuthenticatedCollector()
    )

    jobs = collector.collect(
        criteria=QA_CANADA
    )

    jobs = (
        JobEnrichmentService()
        .enrich(jobs)
    )

    print(
        "\n=============================="
    )

    print(
        "ENRICHED JOBS"
    )

    print(
        "=============================="
    )

    for job in jobs:

        print(
            f"\nTITLE: {job.title}"
        )

        print(
            f"COMPANY: {job.company}"
        )

        print(
            f"LOCATION: {job.location}"
        )

        print(
            f"SKILLS FOUND: {job.skills}"
        )


if __name__ == "__main__":
    main()