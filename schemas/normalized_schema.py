from pydantic import BaseModel

class NormalizedCrypto(BaseModel):
    coin_id: str
    symbol: str
    name: str
    price_usd: float
    market_cap: float | None
    source: str
