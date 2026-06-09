from src.models.match_result import MatchResult
from src.models.career_recommendation import CareerRecommendation


class CareerAdvisorAgent:

    def analyze(
        self,
        match_result: MatchResult
    ) -> CareerRecommendation:

        print("[CareerAdvisorAgent] Generating recommendations...")

        strengths = match_result.matched_skills

        improvement_areas = match_result.missing_skills

        recommended_actions = []

        for skill in improvement_areas:

            recommended_actions.append(
                f"Study {skill}"
            )

        if match_result.score >= 80:

            summary = (
                "Excellent match. The candidate already meets most requirements."
            )

        elif match_result.score >= 50:

            summary = (
                "Good match. Some improvements may increase competitiveness."
            )

        else:

            summary = (
                "Partial match. Several important skills should be developed."
            )

        recommendation = CareerRecommendation(
            summary=summary,
            strengths=strengths,
            improvement_areas=improvement_areas,
            recommended_actions=recommended_actions
        )

        print("[CareerAdvisorAgent] Analysis completed.")

        return recommendation