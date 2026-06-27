from app.core.config import settings
from data.market_data import fetch_ohlcv
from database.db import init_db, save_market_data, save_signal
from strategies.rsi_ema_strategy import add_indicators, generate_signal


def run():
    init_db()

    for symbol in settings.SYMBOLS:
        print(f"\nFetching {symbol}...")

        df = fetch_ohlcv(
            symbol=symbol,
            timeframe=settings.DEFAULT_TIMEFRAME,
            limit=settings.DEFAULT_LIMIT
        )

        df = add_indicators(df)

        save_market_data(symbol, df)

        signal_data = generate_signal(symbol, df)
        save_signal(signal_data)

        print(signal_data)


if __name__ == "__main__":
    run()