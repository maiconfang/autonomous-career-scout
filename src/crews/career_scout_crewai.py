from crewai import (
    Agent,
    Task,
    Crew,
    Process
)

from src.services.profile_service import (
    ProfileService
)

from src.tools.scout_tool import (
    ScoutTool
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


class CareerScoutCrewAI:

    def run(self):

        print()
        print("=" * 60)
        print("CAREER SCOUT CREW AI V2")
        print("=" * 60)

        candidate = (
            ProfileService()
            .load_profile()
        )

        scout_agent = Agent(
            role="Job Scout",
            goal="Collect relevant opportunities.",
            backstory=(
                "Expert in finding QA Automation and "
                "SDET opportunities."
            ),
            verbose=True
        )

        ranking_agent = Agent(
            role="Ranking Specialist",
            goal="Rank opportunities.",
            backstory=(
                "Expert in matching skills and jobs."
            ),
            verbose=True
        )

        persistence_agent = Agent(
            role="Persistence Specialist",
            goal="Persist opportunities.",
            backstory=(
                "Responsible for storing ranked jobs."
            ),
            verbose=True
        )

        advisor_agent = Agent(
            role="Career Advisor",
            goal="Recommend opportunities.",
            backstory=(
                "Senior QA career advisor."
            ),
            verbose=True
        )

        scout_task = Task(
            description="Collect jobs from LinkedIn.",
            expected_output="List of jobs.",
            agent=scout_agent
        )

        ranking_task = Task(
            description="Rank jobs.",
            expected_output="Ranked jobs.",
            agent=ranking_agent
        )

        persistence_task = Task(
            description="Persist jobs.",
            expected_output="Jobs saved.",
            agent=persistence_agent
        )

        advisor_task = Task(
            description="Recommend jobs.",
            expected_output="Top opportunities.",
            agent=advisor_agent
        )

        crew = Crew(
            agents=[
                scout_agent,
                ranking_agent,
                persistence_agent,
                advisor_agent
            ],
            tasks=[
                scout_task,
                ranking_task,
                persistence_task,
                advisor_task
            ],
            process=Process.sequential,
            verbose=True
        )

        print()
        print("[CrewAI] Starting...")
        print()

        try:

            crew.kickoff()

        except Exception as error:

            print()
            print(
                f"[CrewAI WARNING] {error}"
            )

        print()
        print("[CrewAI] Executing tools...")
        print()

        jobs = (
            ScoutTool()
            .run()
        )

        jobs = (
            ScoutTool()
            ._run()
        )

        ranked_jobs = (
            RankingTool()
            .run(
                jobs
            )
        )

        PersistenceTool().run(
            ranked_jobs
        )

        AdvisorTool().run()

        print()
        print("=" * 60)
        print("CAREER SCOUT CREW AI COMPLETED")
        print("=" * 60)