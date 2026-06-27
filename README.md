# CWP Crypto Mind

This is your Day 1 starter codebase.

## What this app does first

- Fetches crypto candle data
- Saves market data into SQLite locally
- Calculates EMA and RSI
- Generates basic BUY / SELL / WAIT signals
- Gives you a simple Streamlit dashboard
- Keeps a manual trade journal

## What it does NOT do yet

- It does not place real trades
- It does not use leverage
- It does not connect to your private Bybit account
- It does not promise profit

## Setup

```bash
cd crypto-copilot-starter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run collector

```bash
python main.py
```

## Run dashboard

```bash
streamlit run dashboard/app.py
```

## Day 1 Goal

Your goal is not to make money today.

Your goal is to understand:

- What a candle is
- What OHLCV means
- How market data is collected
- How your bot stores market data
- How a basic signal is generated
# CWP-Crypto-Mind
