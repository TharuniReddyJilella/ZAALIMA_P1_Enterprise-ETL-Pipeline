from app.api.api_client import APIClient


class StripeExtractor:
    def __init__(self):
        self.client = APIClient(
            "https://jsonplaceholder.typicode.com"
        )

    def extract_customers(self, page=1, limit=5):
        return self.client.get_paginated(
            "/users",
            page=page,
            limit=limit,
        )