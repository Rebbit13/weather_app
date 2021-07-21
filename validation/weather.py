from pydantic import BaseModel

FORECAST_FORMAT = "\n\nВремя суток: {part_name}" \
                  "\n{condition}" \
                  "\nТемпература минимальная: {temp_min} °C" \
                  "\nТемпература средняя: {temp_avg} °C" \
                  "\nТемпература максимальная: {temp_max} °C" \
                  "\nПо ощущениям: {feels_like} °C" \
                  "\nСкорость ветра: {wind_speed} м/с" \
                  "\nПорывы: {wind_gust} м/с" \
                  "\nДавление: {pressure_mm}"

WEATHER_NOW_FORMAT = "Погода на текущий момент: {condition}" \
                     "\nТемпература воздуха: {temperature} °C" \
                     "\nПо ощущениям: {feels_like} °C" \
                     "\nСкорость ветра: {wind_speed} м/с" \
                     "\nПорывы: {wind_gust} м/с" \
                     "\nДавление: {pressure_mm}"

WEATHER_CONDITION = {
    "clear": "ясно",
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


class WeatherLocation(BaseModel):
    altitude: float
    longitude: float


class WeatherNow(BaseModel):
    condition: str
    temp: float
    feels_like: float
    wind_speed: float
    wind_gust: float
    pressure_mm: int

    WEATHER_NOW_FORMAT = "Погода на текущий момент: {condition}" \
                         "\nТемпература воздуха: {temperature} °C" \
                         "\nПо ощущениям: {feels_like} °C" \
                         "\nСкорость ветра: {wind_speed} м/с" \
                         "\nПорывы: {wind_gust} м/с" \
                         "\nДавление: {pressure_mm}"

    def __str__(self):
        return self.WEATHER_NOW_FORMAT.format(condition=WEATHER_CONDITION[self.condition],
                                              temperature=self.temp,
                                              feels_like=self.feels_like,
                                              wind_speed=self.wind_speed,
                                              wind_gust=self.wind_gust,
                                              pressure_mm=self.pressure_mm)


class Forecast(BaseModel):
    part_name: str
    condition: str
    temp_min: float
    temp_avg: float
    temp_max: float
    feels_like: float
    wind_speed: float
    wind_gust: float
    pressure_mm: int

    FORECAST_FORMAT = "\n\nВремя суток: {part_name}" \
                      "\n{condition}" \
                      "\nТемпература минимальная: {temp_min} °C" \
                      "\nТемпература средняя: {temp_avg} °C" \
                      "\nТемпература максимальная: {temp_max} °C" \
                      "\nПо ощущениям: {feels_like} °C" \
                      "\nСкорость ветра: {wind_speed} м/с" \
                      "\nПорывы: {wind_gust} м/с" \
                      "\nДавление: {pressure_mm}"

    def __str__(self):
        return self.FORECAST_FORMAT.format(part_name=FORECAST_PARTS[self.part_name],
                                           condition=WEATHER_CONDITION[self.condition],
                                           temp_min=self.temp_min,
                                           temp_avg=self.temp_avg,
                                           temp_max=self.temp_max,
                                           feels_like=self.feels_like,
                                           wind_speed=self.wind_speed,
                                           wind_gust=self.wind_gust,
                                           pressure_mm=self.pressure_mm)
