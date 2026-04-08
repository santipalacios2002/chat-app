from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.api.deps import DbSession
from app.schemas.common import DeleteResponse
from app.schemas.conversation import (
  ConversationCreate,
  ConversationDetailRead,
  ConversationRead,
  ConversationUpdate,
)
from app.services.chat_service import (
  create_conversation,
  delete_conversation,
  get_conversation,
  list_conversations,
  update_conversation,
)

router = APIRouter()


@router.get("/", response_model=list[ConversationRead])
def read_conversations(db: DbSession) -> list[ConversationRead]:
  return list_conversations(db)


@router.post("/", response_model=ConversationRead, status_code=status.HTTP_201_CREATED)
def create_conversation_endpoint(
  payload: ConversationCreate,
  db: DbSession,
) -> ConversationRead:
  return create_conversation(db, title=payload.title)


@router.get("/{conversation_id}", response_model=ConversationDetailRead)
def read_conversation(conversation_id: UUID, db: DbSession) -> ConversationDetailRead:
  conversation = get_conversation(db, conversation_id)
  if conversation is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")

  return conversation


@router.patch("/{conversation_id}", response_model=ConversationRead)
def update_conversation_endpoint(
  conversation_id: UUID,
  payload: ConversationUpdate,
  db: DbSession,
) -> ConversationRead:
  conversation = update_conversation(db, conversation_id=conversation_id, title=payload.title)
  if conversation is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")

  return conversation


@router.delete("/{conversation_id}", response_model=DeleteResponse)
def delete_conversation_endpoint(conversation_id: UUID, db: DbSession) -> DeleteResponse:
  deleted = delete_conversation(db, conversation_id)
  if deleted is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")

  return deleted
