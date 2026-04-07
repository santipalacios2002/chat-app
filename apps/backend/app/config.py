from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "chat-api"
    database_url: str = "postgresql://chat_user:chat_password@db:5432/chat_app"


settings = Settings()
