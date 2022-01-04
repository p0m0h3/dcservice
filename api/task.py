from fastapi import APIRouter

from fastapi import HTTPException
from containers import service
from containers.exceptions import ContainerNotExited
from .schemas import Task, TaskResult, TaskOutput

router = APIRouter()


@router.get("/tools")
def get_tools():
    return service.tools


@router.post("/task", response_model=TaskResult)
def read_root(task: Task):
    task_id = service.start_task(task.tool, args=task.args)
    return TaskResult(id=task_id, tool=task.tool, args=task.args, stdin=task.stdin)


@router.get("/task/{task_id}/output", response_model=TaskOutput)
def fetch_output(task_id: str):
    try:
        return TaskOutput(id=task_id, output=service.fetch_output(task_id))
    except ContainerNotExited as ex:
        raise HTTPException(
            status_code=503,
            detail="Container output is not available yet. container is running.",
        ) from ex
