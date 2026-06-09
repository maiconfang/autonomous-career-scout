from dataclasses import dataclass


@dataclass
class CareerRecommendation:
    summary: str
    strengths: list[str]
    improvement_areas: list[str]
    recommended_actions: list[str]