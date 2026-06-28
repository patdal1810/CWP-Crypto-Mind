import pandas as pd

from app.signals.strategy import generate_signal


def test_generate_signal_returns_valid_signal():
    df = pd.DataFrame({
        "timestamp": pd.date_range("2026-01-01", periods=1),
        "close": [100.0],
        "ema_50": [120.0],
        "ema_200": [130.0],
        "rsi": [50.0],
    })

    result = generate_signal("BTC/USDT", df)

    assert result["symbol"] == "BTC/USDT"
    assert result["signal"] in ["BUY", "SELL", "WAIT"]
    assert "reason" in result
