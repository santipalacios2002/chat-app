from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.conversation import Conversation
from app.models.message import Message
from app.schemas.common import DeleteResponse
from app.schemas.chat import ChatResponse
from app.schemas.conversation import ConversationRead
from app.schemas.message import MessageRead
from app.schemas.tool_run import ToolRunRead
from app.services.context_service import list_active_context_blocks
from app.services.llm_service import generate_reply
from app.services.tool_service import maybe_collect_web_context


def list_conversations(db: Session) -> list[Conversation]:
  statement = select(Conversation).order_by(Conversation.updated_at.desc(), Conversation.created_at.desc())
  return list(db.scalars(statement))


def create_conversation(db: Session, title: str = "New conversation") -> Conversation:
  conversation = Conversation(title=title)
  db.add(conversation)
  db.commit()
  db.refresh(conversation)
  return conversation


def get_conversation(db: Session, conversation_id: UUID) -> Conversation | None:
  statement = (
    select(Conversation)
    .where(Conversation.id == conversation_id)
    .options(
      selectinload(Conversation.messages),
      selectinload(Conversation.tool_runs),
    )
  )
  return db.scalar(statement)


def update_conversation(db: Session, conversation_id: UUID, title: str) -> Conversation | None:
  conversation = get_conversation(db, conversation_id)
  if conversation is None:
    return None

  conversation.title = title
  conversation.updated_at = datetime.now(timezone.utc)
  db.commit()
  db.refresh(conversation)
  return conversation


def delete_conversation(db: Session, conversation_id: UUID) -> DeleteResponse | None:
  conversation = get_conversation(db, conversation_id)
  if conversation is None:
    return None

  deleted_at = datetime.now(timezone.utc)
  db.delete(conversation)
  db.commit()
  return DeleteResponse(id=conversation_id, deleted_at=deleted_at)


def _build_title(message: str) -> str:
  trimmed = " ".join(message.split())
  if not trimmed:
    return "New conversation"

  return trimmed[:60]


def _save_message(db: Session, conversation_id: UUID, role: str, content: str) -> Message:
  entry = Message(conversation_id=conversation_id, role=role, content=content)
  db.add(entry)
  db.commit()
  db.refresh(entry)
  return entry


def _normalize_chat_response(
  conversation: Conversation,
  user_message: Message,
  assistant_message: Message,
) -> ChatResponse:
  return ChatResponse(
    conversation=ConversationRead.model_validate(conversation),
    message=MessageRead.model_validate(user_message),
    reply=MessageRead.model_validate(assistant_message),
    tool_runs=[ToolRunRead.model_validate(tool_run) for tool_run in conversation.tool_runs],
  )


def send_chat_message(
  db: Session,
  conversation_id: UUID | None,
  user_message: str,
  use_web_context: bool,
) -> ChatResponse:
  conversation = get_conversation(db, conversation_id) if conversation_id else None
  if conversation is None:
    conversation = create_conversation(db, title=_build_title(user_message))

  user_entry = _save_message(db, conversation.id, role="user", content=user_message)

  conversation = get_conversation(db, conversation.id)
  if conversation is None:
    raise ValueError("Conversation disappeared after saving the user message.")

  context_blocks = list_active_context_blocks(db)
  web_context = maybe_collect_web_context(db, conversation.id, user_message, use_web_context)
  web_context_text = web_context["summary"] if web_context else ""

  assistant_text = generate_reply(
    conversation_history=conversation.messages,
    active_context_blocks=context_blocks,
    web_context=web_context_text,
  )

  assistant_entry = _save_message(db, conversation.id, role="assistant", content=assistant_text)

  conversation = get_conversation(db, conversation.id)
  if conversation is None:
    raise ValueError("Conversation disappeared after saving the assistant response.")

  conversation.updated_at = datetime.now(timezone.utc)
  db.commit()
  db.refresh(conversation)

  return _normalize_chat_response(conversation, user_entry, assistant_entry)
