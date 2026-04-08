from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.common import ORMModel


class ContextBlockCreate(BaseModel):
  key: str = Field(min_length=1, max_length=100)
  content: str = Field(min_length=1)
  is_active: bool = True


class ContextBlockRead(ORMModel):
  id: UUID
  key: str
  content: str
  is_active: bool
  created_at: datetime
