import requests
from tenacity import retry, stop_after_attempt, wait_fixed

from app.logger.logger import logger


class APIClient:
    def __init__(self, base_url: str, headers: dict | None = None):
        self.base_url = base_url
        self.headers = headers or {}

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def get(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"Sending GET request to {url}")

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        logger.info("Request successful")

        return response.json()