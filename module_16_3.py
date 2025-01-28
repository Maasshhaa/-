from fastapi import FastAPI, Path, HTTPException
from typing import Dict, Annotated

app = FastAPI()

# Изначальный словарь пользователей
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=3, max_length=20)],
        age: Annotated[int, Path(ge=1, le=120)]
):
    user_id = str(max(map(int, users.keys()), default=0) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1)],
        username: Annotated[str, Path(min_length=3, max_length=20)],
        age: Annotated[int, Path(ge=1, le=120)]
):
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id_str] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1)]
):
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail="User not found")

    del users[user_id_str]
    return f"User {user_id} has been deleted"
