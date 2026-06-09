from dataclasses import dataclass


@dataclass
class MatchResult:
    score: int
    matched_skills: list[str]
    missing_skills: list[str]