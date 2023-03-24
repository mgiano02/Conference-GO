import json
import requests
from events.keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY

headers = {"Authorization": PEXELS_API_KEY}


def location_acl():
    response = requests.get("https://api.pexels.com/v1/search")
    photo = json.loads(response.content)
    location = {"picture_url": photo["picture_url"]}
    return location
