import requests
from schemas.normalized_schema import NormalizedCrypto

URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_coingecko_data():
    response = requests.get(
        URL,
        params={
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 10,
            "page": 1
        }
    )
    response.raise_for_status()

    results = []
    for coin in response.json():
        results.append(
            NormalizedCrypto(
                coin_id=coin["id"],
                symbol=coin["symbol"],
                name=coin["name"],
                price_usd=coin["current_price"],
                market_cap=coin["market_cap"],
                source="coingecko"
            )
        )

    return results
