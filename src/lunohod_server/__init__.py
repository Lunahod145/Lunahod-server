from pathlib import Path

from lunohod_details import (
    Lunohod,
    Wheels,
    VNH3SP30Motor,
    AngularServo90,
)
from fastapi import FastAPI

from .routers import LunohodRoutable
from .config import TomlConfigParser


config = TomlConfigParser(Path(".lunohod_server.toml")).parse()
app = FastAPI()
routable_routers = (
    LunohodRoutable(
        lunohod=Lunohod(
            wheels=Wheels(
                motor=VNH3SP30Motor(
                    IN_A=config.wheels.in_a_pin,
                    IN_B=config.wheels.in_b_pin,
                    PWM=config.wheels.pwm_pin,
                    EN=config.wheels.en_pin,
                ),
                servo=AngularServo90(config.wheels.servo_pin),
            ),
            hand_1=__import__("unittest.mock").mock.Mock(),  # FIXME
            hand_2=__import__("unittest.mock").mock.Mock(),
            bucket=__import__("unittest.mock").mock.Mock(),
            claw=__import__("unittest.mock").mock.Mock(),
        )
    ),
)

for routable_router in routable_routers:
    app.include_router(routable_router.router)
