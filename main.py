from fastapi import FastAPI

from view import town

app = FastAPI()
app.include_router(town.router)

STATIC_PATH = 'static/'
