import requests

from config import API_YANDEX_TOKEN, API_YANDEX_URL, API_YANDEX_LANG

HEADERS = {
    "X-Yandex-API-Key": API_YANDEX_TOKEN
}


def get_weather_data(altitude, longitude):
    r = requests.get(url=API_YANDEX_URL.format(lat=altitude, lon=longitude, lang=API_YANDEX_LANG),
                     headers=HEADERS)
    print(r.json())
