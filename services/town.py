from database.db import Session
from external_services.yandex_weather import get_formed_weather_data
from models.town import Town
from validation.town import TownCreate, TownUpdate


class TownLogic:

    @staticmethod
    def get_all():
        session = Session()
        towns_list = session.query(Town).filter()
        towns_list = [t.json() for t in towns_list]
        return towns_list

    @staticmethod
    def create(town: TownCreate):
        town_weather = get_formed_weather_data(longitude=town.longitude,
                                               altitude=town.altitude)
        town = Town(name=town.name,
                    longitude=town.longitude,
                    altitude=town.altitude,
                    weather_now=town_weather['weather_now'],
                    forecast=town_weather['forecast'])
        session = Session()
        session.add(town)
        session.flush()
        town_json = town.json()
        session.commit()
        return town_json

    @staticmethod
    def update_town_weather(town_id: int, altitude: float, longitude: float):
        session = Session()
        town_weather = get_formed_weather_data(longitude=longitude, altitude=altitude)
        session.query(Town).where(Town.id == town_id).update(Town.weather_now == town_weather['weather_now'],
                                                             Town.forecast == town_weather['forecast'])
        return

    @staticmethod
    def get(town_id: int):
        session = Session()
        town = session.query(Town).filter(Town.id == town_id).one_or_none()
        return town

    @staticmethod
    def update(town_id: int, town: TownUpdate):
        town_concrete = TownLogic.get(town_id)
        if town_concrete:
            town_weather = get_formed_weather_data(longitude=town.longitude,
                                                   altitude=town.altitude)
            session = Session()
            session.query(Town).where(Town.id == town_id).update(town_weather.update(dict(town)))
            session.commit()
            return TownLogic.get(town_id)
        else:
            return None

    @staticmethod
    def delete(town_id):
        session = Session()
        session.query(Town).where(Town.id == town_id).delete()
        session.commit()
