from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="Sovereign Compliance Engine – Regulator API",
    description="Read-only regulatory access to governance audit data",
    version="1.0.0",
    docs_url="/regulator/docs",
    redoc_url="/regulator/redoc"
)

app.include_router(router)
