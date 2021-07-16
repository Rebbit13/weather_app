API_YANDEX_URL = "https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}&[lang={lang}]"
API_YANDEX_LANG = "ru_RU"
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
