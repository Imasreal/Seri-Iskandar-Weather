
import urllib.request
import urllib.parse
import json
import csv
import sqlite3

# 1. Location: Seri Iskandar, Perak
LATITUDE = 4.3667
LONGITUDE = 100.9667

# 2. Date range
START_DATE = "2026-11-01"
END_DATE = "2026-11-15"

# 3. Open-Meteo API configuration
url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
    "timezone": "Asia/Singapore"
}

# 4. Generate API URL
full_url = url + "?" + urllib.parse.urlencode(params)

try:
    print("Downloading historical weather data...")

    # 5. Request data without using requests
    with urllib.request.urlopen(full_url, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))

    # 6. Extract hourly weather information
    hourly = data["hourly"]

    records = []

    for i in range(len(hourly["time"])):
        record = (
            hourly["time"][i],
            hourly["temperature_2m"][i],
            hourly["relative_humidity_2m"][i],
            hourly["precipitation"][i],
            hourly["wind_speed_10m"][i],
            "Open-Meteo Historical Weather"
        )

        records.append(record)

    print("Total records:", len(records))

    # 7. Save data to CSV
    with open("historical_weather.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "observed_at",
            "temperature",
            "humidity",
            "rainfall",
            "wind_speed",
            "source"
        ])

        writer.writerows(records)

    print("CSV file saved successfully!")

    # 8. Connect to SQLite database
    connection = sqlite3.connect("weather.db")
    cursor = connection.cursor()

    # 9. Create database table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actual_weather (
            observation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            observed_at TEXT,
            temperature REAL,
            humidity REAL,
            rainfall REAL,
            wind_speed REAL,
            source TEXT
        )
    """)

    # 10. Insert historical weather data
    cursor.executemany("""
        INSERT INTO actual_weather
        (observed_at, temperature, humidity, rainfall, wind_speed, source)
        VALUES (?, ?, ?, ?, ?, ?)
    """, records)

    connection.commit()
    connection.close()

    print("Database saved successfully!")
    print("Historical weather data collected successfully!")

except Exception as error:
    print("An error occurred:", error)

