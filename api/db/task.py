from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from . import Base
from .user import User


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, index=True)
    tool = Column(String)
    owner_id = Column(Integer, ForeignKey(User.id))
    args = Column(String)

    owner = relationship("User", back_populates="tasks")
