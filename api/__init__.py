from typing import Dict
from fastapi import FastAPI
from .task import router as task


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(task)

    return app
