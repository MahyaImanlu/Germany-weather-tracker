import os
import sqlite3
import pandas as pd


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(PROJECT_ROOT, "data", "germany_weather.db")


conn = sqlite3.connect(DB_PATH)

query = """
    SELECT city, ROUND(AVG(temp), 1) as avg_temp, ROUND(AVG(humidity), 1) as avg_humidity, COUNT(*) as n
    FROM weather
    GROUP BY city
    ORDER BY avg_temp DESC;
"""


df = pd.read_sql(query, conn)
print(df)

conn.close()