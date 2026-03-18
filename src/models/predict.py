import joblib

def load_model(model_path):
    return joblib.load(model_path)

def predict(model, X, threshold):
    probs = model.predict_proba(X)[:, 1]
    signals = (probs > threshold).astype(int)
    return probs, signals