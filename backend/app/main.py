from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.database import Base, engine


@asynccontextmanager
async def lifespan(_: FastAPI):
  # Keep the MVP easy to boot while Alembic is available for later migrations.
  Base.metadata.create_all(bind=engine)
  yield


app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)

app.add_middleware(
  CORSMiddleware,
  allow_origins=settings.backend_cors_origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.api_v1_prefix)


@app.get("/")
def read_root():
  return {"name": settings.app_name, "docs": "/docs", "health": f"{settings.api_v1_prefix}/health"}

