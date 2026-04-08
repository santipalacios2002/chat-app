import { ChatWindow } from "@/components/ChatWindow";

type ConversationPageProps = {
  params: Promise<{
    id: string;
  }>;
};

export default async function ConversationPage({ params }: ConversationPageProps) {
  const { id } = await params;

  return (
    <main className="mx-auto min-h-screen max-w-6xl px-4 py-6 lg:px-6">
      <ChatWindow initialConversationId={id} />
    </main>
  );
}

