import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///crypto_copilot.db")

    SYMBOLS = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]

    DEFAULT_TIMEFRAME = "1h"
    DEFAULT_LIMIT = 250

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


settings = Settings()