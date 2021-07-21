from pydantic import BaseModel


class TownName(BaseModel):
    name: str


class TownComplete(BaseModel):
    id: int
    created_at: str
    name: str
    altitude: float
    longitude: float
    weather_now: str
    forecast: str
