from fastapi import APIRouter
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.backend.db import Base
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.routers.schemas import CreateUser, UpdateUser
from sqlalchemy import select, insert, update, delete
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])


# Получить всех пользователей
@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    result = db.scalars(select(User)).all()
    return result


# Получить пользователя по ID
@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")


# Создать пользователя
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    slug = slugify(user.username)
    new_user = {
        "username": user.username,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "age": user.age,
        "slug": slug,
    }
    db.execute(insert(User).values(**new_user))
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


# Обновить пользователя
@router.put("/update/{user_id}")
async def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    update_data = {
        "firstname": user.firstname,
        "lastname": user.lastname,
        "age": user.age,
    }
    db.execute(update(User).where(User.id == user_id).values(**update_data))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


# Удалить пользователя
@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.scalar(select(User).where(User.id == user_id))
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User deleted successfully!"}


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