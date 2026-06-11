from src.agents.scout_agent import (
    ScoutAgent
)

from src.agents.ranking_agent import (
    RankingAgent
)

from src.agents.persistence_agent import (
    PersistenceAgent
)

from src.agents.career_advisor_agent import (
    CareerAdvisorAgent
)

from src.services.profile_service import (
    ProfileService
)


class CareerScoutCrew:

    def run(self):

        print()

        print(
            "=" * 50
        )

        print(
            "CAREER SCOUT CREW"
        )

        print(
            "=" * 50
        )

        candidate = (
            ProfileService()
            .load_profile()
        )

        jobs = (
            ScoutAgent()
            .execute()
        )

        ranked_jobs = (
            RankingAgent()
            .execute(
                candidate,
                jobs
            )
        )

        PersistenceAgent().execute(
            ranked_jobs
        )

        CareerAdvisorAgent().advise()

        print()

        print(
            "=" * 50
        )

        print(
            "PIPELINE COMPLETED"
        )

        print(
            "=" * 50
        )