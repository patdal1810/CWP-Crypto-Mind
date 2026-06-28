from sqlalchemy.dialects.postgresql import insert

from app.market.models import MarketData


class MarketRepository:
    def __init__(self, db):
        self.db = db

    def save_many(self, symbol: str, df):
        records = []

        for _, row in df.iterrows():
            records.append({
                "symbol": symbol,
                "timestamp": row["timestamp"],
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "volume": float(row["volume"]),
                "ema_50": None if row.get("ema_50") != row.get("ema_50") else float(row.get("ema_50")),
                "ema_200": None if row.get("ema_200") != row.get("ema_200") else float(row.get("ema_200")),
                "rsi": None if row.get("rsi") != row.get("rsi") else float(row.get("rsi")),
            })

        if not records:
            return 0

        stmt = insert(MarketData).values(records)

        stmt = stmt.on_conflict_do_nothing(
            index_elements=["symbol", "timestamp"]
        )

        result = self.db.execute(stmt)
        self.db.commit()

        return result.rowcount