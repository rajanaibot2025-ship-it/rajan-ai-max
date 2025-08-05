# telegram_alert.py
import requests

# ✅ Your bot token and chat ID
TOKEN = '8072407074:AAFeIuNpHEfawy02zwYPnb1LZVop0tLN1gM'
CHAT_ID = '6080091105'

def send_signal(pair, action, confidence, reason_line, filters_status):
    signal_message = f"""
📡 <b>RAJAN AI BOT PRO MAX</b> 📡

🔁 <b>Pair:</b> <code>{pair}</code>
🎯 <b>Signal:</b> <b>{action.upper()}</b>
📊 <b>Confidence:</b> <code>{confidence}%</code>
🧠 <b>Logic:</b> {reason_line}
🧪 <b>Filters:</b> {filters_status}

⚡️ <i>Powered by Rajan AI Candle Brain</i>
"""
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': signal_message,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Telegram signal sent!")
        else:
            print("❌ Failed to send signal:", response.text)
    except Exception as e:
        print("❌ Error sending Telegram signal:", str(e))

