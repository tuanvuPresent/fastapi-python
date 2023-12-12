from typing import Optional, TypeVar, Generic

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class ResponseSchemaBase(BaseModel):
    __abstract__ = True


class DataResponse(ResponseSchemaBase, GenericModel, Generic[T]):
    status: bool = True
    code: str = ''
    message: str = ''
    data: Optional[T] = None

    class Config:
        arbitrary_types_allowed = True