from dotenv import load_dotenv

load_dotenv()

from src.agents.recruiter_agent import RecruiterAgent
from src.agents.candidate_agent import CandidateAgent
from src.agents.match_analyst_agent import MatchAnalystAgent
from src.agents.career_advisor_agent import CareerAdvisorAgent
from src.agents.decision_agent import DecisionAgent
from src.agents.opportunity_analysis_agent import OpportunityAnalysisAgent

from src.services.job_loader import JobLoader
from src.reporting.report_generator import ReportGenerator
from src.openai.opportunity_explainer import OpportunityExplainer

from src.services.opportunity_persistence_service import ( OpportunityPersistenceService )

from src.services.execution_service import (ExecutionService )


def main():

    recruiter_agent = RecruiterAgent()

    candidate_agent = CandidateAgent()

    match_analyst_agent = MatchAnalystAgent()

    career_advisor_agent = CareerAdvisorAgent()

    decision_agent = DecisionAgent()

    opportunity_analysis_agent = OpportunityAnalysisAgent()

    opportunity_explainer = OpportunityExplainer()

    report_generator = ReportGenerator()

    execution_service = (
        ExecutionService()
    )

    opportunity_persistence_service = (
        OpportunityPersistenceService()
    )

    job_loader = JobLoader()

    candidate = candidate_agent.analyze()

    jobs = job_loader.load_jobs()

    results = []

    for file_name, job_text in jobs:

        print(
            f"\nProcessing job: {file_name}"
        )

        job = recruiter_agent.analyze(
            job_text
        )

        match_result = match_analyst_agent.analyze(
            candidate,
            job
        )

        recommendation = career_advisor_agent.analyze(
            match_result
        )

        decision = decision_agent.analyze(
            match_result,
            recommendation
        )

        opportunity_analysis = (
            opportunity_analysis_agent.analyze(
                match_result
            )
        )

        results.append(
            {
                "file_name": file_name,
                "job": job,
                "match_result": match_result,
                "recommendation": recommendation,
                "decision": decision,
                "opportunity_analysis": opportunity_analysis
            }
        )

    results.sort(
        key=lambda item: item["match_result"].score,
        reverse=True
    )

    print("\n")
    print("=" * 80)
    print("TOP OPPORTUNITIES")
    print("=" * 80)

    for index, result in enumerate(
        results,
        start=1
    ):

        analysis = result[
            "opportunity_analysis"
        ]

        print(
            f"\n#{index} - {result['file_name']}"
        )

        print(
            f"Score: {analysis.score}"
        )

        print("\nMatched Skills:")

        if analysis.matched_skills:

            for skill in analysis.matched_skills:

                print(
                    f"  ✓ {skill}"
                )

        else:

            print(
                "  None"
            )

        print("\nMissing Skills:")

        if analysis.missing_skills:

            for skill in analysis.missing_skills:

                print(
                    f"  ✗ {skill}"
                )

        else:

            print(
                "  None"
            )

        print("\nTop Strengths:")

        if analysis.strengths:

            for strength in analysis.strengths:

                print(
                    f"  ✓ {strength}"
                )

        else:

            print(
                "  None"
            )

        print("\nTop Gaps:")

        if analysis.weaknesses:

            for weakness in analysis.weaknesses:

                print(
                    f"  ✗ {weakness}"
                )

        else:

            print(
                "  None"
            )

        print("\nRecommendation:")

        print(
            analysis.recommendation
        )

        print(
            f"\nDecision: {result['decision'].decision}"
        )

        print(
            f"Confidence: {result['decision'].confidence}"
        )

        print(
            f"Reason: {result['decision'].reason}"
        )

        print("\n" + "-" * 80)

        report_generator.generate(
            results
        )

        execution_id = (
            execution_service.create_execution()
        )

        opportunity_persistence_service.save_from_json(
            "reports/opportunities.json",
            execution_id
        )

    top_opportunity = results[0]

    ai_result = (
        opportunity_explainer.explain(
            top_opportunity[
                "opportunity_analysis"
            ]
        )
    )

    print("\n")
    print("=" * 80)
    print("AI EXPLANATION")
    print("=" * 80)

    print(
        ai_result["explanation"]
    )

    print("\n")
    print("=" * 80)
    print("OPENAI METRICS")
    print("=" * 80)

    print(
        f"Model: {ai_result['model']}"
    )

    print(
        f"Prompt Tokens: {ai_result['prompt_tokens']}"
    )

    print(
        f"Completion Tokens: {ai_result['completion_tokens']}"
    )

    print(
        f"Total Tokens: {ai_result['total_tokens']}"
    )

    estimated_cost = (
        ai_result["total_tokens"]
        * 0.000001
    )

    print(
        f"Estimated Cost: ${estimated_cost:.6f}"
    )


if __name__ == "__main__":
    main()