from crewai.tools import BaseTool

from src.agents.career_advisor_agent import (
    CareerAdvisorAgent
)


class AdvisorTool(BaseTool):

    name: str = "Advisor Tool"

    description: str = (
        "Analyze stored opportunities and recommend the best jobs."
    )

    def _run(
        self,
        *args,
        **kwargs
    ):

        print()

        print(
            "[AdvisorTool] Running..."
        )

        CareerAdvisorAgent().advise()

        print()

        print(
            "[AdvisorTool] Completed."
        )

        return (
            "Career recommendations generated."
        )