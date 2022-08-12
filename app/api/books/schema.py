from pydantic import BaseModel, validator

from app.api.books.constants import BOOK_NAME_MAX_LENGTH
from app.core.exception_handler import CustomException
from app.core.message import ErrorMessage


class BookSchema(BaseModel):
    id: int
    name: str
    type: int

    class Config:
        orm_mode = True


class BookSchemaRequest(BaseModel):
    name: str
    type: int

    class Config:
        orm_mode = True

    @validator('name')
    def check_name(cls, v):
        if len(v) > BOOK_NAME_MAX_LENGTH:
            raise CustomException(**ErrorMessage.BOOK_NAME_MAX_LENGTH)
        return v


class BookSchemaResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
