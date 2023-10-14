# Wybierz obraz bazowy
FROM python:3.10-slim

# Skopiuj zawartość aktualnego katalogu do katalogu /app wewnątrz kontenera
COPY . /app

# Ustaw katalog roboczy na /app
WORKDIR /app

# Instaluj zależności
RUN pip install -r requirements.txt

# Wykonaj konwersję do pliku .exe
RUN pyinstaller --onefile program.py
