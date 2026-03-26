from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import numpy as np

app = FastAPI(title="ML Model API", description="API do serwowania modelu ML z laboratorium 03")

# Przygotowanie i trening prostego modelu ML
# Sztuczne dane do treningu
X_train = np.array([[1.0, 1.5], [1.2, 1.8], [2.5, 3.0], [3.0, 3.5]])
# Etykiety
y_train = np.array([0, 0, 1, 1])

# Inicjalizacja i trenowanie modelu
model = LogisticRegression()
model.fit(X_train, y_train)


# Definicja struktury danych wejściowych
class InputData(BaseModel):
    feature1: float
    feature2: float


# Podstawowy endpoint
@app.get("/")
def read_root():
    return {"message": "Witaj w API modelu ML! Przejdź do /docs aby zobaczyć dokumentację."}


# Endpoint predykcji
@app.post("/predict")
def predict(data: InputData):
    # Konwersja danych
    features = np.array([[data.feature1, data.feature2]])
    # Wykonanie predykcji
    prediction = model.predict(features)
    # Zwrócenie wyniku w formacie JSON
    return {"prediction": int(prediction[0])}


# Dodatkowe endpointy
@app.get("/info")
def get_info():
    return {
        "model_type": "LogisticRegression",
        "framework": "scikit-learn",
        "features_count": 2,
        "features_names": ["feature1", "feature2"]
    }


@app.get("/health")
def get_health():
    return {"status": "ok"}