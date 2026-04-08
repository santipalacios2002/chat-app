from fastapi import APIRouter

from app.api.deps import DbSession
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import send_chat_message

router = APIRouter()


@router.post("/", response_model=ChatResponse)
def chat(payload: ChatRequest, db: DbSession) -> ChatResponse:
  return send_chat_message(
    db,
    conversation_id=payload.conversation_id,
    user_message=payload.message,
    use_web_context=payload.use_web_context,
  )

