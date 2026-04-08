"use client";

import { useEffect, useState, useTransition } from "react";

import { MessageInput } from "@/components/MessageInput";
import { MessageList } from "@/components/MessageList";
import { Sidebar } from "@/components/Sidebar";
import { getConversation, getConversations, sendChatMessage } from "@/lib/api";
import type { Conversation, Message } from "@/lib/types";

type ChatWindowProps = {
  initialConversationId?: string;
};

export function ChatWindow({ initialConversationId }: ChatWindowProps) {
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [messages, setMessages] = useState<Message[]>([]);
  const [currentConversationId, setCurrentConversationId] = useState<string | null>(
    initialConversationId ?? null,
  );
  const [useWebContext, setUseWebContext] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  useEffect(() => {
    void loadConversations();
  }, []);

  useEffect(() => {
    if (initialConversationId) {
      void loadConversation(initialConversationId);
    }
  }, [initialConversationId]);

  async function loadConversations() {
    try {
      const response = await getConversations();
      setConversations(response);
    } catch (caughtError) {
      console.error(caughtError);
      setError("Unable to load conversations from the backend.");
    }
  }

  async function loadConversation(conversationId: string) {
    try {
      const conversation = await getConversation(conversationId);
      setCurrentConversationId(conversation.id);
      setMessages(conversation.messages ?? []);
      setError(null);
    } catch (caughtError) {
      console.error(caughtError);
      setError("Unable to load the selected conversation.");
    }
  }

  async function handleSend(content: string) {
    setError(null);

    startTransition(() => {
      void (async () => {
        try {
          const response = await sendChatMessage({
            conversation_id: currentConversationId,
            message: content,
            use_web_context: useWebContext,
          });

          setCurrentConversationId(response.conversation.id);
          setMessages((previous) => {
            if (response.conversation.id !== currentConversationId) {
              return [response.message, response.reply];
            }

            return [...previous, response.message, response.reply];
          });

          await loadConversations();
        } catch (caughtError) {
          console.error(caughtError);
          setError("Unable to send the message. Check that the backend is running.");
        }
      })();
    });
  }

  return (
    <div className="grid gap-4 lg:grid-cols-[320px_minmax(0,1fr)]">
      <Sidebar
        conversations={conversations}
        currentConversationId={currentConversationId}
      />
      <section className="grid min-h-[80vh] gap-4">
        <div className="glass-panel flex items-center justify-between gap-4 p-4">
          <div>
            <p className="text-xs uppercase tracking-[0.2em] text-ink/45">Chat Workspace</p>
            <h1 className="mt-1 font-display text-3xl text-ink">LLM orchestration shell</h1>
          </div>
          <label className="flex items-center gap-3 rounded-full border border-ink/10 bg-white/75 px-4 py-2 text-sm text-ink/75">
            <input
              type="checkbox"
              checked={useWebContext}
              onChange={(event) => setUseWebContext(event.target.checked)}
              className="h-4 w-4 rounded border-ink/20 text-ember focus:ring-ember/30"
            />
            Include optional web context
          </label>
        </div>

        {error ? (
          <div className="rounded-2xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {error}
          </div>
        ) : null}

        <div className="glass-panel flex-1 overflow-hidden p-4">
          <div className="h-full overflow-y-auto pr-2">
            <MessageList messages={messages} />
          </div>
        </div>

        <MessageInput disabled={isPending} onSend={handleSend} />
      </section>
    </div>
  );
}

