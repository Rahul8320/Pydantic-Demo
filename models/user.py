from typing import Any
from pydantic import BaseModel, Field, field_validator, model_validator


class User(BaseModel):
    username: str

    @field_validator("username")
    def username_length(cls, v: str) -> str:
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters long")

        return v


class SignupDto(BaseModel):
    password: str = Field(..., min_length=6, max_length=15)
    confirm_password: str = Field(..., min_length=6, max_length=15)

    @model_validator(mode="after")
    def password_match(cls, values: Any) -> Any:
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")

        return values
