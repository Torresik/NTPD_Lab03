# Używamy oficjalnego, lekkiego obrazu Python 3.9
FROM python:3.9-slim

# Ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR /app

# Kopiujemy plik z listą zależności
COPY requirements.txt .

# Instalujemy zależności (bez zapisywania w pamięci podręcznej, aby obraz był mniejszy)
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy resztę plików projektu (w tym app.py)
COPY . .

# Informujemy, że kontener będzie nasłuchiwał na porcie 8000
EXPOSE 8000

# Komenda uruchamiająca serwer w trybie produkcyjnym po starcie kontenera
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]