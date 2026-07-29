from app.api.api_client import APIClient


class StripeExtractor:
    def __init__(self):
        self.client = APIClient("https://jsonplaceholder.typicode.com")

    def extract_customers(self):
        """
        Temporary implementation using JSONPlaceholder.
        Later we will replace this with the real Stripe API.
        """
        return self.client.get("/users")