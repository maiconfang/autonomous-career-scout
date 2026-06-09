import re

from src.models.candidate_profile import CandidateProfile


class ProfileParser:
    """
    Responsible for transforming a candidate text file
    into a CandidateProfile object.
    """

    KNOWN_SKILLS = [
        "Playwright",
        "Selenium",
        "Salesforce",
        "API Testing",
        "Python",
        "TypeScript",
        "Automation",
        "Java",
        "C#",
        "Postman",
        "REST Assured",
        "Cypress",
    ]

    def parse(self, text: str) -> CandidateProfile:

        years_experience = self._extract_years_experience(text)

        skills = self._extract_skills(text)

        return CandidateProfile(
            years_experience=years_experience,
            skills=skills
        )

    def _extract_years_experience(self, text: str) -> int:

        match = re.search(
            r"(\d+)\s+years\s+of\s+experience",
            text,
            re.IGNORECASE
        )

        if match:
            return int(match.group(1))

        return 0

    def _extract_skills(self, text: str) -> list[str]:

        found_skills = []

        for skill in self.KNOWN_SKILLS:

            if skill.lower() in text.lower():
                found_skills.append(skill)

        return found_skills