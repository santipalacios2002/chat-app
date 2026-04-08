from pathlib import Path
from typing import Sequence

from openai import OpenAI

from app.core.config import settings
from app.models.context_block import ContextBlock
from app.models.message import Message


def _read_prompt(path: Path) -> str:
  if path.exists():
    return path.read_text(encoding="utf-8").strip()

  return ""


def _format_context_blocks(context_blocks: Sequence[ContextBlock]) -> str:
  if not context_blocks:
    return ""

  return "\n\n".join(f"{block.key}:\n{block.content}" for block in context_blocks)


def _format_history_messages(history: Sequence[Message]) -> list[dict[str, str]]:
  return [{"role": message.role, "content": message.content} for message in history]


def generate_reply(
  conversation_history: Sequence[Message],
  active_context_blocks: Sequence[ContextBlock],
  web_context: str = "",
) -> str:
  system_prompt = _read_prompt(settings.prompts_dir / "system_prompt.txt")
  context_text = _format_context_blocks(active_context_blocks)
  history_messages = _format_history_messages(conversation_history)
  latest_user_message = next(
    (message.content for message in reversed(conversation_history) if message.role == "user"),
    "",
  )

  if not settings.openai_api_key:
    details = []
    if context_text:
      details.append("app context attached")
    if web_context:
      details.append("web context requested")
    if history_messages:
      details.append(f"{len(history_messages)} messages in history")

    suffix = f" ({', '.join(details)})" if details else ""
    return (
      "Mock assistant response"
      f"{suffix}: you said \"{latest_user_message}\". Add an `OPENAI_API_KEY` to switch this scaffold"
      " to live model calls."
    )

  client = OpenAI(api_key=settings.openai_api_key)
  response = client.responses.create(
    model=settings.openai_model,
    input=[
      {
        "role": "system",
        "content": f"{system_prompt}\n\nApplication context:\n{context_text}\n\nWeb context:\n{web_context}",
      },
      *history_messages,
    ],
  )

  return response.output_text.strip()
