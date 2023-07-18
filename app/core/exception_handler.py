from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.core.message import ErrorMessage
from app.core.schema import DataResponse


class CustomException(HTTPException):
    status_code: int
    code: str
    message: str

    def __init__(self, status_code: int = 400, code: str = None, message: str = None):
        self.status_code = status_code if status_code else 500
        self.code = code if code else str(self.status_code)
        self.message = message


async def exception_handler(request: Request, exc: HTTPException):
    if not isinstance(exc, CustomException):
        exc = CustomException(**ErrorMessage.SERVER_ERROR)

    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(DataResponse().custom_response(exc.message, exc.code))
    )
