import random
from datetime import datetime

def get_candle_behavior(candle):
    open_price = candle['open']
    close_price = candle['close']
    high = candle['high']
    low = candle['low']

    body = abs(close_price - open_price)
    wick_top = high - max(open_price, close_price)
    wick_bottom = min(open_price, close_price) - low

    if close_price > open_price:
        color = 'green'
    elif close_price < open_price:
        color = 'red'
    else:
        color = 'doji'

    momentum = "strong" if body > wick_top and body > wick_bottom else "weak"
    rejection = "top" if wick_top > body * 1.5 else "bottom" if wick_bottom > body * 1.5 else "none"

    return {
        'color': color,
        'momentum': momentum,
        'rejection': rejection
    }

def rsi_filter(rsi_value):
    if rsi_value > 70:
        return 'overbought'
    elif rsi_value < 30:
        return 'oversold'
    else:
        return 'neutral'

def volume_filter(volume):
    return "high" if volume > 3000 else "low"

def generate_signal(latest_candle, rsi_value, volume, trend="up"):
    behavior = get_candle_behavior(latest_candle)
    rsi_status = rsi_filter(rsi_value)
    volume_status = volume_filter(volume)

    signal = None
    reason = ""

    if behavior['color'] == 'green' and behavior['momentum'] == 'strong' and rsi_status == 'oversold' and volume_status == 'high':
        signal = 'call'
        reason = "Next Green Candle pe UP lena 📈 (Strong Bullish + RSI Oversold + High Volume)"
    elif behavior['color'] == 'red' and behavior['momentum'] == 'strong' and rsi_status == 'overbought' and volume_status == 'high':
        signal = 'put'
        reason = "Next Red Candle pe DOWN lena 📉 (Strong Bearish + RSI Overbought + High Volume)"
    elif behavior['rejection'] == 'bottom' and rsi_status == 'oversold':
        signal = 'call'
        reason = "Bottom wick rejection + RSI Oversold 🔁 Possible reversal: UP"
    elif behavior['rejection'] == 'top' and rsi_status == 'overbought':
        signal = 'put'
        reason = "Top wick rejection + RSI Overbought 🔁 Possible reversal: DOWN"
    else:
        reason = "No clear signal ❌ (Neutral behavior or weak confirmation)"

    return signal, reason

