import abc
from pathlib import Path
from dataclasses import dataclass

import toml
import dataconf


class ABCConfigParser(abc.ABC):
	@abc.abstractmethod
	def parse(self) -> "BaseConfig":
		pass


class TomlConfigParser(ABCConfigParser):
	def __init__(self, path: Path) -> None:
		self._path = path

	def parse(self) -> "BaseConfig":
		data = toml.load(self._path)
		config: BaseConfig = dataconf.dict(data, BaseConfig)  # type: ignore
		return config


@dataclass
class WheelsConfig():
	in_a_pin: int
	in_b_pin: int
	pwm_pin: int
	en_pin: int
	servo_pin: int


@dataclass
class HandConfig():
	base_servo_pin: int
	claw_servo_1_pin: int
	claw_servo_2_pin: int


@dataclass
class BucketConfig():
	active_servo_pin: int


@dataclass
class ClawConfig():
	active_servo_pin: int
	rotation_servo_pin: int


@dataclass
class BaseConfig():
	wheels: WheelsConfig
	hand_1: HandConfig
	hand_2: HandConfig
	bucket: BucketConfig
	claw: ClawConfig
