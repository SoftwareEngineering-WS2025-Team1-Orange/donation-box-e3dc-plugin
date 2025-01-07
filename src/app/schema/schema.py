from dataclasses import field
from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class E3dcConfig(BaseModel):
    e3dc_user: str
    e3dc_password: str
    e3dc_serial: str
    e3dc_config: dict[str, Any] = field(default_factory=dict)


class PasskeyConfigRequest(BaseModel):
    passkey: str
    config: Optional[E3dcConfig] | None = None


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
