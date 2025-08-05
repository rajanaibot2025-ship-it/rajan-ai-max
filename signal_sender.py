# ✅ Final Signal Broadcaster: Website + App + Telegram
import requests

def send_signal_to_website(signal_data):
    try:
        response = requests.post("https://rajanai.in/api/signal", json=signal_data)
        if response.status_code == 200:
            print("🌐 Website ✅ Signal sent successfully!")
        else:
            print("❌ Website ⚠️ Failed:", response.text)
    except Exception as e:
        print("❌ Website ERROR:", e)

def send_signal_to_telegram(signal_text):
    try:
        bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
        chat_id = "YOUR_CHAT_ID"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": signal_text,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("📩 Telegram ✅ Signal sent!")
        else:
            print("❌ Telegram ⚠️ Failed:", response.text)
    except Exception as e:
        print("❌ Telegram ERROR:", e)

def broadcast_signal(signal_data):
    # Generate signal text
    signal_text = (
        f"🟢 Signal: {signal_data['pair']} | Time: {signal_data['time']} | Action: {signal_data['action']}\n"
        f"🧠 Logic: {signal_data['logic']}\n"
        f"📊 Confidence: {signal_data['confidence']}% | Trend: {signal_data['trend']} | Filters: {signal_data['filters']}"
    )
    # 🔁 Send to website and telegram
    send_signal_to_website(signal_data)
    send_signal_to_telegram(signal_text)

