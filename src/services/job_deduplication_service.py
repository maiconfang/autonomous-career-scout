from src.models.job_posting import (
    JobPosting
)


class JobDeduplicationService:

    def deduplicate(
        self,
        jobs: list[JobPosting]
    ) -> list[JobPosting]:

        unique_jobs = []

        seen = set()

        for job in jobs:

            title = (
                job.title.lower().strip()
            )

            company = (
                job.company.lower().strip()
            )

            key = (
                title,
                company
            )

            if key in seen:

                continue

            seen.add(
                key
            )

            unique_jobs.append(
                job
            )

        removed = (
            len(jobs)
            - len(unique_jobs)
        )

        print(
            f"\nDuplicates removed: {removed}"
        )

        print(
            f"Unique jobs: {len(unique_jobs)}"
        )

        return unique_jobs