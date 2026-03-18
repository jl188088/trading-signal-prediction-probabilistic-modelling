import pandas as pd

def backtest(df, initial_balance=10000):
    balance = initial_balance
    position = 0
    equity_curve = []

    for i in range(len(df)):
        signal = df.iloc[i]["signal"]
        price = df.iloc[i]["Close"]

        # BUY
        if signal == 1 and position == 0:
            position = balance / price
            balance = 0

        # SELL
        elif signal == 0 and position > 0:
            balance = position * price
            position = 0

        total_value = balance + (position * price)
        equity_curve.append(total_value)

    df["equity"] = equity_curve
    return df