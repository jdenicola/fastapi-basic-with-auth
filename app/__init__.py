from fastapi import FastAPI, Request
from fastapi.exceptions import ResponseValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.commons.exceptions.exception_handlers import bad_request_exception_handler, forbidden_exception_handler, \
    unauthorized_exception_handler, not_found_exception_handler, internal_server_error_handler
from app.commons.utils.http_utils import get_body, _log_response_to_logger

from app.main.routes import router
from config import Config
from app.commons.logger import LoggerWriter

logger = LoggerWriter('test')

config = Config()


def create_app(config_class=Config):
    app = FastAPI(
        title="my-sample-api",
        description="My sample API",
        version="v0.1",
        openapi_url=config_class.API_ROUTE + "/openapi.json",
        docs_url=config_class.API_ROUTE + "/docs",
        redoc_url=config_class.API_ROUTE + "/redoc",
        contact={
            "name": "My Name",
            "email": "my-email@my-domain.com"
        },
        exception_handlers={
            400: bad_request_exception_handler,
            401: unauthorized_exception_handler,
            403: forbidden_exception_handler,
            404: not_found_exception_handler,
            500: internal_server_error_handler,
            ResponseValidationError: bad_request_exception_handler
        }
    )

    origins = ["*"]

    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"]
                       )

    app.include_router(router)

    @app.middleware("http")
    async def after_request_middleware(request: Request, call_next):
        body = await get_body(request)
        body_data = body.decode('utf-8')
        response = await call_next(request)

        # TODO: Will fix
        disabled = True

        if not (response.headers.get('direct_passthrough')) and not disabled:
            if not response.status_code >= 400:
                await _log_response_to_logger(response, body_data, request, logger.write)
            else:
                await _log_response_to_logger(response, body_data, request, logger.write)
        return response

    return app
