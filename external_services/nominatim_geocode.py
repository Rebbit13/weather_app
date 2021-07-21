from geopy.geocoders import Nominatim

from database.cash import cash
from validation.location import LocationGet

geo_locator = Nominatim(user_agent="evgeniy_weather")


def search_location(search_data: str):
    location = geo_locator.geocode(search_data)
    if location:
        return LocationGet.parse_obj(location.raw)
    # TODO: manage without raise ValueError
    raise ValueError(f'We cannot find place with name {search_data}')


def get_from_cash(search_data: str):
    cashed = cash.get(search_data)
    if cashed:
        return LocationGet.parse_raw(cashed)


def set_cash(search_data: str, location: LocationGet):
    cash.set(name=search_data, value=location.json())


def get_location(search_data: str):
    cashed = get_from_cash(search_data)
    if cashed:
        return cashed
    location = search_location(search_data)
    set_cash(search_data, location)
    return location
