from database.db import Session
from external_services.nominatim_geocode import get_location
from external_services.yandex_weather import get_formed_weather_data
from models.town import Town
from services.mixin import SingletonNaiveMeta
from validation.town import TownName


class TownLogic(metaclass=SingletonNaiveMeta):

    @staticmethod
    def get_all():
        session = Session()
        towns_list = session.query(Town).filter()
        towns_list = [t.json() for t in towns_list]
        return towns_list

    @staticmethod
    def delete(town_id):
        session = Session()
        session.query(Town).where(Town.id == town_id).delete()
        session.commit()

    @staticmethod
    def get(town_id: int):
        session = Session()
        town = session.query(Town).filter(Town.id == town_id).one_or_none()
        return town

    @staticmethod
    def update_weather(town: Town):
        town_weather = get_formed_weather_data(town.altitude, town.longitude)
        if town_weather != {"weather_now": town.weather_now, "forecast": town.forecast}:
            town_id = town.id
            session = Session()
            session.query(Town).where(Town.id == town.id).update(town_weather)
            session.commit()
            return TownLogic.get(town_id)
        return town

    @staticmethod
    def get_duplicate(name: str):
        session = Session()
        town_matches = session.query(Town).filter(Town.name == name).one_or_none()
        if town_matches:
            town_matches = TownLogic.update_weather(town_matches)
            return town_matches

    @staticmethod
    def update(town_id: int, town: TownName):
        location = get_location(town.name)
        duplicate = TownLogic.get_duplicate(location.display_name)
        if duplicate:
            return duplicate
        town_concrete = TownLogic.get(town_id)
        if town_concrete:
            town_weather = get_formed_weather_data(location.lat, location.lon)
            town = {'name': location.display_name,
                    'altitude': location.lat,
                    "longitude": location.lon,
                    "weather_now": town_weather['weather_now'],
                    "forecast": town_weather['forecast']}
            session = Session()
            session.query(Town).where(Town.id == town_id).update(town)
            session.commit()
            return TownLogic.get(town_id)

    @staticmethod
    def create(town: TownName):
        location = get_location(town.name)
        if location is None:
            return None
        duplicate = TownLogic.get_duplicate(location.display_name)
        if duplicate:
            return duplicate.json()
        town_weather = get_formed_weather_data(location.lat, location.lon)
        town = Town(name=location.display_name,
                    longitude=location.lon,
                    altitude=location.lat,
                    weather_now=town_weather['weather_now'],
                    forecast=town_weather['forecast'])
        session = Session()
        session.add(town)
        session.flush()
        town_json = town.json()
        session.commit()
        return town_json
