import os
import sqlite3
import pandas as pd


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(PROJECT_ROOT, "data", "germany_weather.db")
CSV_PATH = os.path.join(PROJECT_ROOT, "data", "weather_clean.csv")


conn = sqlite3.connect(DB_PATH)

query = """
SELECT city, temp, feels_like, humidity, pressure, 
       weather_main, weather_description, wind_speed, 
       cloudiness, visibility, timestamp
FROM weather;
"""

df = pd.read_sql(query, conn)
print(f"Exported len{df} rows.")
print(df.head())

conn.close()

df.to_csv(CSV_PATH, index=False)
print(f"{len(df)} rows exported to {CSV_PATH}")

