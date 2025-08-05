# ✅ test_trade.py – with SmartTradeBrain
from quotex_auto import place_trade
import time

class SmartTradeBrain:
    def __init__(self, asset, trade_type, amount, duration):
        self.asset = asset.upper()
        self.trade_type = trade_type.lower()
        self.amount = amount
        self.duration = duration

    def validate(self):
        if self.trade_type not in ["buy", "sell"]:
            print("❌ Invalid trade type. Use 'buy' or 'sell'.")
            return False
        if not isinstance(self.amount, (int, float)) or self.amount <= 0:
            print("❌ Invalid amount. Must be a positive number.")
            return False
        if not isinstance(self.duration, int) or self.duration <= 0:
            print("❌ Invalid duration. Must be a positive integer.")
            return False
        if not self.asset:
            print("❌ Asset name cannot be empty.")
            return False
        return True

    def send_trade(self, retry=1):
        if not self.validate():
            return False

        print(f"\n📤 SmartTradeBrain: Preparing to place trade...")
        print(f"🔹 Asset     : {self.asset}")
        print(f"🔹 Type      : {self.trade_type.upper()}")
        print(f"🔹 Amount    : {self.amount}")
        print(f"🔹 Duration  : {self.duration} min")

        attempt = 0
        while attempt <= retry:
            print(f"\n🧠 Attempt #{attempt + 1} placing trade...")
            response = place_trade(self.trade_type, amount=self.amount, asset=self.asset, duration=self.duration)

            if response:
                print("✅ Trade sent successfully by SmartTradeBrain!")
                return True
            else:
                print("⚠️ Trade failed. Retrying..." if attempt < retry else "❌ All attempts failed.")
                time.sleep(1.5)  # small delay before retry
            attempt += 1
        return False

# ✅ Configuration
asset     = "EURUSD"     # Example: "EURUSD"
trade_type = "buy"       # "buy" or "sell"
amount     = 100         # Trade amount
duration   = 1           # Duration in minutes

# ✅ Create brain and execute
brain = SmartTradeBrain(asset, trade_type, amount, duration)
brain.send_trade(retry=2)  # Retry 2 times if failed

