from src.models.job_posting import (
    JobPosting
)


class SmartJobDeduplicationService:

    def deduplicate(
        self,
        jobs: list[JobPosting]
    ) -> list[JobPosting]:

        unique_jobs = []

        for job in jobs:

            is_duplicate = False

            for existing_job in unique_jobs:

                if not self.same_company(
                    job,
                    existing_job
                ):
                    continue

                similarity = (
                    self.skill_similarity(
                        job,
                        existing_job
                    )
                )

                if similarity >= 0.80:

                    is_duplicate = True

                    break

            if not is_duplicate:

                unique_jobs.append(
                    job
                )

        removed = (
            len(jobs)
            - len(unique_jobs)
        )

        print(
            "\n=== SMART DEDUPLICATION ==="
        )

        print(
            f"Duplicates removed: {removed}"
        )

        print(
            f"Unique jobs: {len(unique_jobs)}"
        )

        return unique_jobs

    def same_company(
        self,
        job_a: JobPosting,
        job_b: JobPosting
    ) -> bool:

        return (
            job_a.company.lower().strip()
            ==
            job_b.company.lower().strip()
        )

    def skill_similarity(
        self,
        job_a: JobPosting,
        job_b: JobPosting
    ) -> float:

        skills_a = set(
            skill.lower()
            for skill in job_a.skills
        )

        skills_b = set(
            skill.lower()
            for skill in job_b.skills
        )

        if (
            not skills_a
            or
            not skills_b
        ):
            return 0

        intersection = (
            skills_a.intersection(
                skills_b
            )
        )

        union = (
            skills_a.union(
                skills_b
            )
        )

        return (
            len(intersection)
            /
            len(union)
        )