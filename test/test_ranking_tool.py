from src.tools.scout_tool import (
    ScoutTool
)

from src.tools.ranking_tool import (
    RankingTool
)

from src.agents.scout_agent import (
    ScoutAgent
)


jobs = (
    ScoutAgent()
    .execute()
)

ranked_jobs = (
    RankingTool()
    .run(
        jobs
    )
)

print()

print(
    f"Ranked jobs: {len(ranked_jobs)}"
)