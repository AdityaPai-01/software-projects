import os, requests
from dotenv import load_dotenv

load_dotenv()

weather_base_url = os.getenv("WEATHER_BASE_URL")
geocode_base_url = os.getenv("GEOCODE_BASE_URL")

def fetch_coordinates(city_name:str):
    try:
        param = {"name":city_name, "count":1}
        response = requests.get(url=geocode_base_url, params=param)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
            return f"ERROR: {e}"

def fetch_weatherdata(latitude: float, longitude: float):
    try:
        param = {"latitude":latitude, "longitude":longitude,
                 "daily": ["temperature_2m_max","temperature_2m_min"],
                 "current": ["temperature_2m", "wind_speed_10m","weather_code"],
                 "forecast_days":3}
        
        response = requests.get(url=weather_base_url, params=param)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return f"ERROR: {e}"

weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}