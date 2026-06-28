from app.signals.models import Signal


class SignalRepository:
    def __init__(self, db):
        self.db = db

    def save(self, signal_data: dict):
        signal = Signal(
            symbol=signal_data["symbol"],
            timestamp=signal_data["timestamp"],
            signal=signal_data["signal"],
            price=signal_data["price"],
            rsi=signal_data["rsi"],
            ema_50=signal_data["ema_50"],
            ema_200=signal_data["ema_200"],
            reason=signal_data["reason"],
        )

        self.db.add(signal)
        self.db.commit()
        self.db.refresh(signal)

        return signal