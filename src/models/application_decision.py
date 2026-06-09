from dataclasses import dataclass


@dataclass
class ApplicationDecision:
    decision: str
    confidence: str
    reason: str