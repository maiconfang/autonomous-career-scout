from src.models.match_result import MatchResult
from src.models.job_posting import JobPosting
from src.models.candidate_profile import CandidateProfile


class JobMatcher:

    def match(
        self,
        candidate: CandidateProfile,
        job: JobPosting
    ) -> MatchResult:

        matched_skills = []

        missing_skills = []

        candidate_skills = {
            skill.lower()
            for skill in candidate.skills
        }

        for skill in job.skills:

            if skill.lower() in candidate_skills:

                matched_skills.append(skill)

            else:

                missing_skills.append(skill)

        total_skills = len(job.skills)

        if total_skills == 0:

            score = 0

        else:

            score = int(
                (len(matched_skills) / total_skills) * 100
            )

        return MatchResult(
            score=score,
            matched_skills=matched_skills,
            missing_skills=missing_skills
        )