from playwright.sync_api import sync_playwright

from src.models.job_posting import JobPosting
from src.models.search_criteria import SearchCriteria

from src.config.search_profiles import (
    QA_CANADA
)

from src.services.linkedin_url_builder import (
    LinkedInUrlBuilder
)

from src.exporters.job_exporter import (
    JobExporter
)


class LinkedInAuthenticatedCollector:

    STORAGE_STATE = (
        "storage/linkedin_storage_state.json"
    )

    INVALID_VALUES = [
        "·",
        "Privacy & Terms",
        "Ad Choices",
        "Advertising",
        "About",
        "Accessibility",
        "Get the LinkedIn app",
        "More",
        "LinkedIn Corporation ©",
        "Try Premium",
    ]
    
    def scroll_until_loaded(
        self,
        page
    ):

        previous_count = 0

        while True:

            current_count = page.locator(
                "[data-occludable-job-id]"
            ).count()

            print(
                f"Cards loaded: {current_count}"
            )

            if current_count == previous_count:

                print(
                    "\nAll jobs loaded."
                )

                break

            previous_count = current_count

            page.mouse.wheel(
                0,
                10000
            )

            page.wait_for_timeout(
                2000
            )

    def collect(
        self,
        criteria: SearchCriteria = QA_CANADA
    ) -> list[JobPosting]:

        jobs = []

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            context = browser.new_context(
                storage_state=self.STORAGE_STATE
            )

            page = context.new_page()

            search_url = (
                LinkedInUrlBuilder.build(
                    criteria
                )
            )

            print("\nOpening URL:")
            print(search_url)

            page.goto(
                search_url,
                wait_until="domcontentloaded"
            )

            page.wait_for_timeout(
                8000
            )
            
            self.scroll_until_loaded(
                page
            )

            print("\nCurrent URL:")
            print(page.url)

            print("\nPage Title:")
            print(page.title())

            job_cards = page.locator(
                 "[componentkey*='job-card-component-ref']"
            )

            total_cards = job_cards.count()

            print(
                f"\nJob Cards Found: {total_cards}"
            )

            print(
                "\nJobs Found:\n"
            )

            for i in range(total_cards):
                
                print(
                    f"\nProcessing card {i + 1}/{total_cards}"
                )

                try:

                    card = job_cards.nth(i)

                    title = ""

                    company = ""

                    location = ""

                    try:

                        title = (
                            card
                            .locator(
                                ".job-card-list__title--link"
                            )
                            .first
                            .inner_text()
                            .strip()
                        )

                    except:
                        pass

                    try:

                        company = (
                            card
                            .locator(
                                ".artdeco-entity-lockup__subtitle"
                            )
                            .first
                            .inner_text()
                            .strip()
                        )

                    except:
                        pass

                    try:

                        location = (
                            card
                            .locator(
                                ".artdeco-entity-lockup__caption"
                            )
                            .first
                            .inner_text()
                            .strip()
                        )

                    except:
                        pass

                    if not title:
                        continue

                    if any(
                        invalid.lower() in title.lower()
                        for invalid in self.INVALID_VALUES
                    ):
                        continue

                    print(
                        "\n-----------------------------------"
                    )

                    print(
                        f"TITLE: {title}"
                    )

                    print(
                        f"COMPANY: {company}"
                    )

                    print(
                        f"LOCATION: {location}"
                    )

                    job = JobPosting(
                        title=title,
                        company=company,
                        location=location,
                        salary="",
                        skills=[],
                        description=""
                    )

                    jobs.append(
                        job
                    )

                except Exception as e:

                    print(
                        f"ERROR CARD {i}: {e}"
                    )

            print(
                f"\nTotal jobs collected: {len(jobs)}"
            )

            JobExporter.export_to_json(
                jobs
            )

            print(
                "\nCollection completed."
            )

            input(
                "\nPress ENTER to close..."
            )

            browser.close()

        return jobs