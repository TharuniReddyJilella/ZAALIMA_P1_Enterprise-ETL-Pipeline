from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_ENV = os.getenv("APP_ENV")

    STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

    SALESFORCE_CLIENT_ID = os.getenv("SALESFORCE_CLIENT_ID")
    SALESFORCE_CLIENT_SECRET = os.getenv("SALESFORCE_CLIENT_SECRET")
    SALESFORCE_USERNAME = os.getenv("SALESFORCE_USERNAME")
    SALESFORCE_PASSWORD = os.getenv("SALESFORCE_PASSWORD")

    DATABASE_URL = os.getenv("DATABASE_URL")

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    S3_BUCKET = os.getenv("S3_BUCKET")

    LOG_LEVEL = os.getenv("LOG_LEVEL")


settings = Settings()