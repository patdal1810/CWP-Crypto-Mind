from datetime import datetime
from pydantic import BaseModel

from app.core.constants import VALID_SIGNALS


class SignalResult(BaseModel):
    symbol: str
    timestamp: datetime | str
    signal: str
    price: float
    rsi: float | None = None
    ema_50: float | None = None
    ema_200: float | None = None
    reason: str

    def validate_signal(self):
        if self.signal not in VALID_SIGNALS:
            raise ValueError(f"Invalid signal: {self.signal}")
        return self