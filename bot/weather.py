import pgeocode as geo
import requests
from typing import Tuple

import settings
import localizer

def get_daily_weather_forecast(zipcode: str) -> dict:
    """
    Retrieves the daily weather forecast for a given zip code and formats the output.
        Parameters:
            zipcode (str): The zip code to get the weather for.
        Returns:
            (dict of int: float): Map of date->high weather estimate for the date.
    """
    longitude, latitude = get_coordinates(zipcode)

    weather = get_weather(latitude, longitude)
    if weather is None:
        return None
    else:
        daily_forecast = {}
        for day_forecast in weather["daily"]:
            date = localizer.get_localized_datetime(day_forecast["dt"])
            daily_forecast[f"{date.month}/{date.day}"] = day_forecast["temp"]["max"]

        return daily_forecast

def get_weather(latitude: float, longitude: float) -> str:
    """
    Gets the weather forecast for given coordinates.
        Parameters:
            latitude (float): The latitude for the location to get weather for.
            longitude (float): The longitude for the location to get weather for.
        Returns:
            (str): Json object from open weather map response
    """
    # Get weather forecast for location
    request_string = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&units={settings.weather_unit}&exclude=minutely,hourly&appid={settings.owm_token}"
    weather_response = requests.get(request_string)
    
    if (weather_response.status_code == 200):
        return weather_response.json()
    else:
        print(f"Weather API call failed. Error message: {weather_response.text}")
        return None

def get_coordinates(zipcode: str) -> Tuple[float, float]:
    """
    Gets cardinal coordinates for a given zip code.
        Parameters:
            zipcode (str): The zip code to get coordinates for.
        Returns:
            (float, float): The longitude and latitude coordinate pair.
            
    """
    # Get latitude and longitude for location
    us_geo = geo.Nominatim("us")
    location = us_geo.query_postal_code(zipcode)

    # Convert numpy floats to python floats
    return location["longitude"].item(), location["latitude"].item()