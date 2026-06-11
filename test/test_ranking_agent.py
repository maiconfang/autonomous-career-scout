from src.agents.scout_agent import (
    ScoutAgent
)

from src.agents.ranking_agent import (
    RankingAgent
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

print()

print(
    "================================"
)

print(
    "TOP 5 MATCHES"
)

print(
    "================================"
)

for index, (
    job,
    result
) in enumerate(
    ranked_jobs[:5],
    start=1
):

    print()

    print(
        f"#{index}"
    )

    print(
        f"TITLE: {job.title}"
    )

    print(
        f"COMPANY: {job.company}"
    )

    print(
        f"SCORE: {result.score}"
    )