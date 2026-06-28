# scripts/test_db_connection.py
from app.database.session import engine

try:
    with engine.connect() as conn:
        print("✅ Connected to Railway Postgres successfully")
except Exception as e:
    print("❌ Database connection failed")
    print(e)