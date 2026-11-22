import sqlite3
import math
from datetime import datetime

# 1. Connect to database
connection = sqlite3.connect("weather.db")
cursor = connection.cursor()

# 2. Retrieve historical weather data
cursor.execute("""
    SELECT observed_at, temperature, humidity,
           rainfall, wind_speed
    FROM actual_weather
    ORDER BY observed_at
""")

records = cursor.fetchall()
connection.close()

# 3. Check if data exists
if not records:
    print("No weather data found in database.")
    exit()

# 4. Extract weather information
temperatures = []
humidities = []
rainfalls = []
wind_speeds = []

for record in records:
    if record[1] is not None:
        temperatures.append(record[1])

    if record[2] is not None:
        humidities.append(record[2])

    if record[3] is not None:
        rainfalls.append(record[3])

    if record[4] is not None:
        wind_speeds.append(record[4])

# 5. Calculate average
def calculate_average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)

# 6. Calculate statistics
average_temp = calculate_average(temperatures)
maximum_temp = max(temperatures) if temperatures else 0
minimum_temp = min(temperatures) if temperatures else 0

average_humidity = calculate_average(humidities)
maximum_humidity = max(humidities) if humidities else 0
minimum_humidity = min(humidities) if humidities else 0

total_rainfall = sum(rainfalls)
average_wind = calculate_average(wind_speeds)
maximum_wind = max(wind_speeds) if wind_speeds else 0

# 7. Display analysis results
print("\n======================================")
print(" SERI ISKANDAR WEATHER DATA ANALYSIS")
print("======================================")

print("\nDATA INFORMATION")
print("------------------------------")
print("Total weather records:", len(records))
print("First observation:", records[0][0])
print("Last observation:", records[-1][0])

print("\nTEMPERATURE ANALYSIS")
print("------------------------------")
print(f"Average Temperature: {average_temp:.2f} °C")
print(f"Maximum Temperature: {maximum_temp:.2f} °C")
print(f"Minimum Temperature: {minimum_temp:.2f} °C")

print("\nHUMIDITY ANALYSIS")
print("------------------------------")
print(f"Average Humidity: {average_humidity:.2f} %")
print(f"Maximum Humidity: {maximum_humidity:.2f} %")
print(f"Minimum Humidity: {minimum_humidity:.2f} %")

print("\nRAINFALL ANALYSIS")
print("------------------------------")
print(f"Total Rainfall: {total_rainfall:.2f} mm")
print(f"Average Rainfall: {calculate_average(rainfalls):.2f} mm")

print("\nWIND SPEED ANALYSIS")
print("------------------------------")
print(f"Average Wind Speed: {average_wind:.2f} km/h")
print(f"Maximum Wind Speed: {maximum_wind:.2f} km/h")

print("\n======================================")
print(" ANALYSIS COMPLETED SUCCESSFULLY")
print("======================================")
