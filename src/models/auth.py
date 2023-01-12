from pydantic import BaseModel, Field


class UsernameModel(BaseModel):
    username: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "user123",
            }
        }


class AuthModel(UsernameModel):
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "user123",
                "password": "password"
            }
        }


class RegisterModel(AuthModel):
    nickname: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "user123",
                "password": "password",
                "nickname": "nickname123"
            }
        }

