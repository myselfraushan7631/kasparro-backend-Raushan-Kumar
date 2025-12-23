from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal
from core.models import NormalizedData, ETLRun

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/data")
def get_data(db: Session = Depends(get_db)):
    data = db.query(NormalizedData).limit(50).all()
    return {
        "request_id": "req-123",
        "api_latency_ms": 5,
        "data": data
    }

@router.get("/health")
def health(db: Session = Depends(get_db)):
    db.execute("SELECT 1")
    return {"status": "ok"}

@router.get("/stats")
def stats(db: Session = Depends(get_db)):
    runs = db.query(ETLRun).all()
    return runs
