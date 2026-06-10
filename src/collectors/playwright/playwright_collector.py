from playwright.sync_api import sync_playwright


class PlaywrightCollector:

    def collect(
        self,
        url: str
    ):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto(
                url,
                wait_until="networkidle"
            )

            print("\n=== JOBS FOUND ===\n")

            try:

                page.wait_for_selector(
                    "div.base-search-card",
                    timeout=10000
                )

                cards = page.locator(
                    "div.base-search-card"
                )

                count = min(
                    cards.count(),
                    10
                )

                for index in range(count):

                    card = cards.nth(index)

                    try:
                        title = card.locator(
                            "h3"
                        ).inner_text().strip()
                    except:
                        title = "N/A"

                    try:
                        company = card.locator(
                            "h4"
                        ).inner_text().strip()
                    except:
                        company = "N/A"

                    try:
                        location = card.locator(
                            ".job-search-card__location"
                        ).inner_text().strip()
                    except:
                        location = "N/A"

                    print(
                        f"""
{index + 1})

Title: {title}
Company: {company}
Location: {location}
"""
                    )

            except Exception as ex:

                print(
                    f"Error collecting jobs: {ex}"
                )

            input(
                "\nPress ENTER to continue..."
            )

            browser.close()