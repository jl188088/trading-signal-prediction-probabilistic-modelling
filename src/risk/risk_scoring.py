def assign_risk(volatility):
    if volatility < 0.01:
        return "Low"
    elif volatility < 0.02:
        return "Medium"
    else:
        return "High"