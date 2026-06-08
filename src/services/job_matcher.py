from src.models.candidate_profile import CandidateProfile
from src.models.job_posting import JobPosting


class JobMatcher:

    SKILL_ALIASES = {
        "Salesforce CPQ": [
            "Salesforce"
        ]
    }

    def calculate_match(
        self,
        candidate: CandidateProfile,
        job: JobPosting
    ) -> dict:

        matched_skills = []

        missing_skills = []

        for skill in job.skills:

            matched = False

            for candidate_skill in candidate.skills:

                if skill.lower() in candidate_skill.lower():

                    matched = True

                    matched_skills.append(skill)

                    break

            if not matched:

                aliases = self.SKILL_ALIASES.get(
                    skill,
                    []
                )

                for alias in aliases:

                    for candidate_skill in candidate.skills:

                        if alias.lower() in candidate_skill.lower():

                            matched = True

                            matched_skills.append(skill)

                            break

                    if matched:
                        break

            if not matched:

                missing_skills.append(skill)

        total_skills = len(job.skills)

        score = 0

        if total_skills > 0:

            score = round(
                (len(matched_skills) / total_skills) * 100
            )

        return {
            "score": score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        }