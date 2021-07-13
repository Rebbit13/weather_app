from database.db import Session
from models.town import Town
from validation.town import TownCreate, TownUpdate


class TownLogic:

    @staticmethod
    def get_all_towns():
        session = Session()
        towns_list = session.query(Town).filter()
        towns_list = [t.json() for t in towns_list]
        session.close()
        return towns_list

    @staticmethod
    def create_town(town: TownCreate):
        town_weather = {'weather_now': '1', 'forecast': '2'}
        town = Town(name=town.name,
                    longitude=town.longitude,
                    altitude=town.altitude,
                    weather_now=town_weather['weather_now'],
                    forecast=town_weather['forecast'])
        session = Session()
        session.add(town)
        session.flush()
        result = town
        session.commit()
        session.close()
        return result

    @staticmethod
    def get_town(town_id: int):
        session = Session()
        town = session.query(Town).filter(Town.id == town_id).one_or_none()
        session.close()
        return town

    @staticmethod
    def update_town(town_id: int, town: TownUpdate):
        town_concrete = TownLogic.get_town(town_id)
        if town_concrete:
            session = Session()
            session.query(Town).where(Town.id == town_id).update(dict(town))
            session.commit()
            session.close()
            return TownLogic.get_town(town_id)
        else:
            return None

    @staticmethod
    def delete_town(town_id: int):
        town_concrete = TownLogic.get_town(town_id)
        if town_concrete:
            session = Session()
            session.query(Town).where(Town.id == town_id).delete()
            session.commit()
            session.close()
            return True
        else:
            return None
