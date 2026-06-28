import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

import streamlit as st
import plotly.graph_objects as go

from app.market.provider import fetch_ohlcv
from app.signals.strategy import add_indicators, generate_signal

st.set_page_config(page_title="CWP Crypto Mind", layout="wide")

st.title("CWP Crypto Mind")

symbol = st.selectbox("Choose coin", ["BTC/USDT", "ETH/USDT", "SOL/USDT"])
timeframe = st.selectbox("Timeframe", ["1h", "4h", "1d"])

df = fetch_ohlcv(symbol=symbol, timeframe=timeframe, limit=250)
df = add_indicators(df)
signal = generate_signal(symbol, df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Signal", signal["signal"])
col2.metric("Price", f"${signal['price']:,.2f}")
col3.metric("RSI", signal["rsi"])
col4.metric("Trend", "Bullish" if signal["ema_50"] > signal["ema_200"] else "Bearish")

st.info(signal["reason"])

fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=df["timestamp"],
    open=df["open"],
    high=df["high"],
    low=df["low"],
    close=df["close"],
    name="Candles"
))

fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["ema_50"],
    name="EMA 50"
))

fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["ema_200"],
    name="EMA 200"
))

fig.update_layout(height=600, xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)



st.subheader("Latest Market Data")
st.dataframe(df.tail(20))

st.subheader("Risk Calculator")

account_size = st.number_input("Account size ($)", min_value=10.0, value=100.0)
risk_percent = st.number_input("Risk per trade (%)", min_value=0.1, value=1.0)
stop_loss_percent = st.number_input("Stop loss distance (%)", min_value=0.1, value=2.0)

risk_amount = account_size * (risk_percent / 100)
position_size = risk_amount / (stop_loss_percent / 100)

st.write(f"Maximum amount to lose on this trade: ${risk_amount:.2f}")
st.write(f"Suggested position size: ${position_size:.2f}")
