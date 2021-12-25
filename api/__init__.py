from typing import Dict

from fastapi import FastAPI, Depends

from containers import service
from .db import Base, engine, get_db, SessionLocal
from .db.task import Task as TaskRecord
from .schemas import Task


def create_app() -> FastAPI:
    app = FastAPI()

    Base.metadata.create_all(bind=engine)

    @app.post("/task")
    def read_root(task: Task, db: SessionLocal = Depends(get_db)) -> Dict[str, str]:
        task_id = service.start_ta__isk(task.tool, args=task.args)
        task_record = TaskRecord(id=task.id, tool=task.tool, owner_id=1, args=task.args)
        db.add(task_record)
        db.commit()
        return {'task_id': task_id}

    return app
