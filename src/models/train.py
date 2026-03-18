from sklearn.linear_model import LogisticRegression
import joblib

def train_model(X_train, y_train, model_path):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model