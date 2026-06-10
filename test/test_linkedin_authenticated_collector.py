from src.collectors.linkedin.linkedin_authenticated_collector import (
    LinkedInAuthenticatedCollector
)

from src.config.search_profiles import (
    QA_CANADA
)


def main():

    collector = (
        LinkedInAuthenticatedCollector()
    )

    collector.collect(
        criteria=QA_CANADA
    )


if __name__ == "__main__":
    main()