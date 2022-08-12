from typing import List

from fastapi import APIRouter

from app.api.books.schema import BookSchema, BookSchemaRequest, BookSchemaResponse
from app.api.books.service import BookService
from app.core.exception_handler import CustomException
from app.core.message import ErrorMessage
from app.core.schema import DataResponse

book_router = APIRouter()


@book_router.post("/books/", response_model=DataResponse[BookSchemaResponse])
async def create_books(data: BookSchemaRequest):
    return DataResponse().success_response(BookService().create(data))


@book_router.get("/books/", response_model=DataResponse[List[BookSchema]])
async def get_books(limit: int, offset: int = 0):
    return DataResponse().success_response(BookService().list(limit, offset))


@book_router.get("/books/{id}", response_model=DataResponse[BookSchema])
async def retrieve_book(id: str):
    book = BookService().get(id)
    if book is None:
        raise CustomException(**ErrorMessage.NOT_FOUND)
    return DataResponse().success_response(book)


@book_router.put("/books/{id}", response_model=DataResponse[BookSchemaResponse])
async def update_book(id: str, data: BookSchemaRequest):
    book = BookService().update(id, data)
    if book is None:
        raise CustomException(**ErrorMessage.NOT_FOUND)
    return DataResponse().success_response(book)


@book_router.delete("/books/{id}", response_model=DataResponse[BookSchemaResponse])
async def delete_book(id: str):
    book = BookService().delete(id)
    if book is None:
        raise CustomException(**ErrorMessage.NOT_FOUND)
    return DataResponse().success_response(book)
