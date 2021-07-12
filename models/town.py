from datetime import datetime

from sqlalchemy import Column, DateTime, String

from database.db import Base
from models.mixin import BaseMixin


class Town(BaseMixin, Base):
    __tablename__ = 'town'

    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String)
    altitude = Column(String)
    longitude = Column(String)
    weather_now = Column(String)
    forecast = Column(String)

    def __repr__(self):
        return f'Town{self.name}'
