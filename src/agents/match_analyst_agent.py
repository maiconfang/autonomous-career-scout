from src.models.job_posting import JobPosting
from src.models.candidate_profile import CandidateProfile
from src.models.match_result import MatchResult
from src.services.job_matcher import JobMatcher


class MatchAnalystAgent:

    def __init__(self):
        self.job_matcher = JobMatcher()

    def analyze(
        self,
        candidate: CandidateProfile,
        job: JobPosting
    ) -> MatchResult:

        print("[MatchAnalystAgent] Analyzing compatibility...")

        result = self.job_matcher.match(
            candidate,
            job
        )

        print("[MatchAnalystAgent] Analysis completed.")

        return result