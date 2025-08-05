import time
import json
from datetime import datetime
from tv_signal_generator import get_latest_signal  # You must have this logic ready
from quotex_auto import place_trade                # Function to auto trade
from money_manager import update_money, check_limits
from ai_candle_brain import analyze_candle         # Optional: Advanced analysis
from return_fetcher import get_best_pair           # Optional: Highest return pair selector

AUTO_TRADE = True     # ✅ Set to True to enable Auto Trading
TRADE_AMOUNT = 100    # ₹100 per trade
SLEEP_TIME = 15       # Seconds between signal checks

def format_signal_message(signal_data):
    symbol = signal_data["symbol"]
    action = signal_data["action"].upper()
    confidence = signal_data["confidence"]
    timeframe = signal_data["timeframe"]
    reason = signal_data["reason"]
    return (
        f"\n📡 New Signal Detected\n"
        f"📈 Pair: {symbol}\n"
        f"🕒 Timeframe: {timeframe}\n"
        f"📊 Action: {action}\n"
        f"🧠 Logic: {reason}\n"
        f"✅ Confidence: {confidence}%\n"
        f"📤 Mode: {'AUTO' if AUTO_TRADE else 'MANUAL'}"
    )

def main():
    last_signal_time = None

    while True:
        now = datetime.now()

        # ✅ 1. Check if loss limit or trade limit reached
        if not check_limits():
            print("🛑 Trading limits reached. Stopping bot.")
            break

        # ✅ 2. Get best pair based on return (optional)
        symbol = get_best_pair()
        if not symbol:
            print("⏳ No valid pair found. Retrying...")
            time.sleep(SLEEP_TIME)
            continue

        # ✅ 3. Get signal
        signal = get_latest_signal(symbol)
        if signal and signal["time"] != last_signal_time:
            last_signal_time = signal["time"]
            signal["symbol"] = symbol

            # ✅ 4. Analyze candle behavior (optional)
            signal["reason"] = analyze_candle(symbol, signal["action"])

            # ✅ 5. Print signal info
            print(format_signal_message(signal))

            # ✅ 6. Auto-trade
            if AUTO_TRADE:
                result = place_trade(symbol, signal["action"], TRADE_AMOUNT)

                # ✅ 7. Update money manager
                update_money(result, TRADE_AMOUNT)
        else:
            print("🔁 No new signal. Waiting...")
        
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()

