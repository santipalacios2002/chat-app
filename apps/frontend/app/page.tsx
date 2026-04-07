export const dynamic = "force-dynamic";

type HealthResponse = {
  app: string;
  database: string;
  status: string;
};

async function getHealth(): Promise<HealthResponse | null> {
  const apiBaseUrl = process.env.API_BASE_URL ?? "http://backend:8000";

  try {
    const response = await fetch(`${apiBaseUrl}/health`, {
      cache: "no-store"
    });

    if (!response.ok) {
      return null;
    }

    return (await response.json()) as HealthResponse;
  } catch {
    return null;
  }
}

export default async function Home() {
  const health = await getHealth();

  return (
    <main className="page-shell">
      <section className="hero-card">
        <p className="eyebrow">Monorepo Starter</p>
        <h1>Next.js frontend, FastAPI backend, PostgreSQL database.</h1>
        <p className="lede">
          This workspace is split into a frontend app under <code>apps/frontend</code> and a backend API
          under <code>apps/backend</code>, with Docker Compose wiring the full stack together.
        </p>
        <div className="status-grid">
          <article>
            <span className="label">Frontend</span>
            <strong>Ready</strong>
          </article>
          <article>
            <span className="label">Backend</span>
            <strong>{health?.status ?? "Unavailable"}</strong>
          </article>
          <article>
            <span className="label">Database</span>
            <strong>{health?.database ?? "Not connected"}</strong>
          </article>
        </div>
      </section>
    </main>
  );
}
