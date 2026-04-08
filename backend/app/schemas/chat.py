from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.message import MessageRead
from app.schemas.conversation import ConversationRead
from app.schemas.tool_run import ToolRunRead


class ChatRequest(BaseModel):
  conversation_id: UUID | None = None
  message: str = Field(min_length=1)
  use_web_context: bool = False


class ChatResponse(BaseModel):
  conversation: ConversationRead
  message: MessageRead
  reply: MessageRead
  tool_runs: list[ToolRunRead] = []
