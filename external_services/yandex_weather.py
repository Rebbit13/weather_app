import requests

from config import API_YANDEX_TOKEN, API_YANDEX_URL, API_YANDEX_LANG, WEATHER_NOW_FORMAT, FORECAST_FORMAT

HEADERS = {
    "X-Yandex-API-Key": API_YANDEX_TOKEN
}

WEATHER_CONDITION = {
    "clear":"ясно",
    "partly-cloudy": "малооблачно",
    "cloudy": "облачно с прояснениями",
    "overcast": "пасмурно",
    "drizzle": "морось",
    "light-rain": "небольшой дождь",
    "rain": "дождь",
    "moderate-rain": "умеренно сильный дождь",
    "heavy-rain": "сильный дождь",
    "continuous-heavy-rain": "длительный сильный дождь",
    "showers": "ливень",
    "wet-snow": "дождь со снегом",
    "light-snow": "небольшой снег",
    "snow": "снег",
    "snow-showers": "снегопад",
    "hail": "град",
    "thunderstorm": "гроза",
    "thunderstorm-with-rain": "дождь с грозой",
    "thunderstorm-with-hail":  "гроза с градом"
}

FORECAST_PARTS = {
    "night": "ночь",
    "morning": "утро",
    "day": "день",
    "evening": 'вечер',
}


def get_weather(altitude: float, longitude: float):
    r = requests.get(url=API_YANDEX_URL.format(lat=altitude, lon=longitude, lang=API_YANDEX_LANG),
                     headers=HEADERS)
    return r.json()


def form_weather_data_from_json(json: dict):
    fact = json['fact']
    weather_now = WEATHER_NOW_FORMAT.format(condition=WEATHER_CONDITION[fact["condition"]],
                                            temperature=fact['temp'],
                                            feels_like=fact['feels_like'],
                                            wind_speed=fact['wind_speed'],
                                            wind_gust=fact['wind_gust'],
                                            pressure_mm=fact['pressure_mm'])

    forecast = "Прогноз:"
    for part in json['forecast']['parts']:
        forecast += FORECAST_FORMAT.format(part_name=FORECAST_PARTS[part['part_name']],
                                           condition=WEATHER_CONDITION[part["condition"]],
                                           temp_min=part['temp_min'],
                                           temp_avg=part['temp_avg'],
                                           temp_max=part['temp_max'],
                                           feels_like=part['feels_like'],
                                           wind_speed=part['wind_speed'],
                                           wind_gust=part['wind_gust'],
                                           pressure_mm=part['pressure_mm'])
    return {"weather_now": weather_now, "forecast": forecast}


def get_formed_weather_data(altitude: float, longitude: float):
    json = get_weather(altitude, longitude)
    return form_weather_data_from_json(json)
