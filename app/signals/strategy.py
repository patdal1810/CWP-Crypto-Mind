import pandas as pd


def calculate_rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    delta = df["close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["ema_50"] = df["close"].ewm(span=50, adjust=False).mean()
    df["ema_200"] = df["close"].ewm(span=200, adjust=False).mean()
    df["rsi"] = calculate_rsi(df)

    return df


def generate_signal(symbol: str, df: pd.DataFrame) -> dict:
    latest = df.iloc[-1]

    price = float(latest["close"])
    ema_50 = float(latest["ema_50"])
    ema_200 = float(latest["ema_200"])
    rsi = float(latest["rsi"])

    signal = "WAIT"
    reason = "No strong setup."
    # telegram_bot.send_alert(f'{signal}\nPrice: {price}\nEMA_50: {ema_200}\nEMA_200: {ema_200}\nRSI: {rsi}')

    if ema_50 > ema_200 and rsi < 35:
        signal = "BUY"
        reason = "Bullish trend because EMA50 is above EMA200, and RSI suggests price may be oversold."

    elif ema_50 < ema_200 and rsi > 65:
        signal = "SELL"
        reason = "Bearish trend because EMA50 is below EMA200, and RSI suggests price may be overbought."

    

    return {
        "symbol": symbol,
        "timestamp": str(latest["timestamp"]),
        "signal": signal,
        "price": price,
        "rsi": round(rsi, 2),
        "ema_50": round(ema_50, 2),
        "ema_200": round(ema_200, 2),
        "reason": reason,
    }
