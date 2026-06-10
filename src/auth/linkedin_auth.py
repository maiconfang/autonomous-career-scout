from pathlib import Path
import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


load_dotenv()


LINKEDIN_EMAIL = os.getenv(
    "LINKEDIN_EMAIL"
)

LINKEDIN_PASSWORD = os.getenv(
    "LINKEDIN_PASSWORD"
)

STORAGE_STATE_FILE = (
    Path("storage")
    / "linkedin_storage_state.json"
)


def main():

    print("\n=== ENV VALIDATION ===")
    print(f"EMAIL: {LINKEDIN_EMAIL}")
    print(
        f"PASSWORD: {'***' if LINKEDIN_PASSWORD else 'NOT FOUND'}"
    )
    print("======================\n")

    STORAGE_STATE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if not LINKEDIN_EMAIL:
        raise ValueError(
            "LINKEDIN_EMAIL not found in .env"
        )

    if not LINKEDIN_PASSWORD:
        raise ValueError(
            "LINKEDIN_PASSWORD not found in .env"
        )

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()

        print(
            "Opening LinkedIn Login..."
        )

        page.goto(
            "https://www.linkedin.com/login/"
        )

        page.get_by_role(
            "textbox",
            name="Email or phone"
        ).fill(
            LINKEDIN_EMAIL
        )

        page.get_by_role(
            "textbox",
            name="Password"
        ).fill(
            LINKEDIN_PASSWORD
        )

        print(
            "\nCredentials filled successfully."
        )

        input(
            "\nVerify credentials and press ENTER to submit login..."
        )

        page.get_by_role(
            "button",
            name="Sign in",
            exact=True
        ).click()

        input(
            "\nAfter LinkedIn is fully loaded, press ENTER to save the session..."
        )

        page.context.storage_state(
            path=str(
                STORAGE_STATE_FILE
            )
        )

        print(
            f"\nSession saved successfully:"
        )

        print(
            STORAGE_STATE_FILE
        )

        browser.close()


if __name__ == "__main__":
    main()