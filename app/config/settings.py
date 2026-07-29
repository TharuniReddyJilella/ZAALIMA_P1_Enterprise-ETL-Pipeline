import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    API_BASE_URL = os.getenv("API_BASE_URL")
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 30))


settings = Settings()