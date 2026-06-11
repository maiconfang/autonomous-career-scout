from src.agents.job_recommendation_agent import (
    JobRecommendationAgent
)


def main():

    recommendations = (
        JobRecommendationAgent()
        .recommend()
    )

    print(
        "\n=============================="
    )

    print(
        "JOB RECOMMENDATIONS"
    )

    print(
        "=============================="
    )

    for rec in recommendations:

        print(
            f"\nTITLE: {rec['title']}"
        )

        print(
            f"COMPANY: {rec['company']}"
        )

        print(
            f"SCORE: {rec['score']}%"
        )

        print(
            f"PRIORITY: {rec['priority']}"
        )

        print(
            f"MATCHED: {rec['matched_skills']}"
        )

        print(
            f"MISSING: {rec['missing_skills']}"
        )


if __name__ == "__main__":
    main()