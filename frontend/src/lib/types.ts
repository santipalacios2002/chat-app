export type MessageRole = "system" | "user" | "assistant";

export type Message = {
  id: string;
  role: MessageRole;
  content: string;
  created_at: string;
};

export type Conversation = {
  id: string;
  title: string;
  created_at: string;
  updated_at: string;
  messages?: Message[];
};

export type ContextBlock = {
  id: string;
  key: string;
  content: string;
  created_at: string;
};

export type ChatRequest = {
  conversation_id?: string | null;
  message: string;
  use_web_context?: boolean;
};

export type ChatResponse = {
  conversation: Conversation;
  message: Message;
  reply: Message;
};

