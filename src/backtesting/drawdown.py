import numpy as np

def compute_drawdown(equity_curve):
    peak = equity_curve.expanding(min_periods=1).max()
    drawdown = (equity_curve - peak) / peak
    return drawdown


def max_drawdown(drawdown):
    return np.min(drawdown)