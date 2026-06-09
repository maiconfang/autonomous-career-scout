from src.models.candidate_profile import CandidateProfile
from src.services.profile_service import ProfileService


class CandidateAgent:
    """
    Responsible for understanding a candidate profile
    and transforming it into a structured CandidateProfile.
    """

    def __init__(self):
        self.profile_service = ProfileService()

    def analyze(self) -> CandidateProfile:
        """
        Analyze the candidate profile and return
        a structured CandidateProfile object.
        """

        print("[CandidateAgent] Analyzing candidate profile...")

        candidate_profile = self.profile_service.load_profile()

        print("[CandidateAgent] Analysis completed.")

        return candidate_profile