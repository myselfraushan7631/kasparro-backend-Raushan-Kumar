from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from datetime import datetime
from core.database import Base

class RawData(Base):
    __tablename__ = "raw_data"
    id = Column(Integer, primary_key=True)
    source = Column(String)
    payload = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class NormalizedData(Base):
    __tablename__ = "normalized_data"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Float)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class ETLCheckpoint(Base):
    __tablename__ = "etl_checkpoint"
    id = Column(Integer, primary_key=True)
    source = Column(String, unique=True)
    last_processed_id = Column(Integer)

class ETLRun(Base):
    __tablename__ = "etl_runs"
    id = Column(Integer, primary_key=True)
    success = Column(Boolean)
    records_processed = Column(Integer)
    started_at = Column(DateTime)
    finished_at = Column(DateTime)
