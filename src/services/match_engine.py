from src.models.candidate_profile import (
    CandidateProfile
)

from src.models.job_posting import (
    JobPosting
)

from src.models.match_result import (
    MatchResult
)

from src.config.skill_weights import (
    SKILL_WEIGHTS
)

from src.config.title_bonus import (
    TITLE_BONUS
)

from src.config.job_preferences import (
    PREFERRED_TITLES,
    AVOID_TITLES
)


class MatchEngine:

    def calculate_match(
        self,
        candidate: CandidateProfile,
        job: JobPosting
    ) -> MatchResult:

        candidate_skills = {
            skill.lower()
            for skill in candidate.skills
        }

        matched_skills = []

        missing_skills = []

        matched_weight = 0
        total_weight = 0

        for skill in job.skills:

            weight = SKILL_WEIGHTS.get(
                skill,
                1
            )

            total_weight += weight

            if skill.lower() in candidate_skills:

                matched_skills.append(
                    skill
                )

                matched_weight += weight

            else:

                missing_skills.append(
                    skill
                )

        if total_weight == 0:

            base_score = 0

        else:

            coverage_score = (
                matched_weight
                / total_weight
            )

            confidence_score = min(
                len(job.skills) / 10,
                1
            )

            base_score = (
                coverage_score
                * confidence_score
                * 100
            )

        job_title = (
            job.title.lower()
        )

        title_bonus = 0

        for keyword, bonus in TITLE_BONUS.items():

            if keyword in job_title:

                title_bonus += bonus

        preference_bonus = 0

        for keyword, bonus in PREFERRED_TITLES.items():

            if keyword in job_title:

                preference_bonus += bonus

        for keyword, penalty in AVOID_TITLES.items():

            if keyword in job_title:

                preference_bonus += penalty

        score = max(
            0,
            min(
                int(
                    base_score
                    + title_bonus
                    + preference_bonus
                ),
                100
            )
        )

        return MatchResult(
            score=score,
            matched_skills=matched_skills,
            missing_skills=missing_skills
        )