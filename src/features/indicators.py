import pandas as pd

def add_features(df):
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df.dropna(inplace=True)

    # Returns
    df["returns"] = df["Close"].pct_change()

    # Simple Moving Averages
    df["sma_5"] = df["Close"].rolling(window=5).mean()
    df["sma_10"] = df["Close"].rolling(window=10).mean()

    # Volatility
    df["volatility"] = df["returns"].rolling(window=5).std()

    # Momentum
    df["momentum"] = df["Close"] - df["Close"].shift(5)

    df.dropna(inplace=True)
    return df