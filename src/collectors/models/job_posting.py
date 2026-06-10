from dataclasses import dataclass


@dataclass
class JobPosting:

    title: str

    company: str

    location: str

    description: str

    source: str

    url: str