from app.core.config import settings


def run():
    print("Config loaded successfully")
    print(f"Database URL exists: {bool(settings.DATABASE_URL)}")
    print(f"Telegram Chat ID exists: {bool(settings.TELEGRAM_CHAT_ID)}")
    print(f"Symbols: {settings.SYMBOLS}")
    print(f"Default timeframe: {settings.DEFAULT_TIMEFRAME}")
    print(f"Default limit: {settings.DEFAULT_LIMIT}")
    print(f"Telegram token masked: {settings.TELEGRAM_BOT_TOKEN}")


if __name__ == "__main__":
    run()