from docx import Document

from src.models.candidate_profile import CandidateProfile
from src.config.skills import KNOWN_SKILLS


class ResumeParser:

    def parse(self, file_path: str) -> CandidateProfile:

        document = Document(file_path)

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        years_experience = 10

        skills = []

        for skill in KNOWN_SKILLS:

            if skill.lower() in text.lower():

                skills.append(skill)

        print("\n=== RESUME PARSER ===")
        print(f"Skills found: {skills}")

        return CandidateProfile(
            years_experience=years_experience,
            skills=skills
        )