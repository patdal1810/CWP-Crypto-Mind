from app.core.config import settings
from app.core.logging import collector_logger, error_logger
from app.database.session import SessionLocal
from app.market.repository import MarketRepository
from app.signals.repository import SignalRepository
from app.market.provider import get_market_provider
from app.signals.strategy import add_indicators, generate_signal


class MarketCollectorService:
    def __init__(self):
        self.db = SessionLocal()
        self.market_repo = MarketRepository(self.db)
        self.signal_repo = SignalRepository(self.db)
        self.provider = get_market_provider()

    def run(self):
        collector_logger.info("Market collection started")

        try:
            results = []

            for symbol in settings.SYMBOLS:
                try:
                    collector_logger.info(f"Fetching market data for {symbol}")

                    df = self.provider.fetch_ohlcv(
                        symbol=symbol,
                        timeframe=settings.DEFAULT_TIMEFRAME,
                        limit=settings.DEFAULT_LIMIT,
                    )

                    collector_logger.info(f"Fetched {len(df)} candles for {symbol}")

                    df = add_indicators(df)

                    inserted = self.market_repo.save_many(symbol, df)
                    collector_logger.info(
                        f"Saved {inserted} new market rows for {symbol}"
                    )

                    signal_data = generate_signal(symbol, df)
                    self.signal_repo.save(signal_data)

                    collector_logger.info(
                        f"Saved signal for {symbol}: {signal_data['signal']}"
                    )

                    result = {
                        "symbol": symbol,
                        "inserted_rows": inserted,
                        "signal": signal_data["signal"],
                        "price": signal_data["price"],
                        "rsi": signal_data["rsi"],
                        "reason": signal_data["reason"],
                    }

                    results.append(result)

                except Exception as e:
                    error_logger.exception(f"Failed processing symbol {symbol}: {e}")

            collector_logger.info("Market collection completed")
            return results

        finally:
            self.db.close()
            collector_logger.info("Database session closed")