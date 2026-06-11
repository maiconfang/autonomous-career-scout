import json


class JobRecommendationAgent:

    def recommend(
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

            if score >= 90:

                priority = (
                    "Apply Immediately"
                )

            elif score >= 70:

                priority = (
                    "Apply This Week"
                )

            elif score >= 40:

                priority = (
                    "Low Priority"
                )

            else:

                priority = (
                    "Skip"
                )

            recommendation = {

                "title": job["title"],

                "company": job["company"],

                "score": score,

                "priority": priority,

                "matched_skills": (
                    job["matched_skills"]
                ),

                "missing_skills": (
                    job["missing_skills"]
                )
            }

            recommendations.append(
                recommendation
            )

        return recommendations