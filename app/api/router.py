from fastapi import APIRouter

from app.api.books.router import book_router

api = APIRouter()

api.include_router(book_router, tags=['books'])
