from src.agents.scout_agent import (
    ScoutAgent
)

from src.tools.ranking_tool import (
    RankingTool
)

from src.tools.persistence_tool import (
    PersistenceTool
)

from src.tools.advisor_tool import (
    AdvisorTool
)


print()
print("=" * 50)
print("FULL TOOL CHAIN")
print("=" * 50)

jobs = (
    ScoutAgent()
    .execute()
)

ranked_jobs = (
    RankingTool()
    .run(jobs)
)

PersistenceTool().run(
    ranked_jobs
)

AdvisorTool().run()

print()
print("=" * 50)
print("WORKFLOW COMPLETED")
print("=" * 50)