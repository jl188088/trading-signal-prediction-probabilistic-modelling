def generate_commentary(signal, confidence, risk):
    if signal == 1:
        action = "BUY"
    else:
        action = "SELL"
    return f"""
Signal: {action}
Confidence: {round(confidence*100,2)}%
Risk Level: {risk}

Interpretation:
Based on model output and risk analysis, the current signal indicates {action.lower()} with {risk.lower()} risk.
"""