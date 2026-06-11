import json

from src.models.match_result import (
    MatchResult
)

from src.agents.opportunity_analysis_agent import (
    OpportunityAnalysisAgent
)

from src.openai.opportunity_explainer import (
    OpportunityExplainer
)


def main():

    print(
        "\n=== LOADING RANKED JOBS ==="
    )

    with open(
        "out/ranked_jobs.json",
        "r",
        encoding="utf-8"
    ) as file:

        ranked_jobs = json.load(
            file
        )

    if not ranked_jobs:

        print(
            "No ranked jobs found."
        )

        return

    top_job = ranked_jobs[0]

    print(
        f"\nTOP JOB: {top_job['title']}"
    )

    print(
        f"COMPANY: {top_job['company']}"
    )

    match_result = MatchResult(

        score=top_job["score"],

        matched_skills=(
            top_job["matched_skills"]
        ),

        missing_skills=(
            top_job["missing_skills"]
        )
    )

    print(
        "\n=== ANALYZING OPPORTUNITY ==="
    )

    analysis = (
        OpportunityAnalysisAgent()
        .analyze(
            match_result
        )
    )

    print(
        "\n=== OPENAI EXPLANATION ==="
    )

    explanation = (
        OpportunityExplainer()
        .explain(
            analysis
        )
    )

    print(
        "\n=============================="
    )

    print(
        "AI CAREER ADVISOR"
    )

    print(
        "=============================="
    )

    print(
        f"\nTITLE: {top_job['title']}"
    )

    print(
        f"COMPANY: {top_job['company']}"
    )

    print(
        f"SCORE: {top_job['score']}%"
    )

    print(
        "\nEXPLANATION:\n"
    )

    print(
        explanation["explanation"]
    )

    print(
        "\n=============================="
    )

    print(
        "MODEL INFO"
    )

    print(
        "=============================="
    )

    print(
        f"Model: {explanation['model']}"
    )

    print(
        f"Prompt Tokens: {explanation['prompt_tokens']}"
    )

    print(
        f"Completion Tokens: {explanation['completion_tokens']}"
    )

    print(
        f"Total Tokens: {explanation['total_tokens']}"
    )


if __name__ == "__main__":
    main()