import ccxt
import pandas as pd


def fetch_ohlcv(symbol: str = "BTC/USDT", timeframe: str = "1h", limit: int = 250) -> pd.DataFrame:
    exchange = ccxt.bybit({
        "enableRateLimit": True,
    })

    candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    df = pd.DataFrame(
        candles,
        columns=["timestamp", "open", "high", "low", "close", "volume"]
    )

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df
