from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from http.client import responses

from app.schemas.error_schemas import Error, CommonResponse


async def bad_request_exception_handler(request: Request, exc) -> JSONResponse:
    return create_error_json_response(request, exc, status.HTTP_400_BAD_REQUEST)


async def unauthorized_exception_handler(request: Request, exc) -> JSONResponse:
    return create_error_json_response(request, exc, status.HTTP_401_UNAUTHORIZED)


async def forbidden_exception_handler(request: Request, exc) -> JSONResponse:
    return create_error_json_response(request, exc, status.HTTP_403_FORBIDDEN)


async def not_found_exception_handler(request: Request, exc) -> JSONResponse:
    return create_error_json_response(request, exc, status.HTTP_404_NOT_FOUND)


async def internal_server_error_handler(request: Request, exc) -> JSONResponse:
    return create_error_json_response(request, exc, status.HTTP_500_INTERNAL_SERVER_ERROR)


async def service_unavailable_exception_handler(request: Request, exc) -> JSONResponse:
    return create_error_json_response(request, exc, status.HTTP_400_BAD_REQUEST)


def create_error_json_response(request: Request, exc: Exception, status_code: int):
    error = Error.from_exception(
        exc,
        status_code=status_code,
        description=str(exc) or responses[status_code],
    )

    return JSONResponse(
        status_code=status_code,
        content=jsonable_encoder(CommonResponse(errors=[error]).model_dump(exclude_unset=True))
    )
