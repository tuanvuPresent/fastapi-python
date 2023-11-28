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

    def __init__(self, error: ErrorMessage, status_code: int = 400):
        self.status_code = status_code
        self.code = error.code
        self.message = error.message


async def exception_handler(request: Request, exc: HTTPException):
    if not isinstance(exc, CustomException):
        exc = CustomException(ErrorMessage.SERVER_ERROR)
    if exc.code == ErrorMessage.INVALID_AUTH.code:
        exc.status_code = 401
    if exc.code == ErrorMessage.NOT_PERMISSION.code:
        exc.status_code = 403
    if exc.code == ErrorMessage.NOT_FOUND.code:
        exc.status_code = 404

    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(DataResponse().custom_response(exc.message, exc.code))
    )
