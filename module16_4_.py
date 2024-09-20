from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def all_users() -> List[User]:
    return users


@app.get(path="/user/{user_id}")
async def get_users(user_id) -> User:
    try:
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post('/user/{username}/{age}')
async def post_user(username, age) -> User:
    if len(users) == 0:
        user_id = 1
    user_id = len(users) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, age: int, username: str) -> User:
    try:
        user = users[user_id]
        user["username"] = username
        user["age"] = age
        return users[user_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User with ID {user_id} was deleted."
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
