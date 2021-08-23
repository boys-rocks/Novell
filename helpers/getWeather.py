import requests
import os
from helpers.logHelper import logger

WEATHER_API = os.environ.get("WEATHER_API", None)


class settings:
    def __init__(self):
        self.endpoint = "https://api.weatherbit.io/"


setting = settings()


def request(method, path, params=None):
    try:
        resp = requests.request(method, setting.endpoint + path, params=params)
        data = resp.json()
        return data
    except Exception as e:
        logger.warning(f"Exception caught in requests function: {e}")


def parse_location(location_received):
    location_list = location_received.split(",")
    char_list = []

    for element in location_list:
        temp_list = []
        for value in element:
            temp_list.append(value)
        char_list.append(temp_list)

    for sub_list in char_list:
        for index, value in enumerate(sub_list):
            if value == " " and index != 0:
                sub_list[index] = "+"

    temp_list = []
    for sub_list in char_list:
        temp_string = ""
        for char in sub_list:
            temp_string += char
        temp_list.append(temp_string)

    edited_location = ",".join(temp_list)
    return edited_location


def getWeather(location):

    location = parse_location(location)

    try:
        data_one = request(
            "GET", "v2.0/current?units=I&city=" + location + "&key=" + WEATHER_API
        )
        data_two = request(
            "GET", "v2.0/current?units=M&city=" + location + "&key=" + WEATHER_API
        )
        tempf = data_one["data"][0]["temp"]
        tempc = data_two["data"][0]["temp"]
        return tempf, tempc
    except Exception as e:
        logger.warning(f"Exception caught in getWeather function: {e}")
