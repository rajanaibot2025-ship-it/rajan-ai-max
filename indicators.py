# indicators.py ✅ FINAL
def check_rsi(rsi_value):
    if rsi_value < 30:
        return "oversold"
    elif rsi_value > 70:
        return "overbought"
    else:
        return "neutral"

def check_volume(current_volume, avg_volume):
    if current_volume > avg_volume * 1.5:
        return "high"
    elif current_volume < avg_volume * 0.5:
        return "low"
    else:
        return "normal"

def check_trend(candle_list):
    bullish = sum(1 for c in candle_list if c["close"] > c["open"])
    bearish = sum(1 for c in candle_list if c["open"] > c["close"])
    if bullish > bearish:
        return "uptrend"
    elif bearish > bullish:
        return "downtrend"
    else:
        return "sideways"

