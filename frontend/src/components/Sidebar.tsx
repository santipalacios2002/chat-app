import Link from "next/link";

import type { Conversation } from "@/lib/types";

type SidebarProps = {
  conversations: Conversation[];
  currentConversationId: string | null;
};

export function Sidebar({ conversations, currentConversationId }: SidebarProps) {
  return (
    <aside className="glass-panel flex h-full min-h-[320px] flex-col gap-4 p-4">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-xs uppercase tracking-[0.22em] text-ink/45">Conversations</p>
          <h2 className="mt-1 font-display text-2xl text-ink">Recent threads</h2>
        </div>
        <Link href="/chat" className="secondary-button !px-3 !py-2 text-xs">
          New
        </Link>
      </div>
      <div className="flex-1 space-y-2 overflow-y-auto pr-1">
        {conversations.length === 0 ? (
          <p className="rounded-2xl border border-dashed border-ink/12 px-4 py-5 text-sm text-ink/55">
            Your first conversation will appear here after you send a message.
          </p>
        ) : (
          conversations.map((conversation) => {
            const isActive = conversation.id === currentConversationId;

            return (
              <Link
                key={conversation.id}
                href={`/conversations/${conversation.id}`}
                className={`block rounded-2xl border px-4 py-3 transition ${
                  isActive
                    ? "border-ember/40 bg-ember/10 text-ink"
                    : "border-ink/8 bg-white/70 text-ink/75 hover:border-ink/18 hover:bg-white"
                }`}
              >
                <p className="truncate text-sm font-semibold">
                  {conversation.title || "Untitled conversation"}
                </p>
                <p className="mt-1 text-xs text-ink/45">
                  Updated {new Date(conversation.updated_at).toLocaleString()}
                </p>
              </Link>
            );
          })
        )}
      </div>
    </aside>
  );
}

