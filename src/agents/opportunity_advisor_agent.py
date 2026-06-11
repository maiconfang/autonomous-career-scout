import json


class OpportunityAdvisorAgent:

    def advise(
        self,
        ranked_jobs_file: str = (
            "out/ranked_jobs.json"
        )
    ):

        with open(
            ranked_jobs_file,
            "r",
            encoding="utf-8"
        ) as file:

            jobs = json.load(
                file
            )

        recommendations = []

        for job in jobs:

            score = job["score"]

            matched = (
                job["matched_skills"]
            )

            missing = (
                job["missing_skills"]
            )

            if score >= 90:

                recommendation = (
                    "Apply Immediately"
                )

            elif score >= 70:

                recommendation = (
                    "Apply This Week"
                )

            elif score >= 40:

                recommendation = (
                    "Low Priority"
                )

            else:

                recommendation = (
                    "Skip"
                )

            reason = self.build_reason(
                matched,
                missing,
                score
            )

            recommendations.append(
                {
                    "title": (
                        job["title"]
                    ),

                    "company": (
                        job["company"]
                    ),

                    "score": score,

                    "recommendation": (
                        recommendation
                    ),

                    "reason": reason,

                    "matched_skills": (
                        matched
                    ),

                    "missing_skills": (
                        missing
                    )
                }
            )

        return recommendations

    def build_reason(
        self,
        matched_skills,
        missing_skills,
        score
    ):

        if score >= 90:

            return (
                "Excellent match with your profile."
            )

        if score >= 70:

            return (
                "Strong alignment with your skills."
            )

        if score >= 40:

            return (
                "Partial alignment. Review before applying."
            )

        if missing_skills:

            return (
                "Several important skills are missing."
            )

        return (
            "Low relevance compared to other opportunities."
        )