# smart_tv_signal.py
import time
from datetime import datetime
from signal_generator import generate_signal
from quotex_auto import place_trade
from money_manager import update_trade_result
from telegram_sender import send_signal_alert  # ✅ STEP 2: Import Telegram alert sender

AUTO_TRADE = True
INTERVAL = 60  # Candle interval in seconds

def run_bot():
    print("📡 RAJAN AI BOT MAX PRO - SMART TV SIGNAL SYSTEM STARTED")
    while True:
        try:
            signal = generate_signal()

            if signal:
                print(f"\n📶 Signal Received: {signal}")
                
                # ✅ STEP 2: Send signal to Telegram
                send_signal_alert(signal)  # <--- Telegram alert
                
                if AUTO_TRADE:
                    result = place_trade(signal)
                    update_trade_result(result)

            else:
                print("⏳ No signal detected, waiting for next candle...")

            time.sleep(INTERVAL)

        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_bot()

