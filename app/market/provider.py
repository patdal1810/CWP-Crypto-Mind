from abc import ABC, abstractmethod

import ccxt
import pandas as pd

from app.core.exceptions import ExternalProviderException


class MarketProvider(ABC):
    @abstractmethod
    def fetch_ohlcv(
        self,
        symbol: str,
        timeframe: str = "1h",
        limit: int = 250,
    ) -> pd.DataFrame:
        pass


class BybitMarketProvider(MarketProvider):
    def __init__(self):
        self.exchange = ccxt.bybit({
            "enableRateLimit": True,
        })

    def fetch_ohlcv(
        self,
        symbol: str,
        timeframe: str = "1h",
        limit: int = 250,
    ) -> pd.DataFrame:
        try:
            candles = self.exchange.fetch_ohlcv(
                symbol,
                timeframe=timeframe,
                limit=limit,
            )

            df = pd.DataFrame(
                candles,
                columns=["timestamp", "open", "high", "low", "close", "volume"],
            )

            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
            return df

        except Exception as e:
            raise ExternalProviderException(
                f"Failed to fetch OHLCV for {symbol}"
            ) from e


def get_market_provider() -> MarketProvider:
    return BybitMarketProvider()