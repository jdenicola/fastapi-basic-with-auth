from fastapi import APIRouter

from app.main.routes.sample_route import sample_route
from config import Config

config = Config()

router = APIRouter(
    prefix=config.API_ROUTE,
    tags=["main"],
    responses={404: {"description": "Not found"}}
)

router.include_router(sample_route)
