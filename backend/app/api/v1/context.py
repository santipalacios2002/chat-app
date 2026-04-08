from fastapi import APIRouter, status

from app.api.deps import DbSession
from app.schemas.context import ContextBlockCreate, ContextBlockRead
from app.services.context_service import create_context_block, list_context_blocks

router = APIRouter()


@router.get("/", response_model=list[ContextBlockRead])
def read_context_blocks(db: DbSession) -> list[ContextBlockRead]:
  return list_context_blocks(db)


@router.post("/", response_model=ContextBlockRead, status_code=status.HTTP_201_CREATED)
def create_context_block_endpoint(payload: ContextBlockCreate, db: DbSession) -> ContextBlockRead:
  return create_context_block(
    db,
    key=payload.key,
    content=payload.content,
    is_active=payload.is_active,
  )
