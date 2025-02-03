from fastapi import APIRouter
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.backend.db import Base

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users():
    pass


@router.get("/{user_id}")
async def user_by_id(user_id: int):
    pass


@router.post("/create")
async def create_user():
    pass


@router.put("/update")
async def update_user():
    pass


@router.delete("/delete")
async def delete_user():
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String)
    firstname: Mapped[str] = mapped_column(String)
    lastname: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    slug: Mapped[str] = mapped_column(String, unique=True, index=True)

    # Связь с таблицей Task
    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="user")