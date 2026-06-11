from playwright.sync_api import sync_playwright
from posthog import page

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

from src.services.job_skill_extractor import (
    JobSkillExtractor
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

        jobs_panel = page.locator(
            ".scaffold-layout__list"
        )

        jobs_panel.hover()

        previous_count = 0

        no_change_attempts = 0

        while True:

            current_count = page.locator(
                "[data-occludable-job-id]"
            ).count()

            print(
                f"Cards loaded: {current_count}"
            )

            if current_count == previous_count:

                no_change_attempts += 1

                print(
                    f"No new jobs found "
                    f"({no_change_attempts}/3)"
                )

            else:

                no_change_attempts = 0

            if no_change_attempts >= 3:

                print(
                    "\nAll jobs loaded."
                )

                break

            previous_count = current_count

            page.mouse.wheel(
                0,
                800
            )

            page.wait_for_timeout(
                1500
            )

    def collect(
        self,
        criteria: SearchCriteria = QA_CANADA
    ) -> list[JobPosting]:

        jobs = []

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
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

            page.wait_for_selector(
                "[data-occludable-job-id]"
            )

            self.scroll_until_loaded(
                page
            )

            print("\nCurrent URL:")
            print(page.url)

            print("\nPage Title:")
            print(page.title())

            job_cards = page.locator(
               "[data-occludable-job-id]"
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
                    
                    card.click()

                    page.wait_for_timeout(3000)
                    
                    print("\nDETAIL PANEL FOUND:")

                    print(
                        page.locator(
                            "#job-details"
                        ).count()
                    )
                    
                    description = (
                        page
                        .locator("#job-details")
                        .text_content()
                    )

                    print(
                        f"\nDESCRIPTION LENGTH: {len(description)}"
                    )
                    
                    if not card.locator(
                        ".job-card-list__title--link"
                    ).count():
                        continue

                    title = ""

                    company = ""

                    location = ""
                    
                    job_url = ""

                    try:

 
                        title_locator = card.locator(
                            ".job-card-list__title--link"
                        ).first

                        title = (
                            title_locator.text_content() or ""
                        ).strip()

                        href = title_locator.get_attribute(
                            "href"
                        )

                        job_url = ""

                        if href:

                            job_url = (
                                "https://www.linkedin.com"
                                + href
                            )

                        linkedin_job_id = ""

                        if "/jobs/view/" in job_url:

                            linkedin_job_id = (
                                job_url
                                .split("/jobs/view/")[1]
                                .split("/")[0]
                                .split("?")[0]
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
                            .text_content() or ""
                        ).strip()

                    except:
                        pass

                    try:

                        location = (
                            card
                            .locator(
                                ".artdeco-entity-lockup__caption"
                            )
                            .first
                            .text_content() or ""
                        ).strip()

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
                    
                    print(
                        f"JOB ID: {linkedin_job_id}"
                    )
                    
                    skills = (
                        JobSkillExtractor.extract(
                            description
                        )
                    )

                    print(
                        f"SKILLS: {skills}"
                    )

                    job = JobPosting(
                        title=title,
                        company=company,
                        location=location,
                        salary="",
                        skills=skills,
                        description=description,
                        job_url=job_url,
                        linkedin_job_id=linkedin_job_id
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