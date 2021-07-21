from pydantic import BaseModel


class LocationGet(BaseModel):
    display_name: str
    lat: float
    lon: float
