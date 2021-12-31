from typing import List, Dict, Optional

from pydantic import BaseModel


class Task(BaseModel):
    tool: str
    args: Dict[str, str] = {}
    stdin: Optional[str]


class TaskResult(BaseModel):
    id: str
    tool: str
    args: Dict[str, str] = {}
    stdin: Optional[str]
