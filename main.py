import streamlit as st
import yaml
import pandas as pd
from datetime import datetime


from src.data.fetch_data import fetch_data, fetch_crypto_data
from src.data.preprocess import preprocess_data


from src.models.hmm_model import train_hmm, load_hmm, predict_states

from src.risk.probabilistic_risk import compute_var, compute_volatility, risk_label

from src.signals.signal_generator import generate_signal

from src.portfolio.optimizer import optimize_portfolio

from src.backtesting.backtester import backtest
from src.backtesting.metrics import sharpe_ratio
from src.backtesting.drawdown import compute_drawdown, max_drawdown

from src.trading.alpaca_trader import AlpacaTrader


# Load Config
with open("configs/config.yaml", "r") as f:
    config = yaml.safe_load(f)

assets = config.get("assets", [config["asset"]])
returns_dict = {}

# Fetch, preprocess, compute returns per asset
for asset in assets:
    raw_path = f"data/raw/{asset.replace('/', '_')}.csv"

    if config.get("asset_type") == "crypto":
        df_asset = fetch_crypto_data(
            config["alpaca_key"],
            config["alpaca_secret"],
            asset,
            datetime.strptime(config["start_date"], "%Y-%m-%d"),
            datetime.strptime(config["end_date"], "%Y-%m-%d"),
            raw_path
        )
    else:
        df_asset = fetch_data(
            asset,
            config["start_date"],
            config["end_date"],
            raw_path
        )

    df_asset = preprocess_data(raw_path)
    df_asset["returns"] = df_asset["Close"].pct_change()
    df_asset.dropna(inplace=True)
    returns_dict[asset] = df_asset["returns"]

# Combine Returns & Optimize Portfolio
returns_df = pd.DataFrame(returns_dict)
weights = optimize_portfolio(returns_df)

print("Optimal Portfolio Weights:")
for asset, w in zip(assets, weights):
    print(f"{asset}: {w:.2%}")

# Probabilistic Modeling per asset
predictions = []
for asset in assets:
    df_asset = pd.DataFrame({"returns": returns_df[asset]})

    # Train or load HMM
    model = train_hmm(df_asset["returns"], n_states=3, model_path=f"models/hmm_{asset.replace('/', '_')}.pkl")
    model = load_hmm(f"models/hmm_{asset.replace('/', '_')}.pkl")

    # Predict states
    states, probs = predict_states(model, df_asset["returns"])
    df_asset["state"] = states
    df_asset["prob_bull"] = probs[:, 1]

    # Risk Modeling
    df_asset["VaR"] = compute_var(df_asset["returns"])
    df_asset["volatility"] = compute_volatility(df_asset["returns"])
    df_asset["risk"] = risk_label(df_asset["VaR"], df_asset["volatility"])

    # Signal Generation
    df_asset["signal"] = generate_signal(probs)

    # Backtesting
    df_asset = backtest(df_asset)
    df_asset["strategy_returns"] = df_asset["equity"].pct_change()
    df_asset["drawdown"] = compute_drawdown(df_asset["equity"])

    # Save predictions per asset
    df_asset.to_csv(f"outputs/predictions_{asset.replace('/', '_')}.csv", index=False)
    predictions.append(df_asset)


# Portfolio Metrics
portfolio_equity = sum([w * df_asset["equity"] for w, df_asset in zip(weights, predictions)])
portfolio_drawdown = compute_drawdown(portfolio_equity)
portfolio_mdd = max_drawdown(portfolio_drawdown)
portfolio_returns = pd.concat([w * df_asset["strategy_returns"] for w, df_asset in zip(weights, predictions)], axis=1).sum(axis=1)
portfolio_sharpe = sharpe_ratio(portfolio_returns.dropna())

print(f"Portfolio Sharpe Ratio: {portfolio_sharpe:.4f} | Max Drawdown: {portfolio_mdd:.2%}")


# Save portfolio predictions
portfolio_df = pd.DataFrame({
    "equity": portfolio_equity,
    "drawdown": portfolio_drawdown,
    "returns": portfolio_returns
})
portfolio_df.to_csv("outputs/portfolio_predictions.csv", index=False)

# Execute Trades (Safe, weighted by portfolio allocation)
if config.get("enable_trading", False):
    trader = AlpacaTrader(
        key=config["alpaca_key"],
        secret=config["alpaca_secret"],
        base_url=config["alpaca_url"]
    )

    for asset, w, df_asset in zip(assets, weights, predictions):
        latest_prob = df_asset.iloc[-1]["prob_bull"]
        latest_signal = df_asset.iloc[-1]["signal"]

        # Only execute if strong confidence
        if latest_prob > 0.6:
            trader.place_order(asset, latest_signal, size=w)
            print(f"Trade executed for {asset} | Signal: {latest_signal} | Prob: {latest_prob:.2f} | Weight: {w:.2f}")
        else:
            print(f"No trade for {asset}. Prob too low: {latest_prob:.2f}")