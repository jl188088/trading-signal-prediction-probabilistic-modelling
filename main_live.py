import time
import yaml
from datetime import datetime, timedelta

import pandas as pd

from src.data.fetch_data import fetch_data, fetch_crypto_data
from src.data.preprocess import preprocess_data

from src.models.hmm_model import load_hmm, predict_states
from src.risk.probabilistic_risk import compute_var, compute_volatility, risk_label
from src.signals.signal_generator import generate_signal

from src.trading.alpaca_trader import AlpacaTrader


#load config
with open("configs/config.yaml", "r") as f:
    config = yaml.safe_load(f)


#initialize trader
trader = AlpacaTrader(
    config["alpaca_key"],
    config["alpaca_secret"],
    config["alpaca_url"]
)


#load trained hmm model once
model = load_hmm("models/hmm.pkl")

print("Starting probabilistic live trading loop...")

while True:
    try:
        #fetch latest data
        raw_path = "data/raw/live_data.csv"

        if config.get("asset_type") == "crypto":
            df = fetch_crypto_data(
                config["alpaca_key"],
                config["alpaca_secret"],
                config["asset"],
                datetime.now() - timedelta(days=7),
                datetime.now(),
                raw_path
            )
        else:
            df = fetch_data(
                config["asset"],
                datetime.now() - timedelta(days=7),
                datetime.now(),
                raw_path
            )

        #preprocess

        df = preprocess_data(raw_path)

        #compute returns (core feature)
        df["returns"] = df["Close"].pct_change()
        df.dropna(inplace=True)

        #hmm inference (no training)
        states, probs = predict_states(model, df["returns"])

        df["state"] = states
        df["prob_bull"] = probs[:, 1]  #assuming state 1 = bull

        #risk modeling
        var = compute_var(df["returns"])
        volatility = compute_volatility(df["returns"])
        risk = risk_label(var, volatility)

        df["VaR"] = var
        df["volatility"] = volatility
        df["risk"] = risk

        #generate signal
        signal = generate_signal(probs)
        df["signal"] = signal

        #save predictions (for dashboard)
        df.to_csv("outputs/predictions.csv", index=False)


        #execute trade
        trader.place_order(config["asset"], signal)

        print(f"[{datetime.now()}] Trade executed for {config['asset']} | Signal: {signal} | Risk: {risk}")

        #wait before next iteration
        time.sleep(60)

    except KeyboardInterrupt:
        print("Live trading stopped manually.")
        break

    except Exception as e:
        print("Error in live loop:", e)
        time.sleep(60)