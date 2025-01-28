from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Список пользователей
users = []


# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    user_id = len(users) + 1  # Генерация ID на основе длины списка
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int = Path(..., ge=1), username: str = None, age: int = None):
    for user in users:
        if user.id == user_id:
            if username is not None:
                user.username = username
            if age is not None:
                user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int = Path(..., ge=1)):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
