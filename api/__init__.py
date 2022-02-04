from typing import Dict
from fastapi import FastAPI
from .task import router as task


def create_app() -> FastAPI:
    description = """
dcservice or Docker Computation Service is a docker based sand-boxed task processing HTTP API implementation.
It takes a set of defined tools (as docker images) and their respective input and listens for task requests on an HTTP REST API.
    """
    app = FastAPI(
        title="DCSERVICE",
        description=description,
        version="0.1",
        contact={
            "name": "Pouria Mokhtari",
            "url": "https://github.com/pouriamokhtari/dcservice",
            "email": "contact@pouriamokhtari.ir",
        },
        license_info={
            "name": "MIT License",
            "url": "https://mit-license.org/",
        },
    )

    app.include_router(task)

    return app
