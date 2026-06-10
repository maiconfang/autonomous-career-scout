from src.collectors.playwright.playwright_collector import (
    PlaywrightCollector
)


def main():

    collector = PlaywrightCollector()

    job = collector.collect(
        "https://example.com"
    )

    print("\n=== PLAYWRIGHT COLLECTOR TEST ===\n")

    print(job)


if __name__ == "__main__":
    main()