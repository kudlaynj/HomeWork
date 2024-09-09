from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/user/{admin}")
async def welcome_admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/{user_id}")
async def id_user(user_id: int = Path(min_length=1, max_length=100,
                                      description="Enter User ID", example="1")) -> dict:
    return {"User": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20,
                                                  description="Enter username", example="UrbanUser")],
                    age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> dict:
    return {"Информация о пользователе": f"Имя: {username}, Возраст: {age}"}
