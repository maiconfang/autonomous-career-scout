from dataclasses import dataclass, field
from typing import List


@dataclass
class JobPosting:

    title: str

    company: str

    location: str

    salary: str = ""

    skills: List[str] = field(default_factory=list)

    description: str = ""

    job_url: str = ""

    linkedin_job_id: str = ""