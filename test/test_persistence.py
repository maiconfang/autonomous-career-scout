from src.services.opportunity_persistence_service import (
    OpportunityPersistenceService
)

OpportunityPersistenceService().save_from_json(
    "reports/opportunities.json"
)