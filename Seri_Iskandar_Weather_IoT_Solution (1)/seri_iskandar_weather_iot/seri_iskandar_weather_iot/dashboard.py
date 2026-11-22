
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# =====================================
# DATABASE CONNECTION
# =====================================

def get_weather_data():
    try:
        connection = sqlite3.connect("weather.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT observed_at, temperature, humidity,
                   rainfall, wind_speed
            FROM actual_weather
            ORDER BY observed_at DESC
        """)

        records = cursor.fetchall()
        connection.close()

        return records

    except sqlite3.Error as error:
        messagebox.showerror("Database Error", str(error))
        return []


# =====================================
# CALCULATE WEATHER STATISTICS
# =====================================

def calculate_statistics(records):

    temperatures = [r[1] for r in records if r[1] is not None]
    humidities = [r[2] for r in records if r[2] is not None]
    rainfalls = [r[3] for r in records if r[3] is not None]
    wind_speeds = [r[4] for r in records if r[4] is not None]

    def average(values):
        return sum(values) / len(values) if values else 0

    return {
        "average_temp": average(temperatures),
        "max_temp": max(temperatures) if temperatures else 0,
        "min_temp": min(temperatures) if temperatures else 0,
        "average_humidity": average(humidities),
        "total_rainfall": sum(rainfalls),
        "average_wind": average(wind_speeds),
        "total_records": len(records)
    }


# =====================================
# MAIN WINDOW
# =====================================

root = tk.Tk()
root.title("Seri Iskandar Weather Dashboard")
root.geometry("1100x700")
root.configure(bg="#EAF2F8")


# =====================================
# TITLE
# =====================================

title = tk.Label(
    root,
    text="SERI ISKANDAR WEATHER MONITORING",
    font=("Arial", 22, "bold"),
    bg="#EAF2F8",
    fg="#154360"
)

title.pack(pady=20)


subtitle = tk.Label(
    root,
    text="Historical Weather Data Analysis",
    font=("Arial", 12),
    bg="#EAF2F8"
)

subtitle.pack()


# =====================================
# STATISTICS DISPLAY
# =====================================

stats_frame = tk.Frame(root, bg="#EAF2F8")
stats_frame.pack(pady=25)


def create_metric(parent, title, value, column):
    frame = tk.Frame(
        parent,
        bg="white",
        padx=20,
        pady=15,
        relief="ridge",
        borderwidth=2
    )

    frame.grid(row=0, column=column, padx=8)

    tk.Label(
        frame,
        text=title,
        font=("Arial", 11, "bold"),
        bg="white"
    ).pack()

    label = tk.Label(
        frame,
        text=value,
        font=("Arial", 17, "bold"),
        fg="#2874A6",
        bg="white"
    )

    label.pack(pady=8)

    return label


temp_label = create_metric(
    stats_frame, "Average Temperature", "-- °C", 0
)

humidity_label = create_metric(
    stats_frame, "Average Humidity", "-- %", 1
)

rainfall_label = create_metric(
    stats_frame, "Total Rainfall", "-- mm", 2
)

wind_label = create_metric(
    stats_frame, "Average Wind Speed", "-- km/h", 3
)


# =====================================
# WEATHER TABLE
# =====================================

table_title = tk.Label(
    root,
    text="Historical Weather Records",
    font=("Arial", 16, "bold"),
    bg="#EAF2F8",
    fg="#154360"
)

table_title.pack(pady=10)


table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=25, pady=10)


columns = (
    "Date and Time",
    "Temperature (°C)",
    "Humidity (%)",
    "Rainfall (mm)",
    "Wind Speed (km/h)"
)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for column in columns:
    tree.heading(column, text=column)
    tree.column(column, width=190, anchor="center")

tree.pack(side="left", fill="both", expand=True)


scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")


# =====================================
# REFRESH DASHBOARD
# =====================================

def refresh_dashboard():

    records = get_weather_data()

    # Clear previous table records
    for item in tree.get_children():
        tree.delete(item)

    if not records:
        temp_label.config(text="-- °C")
        humidity_label.config(text="-- %")
        rainfall_label.config(text="-- mm")
        wind_label.config(text="-- km/h")

        messagebox.showwarning(
            "No Data",
            "No weather records found. Run historical_data.py first."
        )

        return

    # Insert records into table
    for record in records:
        tree.insert("", "end", values=record)

    # Calculate statistics
    stats = calculate_statistics(records)

    temp_label.config(
        text=f"{stats['average_temp']:.1f} °C"
    )

    humidity_label.config(
        text=f"{stats['average_humidity']:.1f} %"
    )

    rainfall_label.config(
        text=f"{stats['total_rainfall']:.1f} mm"
    )

    wind_label.config(
        text=f"{stats['average_wind']:.1f} km/h"
    )

    records_label.config(
        text=f"Total Weather Records: {stats['total_records']}"
    )


# =====================================
# BUTTONS AND FOOTER
# =====================================

button_frame = tk.Frame(root, bg="#EAF2F8")
button_frame.pack(pady=15)


refresh_button = tk.Button(
    button_frame,
    text="Refresh Dashboard",
    font=("Arial", 11, "bold"),
    bg="#2874A6",
    fg="white",
    command=refresh_dashboard,
    padx=15,
    pady=8
)

refresh_button.pack(side="left", padx=10)


records_label = tk.Label(
    root,
    text="Total Weather Records: 0",
    font=("Arial", 11, "bold"),
    bg="#EAF2F8"
)

records_label.pack(pady=5)


footer = tk.Label(
    root,
    text="Weather Data Source: Open-Meteo Historical Weather API",
    font=("Arial", 9),
    bg="#EAF2F8",
    fg="gray"
)

footer.pack(pady=8)


# =====================================
# START DASHBOARD
# =====================================

refresh_dashboard()

root.mainloop()
