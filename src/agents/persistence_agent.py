from src.exporters.ranked_jobs_exporter import (
    RankedJobsExporter
)

from src.services.job_persistence_service import (
    JobPersistenceService
)


class PersistenceAgent:

    def __init__(self):

        self.persistence_service = (
            JobPersistenceService()
        )

    def execute(
        self,
        ranked_jobs
    ):

        print()

        print(
            "[PersistenceAgent] Exporting jobs..."
        )

        RankedJobsExporter.export(
            ranked_jobs
        )

        print()

        print(
            "[PersistenceAgent] Saving jobs..."
        )

        self.persistence_service.save_ranked_jobs(
            "out/ranked_jobs.json"
        )

        print()

        print(
            "[PersistenceAgent] Completed."
        )