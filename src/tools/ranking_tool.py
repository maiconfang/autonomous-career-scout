from crewai.tools import BaseTool

from src.agents.ranking_agent import (
    RankingAgent
)

from src.services.profile_service import (
    ProfileService
)


class RankingTool(BaseTool):

    name: str = "Ranking Tool"

    description: str = (
        "Rank opportunities according to the candidate profile."
    )

    def _run(
        self,
        jobs
    ):

        print()

        print(
            "[RankingTool] Running..."
        )

        candidate = (
            ProfileService()
            .load_profile()
        )

        ranked_jobs = (
            RankingAgent()
            .execute(
                candidate,
                jobs
            )
        )

        print()

        print(
            f"[RankingTool] Ranked jobs: {len(ranked_jobs)}"
        )

        return ranked_jobs