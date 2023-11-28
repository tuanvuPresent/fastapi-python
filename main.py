from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from debug_toolbar.middleware import DebugToolbarMiddleware
from app.api.router import api
from app.core.exception_handler import exception_handler
from app.core.settings import settings
from app.core.database import Base, engine
import sentry_sdk


Base.metadata.create_all(engine)  # only create new table. recommend migrate Alembic.

sentry_sdk.init(
    dsn=settings.SENTRY_DNS,
    traces_sample_rate=0.5,
    profiles_sample_rate=1.0,
)

app = FastAPI(debug=settings.DEBUG)

app.add_middleware(
    DebugToolbarMiddleware,
    panels=["debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, exception_handler)

app.include_router(api, prefix="/api/v1")
