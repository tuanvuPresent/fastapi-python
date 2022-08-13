from pydantic import BaseModel


class LoginRequestSchema(BaseModel):
    username: str
    password: int

    class Config:
        orm_mode = True


class LoginRequestResponse(BaseModel):
    token: str

    class Config:
        orm_mode = True
