from src.services.opportunity_query_service import (
    OpportunityQueryService
)


service = (
    OpportunityQueryService()
)

service.print_top_jobs(
    minimum_score=60
)