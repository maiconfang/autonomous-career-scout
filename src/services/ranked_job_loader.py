import json

from src.models.job_posting import (
    JobPosting
)


class RankedJobLoader:

    def load_ranked_jobs(
        self
    ) -> list[JobPosting]:

        with open(
            "out/ranked_jobs.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

        jobs = []

        for item in data:

            job = JobPosting(

                linkedin_job_id=item.get(
                    "linkedin_job_id",
                    ""
                ),

                title=item.get(
                    "title",
                    ""
                ),

                company=item.get(
                    "company",
                    ""
                ),

                location=item.get(
                    "location",
                    ""
                ),

                job_url=item.get(
                    "job_url",
                    ""
                ),

                description=item.get(
                    "description",
                    ""
                ),

                skills=item.get(
                    "job_skills",
                    []
                )
            )

            jobs.append(
                job
            )

        return jobs