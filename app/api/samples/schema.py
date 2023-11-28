from pydantic import BaseModel, validator
from typing import Optional, List
from .constants import NAME_MAX_LENGTH
from app.core.exception_handler import CustomException
from app.core.message import ErrorMessage
from app.core.filters import BaseFilter
from app.core.pagination import PaginationSchema

class SampleSchema(BaseModel):
    id: int
    name: str
    type: int

    class Config:
        orm_mode = True


class SampleListPaginationSchema(PaginationSchema):
    data: List[SampleSchema]


class SampleSchemaRequest(BaseModel):
    name: str
    type: int

    class Config:
        orm_mode = True

    @validator('name')
    def check_name(cls, v):
        if len(v) > NAME_MAX_LENGTH:
            raise CustomException(ErrorMessage.BOOK_NAME_MAX_LENGTH)
        return v


class SampleSchemaResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True


class SampleFilter(BaseFilter):
    name: Optional[str]
