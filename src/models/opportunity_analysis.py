from dataclasses import dataclass


@dataclass
class OpportunityAnalysis:

    score: int

    matched_skills: list[str]

    missing_skills: list[str]

    strengths: list[str]

    weaknesses: list[str]

    recommendation: str