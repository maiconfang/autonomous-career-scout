from playwright.sync_api import sync_playwright


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context(
            storage_state=
            "storage/linkedin_storage_state.json"
        )

        page = context.new_page()

        page.goto(
            "https://www.linkedin.com/feed/"
        )

        input(
            "\nPress ENTER to close..."
        )

        browser.close()


if __name__ == "__main__":
    main()