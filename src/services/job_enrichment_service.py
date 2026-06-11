from src.models.job_posting import JobPosting
from src.services.job_parser import JobParser


class JobEnrichmentService:

    def __init__(self):

        self.job_parser = JobParser()

    def enrich(
        self,
        jobs: list[JobPosting]
    ) -> list[JobPosting]:

        enriched_jobs = []

        for job in jobs:

            extracted_skills = (
                self.job_parser.extract_skills(
                    job.description
                )
            )

            job.skills = extracted_skills

            enriched_jobs.append(
                job
            )

        return enriched_jobs