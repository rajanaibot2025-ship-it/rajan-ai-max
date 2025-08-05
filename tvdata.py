import requests
import datetime

def get_candles(symbol="EURUSD", interval="1", limit=5):
    """
    TradingView data fetcher – returns latest candles
    """
    url = f"https://scanner.tradingview.com/america/scan"
    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "symbols": {
            "tickers": [f"OANDA:{symbol}"],
            "query": {"types": []}
        },
        "columns": [
            f"close|{interval}",
            f"open|{interval}",
            f"high|{interval}",
            f"low|{interval}",
            f"volume|{interval}"
        ]
    }

    try:
        res = requests.post(url, json=payload, headers=headers, timeout=5)
        data = res.json()
        candles = []
        for i in range(limit):
            item = data["data"][0]["d"]
            candles.append({
                "time": datetime.datetime.now().strftime("%H:%M"),
                "open": item[1],
                "close": item[0],
                "high": item[2],
                "low": item[3],
                "volume": item[4]
            })
        return candles
    except Exception as e:
        print("⚠️ Error fetching candles:", e)
        return []

