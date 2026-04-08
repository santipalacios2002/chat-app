import Link from "next/link";

const architecture = [
  "Next.js frontend for the chat-first browser experience",
  "FastAPI backend for orchestration, persistence, and tool routing",
  "PostgreSQL for conversations, messages, context blocks, and tool runs",
  "Docker Compose for local development and single-instance deployment",
];

export default function HomePage() {
  return (
    <main className="mx-auto flex min-h-screen max-w-6xl flex-col px-6 py-10 lg:px-10">
      <section className="glass-panel grid gap-8 p-8 lg:grid-cols-[1.4fr_0.9fr] lg:p-12">
        <div className="space-y-6">
          <span className="inline-flex rounded-full border border-ink/10 bg-white/60 px-3 py-1 text-xs uppercase tracking-[0.25em] text-ink/65">
            MVP Scaffold
          </span>
          <div className="space-y-4">
            <h1 className="font-display text-5xl leading-tight text-ink lg:text-7xl">
              Ship a chat app now, grow it without rewriting later.
            </h1>
            <p className="max-w-2xl text-base leading-7 text-ink/75 lg:text-lg">
              This starter keeps the surface area small while leaving room for LLM orchestration,
              context injection, tool routing, and conversation persistence.
            </p>
          </div>
          <div className="flex flex-wrap gap-3">
            <Link href="/chat" className="primary-button">
              Open chat
            </Link>
            <a href="http://localhost:8000/docs" className="secondary-button">
              API docs
            </a>
          </div>
        </div>
        <div className="rounded-[2rem] border border-ink/10 bg-cloud/90 p-6 shadow-glow">
          <p className="mb-4 text-sm uppercase tracking-[0.2em] text-ink/45">Architecture</p>
          <ul className="space-y-3 text-sm leading-6 text-ink/75">
            {architecture.map((item) => (
              <li key={item} className="rounded-2xl border border-ink/8 bg-white/75 px-4 py-3">
                {item}
              </li>
            ))}
          </ul>
        </div>
      </section>
    </main>
  );
}

