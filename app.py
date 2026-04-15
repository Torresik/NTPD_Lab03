from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import numpy as np
import os

app = FastAPI(title="ML Model API", description="API do serwowania modelu ML z laboratorium 05")

X_train = np.array([[1.0, 1.5], [1.2, 1.8], [2.5, 3.0], [3.0, 3.5]])
y_train = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(X_train, y_train)

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def read_root():
    return {"message": "Witaj w API modelu ML! Przejdź do /docs aby zobaczyć dokumentację."}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[data.feature1, data.feature2]])
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}

@app.get("/info")
def get_info():
    return {
        "model_type": "LogisticRegression",
        "framework": "scikit-learn",
        "features_count": 2,
    }

@app.get("/health")
def get_health():
    return {"status": "ok"}

# Zadanie 5
@app.get("/env-test")
def test_env():
    # Pobieramy zmienną SECRET_API_KEY. Jeśli jej nie ma, zwracamy "Brak klucza"
    api_key = os.environ.get("SECRET_API_KEY", "Brak klucza")
    return {"secret_key_loaded": api_key}