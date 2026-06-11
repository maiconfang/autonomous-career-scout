from src.agents.scout_agent import (
    ScoutAgent
)

from src.agents.ranking_agent import (
    RankingAgent
)

from src.agents.persistence_agent import (
    PersistenceAgent
)

from src.services.profile_service import (
    ProfileService
)


print(
    "\n=== LOADING PROFILE ==="
)

candidate = (
    ProfileService()
    .load_profile()
)

print(
    "\n=== COLLECTING JOBS ==="
)

jobs = (
    ScoutAgent()
    .execute()
)

print(
    "\n=== RANKING JOBS ==="
)

ranked_jobs = (
    RankingAgent()
    .execute(
        candidate,
        jobs
    )
)

print(
    "\n=== PERSISTING JOBS ==="
)

PersistenceAgent().execute(
    ranked_jobs
)