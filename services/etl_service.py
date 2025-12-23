from core.models import NormalizedCryptoPrice, ETLRun
from datetime import datetime

def run_crypto_etl(db, records):
    start = datetime.utcnow()
    count = 0

    for record in records:
        db.add(
            NormalizedCryptoPrice(
                coin_id=record.coin_id,
                symbol=record.symbol,
                name=record.name,
                price_usd=record.price_usd,
                market_cap=record.market_cap,
                source=record.source
            )
        )
        count += 1

    db.add(
        ETLRun(
            success=True,
            records_processed=count,
            started_at=start,
            finished_at=datetime.utcnow()
        )
    )
    db.commit()
