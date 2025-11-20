from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    EBAY_PROD_CLIENT_ID: str
    EBAY_VERIFICATION_TOKEN: str
    BASE_URL: str
    EBAY_SANDBOX_CLIENT_ID: str


    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()