# TODO: debug redis connection
from fastapi import FastAPI

import view.town
from services.town import TownLogic

app = FastAPI()
app.include_router(view.town.router)

TownLogic().warm_the_cash()

STATIC_PATH = 'static/'
