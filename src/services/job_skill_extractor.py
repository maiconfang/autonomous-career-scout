class JobSkillExtractor:

    KNOWN_SKILLS = [
        "Playwright",
        "Selenium",
        "Cypress",
        "Java",
        "Python",
        "TypeScript",
        "JavaScript",
        "Node.js",
        "REST API",
        "API Testing",
        "AWS",
        "CI/CD",
        "Docker",
        "PostgreSQL",
        "Salesforce"
    ]

    @classmethod
    def extract(
        cls,
        description: str
    ) -> list[str]:

        description_lower = (
            description.lower()
        )

        found_skills = []

        for skill in cls.KNOWN_SKILLS:

            if skill.lower() in description_lower:

                found_skills.append(
                    skill
                )

        return found_skills