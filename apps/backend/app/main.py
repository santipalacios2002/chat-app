from fastapi import FastAPI, HTTPException

from app.config import settings
from app.db import check_database_connection

app = FastAPI(title=settings.app_name)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Backend is running"}


@app.get("/health")
def read_health() -> dict[str, str]:
    try:
        is_connected = check_database_connection(settings.database_url)
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Database unavailable") from exc

    return {
        "app": settings.app_name,
        "status": "ok",
        "database": "connected" if is_connected else "unavailable",
    }
