from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/users")
async def post_user(username: str, age: int) -> User:
    current_index = len(users)
    users.append({"id": current_index, "username": username, "age": age})
    return users[-1]


@app.put("/users/{user_id}")
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        user = users[user_id]
        user["username"] = username
        user["age"] = age
        return f"The user {user_id} has been updated."
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User with ID {user_id} was deleted."
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
