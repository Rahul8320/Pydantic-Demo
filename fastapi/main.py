from http import HTTPStatus
from typing import Dict
from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


class UserSignup(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=15)


class Settings(BaseModel):
    app_name: str = "Coder App"
    admin_email: EmailStr = "admin@coder.com"


def get_settings() -> Settings:
    return Settings()


@app.post("/signup", status_code=HTTPStatus.CREATED)
def signup(user: UserSignup) -> Dict[str, int | str]:
    return {
        "status": HTTPStatus.CREATED,
        "message": f"User {user.username} signed up successfully",
    }


@app.get("/settings", status_code=HTTPStatus.OK)
def retrieve_settings(
    settings: Settings = Depends(get_settings),
) -> Dict[str, int | Settings]:
    return {"status": HTTPStatus.OK, "data": settings}
