from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL is missing. Add it to your .env file.")


engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)