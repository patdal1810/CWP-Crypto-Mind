import sqlite3
from pathlib import Path

DB_PATH = Path("crypto_copilot.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS market_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        open REAL NOT NULL,
        high REAL NOT NULL,
        low REAL NOT NULL,
        close REAL NOT NULL,
        volume REAL NOT NULL,
        ema_50 REAL,
        ema_200 REAL,
        rsi REAL,
        UNIQUE(symbol, timestamp)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS signals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        signal TEXT NOT NULL,
        price REAL NOT NULL,
        rsi REAL,
        ema_50 REAL,
        ema_200 REAL,
        reason TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        symbol TEXT NOT NULL,
        side TEXT NOT NULL,
        entry_price REAL NOT NULL,
        exit_price REAL,
        result TEXT,
        pnl REAL,
        notes TEXT,
        mistake TEXT
    )
    """)

    conn.commit()
    conn.close()


def clean_float(value):
    if value != value:
        return None
    return float(value)


def save_market_data(symbol, df):
    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
        INSERT OR IGNORE INTO market_data (
            symbol, timestamp, open, high, low, close, volume, ema_50, ema_200, rsi
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            symbol,
            str(row["timestamp"]),
            float(row["open"]),
            float(row["high"]),
            float(row["low"]),
            float(row["close"]),
            float(row["volume"]),
            clean_float(row.get("ema_50")),
            clean_float(row.get("ema_200")),
            clean_float(row.get("rsi")),
        ))

    conn.commit()
    conn.close()


def save_signal(signal_data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO signals (
        symbol, timestamp, signal, price, rsi, ema_50, ema_200, reason
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        signal_data["symbol"],
        signal_data["timestamp"],
        signal_data["signal"],
        signal_data["price"],
        signal_data["rsi"],
        signal_data["ema_50"],
        signal_data["ema_200"],
        signal_data["reason"],
    ))

    conn.commit()
    conn.close()
