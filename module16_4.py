from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def all_users() -> List[User]:
    return users


@app.get('/user/{user_id}')
async def get_users(user_id: int):
    user_index = None
    for i in range(len(users)):
        if users[i].id == user_id:
            user_index = i
            break
    if user_index is not None:
        return user_index
    else:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post('/user/{username}/{age}')
async def post_user(username, age) -> User:
    if len(users) == 0:
        user_id = 1
    user_id = users[-1].id + 1 if users != [] else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", exemple='24')],
                      user_id: int = Path(ge=1, le=100, description="Enter User ID", example='16')) -> str:
    for up_user in users:
        if up_user.id == user_id:
            up_user.username = username
            up_user.age = age
            return f"The user {user_id} is updated."
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User with ID {user_id} was deleted."
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
