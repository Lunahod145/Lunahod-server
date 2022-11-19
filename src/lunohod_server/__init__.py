from lunohod_details import Lunohod
from fastapi import FastAPI

from .routers import LunohodRouterFactory


app = FastAPI()
routers = [
    LunohodRouterFactory(__import__("unittest.mock").mock.Mock()),  # TODO
]
for router in routers:
    app.include_router(router)
