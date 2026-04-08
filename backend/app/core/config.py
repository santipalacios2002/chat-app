from functools import cached_property
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  model_config = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    case_sensitive=False,
  )

  app_name: str = "Chat App API"
  api_v1_prefix: str = "/api/v1"
  database_url: str = "postgresql+psycopg://chatapp:chatapp@postgres:5432/chatapp"
  openai_api_key: str | None = None
  openai_model: str = "gpt-4.1-mini"
  backend_cors_origins: list[str] = ["http://localhost:3000"]

  @field_validator("backend_cors_origins", mode="before")
  @classmethod
  def parse_cors_origins(cls, value: str | list[str]) -> list[str]:
    if isinstance(value, list):
      return value

    return [item.strip() for item in value.split(",") if item.strip()]

  @cached_property
  def prompts_dir(self) -> Path:
    return Path(__file__).resolve().parent.parent / "prompts"


settings = Settings()

