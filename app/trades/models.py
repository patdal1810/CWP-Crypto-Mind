# app/database/models/trade.py

from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from sqlalchemy.sql import func

from app.database.base import Base


class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(DateTime, nullable=False)
    symbol = Column(String(20), nullable=False, index=True)
    side = Column(String(10), nullable=False)

    entry_price = Column(Float, nullable=False)
    exit_price = Column(Float, nullable=True)

    result = Column(String(20), nullable=True)
    pnl = Column(Float, nullable=True)

    notes = Column(Text, nullable=True)
    mistake = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())