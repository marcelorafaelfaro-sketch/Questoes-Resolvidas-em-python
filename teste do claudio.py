import requests

resp = requests.get("https://api.open-meteo.com/v1/forecast", params={
    "latitude": -1.4558, "longitude": -48.5039,   # Belém (aprox.)
    "hourly": "precipitation", "past_days": 1,
    "timezone": "America/Belem",
}, timeout=15).json()

for hora, mm in zip(resp["hourly"]["time"], resp["hourly"]["precipitation"]):
    print(hora, mm, "mm")