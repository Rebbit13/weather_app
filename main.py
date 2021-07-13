from fastapi import FastAPI

import view.town

app = FastAPI()
app.include_router(view.town.router)

STATIC_PATH = 'static/'