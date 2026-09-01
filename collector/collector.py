import requests
import json
from datetime import datetime, timezone
import os


cities = {
  "Berlin":{"lat":52.5244, "lon":13.4105},
  "Hamburg":{"lat":53.5511, "lon":9.9937},
  "Munich":{"lat":48.1374, "lon":11.5755}
}

Output_Dir = "data/raw"
API_KEY = os.environ.get("...")

def fetch_weather(lat, lon):
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"
  resp = requests.get(url, timeout=10)
  resp.raise_for_status()
  return resp.json()

def save_raw(city_name, data):
  os.makedirs(Output_Dir, exist_ok=True)
  ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
  path = f"{Output_Dir}/{city_name}_{ts}.json"
  with open(path, "w") as f:
    json.dump(data, f)


if __name__ == "__main__":
    for name, coords in cities.items():
        try:
            data = fetch_weather(coords["lat"], coords["lon"])
            save_raw(name, data)
        except Exception as e:
            print(f"Failed for {name}: {e}")
  
