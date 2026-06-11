from src.services.job_ranking_service import (
    JobRankingService
)

from src.models.candidate_profile import (
    CandidateProfile
)

from src.models.job_posting import (
    JobPosting
)

from src.models.match_result import (
    MatchResult
)


class RankingAgent:

    def __init__(self):

        self.ranking_service = (
            JobRankingService()
        )

    def execute(
        self,
        candidate: CandidateProfile,
        jobs: list[JobPosting]
    ) -> list[
        tuple[
            JobPosting,
            MatchResult
        ]
    ]:

        print()

        print(
            "[RankingAgent] Ranking jobs..."
        )

        ranked_jobs = (
            self.ranking_service.rank_jobs(
                candidate,
                jobs
            )
        )

        print(
            f"[RankingAgent] Ranked jobs: {len(ranked_jobs)}"
        )

        if ranked_jobs:

            best_job = ranked_jobs[0]

            print()

            print(
                "[RankingAgent] Top Match:"
            )

            print(
                best_job[0].title
            )

            print(
                f"Score: {best_job[1].score}"
            )

        return ranked_jobs