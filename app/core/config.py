from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    TELEGRAM_BOT_TOKEN: SecretStr
    TELEGRAM_CHAT_ID: str

    SYMBOLS: list[str] = [
        "BTC/USDT",
        "ETH/USDT",
        "SOL/USDT",
    ]

    DEFAULT_TIMEFRAME: str = "1h"
    DEFAULT_LIMIT: int = 250

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()