import json

from src.repositories.opportunity_report_repository import (
    OpportunityReportRepository
)


class OpportunityReportExporter:

    @staticmethod
    def export(
        job,
        analysis,
        decision
    ):

        report = {

            "linkedin_job_id":
                job.linkedin_job_id,

            "title":
                job.title,

            "company":
                job.company,

            "score":
                analysis.score,

            "matched_skills":
                analysis.matched_skills,

            "missing_skills":
                analysis.missing_skills,

            "strengths":
                analysis.strengths,

            "weaknesses":
                analysis.weaknesses,

            "recommendation":
                analysis.recommendation,

            "decision":
                decision.decision,

            "confidence":
                decision.confidence,

            "reason":
                decision.reason
        }

        with open(
            "out/opportunity_report.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )

        OpportunityReportRepository().save(
            linkedin_job_id=job.linkedin_job_id,
            title=job.title,
            company=job.company,
            score=analysis.score,
            decision=decision.decision,
            confidence=decision.confidence,
            recommendation=analysis.recommendation,
            strengths=analysis.strengths,
            weaknesses=analysis.weaknesses,
            matched_skills=analysis.matched_skills,
            missing_skills=analysis.missing_skills
        )

        print()
        print(
            "Opportunity report exported:"
        )
        print(
            "out/opportunity_report.json"
        )

        print()
        print(
            "Opportunity report saved to PostgreSQL."
        )