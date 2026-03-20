import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Probabilistic Trading Dashboard", layout="wide")
st.title("Probabilistic Trading System (HMM + Risk Modeling)")


#load data
try:
    df = pd.read_csv("outputs/predictions.csv")
except FileNotFoundError:
    st.warning("No predictions found yet. Run main.py or main_live.py first.")
    st.stop()


#metrics
latest = df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Signal", "BUY" if latest["signal"] == 1 else "SELL")
col2.metric("Bull Probability", f"{latest['prob_bull']:.2f}")
col3.metric("Risk Level", latest["risk"])
col4.metric("Volatility", f"{latest['volatility']:.4f}")


#price + regime
st.subheader("Price")
st.line_chart(df["Close"])

st.subheader("Market Regimes (HMM States)")
st.line_chart(df["state"])


#probabilities
st.subheader("Bull Market Probability")
st.line_chart(df["prob_bull"])


#risk metrics
st.subheader("Volatility")
st.line_chart(df["volatility"])


#signal visualization
st.subheader("Signal Over Time")
st.line_chart(df["signal"])

#raw data
with st.expander("Show Raw Data"):
    st.dataframe(df.tail(100))


#equity curve
st.subheader("Equity Curve (Backtest)")
st.line_chart(df["equity"])


#strategy returns
df["strategy_returns"] = df["equity"].pct_change()

#sharpe ratio
sharpe = np.mean(df["strategy_returns"].dropna()) / np.std(df["strategy_returns"].dropna())

st.metric("Sharpe Ratio", f"{sharpe:.2f}")