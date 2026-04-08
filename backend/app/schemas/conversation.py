from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.common import ORMModel
from app.schemas.message import MessageRead
from app.schemas.tool_run import ToolRunRead


class ConversationCreate(BaseModel):
  title: str = Field(default="New conversation", min_length=1, max_length=255)


class ConversationUpdate(BaseModel):
  title: str = Field(min_length=1, max_length=255)


class ConversationRead(ORMModel):
  id: UUID
  title: str
  created_at: datetime
  updated_at: datetime


class ConversationDetailRead(ConversationRead):
  messages: list[MessageRead]
  tool_runs: list[ToolRunRead] = []
