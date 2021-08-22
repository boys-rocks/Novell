import requests
import os
from helpers.logHelper import logger

WEATHER_API = os.environ.get("WEATHER_API", None)
class settings():
    def __init__(self):
        self.endpoint = "http://dataservice.accuweather.com/"
setting = settings()

def request(method, path, params=None):
    try:
        resp = requests.request(method, setting.endpoint + path, params = params)
        data = resp.json()
        return data
    except Exception as e:
        logger.warning(f"Exception caught in requests function: {e}")
        
def getLocationKey(location):
    try:
        data = request("GET", "locations/v1/search?q="+location+"&apikey="+WEATHER_API)
        location_key = data[0]["Key"]
        location_country = data[0]["Country"]["EnglishName"]
        return [location_key, location_country]
    except Exception as e:
        logger.warning(f"Exception caught in getLocationKey function: {e}")
def getWeather(location_key):
    try:
        data = request("GET", "currentconditions/v1/"+location_key+"?apikey="+WEATHER_API)
        tempf= data[0]["Temperature"]["Imperial"]["Value"]
        tempc= data[0]["Temperature"]["Metric"]["Value"]
        return [tempf,tempc]
    except Exception as e:
        logger.warning(f"Exception caught in getWeather function: {e}")
