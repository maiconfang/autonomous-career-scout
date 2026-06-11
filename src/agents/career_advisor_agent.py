from src.services.opportunity_query_service import (
    OpportunityQueryService
)


class CareerAdvisorAgent:

    def __init__(self):

        self.query_service = (
            OpportunityQueryService()
        )

    def advise(self):

        jobs = (
            self.query_service.get_top_5_jobs()
        )

        print()

        print("=" * 40)
        print("CAREER ADVISOR")
        print("=" * 40)

        for index, job in enumerate(
            jobs,
            start=1
        ):

            print()

            print(
                f"{index}. {job[2]}"
            )

            print(
                f"Company: {job[3]}"
            )

            print(
                f"Location: {job[4]}"
            )

            print(
                f"Score: {job[8]}"
            )

            print(
                f"Recommendation: {job[9]}"
            )

            print(
                f"Job ID: {job[1]}"
            )

            print(
                f"URL: {job[5]}"
            )