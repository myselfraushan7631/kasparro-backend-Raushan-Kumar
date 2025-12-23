from fastapi import FastAPI
from api.routes import router
from ingestion.orchestrator import run_all
from core.database import engine
from core.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.on_event("startup")
def startup():
    run_all()
