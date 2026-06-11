import json

from src.repositories.job_repository import (
    JobRepository
)


class JobPersistenceService:

    def __init__(self):

        self.repository = (
            JobRepository()
        )

    def save_ranked_jobs(
        self,
        ranked_jobs_path: str
    ):

        with open(
            ranked_jobs_path,
            "r",
            encoding="utf-8"
        ) as file:

            jobs = json.load(file)

        saved_count = 0

        skipped_count = 0

        for job in jobs:

            linkedin_job_id = job.get(
                "linkedin_job_id",
                ""
            )

            if self.repository.job_exists(
                linkedin_job_id
            ):

                skipped_count += 1

                continue

            score = job.get(
                "score",
                0
            )

            recommendation = (
                self._get_recommendation(
                    score
                )
            )

            skills = {

                "matched_skills":
                job.get(
                    "matched_skills",
                    []
                ),

                "missing_skills":
                job.get(
                    "missing_skills",
                    []
                )
            }

            self.repository.save(

                linkedin_job_id=linkedin_job_id,

                title=job.get(
                    "title",
                    ""
                ),

                company=job.get(
                    "company",
                    ""
                ),

                location=job.get(
                    "location",
                    ""
                ),

                job_url=job.get(
                    "job_url",
                    ""
                ),

                description=job.get(
                    "description",
                    ""
                ),

                skills=skills,

                score=score,

                recommendation=recommendation
            )

            saved_count += 1

        print()

        print(
            f"Jobs saved: {saved_count}"
        )

        print(
            f"Jobs skipped: {skipped_count}"
        )

    def _get_recommendation(
        self,
        score: int
    ) -> str:

        if score >= 80:

            return (
                "APPLY_IMMEDIATELY"
            )

        if score >= 60:

            return (
                "APPLY_THIS_WEEK"
            )

        if score >= 40:

            return (
                "LOW_PRIORITY"
            )

        return "SKIP"