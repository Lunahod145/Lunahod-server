from lunohod_details import Lunohod
from fastapi import FastAPI

from .routers import LunohodRoutable


app = FastAPI()
routable_routers = [
    LunohodRoutable(__import__("unittest.mock").mock.Mock()),  # TODO
]
for routable_router in routable_routers:
    app.include_router(routable_router.router)
