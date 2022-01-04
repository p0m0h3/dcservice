"""
schema definition for task api
"""
from typing import Dict, Optional

from pydantic import BaseModel


class Task(BaseModel):
    """
    a task unit to be started
    """

    tool: str
    args: Dict[str, str] = {}
    stdin: Optional[str] = ""


class TaskResult(BaseModel):
    """
    an started task report
    """

    id: str
    tool: str
    args: Dict[str, str] = {}
    stdin: Optional[str] = ""


class TaskOutput(BaseModel):
    """
    a finished task output
    """

    id: str
    output: str
