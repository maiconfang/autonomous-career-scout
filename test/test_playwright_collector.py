from src.collectors.playwright.playwright_collector import (
    PlaywrightCollector
)

collector = PlaywrightCollector()

job = collector.collect_example()

print(job)