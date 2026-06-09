from dataclasses import dataclass

from src.models.opportunity_analysis import OpportunityAnalysis


@dataclass
class OpportunityReport:

    analysis: OpportunityAnalysis

    explanation: str