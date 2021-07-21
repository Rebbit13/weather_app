import json
import os
from datetime import timedelta

import requests

from database.cash import cash
from external_services.config import API_YANDEX_URL, API_YANDEX_LANG
from validation.weather import WeatherLocation, Forecast, WeatherNow

HEADERS = {
    "X-Yandex-API-Key": os.environ['API_YANDEX_TOKEN']
}


def get_weather(location: WeatherLocation):
    cashed = cash.get(location.json())
    if cashed is None:
        r = requests.get(url=API_YANDEX_URL.format(lat=location.altitude,
                                                   lon=location.longitude,
                                                   lang=API_YANDEX_LANG),
                         headers=HEADERS)
        cash.setex(location.json(),
                   timedelta(hours=int(os.environ['CASH_HOURS_TO_LIVE'])),
                   r.content)
        return r.json()
    else:
        return json.loads(cashed.decode('utf-8'))


def form_weather_data_from_json(json_dict: dict):
    weather_now_obj = WeatherNow.parse_obj(json_dict['fact'])
    weather_now = str(weather_now_obj)
    forecast = "Прогноз:"
    for part in json_dict['forecast']['parts']:
        forecast_obj = Forecast.parse_obj(part)
        forecast += str(forecast_obj)
    return {"weather_now": weather_now, "forecast": forecast}


def get_formed_weather_data(altitude: float, longitude: float):
    json_dict = get_weather(WeatherLocation(altitude, longitude))
    return form_weather_data_from_json(json_dict)
