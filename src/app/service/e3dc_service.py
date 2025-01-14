from fastapi import HTTPException

from e3dc import E3DC
from ..schema.schema import E3dcConfig


class E3dcService:
    def __init__(self):
        self.e3dc_obj = None

    def _build_e3dc_obj(self, local_config: E3dcConfig):
        self.e3dc_obj = E3DC(E3DC.CONNECT_WEB, username=local_config.e3dc_user, password=local_config.e3dc_password,
                             serialNumber=local_config.e3dc_serial,
                             isPasswordMd5=False,
                             configuration=local_config.e3dc_config)

    def configure_service(self, config: E3dcConfig):
        self._build_e3dc_obj(config)

    def disconnect(self):
        self.e3dc_obj = None


    def poll(self, config: E3dcConfig | None):
        if config:
            self._build_e3dc_obj(config)

        if not self.e3dc_obj:
            raise HTTPException(status_code=400, detail="No config provided")

        return self.e3dc_obj.poll(keepAlive=True)
