from datetime import datetime
from pydantic import BaseModel


class Candle(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


class MarketCollectionResult(BaseModel):
    symbol: str
    inserted_rows: int
    signal: str
    price: float
    rsi: float | None = None
    reason: str