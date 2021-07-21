import logging

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette import status
from starlette.templating import Jinja2Templates

from services.town import TownLogic
from validation.town import TownName

router = APIRouter()
templates = Jinja2Templates(directory="templates")


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level='DEBUG', format=LOG_FORMAT)
logger = logging.getLogger()


async def return_404_not_found(town_id):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"message": f'There is no town with id {town_id}'})


@router.get('/api/town/')
async def get_all_towns():
    result = TownLogic().get_all()
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"towns": result})


@router.post('/api/town/')
async def create_town(town: TownName):
    town_json = TownLogic().create(town)
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content=town_json)


@router.get('/api/town/{town_id}/')
async def get_town(town_id: int):
    town_json = TownLogic().get(town_id)
    if town_json:
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=town_json)
    else:
        return await return_404_not_found(town_id)


@router.put('/api/town/{town_id}/')
async def update_town(town_id: int, town: TownName):
    town_json = TownLogic().update(town_id, town)
    if town_json:
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content=town_json)
    else:
        return await return_404_not_found(town_id)


@router.delete('/api/town/{town_id}/')
async def delete_town(town_id):
    town_json = TownLogic().get(town_id)
    if town_json:
        TownLogic().delete(town_id)
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message": f'Delete town with id {town_id}'})
    else:
        return await return_404_not_found(town_id)


@router.get('/')
async def get_towns_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "towns": TownLogic().get_all()})
