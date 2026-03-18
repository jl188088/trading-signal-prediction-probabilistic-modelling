import pandas as pd

def preprocess_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df.sort_values("Date", inplace=True)
    
    # Ensure numeric columns are floats
    numeric_cols = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    
    df.dropna(inplace=True)  # Drop rows where conversion failed
    return df