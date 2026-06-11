from src.models.candidate_profile import (
    CandidateProfile
)

from src.models.job_posting import (
    JobPosting
)

from src.services.match_engine import (
    MatchEngine
)


def main():

    candidate = CandidateProfile(
        years_experience=10,
        skills=[
            "Playwright",
            "TypeScript",
            "JavaScript",
            "API Testing",
            "Postman",
            "REST Assured",
            "CI/CD",
            "Salesforce"
        ]
    )

    job = JobPosting(
        title="Sr SDET – AWS Serverless",
        company="Applicantz",
        location="Canada (Remote)",
        salary="",
        skills=[
            "Cypress",
            "Java",
            "TypeScript",
            "JavaScript",
            "Node.js",
            "CI/CD",
            "Automation Framework"
        ],
        description=""
    )

    result = (
        MatchEngine()
        .calculate_match(
            candidate,
            job
        )
    )

    print("\nMATCH RESULT")
    print("=" * 50)

    print(
        f"Score: {result.score}%"
    )

    print(
        f"Matched Skills: {result.matched_skills}"
    )

    print(
        f"Missing Skills: {result.missing_skills}"
    )


if __name__ == "__main__":
    main()