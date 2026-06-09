from src.models.job_posting import JobPosting
from src.services.job_parser import JobParser


class RecruiterAgent:
    """
    Responsible for understanding a job description
    and transforming it into a structured JobPosting.
    """

    def __init__(self):
        self.job_parser = JobParser()

    def analyze(self, job_description: str) -> JobPosting:
        """
        Analyze a raw job description and return
        a structured JobPosting object.
        """

        print("[RecruiterAgent] Analyzing job posting...")

        job_posting = self.job_parser.parse(job_description)

        print("[RecruiterAgent] Analysis completed.")

        return job_posting