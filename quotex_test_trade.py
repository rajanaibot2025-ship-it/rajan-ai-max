import json
import requests
import time

print("\n[🚀] RAJAN AI BOT: Starting Quotex Auto Trader Test")

# ✅ Load Cookies
try:
    with open("cookies.json", "r") as f:
        cookies_data = json.load(f)
        print(f"[✅] Loaded {len(cookies_data)} cookies from cookies.json")
except Exception as e:
    print(f"[❌] Error loading cookies: {e}")
    exit()

# ✅ Convert cookies to requests format
cookies = {cookie['name']: cookie['value'] for cookie in cookies_data}

# ✅ Correct Quotex Trade Headers (Real Browser-style)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://quotex.io",
    "Referer": "https://quotex.io/",
    "Connection": "keep-alive"
}

# ✅ Example Trade Payload
payload = {
    "market": "EURUSD",
    "price": 1,
    "direction": "call",   # or "put"
    "expiration": 1,
    "type": "turbo"
}

# ✅ Quotex Trade API URL
url = "https://quote.quotex.io/trade/push"

# ✅ Start session and send request
session = requests.Session()

try:
    response = session.post(url, headers=headers, cookies=cookies, json=payload)

    if response.status_code == 200:
        print("[✅] Trade Placed Successfully ✔️")
        print("[📝] Response:", response.json())
    else:
        print(f"[❌] Trade Failed → {response.status_code}")
        print("[🔎] Response Text:", response.text)

except Exception as e:
    print(f"[❌] Error sending trade request: {e}")

