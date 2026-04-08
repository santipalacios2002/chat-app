import uuid
from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Conversation(Base):
  __tablename__ = "conversations"

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  title: Mapped[str] = mapped_column(String(255), default="New conversation")
  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),
    onupdate=func.now(),
  )

  messages = relationship(
    "Message",
    back_populates="conversation",
    cascade="all, delete-orphan",
    order_by="Message.created_at",
  )
  tool_runs = relationship("ToolRun", back_populates="conversation", cascade="all, delete-orphan")

