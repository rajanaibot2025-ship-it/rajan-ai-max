import json
import httpx

def load_cookies():
    with open("cookies.json", "r") as file:
        raw_cookies = json.load(file)
    return {cookie['name']: cookie['value'] for cookie in raw_cookies}

def get_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://quotex.com/",
        "Origin": "https://quotex.com",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
    }

# ✅ FIXED: Accepting `symbol` and `action`
def place_trade(symbol, action):
    print(f"\n🚀 RAJAN AI BOT: Placing trade → {symbol} | {action}")

    cookies = load_cookies()
    print(f"[✅] Loaded {len(cookies)} cookies from cookies.json")

    # 🛠️ Direction Mapping
    direction = "call" if action.lower() == "buy" else "put"

    # ✅ Set URL and payload
    url = "https://quotex.com/en/trade/digital"
    payload = {
        "amount": 100,         # 💰 Trade amount (customize)
        "asset": symbol,       # 🔁 Dynamic asset
        "direction": direction, # 📈 or 📉
        "expiration": 1         # 🕐 1 minute expiry
    }

    try:
        with httpx.Client(headers=get_headers(), cookies=cookies, timeout=15.0) as client:
            response = client.post(url, json=payload)
            if response.status_code == 200:
                print("✅ Trade Placed Successfully!")
                print("📊 Response:", response.json())
            else:
                print(f"❌ Trade Failed → {response.status_code}")
                print("🔎 Response Text:", response.text[:300])
    except Exception as e:
        print("⚠️ Exception occurred:", e)

# ✅ Optional test call
if __name__ == "__main__":
    place_trade("EURUSD", "BUY")

