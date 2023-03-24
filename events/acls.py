import json
import requests
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_photo(city, state):
    url = "https://api.pexels.com/v1/search"
    params = {"per_page": 1, "query": city + " " + state}
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, params=params, headers=headers)
    content = json.loads(response.content)
    return {"picture_url": content["photos"][0]["src"]["original"]}


def weather_data(city, state):
    url_geo = "http://api.openweathermap.org/geo/1.0/direct"
    params_geo = {"q": f"{city},{state},US", "appid": OPEN_WEATHER_API_KEY}
    response = requests.get(url_geo, params=params_geo)
    content = json.loads(response.content)
    try:
        latitude = content[0]["lat"]
        longitude = content[0]["lon"]
    except (KeyError, IndexError):
        return None

    url_data = "https://api.openweathermap.org/data/2.5/weather"
    params_data = {
        "lat": latitude,
        "lon": longitude,
        "unit": "imperial",
        "appid": OPEN_WEATHER_API_KEY,
    }
    response_data = requests.get(url_data, params=params_data)
    content_data = json.loads(response_data.content)
    try:
        return {
            "main_temperature": content_data["main"]["temp"],
            "weather_description": content_data["weather"][0]["description"],
        }
    except (KeyError, IndexError):
        return {"main_temperature": None, "weather_description": None}
