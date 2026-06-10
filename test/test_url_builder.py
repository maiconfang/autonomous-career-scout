from src.config.search_profiles import (
    QA_CANADA
)

from src.services.linkedin_url_builder import (
    LinkedInUrlBuilder
)


url = LinkedInUrlBuilder.build(
    QA_CANADA
)

print("\nGenerated URL:\n")

print(url)