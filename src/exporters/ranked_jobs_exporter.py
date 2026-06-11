import json
from pathlib import Path

from src.models.job_posting import (
    JobPosting
)

from src.models.match_result import (
    MatchResult
)


class RankedJobsExporter:

    OUTPUT_FILE = (
        "out/ranked_jobs.json"
    )

    @classmethod
    def export(
        cls,
        ranked_jobs: list[
            tuple[
                JobPosting,
                MatchResult
            ]
        ]
    ):

        Path(
            "out"
        ).mkdir(
            exist_ok=True
        )

        data = []

        for rank, (
            job,
            result
        ) in enumerate(
            ranked_jobs,
            start=1
        ):

            data.append(
                {
                    "rank": rank,

                    "linkedin_job_id": (
                        job.linkedin_job_id
                    ),

                    "title": job.title,

                    "company": job.company,

                    "location": job.location,

                    "job_url": job.job_url,

                    "score": result.score,

                    "matched_skills": (
                        result.matched_skills
                    ),

                    "missing_skills": (
                        result.missing_skills
                    ),

                    "job_skills": (
                        job.skills
                    ),

                    "description": (
                        job.description
                    )
                }
            )

        with open(
            cls.OUTPUT_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"\nRanked jobs exported to:\n{cls.OUTPUT_FILE}"
        )