from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Enterprise ETL Pipeline"
    APP_VERSION: str = "1.0.0"

    STRIPE_API_KEY: str = ""
    SALESFORCE_API_KEY: str = ""

    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()