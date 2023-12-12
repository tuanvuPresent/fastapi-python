from typing import List

from fastapi import APIRouter, Depends
from fastapi_restful.cbv import cbv
from app.core.pagination import LimitOffsetPagination
from .schema import (
    SampleSchema,
    SampleListPaginationSchema,
    SampleSchemaRequest,
    SampleSchemaResponse,
    SampleFilter,
)
from .service import SampleService
from app.core.exception_handler import CustomException
from app.core.message import ErrorMessage
from app.core.schema import DataResponse

sample_router = APIRouter()


@cbv(sample_router)
class SampleApiView:
    @sample_router.post("/samples/", response_model=DataResponse[SampleSchemaResponse])
    async def create(self, data: SampleSchemaRequest):
        return DataResponse(data=SampleService().create(data))

    @sample_router.get("/samples/", response_model=DataResponse[SampleListPaginationSchema])
    async def list(
        self,
        pagination: LimitOffsetPagination = Depends(),
        filter_kwargs: SampleFilter = Depends(),
    ):  
        return DataResponse(data=SampleService().list(filter_kwargs.dict(), pagination))

    @sample_router.get("/samples/{id}", response_model=DataResponse[SampleSchema])
    async def retrieve(self, id: str):
        book = SampleService().get(id)
        if book is None:
            raise CustomException(ErrorMessage.NOT_FOUND)
        return DataResponse(data=book)

    @sample_router.put(
        "/samples/{id}", response_model=DataResponse[SampleSchemaResponse]
    )
    async def update(self, id: str, data: SampleSchemaRequest):
        book = SampleService().update(id, data)
        if book is None:
            raise CustomException(ErrorMessage.NOT_FOUND)
        return DataResponse(data=book)

    @sample_router.delete(
        "/samples/{id}", response_model=DataResponse[SampleSchemaResponse]
    )
    async def delete(self, id: str):
        book = SampleService().delete(id)
        if book is None:
            raise CustomException(ErrorMessage.NOT_FOUND)
        return DataResponse(data=book)
