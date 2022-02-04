import base64
from fastapi import APIRouter

from fastapi import HTTPException
from containers import service
from containers.exceptions import (
    ContainerNotExited,
    ContainerNotFound,
    ArgumentNotFound,
)
from .schemas import Task, TaskResult, TaskOutput, TaskStatus

router = APIRouter()


@router.get("/tools")
def get_tools():
    return service.tools


@router.post("/task", response_model=TaskResult)
def create_task(task: Task):
    try:
        task_id = service.start_task(task.tool, args=task.args)
    except ArgumentNotFound as ex:
        raise HTTPException(
            status_code=422, detail="A required argument is not entered."
        ) from ex
    return TaskResult(id=task_id, tool=task.tool, args=task.args, stdin=task.stdin)


@router.get("/task/{task_id}", response_model=TaskStatus)
def get_task(task_id: str):
    try:
        return TaskStatus(id=task_id, status=service.task_status(task_id))
    except ContainerNotFound as ex:
        raise HTTPException(status_code=404) from ex


@router.get("/task/{task_id}/output", response_model=TaskOutput)
def fetch_output(task_id: str):
    try:
        return TaskOutput(
            id=task_id, output=base64.b64encode(service.fetch_output(task_id))
        )
    except ContainerNotExited as ex:
        raise HTTPException(
            status_code=503,
            detail="Container output is not available yet. container is running.",
        ) from ex
