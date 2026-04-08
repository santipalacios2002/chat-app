from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.context_block import ContextBlock


def list_context_blocks(db: Session) -> list[ContextBlock]:
  return list(db.scalars(select(ContextBlock).order_by(ContextBlock.created_at.desc())))


def list_active_context_blocks(db: Session) -> list[ContextBlock]:
  statement = (
    select(ContextBlock)
    .where(ContextBlock.is_active.is_(True))
    .order_by(ContextBlock.created_at.desc())
  )
  return list(db.scalars(statement))


def create_context_block(db: Session, key: str, content: str, is_active: bool = True) -> ContextBlock:
  block = ContextBlock(key=key, content=content, is_active=is_active)
  db.add(block)
  db.commit()
  db.refresh(block)
  return block
