from dataclasses import field
from datetime import datetime
from typing import Any

from pydantic import BaseModel


class E3dcConfig(BaseModel):
    e3dc_user: str
    e3dc_password: str
    e3dc_serial: str
    e3dc_config: dict[str, Any] = field(default_factory=dict)
    passkey: str


class Production(BaseModel):
    solar: int
    add: int
    grid: int


class Consumption(BaseModel):
    battery: int
    house: int
    wallbox: int


class PollResponse(BaseModel):
    time: datetime
    sysStatus: int
    stateOfCharge: int
    production: Production
    consumption: Consumption