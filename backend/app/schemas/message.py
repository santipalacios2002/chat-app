from datetime import datetime
from uuid import UUID

from app.schemas.common import ORMModel


class MessageRead(ORMModel):
  id: UUID
  conversation_id: UUID
  role: str
  content: str
  created_at: datetime

