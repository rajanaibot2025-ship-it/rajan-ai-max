# place_trade.py

import time

def place_trade(signal):
    """
    Yeh function trade place karta hai given signal ke according.
    Signal ek dictionary hai jisme yeh keys honi chahiye:
    - 'pair': e.g., 'EURUSD'
    - 'action': 'buy' ya 'sell'
    - 'time': duration in seconds (like 60)
    - 'amount': trade amount (like 10)
    """
    
    try:
        pair = signal.get("pair")
        action = signal.get("action")  # 'buy' ya 'sell'
        duration = signal.get("time", 60)
        amount = signal.get("amount", 10)

        print("🟢 Trade Signal Received:")
        print(f"  📊 Pair: {pair}")
        print(f"  📈 Action: {action.upper()}")
        print(f"  ⏱️ Time: {duration} sec")
        print(f"  💵 Amount: ${amount}")
        
        # Simulated delay for placing trade
        print("⏳ Placing trade on Quotex...")
        time.sleep(2)

        # NOTE: Real Quotex API or browser automation code yahan add hoga
        print("✅ Trade placed successfully!")

    except Exception as e:
        print("❌ Error placing trade:", str(e))

