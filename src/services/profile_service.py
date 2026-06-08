from src.models.candidate_profile import CandidateProfile


class ProfileService:

    def load_profile(self) -> CandidateProfile:

        return CandidateProfile(
            years_experience=10,
            skills=[
                "Playwright",
                "Selenium",
                "API Testing",
                "Salesforce",
                "Python",
                "TypeScript",
                "Automation"
            ]
        )