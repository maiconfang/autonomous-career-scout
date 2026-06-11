from crewai.tools import BaseTool

from src.agents.persistence_agent import (
    PersistenceAgent
)


class PersistenceTool(BaseTool):

    name: str = "Persistence Tool"

    description: str = (
        "Persist ranked opportunities into JSON and PostgreSQL."
    )

    def _run(
        self,
        ranked_jobs
    ):

        print()

        print(
            "[PersistenceTool] Running..."
        )

        PersistenceAgent().execute(
            ranked_jobs
        )

        print()

        print(
            "[PersistenceTool] Completed."
        )

        return (
            "Jobs persisted successfully."
        )