from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/{admin}")
async def welcome() -> dict:
    return {"message": "Вы вошли как администратор"}
