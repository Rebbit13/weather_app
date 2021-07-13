import logging

from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette import status

from services.town import TownLogic
from validation.town import TownCreate, TownUpdate

router = APIRouter()

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level='DEBUG', format=LOG_FORMAT)
logger = logging.getLogger()


@router.get('/api/town/', response_model=TownCreate)
async def get_all_towns():
    result = TownLogic.get_all_towns()
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"towns": result})


@router.post('/api/town/')
async def create_town(town: TownCreate):
    town = TownLogic.create_town(town)
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content=town.json())


@router.get('/api/town/{town_id}/')
async def get_town(town_id: int):
    town = TownLogic.get_town(town_id)
    if town:
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=town.json())
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": f'There is no town with id {town_id}'})


@router.put('/api/town/{town_id}/')
async def update_town(town_id: int, town: TownUpdate):
    town_updated = TownLogic.update_town(town_id, town)
    if town_updated:
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=town_updated.json())
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": f'There is no town with id {town_id}'})


@router.delete('/api/town/{town_id}/')
async def delete_town(town_id):
    town_updated = TownLogic.delete_town(town_id)
    if town_updated:
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message": f'Delete town with id {town_id}'})
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                            content={"message": f'There is no town with id {town_id}'})
