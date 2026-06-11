from src.tools.scout_tool import (
    ScoutTool
)

from src.tools.ranking_tool import (
    RankingTool
)


print()

print("AGENTIC WORKFLOW")

print()

jobs = (
    ScoutTool()
    ._run()
)

print()

print(
    "Scout completed."
)