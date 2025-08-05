# ✅ smart_brain.py – Future-Ready Logic & Healing Core
import random
import json
from datetime import datetime

class SmartBrain:
    def __init__(self):
        self.version = "v2.0-FutureReady"
        self.log_file = "brain_logs.json"
        self.confidence_threshold = 75  # Default confidence %

    def auto_heal(self):
        print("🧠 SmartBrain Healing: Monitoring system integrity...")
        # Placeholder healing logic (can be upgraded to scan error logs)
        return True

    def adapt_to_market(self, market_data):
        print("🔄 Adapting logic to market environment...")
        # Simulate adaptation
        if market_data.get("volatility", 0) > 70:
            self.confidence_threshold += 5
        else:
            self.confidence_threshold = 75

    def analyze_signal(self, signal):
        direction = signal.get("direction", "")
        trend = signal.get("trend", "")
        volume = signal.get("volume", 50)
        rsi = signal.get("rsi", 50)

        reason = []
        confidence = 0

        if trend == direction:
            reason.append("Trend match")
            confidence += 30

        if 45 < rsi < 55:
            reason.append("RSI Neutral – Stable Market")
            confidence += 20

        if volume > 70:
            reason.append("High Volume Confirmation")
            confidence += 25

        if direction == "call" and signal.get("last_candle") == "green":
            reason.append("Momentum supports UP")
            confidence += 15
        elif direction == "put" and signal.get("last_candle") == "red":
            reason.append("Momentum supports DOWN")
            confidence += 15

        if confidence > 100:
            confidence = 100

        return {
            "direction": direction,
            "confidence": confidence,
            "reason": ", ".join(reason),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }

    def save_log(self, analysis):
        try:
            with open(self.log_file, "a") as f:
                f.write(json.dumps(analysis) + "\n")
        except Exception as e:
            print(f"⚠️ Error saving log: {e}")

    def smart_decide(self, signal):
        self.auto_heal()
        self.adapt_to_market(signal)
        analysis = self.analyze_signal(signal)
        self.save_log(analysis)
        return analysis

# Example usage:
if __name__ == "__main__":
    brain = SmartBrain()

    fake_signal = {
        "direction": "call",
        "trend": "call",
        "volume": 80,
        "rsi": 50,
        "last_candle": "green"
    }

    decision = brain.smart_decide(fake_signal)
    print(f"\n🧠 DECISION: {decision['direction'].upper()} | Confidence: {decision['confidence']}%")
    print(f"📋 REASON: {decision['reason']}")

