from dataclasses import dataclass
from typing import List


@dataclass
class JobPosting:

    title: str

    company: str

    location: str

    salary: str

    skills: List[str]

    description: str