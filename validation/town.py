from pydantic import BaseModel, validator


class TownCreate(BaseModel):
    name: str
    altitude: float
    longitude: float

    @validator("altitude")
    def check_altitude(cls, v):
        if v < -90:
            raise ValueError("altitude cannot be lesser then -90")
        elif v > 90:
            raise ValueError("altitude cannot be greater then 90")
        return v

    @validator("longitude")
    def check_longitude(cls, v):
        if v < -180:
            raise ValueError("longitude cannot be lesser then -180")
        elif v > 180:
            raise ValueError("longitude cannot be greater then 180")
        return v


class TownComplete(BaseModel):
    id: int
    created_at: str
    name: str
    altitude: float
    longitude: float
    weather_now: str
    forecast: str


class TownUpdate(BaseModel):
    name: str = None
    altitude: float = None
    longitude: float = None
