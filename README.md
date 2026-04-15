# Dokumentacja: API do serwowania modelu ML (FastAPI + Docker)

## O projekcie
Aplikacja serwująca prosty model uczenia maszynowego (Logistic Regression) zbudowana w oparciu o framework FastAPI. Środowisko uruchomieniowe zostało skonteneryzowane przy użyciu platformy Docker.

## Zmienne środowiskowe i zasoby
- **Zmienne środowiskowe:** Aplikacja domyślnie nasłuchuje na porcie konfigurowanym przez polecenie Uvicorn (domyślnie `8000`).
- **Zasoby:** Kontener wymaga minimalnych zasobów (przydział 0.5 vCPU oraz ok. 100 MB RAM jest w zupełności wystarczający dla uproszczonego modelu scikit-learn).
- **Zależności:** Aplikacja wymaga bazy Redis do pełnego uruchomienia środowiska w trybie Compose.

## Instrukcje uruchamiania aplikacji

### 1. Uruchomienie lokalne (bez Dockera)
Wymaga zainstalowanego środowiska Python 3.9+.
```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000