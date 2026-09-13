# 🌦️ Weather CLI

A command-line weather application built with Python and `requests`, using the Open-Meteo API.

## What it does

- Ask the user for a city name.
- Fetch the city's location and coordinates.
- Fetch current weather data using those coordinates.
- Display temperature, wind speed, and weather condition.
- Display a short multi-day forecast.
- Handle invalid cities and API/request errors gracefully.

## Example Output

```text
================================
        WEATHER CLI
================================

Enter city: Mumbai

Location
--------
City: Mumbai
Country: India

Current Weather
---------------
Temperature: 28°C
Wind Speed: 14 km/h
Condition: Clear sky

Forecast
--------
Today:    30°C / 25°C
Tomorrow: 31°C / 25°C
Day 3:    30°C / 24°C

================================