from playwright.sync_api import sync_playwright

from src.config.search_profiles import QA_CANADA
from src.services.linkedin_url_builder import LinkedInUrlBuilder


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context(
            storage_state="storage/linkedin_storage_state.json"
        )

        page = context.new_page()

        page.goto(
            LinkedInUrlBuilder.build(
                QA_CANADA
            ),
            wait_until="domcontentloaded"
        )

        page.wait_for_timeout(
            5000999
        )

        print(
            "\nTrying LinkedIn jobs panel scroll..."
        )

        jobs_panel = page.locator(
            ".scaffold-layout__list"
        )

        print(
            f"Found: {jobs_panel.count()}"
        )

        jobs_panel.hover()

        for i in range(20):

            print(
                f"Scroll {i + 1}"
            )

            page.mouse.wheel(
                0,
                800
            )

            page.wait_for_timeout(
                1000
            )

        input(
            "\nPress ENTER to close..."
        )

        browser.close()


if __name__ == "__main__":
    main()