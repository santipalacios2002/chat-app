"use client";

import { useState } from "react";

type MessageInputProps = {
  disabled?: boolean;
  onSend: (value: string) => Promise<void>;
};

export function MessageInput({ disabled = false, onSend }: MessageInputProps) {
  const [value, setValue] = useState("");

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const trimmed = value.trim();
    if (!trimmed || disabled) {
      return;
    }

    setValue("");
    await onSend(trimmed);
  }

  return (
    <form onSubmit={handleSubmit} className="glass-panel space-y-3 p-4">
      <textarea
        value={value}
        onChange={(event) => setValue(event.target.value)}
        placeholder="Send a message to the backend orchestration layer..."
        rows={4}
        className="min-h-28 w-full resize-none rounded-[1.5rem] border border-ink/10 bg-white/80 px-4 py-3 text-sm text-ink outline-none transition placeholder:text-ink/35 focus:border-ember/40 focus:ring-2 focus:ring-ember/15"
      />
      <div className="flex items-center justify-between gap-3">
        <p className="text-xs text-ink/45">
          Messages are persisted in PostgreSQL and returned through FastAPI.
        </p>
        <button type="submit" className="primary-button disabled:opacity-60" disabled={disabled}>
          {disabled ? "Sending..." : "Send"}
        </button>
      </div>
    </form>
  );
}

