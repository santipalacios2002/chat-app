import type { Message } from "@/lib/types";

type MessageListProps = {
  messages: Message[];
};

export function MessageList({ messages }: MessageListProps) {
  if (messages.length === 0) {
    return (
      <div className="flex h-full items-center justify-center rounded-[2rem] border border-dashed border-ink/12 bg-white/55 p-8 text-center text-sm leading-6 text-ink/55">
        Ask a question, draft an idea, or test the API. The MVP stores each exchange so this can
        grow into a real multi-conversation app.
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {messages.map((message) => {
        const isUser = message.role === "user";

        return (
          <article
            key={message.id}
            className={`max-w-3xl rounded-[1.75rem] border px-5 py-4 shadow-sm ${
              isUser
                ? "ml-auto border-ember/25 bg-ember/10"
                : "border-ink/8 bg-white/90"
            }`}
          >
            <p className="mb-2 text-xs uppercase tracking-[0.2em] text-ink/45">{message.role}</p>
            <p className="whitespace-pre-wrap text-sm leading-7 text-ink/85">{message.content}</p>
          </article>
        );
      })}
    </div>
  );
}

