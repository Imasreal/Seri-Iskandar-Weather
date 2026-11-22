# TFB2093 Internet-of-Things Project
## Seri Iskandar Weather Monitoring and Forecast Evaluation

**Group members:** [Insert names and IDs]  
**Course:** TFB2093 Internet-of-Things  
**Location:** Seri Iskandar, Perak, Malaysia  
**Data collection period:** [Start date/time] to [End date/time]

## 1. Introduction
Weather information is useful for daily planning and understanding local environmental conditions. This project develops a small-scale weather data acquisition and analytics system for Seri Iskandar, Perak. The system retrieves weather information from the Open-Meteo API, stores time-stamped records, analyzes weather trends and presents the results through an interactive dashboard.

**Objectives**
1. Retrieve temperature, relative humidity, precipitation and wind-speed data for Seri Iskandar.
2. Store time-stamped current-condition and forecast records.
3. Collect data continuously for at least 72 hours.
4. Visualize historical weather and forecast information.
5. Evaluate forecast errors using matched timestamps.

## 2. Problem Statement
Weather conditions change over time, so a single reading cannot show local trends. Continuous data collection is needed to build a historical record. Forecasts should also be evaluated against corresponding weather conditions at the forecast valid time. This project addresses these needs by collecting time-stamped data for at least three continuous days and presenting the results for analysis.

## 3. System Design
### 3.1 Architecture Overview
[Insert your architecture diagram: Open-Meteo API → Python collector → SQLite database → analysis → Streamlit dashboard.]

### 3.2 Components Used
- Open-Meteo API: weather data source.
- Python and Requests: periodic data retrieval.
- SQLite: local database.
- Pandas: data handling and analysis.
- Streamlit: dashboard interface.
- Plotly: interactive charts.

### 3.3 Data Flow
The Python collector sends a request to Open-Meteo using the latitude and longitude of Seri Iskandar. It receives current-condition fields and hourly forecast values. The collector stores current-condition records with their timestamps and stores forecast values with both issue time and valid time. The dashboard reads the database, displays indicators and charts, and calculates forecast error for matched records.

## 4. Database Design
The database contains three tables:
- `actual_weather`: timestamp, temperature, humidity, rainfall, wind speed and source description.
- `forecast_weather`: issue timestamp, valid timestamp, forecast temperature, humidity, rainfall and wind speed.
- `collection_log`: collection timestamp, status and message.

[Insert database schema/table screenshot.]

## 5. Data Visualization
The Streamlit dashboard displays the latest available conditions, historical time-series charts, forecast snapshots and forecast-versus-actual evaluation.

[Insert dashboard screenshots and explain each chart.]

## 6. Cost Considerations
The software stack uses Python, SQLite, Streamlit, Plotly and the Open-Meteo API. These can be used without a software licence fee for this implementation. The project uses an existing computer and internet connection. Add any actual hosting, hardware or connectivity costs incurred by the group.

## 7. Conclusion
The project implemented [describe completed features]. Data was collected from [start] to [end], for a total of [number] hours, with [number] successful collection records. The evaluation produced [insert MAE/RMSE and parameter]. The main limitation is [describe limitations]. Future improvements include using an independent physical weather station, longer collection periods and more forecast horizons.

## References
[Add sources in IEEE reference format. Cite Open-Meteo documentation and any software/API documentation actually used.]

## Marking Rubric
[Insert the marking rubric from the assignment brief as the final page.]
