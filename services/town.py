import json
import os
from datetime import timedelta

from redis import Redis

from database.db import Session
from external_services.yandex_weather import get_formed_weather_data
from models.town import Town
from services.mixin import SingletonNaiveMeta
from validation.town import TownCreate, TownUpdate


class TownLogic(metaclass=SingletonNaiveMeta):
    cash = Redis(host="cash", port=os.environ['REDIS_PORT'], password=os.environ['REDIS_PASSWORD'])

    def _set_cash(self, town: Town):
        self.cash.setex(name=town.id,
                        time=timedelta(hours=int(os.environ['CASH_HOURS_TO_LIVE'])),
                        value=json.dumps(town.json()))
        towns = json.loads(self.cash.get('towns').decode('utf-8'))
        duplicates = [towns.index(town_dict) for town_dict in towns if town_dict['id'] == town.id]
        for index in duplicates:
            towns.pop(index)
        towns.append(town.json())
        self.cash.set("towns", json.dumps(towns))

    def _get_one_from_cash(self, town_id: int):
        return json.loads(self.cash.get(town_id).decode('utf-8'))

    def _get_all_from_cash(self):
        return json.loads(self.cash.get('towns').decode('utf-8'))

    def _delete_from_cash(self, town_id):
        self.cash.delete(town_id)
        towns = json.loads(self.cash.get('towns').decode('utf-8'))
        towns_for_delete = [towns.index(town_dict) for town_dict in towns if town_dict['id'] == int(town_id)]
        for index in towns_for_delete:
            towns.pop(index)
        self.cash.set("towns", json.dumps(towns))

    def warm_the_cash(self):
        session = Session()
        towns = session.query(Town).filter()
        towns = [t.json() for t in towns]
        self.cash.set("towns", json.dumps(towns))

    def get_all(self):
        return self._get_all_from_cash()

    def create(self, town: TownCreate):
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
        self._set_cash(town)
        town_json = town.json()
        session.commit()
        return town_json

    def _update_town_weather(self, town):
        session = Session()
        town_id = town.id
        town_weather = get_formed_weather_data(longitude=town.longitude,
                                               altitude=town.altitude)
        town.weather_now, town.forecast = town_weather['weather_now'], town_weather['forecast']
        session.query(Town).where(Town.id == town_id).update(town.json())
        self._set_cash(town)
        session.commit()
        return self._get_one_from_cash(town_id)

    def get(self, town_id: int):
        town_cashed = self._get_one_from_cash(town_id)
        if town_cashed:
            return town_cashed
        session = Session()
        town = session.query(Town).filter(Town.id == town_id).one_or_none()
        if town:
            town = self._update_town_weather(town)
        return town

    def update(self, town_id: int, town: TownUpdate):
        session = Session()
        town_concrete = session.query(Town).filter(Town.id == town_id).one_or_none()
        if town_concrete:
            if town.name:
                town_concrete.name = town.name
            if town.longitude:
                town_concrete.longitude = town.longitude
            if town.altitude:
                town_concrete.altitude = town.altitude
            town = self._update_town_weather(town_concrete)
            return town

    def delete(self, town_id):
        self._delete_from_cash(town_id)
        session = Session()
        session.query(Town).where(Town.id == town_id).delete()
        session.commit()
