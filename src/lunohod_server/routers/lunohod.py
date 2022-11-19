import typing as t

from classy_fastapi import Routable, put

if t.TYPE_CHECKING:
    from lunohod_details import Lunohod


class LunohodRoutable(Routable):
    def __init__(self, lunohod: "Lunohod", *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._lunohod = lunohod

    @put("wheels/set_min_angle")
    async def _wheels__set_min_angle(self) -> None:
        self._lunohod.wheels.set_min_angle()

    @put("wheels/set_mid_angle")
    async def _wheels__set_mid_angle(self) -> None:
        self._lunohod.wheels.set_mid_angle()

    @put("wheels/set_max_angle")
    async def _wheels__set_max_angle(self) -> None:
        self._lunohod.wheels.set_max_angle()

    @put("wheels/set_angle")
    async def _wheels__set_angle(self, angle: int) -> None:
        self._lunohod.wheels.set_angle(angle)

    @put("wheels/set_speed")
    async def _wheels__set_speed(self, value: int) -> None:
        self._lunohod.wheels.set_speed(value)

    # async def _wheels__get_speed(self) -> int:
    #     return self._lunohod.wheels.get_speed()

    @put("wheels/backward")
    async def _wheels__backward(self) -> None:
        self._lunohod.wheels.backward()

    @put("wheels/forward")
    async def _wheels__forward(self) -> None:
        self._lunohod.wheels.forward()

    @put("wheels/reverse")
    async def _wheels__reverse(self) -> None:
        self._lunohod.wheels.reverse()

    @put("wheels/stop")
    async def _wheels__stop(self) -> None:
        self._lunohod.wheels.stop()


    @put("bucket/activate")
    async def _bucket__activate(self) -> None:
        self._lunohod.bucket.activate()

    @put("bucket/deactivate")
    async def _bucket__deactivate(self) -> None:
        self._lunohod.bucket.deactivate()


    @put("claw/activate")
    async def _claw__activate(self) -> None:
        self._lunohod.claw.activate()

    @put("claw/deactivate")
    async def _claw__deactivate(self) -> None:
        self._lunohod.claw.deactivate()

    @put("claw/set_angle")
    async def _claw__set_angle(self, angle: int) -> None:
        self._lunohod.claw.set_angle(angle)

    @put("claw/set_min_angle")
    async def _claw__set_min_angle(self) -> None:
        self._lunohod.claw.set_min_angle()

    @put("claw/set_mid_angle")
    async def _claw__set_mid_angle(self) -> None:
        self._lunohod.claw.set_mid_angle()

    @put("claw/set_max_angle")
    async def _claw__set_max_angle(self) -> None:
        self._lunohod.claw.set_max_angle()


    @put("hand_1/set_x_angle")
    async def _hand_1__set_x_angle(self, angle: int) -> None:
        self._lunohod.hand_1.set_x_angle(angle)

    @put("hand_1/set_x_min_angle")
    async def _hand_1__set_x_min_angle(self) -> None:
        self._lunohod.hand_1.set_x_min_angle()

    @put("hand_1/set_x_mid_angle")
    async def _hand_1__set_x_mid_angle(self) -> None:
        self._lunohod.hand_1.set_x_mid_angle()

    @put("hand_1/set_x_max_angle")
    async def _hand_1__set_x_max_angle(self) -> None:
        self._lunohod.hand_1.set_x_max_angle()

    @put("hand_1/set_y_angle")
    async def _hand_1__set_y_angle(self, angle: int) -> None:
        self._lunohod.hand_1.set_y_angle(angle)

    @put("hand_1/set_y_min_angle")
    async def _hand_1__set_y_min_angle(self) -> None:
        self._lunohod.hand_1.set_y_min_angle()

    @put("hand_1/set_y_mid_angle")
    async def _hand_1__set_y_mid_angle(self) -> None:
        self._lunohod.hand_1.set_y_mid_angle()

    @put("hand_1/set_y_max_angle")
    async def _hand_1__set_y_max_angle(self) -> None:
        self._lunohod.hand_1.set_y_max_angle()


    @put("hand_2/set_x_angle")
    async def _hand_2__set_x_angle(self, angle: int) -> None:
        self._lunohod.hand_2.set_x_angle(angle)

    @put("hand_2/set_x_min_angle")
    async def _hand_2__set_x_min_angle(self) -> None:
        self._lunohod.hand_2.set_x_min_angle()

    @put("hand_2/set_x_mid_angle")
    async def _hand_2__set_x_mid_angle(self) -> None:
        self._lunohod.hand_2.set_x_mid_angle()

    @put("hand_2/set_x_max_angle")
    async def _hand_2__set_x_max_angle(self) -> None:
        self._lunohod.hand_2.set_x_max_angle()

    @put("hand_2/set_y_angle")
    async def _hand_2__set_y_angle(self, angle: int) -> None:
        self._lunohod.hand_2.set_y_angle(angle)

    @put("hand_2/set_y_min_angle")
    async def _hand_2__set_y_min_angle(self) -> None:
        self._lunohod.hand_2.set_y_min_angle()

    @put("hand_2/set_y_mid_angle")
    async def _hand_2__set_y_mid_angle(self) -> None:
        self._lunohod.hand_2.set_y_mid_angle()

    @put("hand_2/set_y_max_angle")
    async def _hand_2__set_y_max_angle(self) -> None:
        self._lunohod.hand_2.set_y_max_angle()
