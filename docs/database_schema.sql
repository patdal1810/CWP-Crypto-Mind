CREATE TABLE market_data (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    open NUMERIC NOT NULL,
    high NUMERIC NOT NULL,
    low NUMERIC NOT NULL,
    close NUMERIC NOT NULL,
    volume NUMERIC NOT NULL,
    ema_50 NUMERIC,
    ema_200 NUMERIC,
    rsi NUMERIC,
    UNIQUE(symbol, timestamp)
);

CREATE TABLE signals (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    signal VARCHAR(10) NOT NULL,
    price NUMERIC NOT NULL,
    rsi NUMERIC,
    ema_50 NUMERIC,
    ema_200 NUMERIC,
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE trades (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    side VARCHAR(10) NOT NULL,
    entry_price NUMERIC NOT NULL,
    exit_price NUMERIC,
    result VARCHAR(20),
    pnl NUMERIC,
    notes TEXT,
    mistake TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
