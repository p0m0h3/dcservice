from typing import List, Dict

from pydantic import BaseModel


class Task(BaseModel):
    id: str
    tool: str
    args: Dict[str, str] = {}
    owner_id: int

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    email: str
    is_active: bool
    tasks: List[Task] = []

    class Config:
        orm_mode = True
