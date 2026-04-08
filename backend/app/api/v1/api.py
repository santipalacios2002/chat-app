from fastapi import APIRouter

from app.api.v1 import chat, context, conversations, health

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(conversations.router, prefix="/conversations", tags=["conversations"])
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(context.router, prefix="/context", tags=["context"])

