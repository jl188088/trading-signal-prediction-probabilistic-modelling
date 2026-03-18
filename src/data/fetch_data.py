import pandas as pd
import yfinance as yf
import requests
from datetime import datetime
from alpaca.data.historical.crypto import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def log_request_id(request_id, endpoint):
    """Append the X-Request-ID to a log file with timestamp and endpoint"""
    with open("logs/request_ids.log", "a") as f:
        f.write(f"{datetime.now()} | Endpoint: {endpoint} | X-Request-ID: {request_id}\n")


def fetch_data(asset, start_date, end_date, save_path):
    """Fetch stock data via yFinance (simulate request ID logging)"""
    df = yf.download(asset, start=start_date, end=end_date)
    df.reset_index(inplace=True)
    df.to_csv(save_path, index=False)
    print(f"Stock data saved to {save_path}")

    # Simulate X-Request-ID for yFinance (since no header exists)
    request_id = f"yfinance-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    log_request_id(request_id, "yfinance")
    print("Simulated X-Request-ID for yFinance:", request_id)

    return df


def fetch_crypto_data(api_key, api_secret, symbol, start, end, save_path):
    """Fetch crypto data via Alpaca Crypto API and log X-Request-ID"""
    client = CryptoHistoricalDataClient(api_key, api_secret)

    request_params = CryptoBarsRequest(
        symbol_or_symbols=[symbol],
        timeframe=TimeFrame.Day,
        start=start,
        end=end
    )

    # Retrieve crypto bars
    bars = client.get_crypto_bars(request_params)

    # Log X-Request-ID from Alpaca SDK
    # Note: Alpaca SDK does not expose headers directly, so we also show how to log with requests
    try:
        # Making a raw request to log X-Request-ID
        url = f"https://data.alpaca.markets/v2/crypto/bars?symbols={symbol}&timeframe=1Day&start={start.isoformat()}&end={end.isoformat()}"
        headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": api_secret
        }
        response = requests.get(url, headers=headers)
        x_request_id = response.headers.get("X-Request-ID", "N/A")
        log_request_id(x_request_id, "alpaca_crypto_bars")
        print("X-Request-ID from Alpaca Crypto API:", x_request_id)
    except Exception as e:
        print("Error logging X-Request-ID:", e)

    # Filter for requested symbol
    df = bars.df[bars.df["symbol"] == symbol].copy()
    df.to_csv(save_path, index=False)
    print(f"Crypto data saved to {save_path}")

    # Print the DataFrame as requested
    print("Retrieved crypto bars DataFrame:")
    print(df)

    return df