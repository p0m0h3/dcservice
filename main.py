from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

from containers import service

app = FastAPI()


class Arg(BaseModel):
    key: str
    value: str


class Task(BaseModel):
    tool_id: str
    args: Dict[str, str]


@app.post("/task")
def read_root(task: Task) -> Dict[str, str]:
    task_id = service.start_task(task.tool_id, args=task.args)
    return {'task_id': task_id}
