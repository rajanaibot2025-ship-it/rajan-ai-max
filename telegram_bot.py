import requests

# 🔐 Replace with your actual bot token
bot_token = '8072407074:AAFeIuNpHEfawy02zwYPnb1LZVop0tLN1gM'

# 🔑 Replace with your actual chat ID
chat_id = '6080091105'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print("✅ Message sent successfully!")
    else:
        print("❌ Failed to send message!")
        print(response.text)

