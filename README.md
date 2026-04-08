# Chat App MVP

A monorepo-style scaffold for a chat-first web app with a Next.js frontend, FastAPI backend, PostgreSQL, and Docker Compose.

## Stack

- Frontend: Next.js, TypeScript, Tailwind CSS
- Backend: FastAPI, SQLAlchemy, Alembic, Pydantic
- Database: PostgreSQL
- Infra: Docker Compose

## Project Layout

```text
chat-app/
├── README.md
├── .env.example
├── docker-compose.yml
├── frontend/
├── backend/
└── infra/
```

## Quick Start

1. Copy `.env.example` to `.env`.
2. Start the stack:

```bash
docker compose up --build
```

3. Open:

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API docs: http://localhost:8000/docs

## Notes

- The backend is ready for Alembic migrations, but also creates tables on startup for a smoother MVP bootstrap.
- If `OPENAI_API_KEY` is unset, chat responses fall back to a deterministic mock assistant reply so the full stack still works locally.

