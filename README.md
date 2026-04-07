## FIRST APP

Monorepo-style starter project with:

- Next.js + TypeScript frontend in `apps/frontend`
- FastAPI backend in `apps/backend`
- PostgreSQL database via Docker Compose

### Run with Docker

1. Copy `.env.example` to `.env` if you want to override defaults.
2. Start the stack:

```bash
docker compose up --build
```

Services:

- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- PostgreSQL: `localhost:5432`