import time

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

from app.config.settings import settings
from app.logger.logger import logger


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )
    def get(self, endpoint: str, params=None):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"GET {url}")

        try:
            # Simulate rate limiting
            time.sleep(1)

            response = requests.get(
                url,
                params=params,
                timeout=settings.REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            logger.info("Request completed successfully")

            return response.json()

        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise

    def get_paginated(self, endpoint: str, page: int = 1, limit: int = 5):
        params = {
            "_page": page,
            "_limit": limit,
        }

        return self.get(endpoint, params=params)