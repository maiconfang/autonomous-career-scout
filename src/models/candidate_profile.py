from dataclasses import dataclass
from typing import List


@dataclass
class CandidateProfile:

    years_experience: int

    skills: List[str]