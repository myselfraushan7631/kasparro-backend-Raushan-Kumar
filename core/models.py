from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class NormalizedCryptoPrice(Base):
    __tablename__ = "normalized_crypto_prices"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    name = Column(String)
    price_usd = Column(Float)
    market_cap_usd = Column(Float)
    volume_24h_usd = Column(Float)
    source = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ETLRun(Base):
    __tablename__ = "etl_runs"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    message = Column(String)
    run_at = Column(DateTime, default=datetime.utcnow)
