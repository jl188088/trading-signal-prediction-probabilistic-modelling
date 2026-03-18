def generate_signal(state_probs, bull_state=1, threshold=0.6):
    latest_probs = state_probs[-1]

    if latest_probs[bull_state] > threshold:
        return 1  # BUY
    else:
        return 0  # SELL