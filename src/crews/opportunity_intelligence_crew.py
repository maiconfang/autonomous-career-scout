from src.exporters.opportunity_report_exporter import (
    OpportunityReportExporter
)

from src.agents.candidate_agent import (
    CandidateAgent
)

from src.agents.match_analyst_agent import (
    MatchAnalystAgent
)

from src.agents.opportunity_analysis_agent import (
    OpportunityAnalysisAgent
)

from src.agents.decision_agent import (
    DecisionAgent
)

from src.agents.opportunity_advisor_agent import (
    OpportunityAdvisorAgent
)

from src.services.ranked_job_loader import (
    RankedJobLoader
)


class OpportunityIntelligenceCrew:

    def run(self):

        print()
        print("=" * 60)
        print("OPPORTUNITY INTELLIGENCE CREW")
        print("=" * 60)

        candidate = (
            CandidateAgent()
            .analyze()
        )

        jobs = (
            RankedJobLoader()
            .load_ranked_jobs()
        )

        if not jobs:

            print()
            print("No ranked jobs found.")
            return

        job = jobs[0]

        print()
        print(
            f"Analyzing: {job.title}"
        )

        match_result = (
            MatchAnalystAgent()
            .analyze(
                candidate,
                job
            )
        )

        opportunity_analysis = (
            OpportunityAnalysisAgent()
            .analyze(
                match_result
            )
        )

        recommendation = (
            OpportunityAdvisorAgent()
            .advise()
        )

        decision = (
            DecisionAgent()
            .analyze(
                match_result,
                recommendation
            )
        )
        
        OpportunityReportExporter.export(
            job,
            opportunity_analysis,
            decision
        )

        print()
        print("=" * 60)
        print("FINAL DECISION")
        print("=" * 60)

        print(
            f"Decision: {decision.decision}"
        )

        print(
            f"Confidence: {decision.confidence}"
        )

        print(
            f"Reason: {decision.reason}"
        )