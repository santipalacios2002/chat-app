from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ORMModel(BaseModel):
  model_config = ConfigDict(from_attributes=True)


class HealthResponse(BaseModel):
  status: str
  service: str = "backend"
  version: str = "0.1.0"


class DeleteResponse(BaseModel):
  success: bool = True
  id: UUID
  deleted_at: datetime
