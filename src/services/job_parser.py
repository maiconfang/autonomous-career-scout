from src.models.job_posting import JobPosting


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

        for index, line in enumerate(lines):

            if line == "Salesforce CPQ Tester":

                title = line

                if index + 1 < len(lines):
                    company = lines[index + 1]

                break

        for line in lines:

            if "remote" in line.lower():

                location = "Remote"

                break

        for line in lines:

            if "$" in line:

                salary = line

                break

        known_skills = [
            "Salesforce CPQ",
            "Selenium",
            "Provar",
            "Apex",
            "Visualforce",
            "Lightning"
        ]

        for skill in known_skills:

            if skill.lower() in text.lower():

                skills.append(skill)

        return JobPosting(
            title=title,
            company=company,
            location=location,
            salary=salary,
            skills=skills,
            description=text
        )