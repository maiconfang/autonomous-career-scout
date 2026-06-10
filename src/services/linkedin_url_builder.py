from urllib.parse import quote

from src.models.search_criteria import (
    SearchCriteria
)


class LinkedInUrlBuilder:

    @staticmethod
    def build(
        criteria: SearchCriteria
    ) -> str:

        url = (
            "https://www.linkedin.com/jobs/search/"
            f"?keywords={quote(criteria.keywords)}"
            f"&location={quote(criteria.location)}"
        )

        url += (
            f"&f_TPR=r{criteria.posted_last_seconds}"
        )

        if criteria.remote_only:

            url += "&f_WT=2"

        if criteria.experience_levels:

            levels = ",".join(
                str(level)
                for level in criteria.experience_levels
            )

            url += f"&f_E={levels}"

        if criteria.job_types:

            job_types = ",".join(
                criteria.job_types
            )

            url += f"&f_JT={job_types}"

        if criteria.under_10_applicants:

            url += "&f_SB2=2"

        url += (
            f"&sortBy={criteria.sort_by}"
        )

        return url