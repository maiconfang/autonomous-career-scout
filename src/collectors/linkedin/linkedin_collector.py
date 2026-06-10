from urllib.parse import quote

from src.collectors.playwright.playwright_collector import (
    PlaywrightCollector
)


class LinkedInCollector:

    def __init__(self):

        self.playwright_collector = (
            PlaywrightCollector()
        )

    def search_jobs(
        self,
        keyword: str,
        location: str,
        limit: int = 10
    ):

        encoded_keyword = quote(
            keyword
        )

        encoded_location = quote(
            location
        )

        search_url = (
            "https://www.linkedin.com/jobs/search/"
            f"?keywords={encoded_keyword}"
            f"&location={encoded_location}"
        )

        print(
            f"\nOpening LinkedIn Search:\n{search_url}\n"
        )

        return self.playwright_collector.collect(
            search_url
        )