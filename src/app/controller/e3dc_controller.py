from fastapi import APIRouter, Response

from e3dc import SendError
from ..service import auth_service, e3dc_service
from ..schema.schema import PollResponse, PasskeyConfigRequest

router = APIRouter()


@router.post("/load_config", status_code=201)
def load_config(pc_request: PasskeyConfigRequest) -> Response:
    auth_service.validate_passkey(pc_request.passkey)

    if e3dc_service.e3dc_obj is not None:
        e3dc_service.disconnect()

    try:
        e3dc_service.configure_service(pc_request.config)
        return Response(status_code=201)
    except SendError:
        return Response(status_code=401)

@router.post("/poll", response_model=PollResponse, status_code=200)
def poll(pc_request: PasskeyConfigRequest) -> PollResponse:
    auth_service.validate_passkey(pc_request.passkey)
    return e3dc_service.poll(pc_request.config)
