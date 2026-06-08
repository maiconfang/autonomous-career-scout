from src.services.job_matcher import JobMatcher
from src.services.job_parser import JobParser
from src.services.profile_service import ProfileService
from src.tools.playwright_client import PlaywrightClient
from src.tools.scraper_tool import ScraperTool


def main():

    playwright_client = PlaywrightClient()

    scraper_tool = ScraperTool()

    job_parser = JobParser()

    profile_service = ProfileService()

    job_matcher = JobMatcher()

    html = playwright_client.get_page_content(
        "https://ca.indeed.com/viewjob?jk=8cc5df99bb9e0fe2"
    )

    text = scraper_tool.extract_text(
        html
    )

    job_posting = job_parser.parse(
        text
    )

    candidate_profile = profile_service.load_profile()

    match_result = job_matcher.calculate_match(
        candidate_profile,
        job_posting
    )

    print("\n=== JOB ===")
    print(job_posting)

    print("\n=== CANDIDATE ===")
    print(candidate_profile)

    print("\n=== MATCH RESULT ===")
    print(match_result)


if __name__ == "__main__":
    main()