import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    UVICORN_PORT = os.getenv('UVICORN_PORT', '8000')
    UVICORN_HOST = os.getenv('UVICORN_HOST', '127.0.0.1')
    UVICORN_WORKERS = os.getenv('UVICORN_WORKERS', '1')

    API_ROUTE = "/api/v1.0"


class TestConfig(Config):
    TESTING = True
