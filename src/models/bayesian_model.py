import numpy as np

def bayesian_update(prior, likelihood):
    posterior = prior * likelihood
    return posterior / posterior.sum()


def compute_bull_probability(returns):
    # Simple likelihood assumption
    likelihood_bull = np.exp(returns)
    likelihood_bear = np.exp(-returns)

    prior = np.array([0.5, 0.5])
    probs = []

    for i in range(len(returns)):
        likelihood = np.array([likelihood_bear[i], likelihood_bull[i]])
        posterior = bayesian_update(prior, likelihood)
        probs.append(posterior[1])  # bull probability
        prior = posterior

    return np.array(probs)