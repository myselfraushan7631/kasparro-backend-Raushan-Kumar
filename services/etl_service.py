from datetime import datetime
from core.models import NormalizedCryptoPrice, ETLRun

def run_crypto_etl(db, records):
    start = datetime.utcnow()
    count = 0

    for record in records:
        db.add(
            NormalizedCryptoPrice(
                symbol=record.symbol,
                name=record.name,
                price_usd=record.price_usd,
                market_cap_usd=getattr(record, "market_cap", None),
               volume_24h_usd=getattr(record, "volume_24h_usd", None),
              source=record.source
            )
        )
        count += 1

    db.add(
        ETLRun(
            status="SUCCESS",
            message=f"Inserted {count} records",
            run_at=datetime.utcnow()
        )
    )

    db.commit()
