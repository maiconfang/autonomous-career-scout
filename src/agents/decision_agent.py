from src.models.match_result import MatchResult
from src.models.career_recommendation import CareerRecommendation
from src.models.application_decision import ApplicationDecision


class DecisionAgent:

    def analyze(
        self,
        match_result: MatchResult,
        recommendation: CareerRecommendation
    ) -> ApplicationDecision:

        print("[DecisionAgent] Making application decision...")

        score = match_result.score

        if score >= 80:

            decision = "APPLY"

            confidence = "HIGH"

            reason = (
                f"Strong match detected ({score}%). "
                "The candidate already satisfies most requirements."
            )

        elif score >= 50:

            decision = "APPLY"

            confidence = "MEDIUM"

            reason = (
                f"Moderate match detected ({score}%). "
                "The candidate has relevant experience but should address some skill gaps."
            )

        elif score >= 30:

            decision = "CONSIDER"

            confidence = "LOW"

            reason = (
                f"Partial match detected ({score}%). "
                "The candidate has transferable skills but significant improvements are needed."
            )

        else:

            decision = "DO_NOT_APPLY"

            confidence = "HIGH"

            reason = (
                f"Low match detected ({score}%). "
                "Too many critical requirements are currently missing."
            )

        print("[DecisionAgent] Analysis completed.")

        return ApplicationDecision(
            decision=decision,
            confidence=confidence,
            reason=reason
        )