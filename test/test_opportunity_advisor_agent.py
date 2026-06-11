from src.agents.opportunity_advisor_agent import (
    OpportunityAdvisorAgent
)


def main():

    recommendations = (
        OpportunityAdvisorAgent()
        .advise()
    )

    print(
        "\n=============================="
    )

    print(
        "OPPORTUNITY ADVISOR"
    )

    print(
        "=============================="
    )

    for item in recommendations[:10]:

        print(
            f"\nTITLE: {item['title']}"
        )

        print(
            f"COMPANY: {item['company']}"
        )

        print(
            f"SCORE: {item['score']}%"
        )

        print(
            f"RECOMMENDATION: {item['recommendation']}"
        )

        print(
            f"REASON: {item['reason']}"
        )

        print(
            f"MATCHED: {item['matched_skills']}"
        )

        print(
            f"MISSING: {item['missing_skills']}"
        )


if __name__ == "__main__":
    main()