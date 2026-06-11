from src.collectors.linkedin.linkedin_authenticated_collector import (
    LinkedInAuthenticatedCollector
)

from src.config.search_profiles import (
    QA_CANADA
)

<<<<<<< HEAD
=======
from src.services.job_enrichment_service import (
    JobEnrichmentService
)

>>>>>>> 08bda95 (feat(agentic-ai): implement Opportunity Intelligence Crew with PostgreSQL persistence)

def main():

    collector = (
        LinkedInAuthenticatedCollector()
    )

<<<<<<< HEAD
    collector.collect(
        criteria=QA_CANADA
    )

=======
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

>>>>>>> 08bda95 (feat(agentic-ai): implement Opportunity Intelligence Crew with PostgreSQL persistence)

if __name__ == "__main__":
    main()