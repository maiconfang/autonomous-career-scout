from src.services.job_persistence_service import (
    JobPersistenceService
)


service = (
    JobPersistenceService()
)

service.save_ranked_jobs(
    "out/ranked_jobs.json"
)