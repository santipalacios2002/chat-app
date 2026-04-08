from typing import Any
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.tool_run import ToolRun


def maybe_collect_web_context(
  db: Session,
  conversation_id: UUID | None,
  user_message: str,
  enabled: bool,
) -> dict[str, Any] | None:
  if not enabled:
    return None

  output = {
    "mode": "placeholder",
    "summary": f"Optional web context is enabled for: {user_message[:120]}",
  }

  tool_run = ToolRun(
    conversation_id=conversation_id,
    tool_name="web-context",
    status="completed",
    input_payload={"message": user_message},
    output_payload=output,
  )
  db.add(tool_run)
  db.commit()

  return output

