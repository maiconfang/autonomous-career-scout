from dataclasses import dataclass


@dataclass
class SearchCriteria:

    keywords: str

    location: str = "Canada"

    posted_last_seconds: int = 172800

    remote_only: bool = True

    experience_levels: list[int] | None = None

    job_types: list[str] | None = None

    under_10_applicants: bool = True

    sort_by: str = "DD"