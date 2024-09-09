from fastapi import FastAPI

app = FastAPI()


@app.get("/user/{admin}")
async def welcome_admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/{user_id}")
async def id_user(user_id: int) -> dict:
    return {"User": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def user_info(username: str, age: int) -> dict:
    return {"Информация о пользователе":  f"Имя: {username}, Возраст: {age}"}

