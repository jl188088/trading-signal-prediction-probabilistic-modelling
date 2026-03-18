import numpy as np

def optimize_portfolio(returns_df):
    """
    Simple mean-variance optimization
    """
    mean_returns = returns_df.mean()
    cov_matrix = returns_df.cov()

    num_assets = len(mean_returns)

    weights = np.ones(num_assets) / num_assets

    # Sharpe maximization (simplified)
    inv_cov = np.linalg.pinv(cov_matrix.values)
    weights = inv_cov @ mean_returns.values

    weights = weights / np.sum(weights)

    return weights