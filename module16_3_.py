from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Exemple, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_message(username: str = Path(min_length=5, max_length=20,
                                            description="Enter Username", example="UrbanUser"),
                       age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = username, age
    return f"User {username} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_users(username: Annotated[str, Path(min_length=5, max_length=20,
                                                     description="Enter username", example="UrbanUser")],
                       user_id: str = Path(min_length=1, max_length=100,
                                           description="Enter User ID", example="1"),
                       age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> str:
    users[user_id] = age, username
    return f"The user {user_id} has bin updated."


@app.delete("/user/{user_id}")
async def delete_users(user_id: str) -> str:
    users.pop(user_id)
    return f"Message with {user_id} was deleted."
