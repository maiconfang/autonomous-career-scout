from src.models.match_result import MatchResult
from src.models.opportunity_analysis import OpportunityAnalysis


class OpportunityAnalysisAgent:

    def analyze(
        self,
        match_result: MatchResult
    ) -> OpportunityAnalysis:

        print(
            "[OpportunityAnalysisAgent] Generating opportunity analysis..."
        )

        strengths = (
            match_result.matched_skills[:3]
        )

        weaknesses = (
            match_result.missing_skills[:3]
        )

        if match_result.score >= 80:

            recommendation = (
                "Strong match. Apply immediately."
            )

        elif match_result.score >= 60:

            if weaknesses:

                recommendation = (
                    f"Good opportunity. Consider improving "
                    f"{weaknesses[0]} to increase competitiveness."
                )

            else:

                recommendation = (
                    "Good opportunity. Consider applying."
                )

        elif match_result.score >= 40:

            if weaknesses:

                recommendation = (
                    f"Partial match. Focus on learning "
                    f"{weaknesses[0]} before prioritizing this opportunity."
                )

            else:

                recommendation = (
                    "Partial match. Additional evaluation recommended."
                )

        else:

            recommendation = (
                "Low compatibility. Focus on other opportunities first."
            )

        print(
            "[OpportunityAnalysisAgent] Analysis completed."
        )

        return OpportunityAnalysis(
            score=match_result.score,
            matched_skills=match_result.matched_skills,
            missing_skills=match_result.missing_skills,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendation=recommendation
        )