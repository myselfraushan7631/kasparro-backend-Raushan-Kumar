from core.database import SessionLocal
from services.etl_service import run_crypto_etl
from ingestion.coinpaprika_source import fetch_coinpaprika_data
from ingestion.coingecko_source import fetch_coingecko_data

def run_all():
    db = SessionLocal()
    run_crypto_etl(db, fetch_coinpaprika_data())
    run_crypto_etl(db, fetch_coingecko_data())
    db.close()
