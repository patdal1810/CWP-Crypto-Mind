import pandas as pd

from app.signals.strategy import add_indicators


def test_add_indicators_creates_columns():
    df = pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01", periods=250, freq="h"),
        "open": range(250),
        "high": range(1, 251),
        "low": range(250),
        "close": range(250),
        "volume": range(250),
    })

    result = add_indicators(df)

    assert "ema_50" in result.columns
    assert "ema_200" in result.columns
    assert "rsi" in result.columns