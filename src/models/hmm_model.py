import numpy as np
from hmmlearn.hmm import GaussianHMM
import joblib

def train_hmm(returns, n_states=3, model_path="models/hmm.pkl"):
    model = GaussianHMM(n_components=n_states, covariance_type="diag", n_iter=1000)
    returns = returns.values.reshape(-1, 1)

    model.fit(returns)
    joblib.dump(model, model_path)

    return model


def load_hmm(model_path="models/hmm.pkl"):
    return joblib.load(model_path)


def predict_states(model, returns):
    returns = returns.values.reshape(-1, 1)
    states = model.predict(returns)
    probs = model.predict_proba(returns)
    return states, probs