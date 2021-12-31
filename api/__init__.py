from typing import Dict

from fastapi import FastAPI, Depends

from containers import service
from .schemas import Task, TaskResult


def create_app() -> FastAPI:
    app = FastAPI()

    @app.post("/task")
    def read_root(task: Task) -> TaskResult:
        task_id = service.start_task(task.tool, args=task.args)
        return {'task_id': task_id}

    return app
