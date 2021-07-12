from sqlalchemy import Column, Integer


class BaseMixin:
    id = Column(Integer, primary_key=True)
