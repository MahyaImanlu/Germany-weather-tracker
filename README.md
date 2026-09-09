# Germany-weather-tracker

An automated data pipeline that analyzes weather conditions in three cities of Germany over approx. 8 days from a real-time API.

## 📡 Data Source

Data is collected from https://openweathermap.org/current with a unique API key.

## 🛠️ Tools used

- Python
- Power BI
- SQL

## 📁 Project structure

- `.github/workflows/`: collect.yml — GitHub Actions workflow that runs the collector every hour.
- `collector/`: collector.py — fetches real-time data from the API
- `data/`: contains raw files, database file and csv file
     - `raw/` — raw JSON snapshots collected every hour
     - `germany_weather.db` — cleaned SQLite database
     - `weather_clean.csv` — exported dataset used for loading into Power BI
- `requirements.txt` — Python dependencies
- `pipeline/` — contains 3 scripts:
     - `parse_and_load.py` — parses raw JSON files, cleans data, deduplicates records, and makes data ready for analysis
     - `check_data.py` — runs a SQL script to check the validity of the data
     - `export_csv.py` — exports clean data to a csv file for use in Power BI
- `Power BI/`: Dashboard
     - `dashboard_screenshot.jpg`
     - `weather_condition_dashboard.pbix`

## 📊 Overview

- I have collected 138 data points over 8 days for 3 cities in Germany: 1. Berlin, 2. Hamburg, 3. Munich.
- Over 8 days, we would expect around 576 data points to be collected (3 cities × 24 hours × 8 days), but we only collected 138. This is likely due to GitHub Actions' free-tier scheduling, which occasionally delays or skips scheduled runs during high-traffic periods, resulting in an actual collection interval closer to every 4 hours instead of the configured hourly schedule.
- The average temperature over the 8 days is 17.93°C.
- The weather condition over this data collection period was mostly cloudy (84.06%), which matches the real weather conditions in Germany.
- The highest average temperature over the 8 days of data collection was recorded in Munich. At the same time, the lowest average humidity was also recorded in Munich.
- From this chart, I have figured out that temperature and humidity have an inverse relationship.
- After analyzing the average temperature by hour for each city, we can see that in the morning hours we have the lowest average temperature, and in the evening, at approximately 3 PM, we have the highest average temperature.

## ✍️ Author

Mahya