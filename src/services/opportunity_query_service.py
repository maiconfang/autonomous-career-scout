from src.repositories.job_repository import (
    JobRepository
)


class OpportunityQueryService:

    def __init__(self):

        self.repository = (
            JobRepository()
        )

    def get_all_jobs(self):

        return (
            self.repository.find_all()
        )

    def get_top_jobs(
        self,
        minimum_score: int = 80
    ):

        return (
            self.repository.find_top_matches(
                minimum_score
            )
        )

    def get_top_5_jobs(self):

        return (
            self.repository.find_top_5_jobs()
        )

    def get_jobs_by_company(
        self,
        company_name: str
    ):

        return (
            self.repository.find_by_company(
                company_name
            )
        )

    def get_jobs_by_recommendation(
        self,
        recommendation: str
    ):

        return (
            self.repository.find_by_recommendation(
                recommendation
            )
        )

    def print_top_jobs(
        self,
        minimum_score: int = 80
    ):

        jobs = (
            self.get_top_jobs(
                minimum_score
            )
        )

        self._print_jobs(jobs)

    def print_top_5_jobs(self):

        jobs = (
            self.get_top_5_jobs()
        )

        self._print_jobs(jobs)

    def _print_jobs(
        self,
        jobs
    ):

        print()

        print(
            "=" * 40
        )

        print(
            "TOP JOBS"
        )

        print(
            "=" * 40
        )

        for job in jobs:

            print()

            print(
                f"TITLE: {job[1]}"
            )

            print(
                f"COMPANY: {job[2]}"
            )

            print(
                f"SCORE: {job[4]}"
            )

            print(
                f"RECOMMENDATION: {job[5]}"
            )