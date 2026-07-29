import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from app.logger.logger import logger


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def get(self, endpoint: str, params=None):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"GET {url}")

        response = requests.get(
            url,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        logger.info("Request completed successfully")

        return response.json()

    def get_paginated(self, endpoint: str, page: int = 1, limit: int = 5):
        params = {
            "_page": page,
            "_limit": limit,
        }

        return self.get(endpoint, params=params)