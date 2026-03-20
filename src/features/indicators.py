import pandas as pd

def add_features(df):
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df.dropna(inplace=True)

    #returns
    df["returns"] = df["Close"].pct_change()

    #simple Moving Averages
    df["sma_5"] = df["Close"].rolling(window=5).mean()
    df["sma_10"] = df["Close"].rolling(window=10).mean()

    #volatility
    df["volatility"] = df["returns"].rolling(window=5).std()

    #momentum
    df["momentum"] = df["Close"] - df["Close"].shift(5)

    df.dropna(inplace=True)
    return df