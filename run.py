import uvicorn
from app import create_app
from config import Config

app = create_app()


def print_routes(application):
    for route in application.routes:
        try:
            print(route.methods, route.path)
        except AttributeError:
            print(f"[{route.path}]")
            print_routes(route)


print_routes(app)

if __name__ == "__main__":
    config = Config
    uvicorn.run(app, host=config.UVICORN_HOST, port=int(config.UVICORN_PORT))
