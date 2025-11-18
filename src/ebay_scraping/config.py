from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    EBAY_VERIFICATION_TOKEN : str
    BASE_URL: str


    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()