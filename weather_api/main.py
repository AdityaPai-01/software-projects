from functions import fetch_coordinates, fetch_weatherdata,weather_codes

init_text = """
====================
    WEATHER CLI     
====================
"""
print(init_text)

city_name = input("enter city name >>>: ").title()
geo_data = fetch_coordinates(city_name)["results"][0]

if not isinstance(geo_data, str):
    header_text = f"""
Location
----------------
City Name: {geo_data["name"]}
Country:   {geo_data["country"]}
    """
    print(header_text)
else:
    print(geo_data)

weather_data = fetch_weatherdata(geo_data['latitude'],geo_data['longitude'])
if not isinstance(weather_data, str):
    weather_text = f"""
Current Weather (measure-unit)
----------------
Temperature: {weather_data["current"]["temperature_2m"]}-{weather_data["current_units"]["temperature_2m"]}
Wind Speed:  {weather_data["current"]["wind_speed_10m"]}-{weather_data["current_units"]["wind_speed_10m"]}
Condition:   {weather_codes.get(weather_data["current"]["weather_code"], "Unknown Weather")}-{weather_data["current_units"]["weather_code"]}

Forecast (Max/Min)
----------------
Today:          {weather_data["daily"]["temperature_2m_max"][0]}-°C / {weather_data["daily"]["temperature_2m_min"][0]}-°C
Tomorrow:       {weather_data["daily"]["temperature_2m_max"][1]}-°C / {weather_data["daily"]["temperature_2m_min"][1]}-°C
The day after:  {weather_data["daily"]["temperature_2m_max"][2]}-°C / {weather_data["daily"]["temperature_2m_min"][2]}-°C
    """
    print(weather_text)
else:    
    print(weather_data)
