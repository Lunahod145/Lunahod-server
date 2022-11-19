import typing as t

from fastapi import APIRouter

if t.TYPE_CHECKING:
    from lunohod_details import Lunohod


class LunohodRouterFactory(APIRouter):
    def __init__(self, lunohod: "Lunohod", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._lunohod = lunohod

        self.add_api_route("/hello", self.hello, methods=["GET"])


    async def hello(self):
        return {"Hello": str(self._lunohod)}
