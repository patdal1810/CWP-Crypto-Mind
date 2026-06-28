from app.core.config import settings


def test_config_loads():
    assert settings.DATABASE_URL
    assert settings.TELEGRAM_CHAT_ID
    assert settings.DEFAULT_TIMEFRAME == "1h"
    assert settings.DEFAULT_LIMIT == 250
    assert len(settings.SYMBOLS) > 0