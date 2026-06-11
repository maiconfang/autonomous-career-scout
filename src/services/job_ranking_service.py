from src.models.candidate_profile import (
    CandidateProfile
)

from src.models.job_posting import (
    JobPosting
)

from src.models.match_result import (
    MatchResult
)

from src.services.match_engine import (
    MatchEngine
)


class JobRankingService:

    def __init__(self):

        self.match_engine = (
            MatchEngine()
        )

    def rank_jobs(
        self,
        candidate: CandidateProfile,
        jobs: list[JobPosting]
    ) -> list[tuple[JobPosting, MatchResult]]:

        ranked_jobs = []

        for job in jobs:

            result = (
                self.match_engine
                .calculate_match(
                    candidate,
                    job
                )
            )

            ranked_jobs.append(
                (
                    job,
                    result
                )
            )

        ranked_jobs.sort(
            key=lambda item: item[1].score,
            reverse=True
        )

        return ranked_jobs