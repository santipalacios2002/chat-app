import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import JSON, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ToolRun(Base):
  __tablename__ = "tool_runs"

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  conversation_id: Mapped[uuid.UUID | None] = mapped_column(
    UUID(as_uuid=True),
    ForeignKey("conversations.id", ondelete="CASCADE"),
    index=True,
    nullable=True,
  )
  tool_name: Mapped[str] = mapped_column(String(100))
  status: Mapped[str] = mapped_column(String(50), default="completed")
  input_payload: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
  output_payload: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

  conversation = relationship("Conversation", back_populates="tool_runs")

