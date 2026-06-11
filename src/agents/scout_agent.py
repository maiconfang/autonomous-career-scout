


from src.collectors.linkedin.linkedin_authenticated_collector import LinkedInAuthenticatedCollector


class ScoutAgent:

    def __init__(self):

        self.collector = (
            LinkedInAuthenticatedCollector()
        )

    def execute(self):

        print()

        print(
            "[ScoutAgent] Collecting jobs..."
        )

        jobs = (
            self.collector.collect()
        )

        print(
            f"[ScoutAgent] Jobs collected: {len(jobs)}"
        )

        return jobs