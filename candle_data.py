# ✅ candle_data.py – Final Smart Candle Data + Brain System
import requests
import datetime
import time

def get_unix_time(dt):
    return int(time.mktime(dt.timetuple()))

def get_latest_candle(symbol="EURUSD", interval="1", lookback_minutes=2880):  # 2 days = 2880 minutes
    """
    Fetch 2 days of 1-minute candles from TradingView proxy
    """
    end_time = int(time.time())
    start_time = end_time - (lookback_minutes * 60)

    url = f"https://api.tradingview.com/history?symbol={symbol}&resolution={interval}&from={start_time}&to={end_time}"
    
    # NOTE: You must replace this with real proxy/API later
    response = requests.get(url)
    data = response.json()

    if "c" not in data:
        print("❌ Candle data not found.")
        return None

    candles = []
    for i in range(len(data["t"])):
        candle = {
            "time": datetime.datetime.fromtimestamp(data["t"][i]),
            "open": data["o"][i],
            "high": data["h"][i],
            "low": data["l"][i],
            "close": data["c"][i],
            "volume": data["v"][i]
        }
        candles.append(candle)

    return candles[-1], candles  # latest_candle, all_candles

# ✅ Optional: Smart breakdown at sub-second level (stub logic for now)
def analyze_candle_behavior(candle):
    body = abs(candle["close"] - candle["open"])
    wick_top = candle["high"] - max(candle["open"], candle["close"])
    wick_bottom = min(candle["open"], candle["close"]) - candle["low"]

    behavior = []

    if wick_bottom > wick_top and wick_bottom > body * 0.5:
        behavior.append("Strong bullish rejection wick")
    if wick_top > wick_bottom and wick_top > body * 0.5:
        behavior.append("Strong bearish rejection wick")
    if body > max(wick_top, wick_bottom):
        behavior.append("Strong momentum candle")

    return behavior

# ✅ For debug/test
if __name__ == "__main__":
    latest, all_data = get_latest_candle()
    print("🕒 Latest Candle:", latest)
    print("🧠 Behavior:", analyze_candle_behavior(latest))

