from src.models.candidate_profile import CandidateProfile
from src.services.resume_parser import ResumeParser


class ProfileService:

    def __init__(self):
        self.resume_parser = ResumeParser()

    def load_profile(self) -> CandidateProfile:

        return self.resume_parser.parse(
            "data/resumes/maicon_fang_resume.docx"
        )