from src.collectors.linkedin.linkedin_authenticated_collector import (
    LinkedInAuthenticatedCollector
)

from src.config.search_profiles import (
    QA_CANADA
)

from src.services.smart_job_deduplication_service import (
    SmartJobDeduplicationService
)

from src.services.job_enrichment_service import (
    JobEnrichmentService
)

from src.services.job_ranking_service import (
    JobRankingService
)

from src.services.profile_service import (
    ProfileService
)

from src.exporters.ranked_jobs_exporter import (
    RankedJobsExporter
)


def main():

    print(
        "\n=== LOADING PROFILE ==="
    )

    candidate = (
        ProfileService()
        .load_profile()
    )

    print(
        f"Skills: {candidate.skills}"
    )

    print(
        "\n=== COLLECTING JOBS ==="
    )

    collector = (
        LinkedInAuthenticatedCollector()
    )

    jobs = collector.collect(
        criteria=QA_CANADA
    )

    print(
        "\n=== ENRICHING JOBS ==="
    )

    jobs = (
        JobEnrichmentService()
        .enrich(jobs)
    )

    print(
        "\n=== SMART DEDUPLICATION ==="
    )

    jobs = (
        SmartJobDeduplicationService()
        .deduplicate(
            jobs
        )
    )


    print(
        "\n=== RANKING JOBS ==="
    )

    ranked_jobs = (
        JobRankingService()
        .rank_jobs(
            candidate,
            jobs
        )
    )

    RankedJobsExporter.export(
        ranked_jobs
    )

    print(
        "\n=============================="
    )

    print(
        "TOP JOB MATCHES"
    )

    print(
        "=============================="
    )

    for index, (
        job,
        result
    ) in enumerate(
        ranked_jobs,
        start=1
    ):

        print(
            f"\n#{index}"
        )

        print(
            f"TITLE: {job.title}"
        )

        print(
            f"COMPANY: {job.company}"
        )

        print(
            f"SCORE: {result.score}%"
        )

        print(
            f"MATCHED: {result.matched_skills}"
        )

        print(
            f"MISSING: {result.missing_skills}"
        )

    print(
        "\n=============================="
    )

    print(
        "RANKING EXPORTED"
    )

    print(
        "=============================="
    )

    print(
        "out/ranked_jobs.json"
    )


if __name__ == "__main__":
    main()