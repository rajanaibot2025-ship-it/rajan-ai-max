def analyze_candle(candle):
    open_price = candle["open"]
    close_price = candle["close"]
    high = candle["high"]
    low = candle["low"]
    volume = candle.get("volume", 0)

    body = abs(close_price - open_price)
    total_range = high - low
    upper_wick = high - max(open_price, close_price)
    lower_wick = min(open_price, close_price) - low

    body_ratio = body / total_range if total_range != 0 else 0
    upper_wick_ratio = upper_wick / total_range if total_range != 0 else 0
    lower_wick_ratio = lower_wick / total_range if total_range != 0 else 0

    signal = "No clear signal"
    confidence = 50
    reason = "Neutral or weak candle"

    # Strong Bullish Candle
    if close_price > open_price and body_ratio > 0.6 and lower_wick_ratio < 0.2:
        signal = "Next Green Candle pe BUY lena"
        confidence = 85
        reason = "Bullish candle with strong body"

    # Strong Bearish Candle
    elif open_price > close_price and body_ratio > 0.6 and upper_wick_ratio < 0.2:
        signal = "Next Red Candle pe SELL lena"
        confidence = 85
        reason = "Bearish candle with strong body"

    # Rejection from Bottom (Green candle with strong lower wick)
    elif close_price > open_price and lower_wick_ratio > 0.4:
        signal = "Support rejection detected – BUY signal"
        confidence = 75
        reason = "Lower wick rejection on bullish candle"

    # Rejection from Top (Red candle with strong upper wick)
    elif open_price > close_price and upper_wick_ratio > 0.4:
        signal = "Resistance rejection detected – SELL signal"
        confidence = 75
        reason = "Upper wick rejection on bearish candle"

    # Volume boost confirmation
    if volume > 900:
        confidence += 5
        reason += " + High Volume Boost"

    return signal, min(confidence, 95), reason


if __name__ == "__main__":
    print("\n🧠 AI Candle Brain Output:")

    test_candle = {
        "open": 1.1000,
        "close": 1.1055,
        "high": 1.1060,
        "low": 1.0995,
        "volume": 950
    }

    signal, confidence, reason = analyze_candle(test_candle)
    print(f"{reason} | Confidence: {confidence}%")
    print(f"📊 Signal: {signal} ✅")

