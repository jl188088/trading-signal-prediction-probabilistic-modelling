import numpy as np

def compute_var(returns, confidence=0.95):
    return np.percentile(returns, (1 - confidence) * 100)

def compute_volatility(returns):
    return np.std(returns)

def risk_label(var, volatility):
    if volatility < 0.01:
        return "Low"
    elif volatility < 0.02:
        return "Medium"
    else:
        return "High"