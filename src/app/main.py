from fastapi import FastAPI
from .controller.e3dc_controller import router as e3dc_router

app = FastAPI()

app.include_router(e3dc_router)


@app.get("/health")
def read_root():
    return {"status": "ok"}
