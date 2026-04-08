import type { ChatRequest, ChatResponse, Conversation } from "@/lib/types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
const API_PREFIX = "/api/v1";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${API_PREFIX}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return (await response.json()) as T;
}

export async function getConversations(): Promise<Conversation[]> {
  return request<Conversation[]>("/conversations/");
}

export async function getConversation(conversationId: string): Promise<Conversation> {
  return request<Conversation>(`/conversations/${conversationId}`);
}

export async function sendChatMessage(payload: ChatRequest): Promise<ChatResponse> {
  return request<ChatResponse>("/chat/", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

