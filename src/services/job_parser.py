from src.models.job_posting import JobPosting
from src.config.skills import KNOWN_SKILLS


class JobParser:

    def parse(self, text: str) -> JobPosting:

        title = "Unknown"
        company = "Unknown"
        location = "Unknown"
        salary = "Unknown"

        skills = []

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        # Title

        if len(lines) > 0:
            title = lines[0]

        # Company

        if len(lines) > 1:
            company = lines[1]

        # Location

        for line in lines:

            if "remote" in line.lower():

                location = "Remote"

                break

        # Salary

        for line in lines:

            if "$" in line:

                salary = line

                break

        # Skills

        for skill in KNOWN_SKILLS:

            if skill.lower() in text.lower():

                skills.append(skill)

        print("\n=== JOB PARSER ===")
        print(f"Title: {title}")
        print(f"Skills found: {skills}")

        return JobPosting(
            title=title,
            company=company,
            location=location,
            salary=salary,
            skills=skills,
            description=text
        )
        
        
    def extract_skills(
        self,
        text: str
    ) -> list[str]:

        skills = []

        for skill in KNOWN_SKILLS:

            if skill.lower() in text.lower():

                skills.append(skill)

        return skills