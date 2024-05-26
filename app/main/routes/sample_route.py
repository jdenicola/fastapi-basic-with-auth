from fastapi import APIRouter, Depends

from app.schemas.sample_model import SampleModel
from app.commons.enum.sample_roles_enum import SampleRoleEnum
from app.dependencies.sample_role_query import SampleRoleQuery

sample_route = APIRouter(
    prefix="/sample"
)


@sample_route.get("/")
async def sample_route_get(model: SampleModel):
    return model


@sample_route.get("/hidden", include_in_schema=False)
async def sample_hidden_route_get(model: SampleModel):
    return model


@sample_route.post("/", dependencies=[Depends(SampleRoleQuery([SampleRoleEnum.ADMIN]))])
async def sample_secured_post_route(model: SampleModel):
    return model


"""
Pydantic models

Remember to set `from_attributes` flag on config Class if you use ORM Mode
https://docs.pydantic.dev/latest/concepts/models/#rebuild-model-schema
"""
