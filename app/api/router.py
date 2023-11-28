from fastapi import APIRouter

from app.api.samples.router import sample_router

api = APIRouter()

api.include_router(sample_router, tags=['samples'])
