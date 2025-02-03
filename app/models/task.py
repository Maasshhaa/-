from fastapi import APIRouter
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.backend.db import Base
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.user import User
from app.routers.schemas import CreateTask, UpdateTask
from sqlalchemy import select, insert, update, delete

router = APIRouter(prefix="/task", tags=["task"])


# Получить все задачи
@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(Task)).all()
    return result


# Получить задачу по ID
@router.get("/{task_id}")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task:
        return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")


# Создать задачу
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    new_task = {
        "title": task.title,
        "content": task.content,
        "priority": task.priority,
        "user_id": user_id,
    }
    db.execute(insert(Task).values(**new_task))
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


# Обновить задачу
@router.put("/update/{task_id}")
async def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalar(select(Task).where(Task.id == task_id))
    if not existing_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

    update_data = {
        "title": task.title,
        "content": task.content,
        "priority": task.priority,
    }
    db.execute(update(Task).where(Task.id == task_id).values(**update_data))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}


# Удалить задачу
@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.scalar(select(Task).where(Task.id == task_id))
    if not existing_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task deleted successfully!"}


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