from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api.router import api
from app.core.exception_handler import exception_handler
from app.core.settings import settings
from celery_app.tasks import create_tasks


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_exception_handler(HTTPException, exception_handler)

app.include_router(api, prefix='/api/v1')


@app.get("/background-tasks")
async def background_tasks():
    create_tasks.delay(1, 2, 3)
    return {"message": "Run background"}
