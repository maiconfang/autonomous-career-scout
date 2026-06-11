from crewai.tools import BaseTool

from src.agents.scout_agent import (
    ScoutAgent
)


class ScoutTool(BaseTool):

    name: str = "Scout Tool"

    description: str = (
        "Collect jobs from LinkedIn."
    )

    def _run(
        self,
        *args,
        **kwargs
    ):

        print()

        print(
            "[ScoutTool] Running..."
        )

        jobs = (
            ScoutAgent()
            .execute()
        )

        print()

        print(
            f"[ScoutTool] Jobs found: {len(jobs)}"
        )

        return jobs