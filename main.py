from app.core.config import settings
from app.market.provider import fetch_ohlcv
from database.db import init_db, save_market_data, save_signal
from app.signals.strategy import add_indicators, generate_signal
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

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