from app.api.api_client import APIClient

from app.config.settings import settings
class StripeExtractor:
    def __init__(self):
       self.client = APIClient(settings.API_BASE_URL)

    def extract_customers(self, page=1, limit=5):
        return self.client.get_paginated(
            "/users",
            page=page,
            limit=limit,
        )