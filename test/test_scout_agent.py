from src.agents.scout_agent import (
    ScoutAgent
)

agent = ScoutAgent()

jobs = agent.execute()

print()

print(
    f"Returned jobs: {len(jobs)}"
)