from playwright.sync_api import sync_playwright


class PlaywrightClient:

    def get_page_content(self, url: str) -> str:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto(url)

            content = page.content()

            browser.close()

            return content