from datetime import datetime
from typing import Any
from uuid import UUID

from app.schemas.common import ORMModel


class ToolRunRead(ORMModel):
  id: UUID
  conversation_id: UUID | None
  tool_name: str
  status: str
  input_payload: dict[str, Any] | None
  output_payload: dict[str, Any] | None
  created_at: datetime
