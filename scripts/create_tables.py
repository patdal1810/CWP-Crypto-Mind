from app.database.base import Base
from app.database.session import engine

# Important: import models so SQLAlchemy knows about them
from app.database.models import MarketData, Signal, Trade


def create_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")


if __name__ == "__main__":
    create_tables()