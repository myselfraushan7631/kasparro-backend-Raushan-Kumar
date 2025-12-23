import requests
from schemas.normalized_schema import NormalizedCrypto
from core.config import settings

BASE_URL = "https://api.coinpaprika.com/v1"

def fetch_coinpaprika_data():
    headers = {
        "Authorization": f"Bearer {settings.COINPAPRIKA_API_KEY}"
    }

    coins = requests.get(f"{BASE_URL}/coins", headers=headers).json()[:10]
    results = []

    for coin in coins:
        if not coin.get("is_active"):
            continue

        ticker = requests.get(
            f"{BASE_URL}/tickers/{coin['id']}",
            headers=headers
        ).json()

        results.append(
            NormalizedCrypto(
                coin_id=coin["id"],
                symbol=coin["symbol"],
                name=coin["name"],
                price_usd=ticker["quotes"]["USD"]["price"],
                market_cap=ticker["quotes"]["USD"]["market_cap"],
                source="coinpaprika"
            )
        )

    return results
