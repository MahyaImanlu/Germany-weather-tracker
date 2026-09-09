import json
import glob
import os
import sqlite3
import pandas as pd


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
DB_PATH = os.path.join(PROJECT_ROOT, "data", "germany_weather.db")


def load_all_raw_files():
    records = []
    files = glob.glob(f"{RAW_DIR}/*.json")
    print(f"{len(files)} raw files found.")

    for filepath in files:
        filename = filepath.replace('\\', '/').split('/')[-1]
        city_from_filename = filename.split('_')[0]

        with open (filepath, 'r') as f:
            data = json.load(f)

        records.append({
                "city": city_from_filename,
                "temp": data.get("main", {}).get("temp"),
                "feels_like": data.get("main", {}).get("feels_like"),
                "humidity": data.get("main", {}).get("humidity"),
                "pressure": data.get("main", {}).get("pressure"),
                "weather_main": data.get("weather", [{}])[0].get("main"),
                "weather_description": data.get("weather", [{}])[0].get("description"),
                "wind_speed": data.get("wind", {}).get("speed"),
                "cloudiness": data.get("clouds", {}).get("all"),
                "visibility": data.get("visibility"),
                "timestamp": data.get("dt"),
            })

    return records


def main():
    records = load_all_raw_files()
    df = pd.DataFrame(records)
    print(f"Total records before dedup:{len(df)}")

    df = df.drop_duplicates(subset=["city", "timestamp"])
    print(f"Total records after dedup: {len(df)}")
    df = df.dropna(subset=["temp"])

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("weather", conn, if_exists='replace', index=False)
    conn.close()
    print(f"Loaded {len(df)} clean records into {DB_PATH}")


if __name__ == "__main__":
    main()