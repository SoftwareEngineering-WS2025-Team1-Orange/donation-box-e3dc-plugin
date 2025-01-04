from fastapi import APIRouter, Depends, HTTPException

from ..service.e3dc_service import E3dcService

from ..schema.schema import E3dcConfig, PollResponse

router = APIRouter()


@router.post("/load_config", status_code=201)
def load_config(config: E3dcConfig, e3dc_service: E3dcService = Depends()):
    e3dc_service.configure_service(config)


@router.post("/poll", response_model=PollResponse, status_code=200)
def poll(config: E3dcConfig | None, e3dc_service: E3dcService = Depends()):
    return e3dc_service.poll(config)
