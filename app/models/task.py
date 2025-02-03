from fastapi import APIRouter
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.db import Base

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks():
    pass


@router.get("/{task_id}")
async def task_by_id(task_id: int):
    pass


@router.post("/create")
async def create_task():
    pass


@router.put("/update")
async def update_task():
    pass


@router.delete("/delete")
async def delete_task():
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(String)
    priority: Mapped[int] = mapped_column(Integer, default=0)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String, unique=True, index=True)

    # Связь с таблицей User
    user: Mapped["User"] = relationship("User", back_populates="tasks")