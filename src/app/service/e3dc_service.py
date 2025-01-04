from fastapi import HTTPException

from e3dc import E3DC
from ..schema.schema import E3dcConfig


class E3dcService:
    def __init__(self):
        self.config = None

    def configure_service(self, config: E3dcConfig):
        self.config = config

    def poll(self, config: E3dcConfig | None):
        local_config = config or self.config

        if not local_config:
            raise HTTPException(status_code=400, detail="No config provided")

        e3dc_obj = E3DC(E3DC.CONNECT_WEB, username=local_config.e3dc_user, password=local_config.e3dc_password,
                        serialNumber=local_config.e3dc_serial,
                        isPasswordMd5=False,
                        configuration=local_config.e3dc_config)

        return e3dc_obj.poll(keepAlive=True)
