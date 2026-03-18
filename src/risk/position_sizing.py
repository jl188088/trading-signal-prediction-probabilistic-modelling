def calculate_position_size(balance, risk_per_trade, volatility):
    """
    Simple risk-based position sizing
    """
    if volatility == 0:
        return 0

    position_size = (balance * risk_per_trade) / volatility
    return max(1, int(position_size))


def should_trade(probability, threshold=0.6):
    return probability > threshold