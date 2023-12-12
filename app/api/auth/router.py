from datetime import datetime

from fastapi import APIRouter
from fastapi_restful.cbv import cbv

from .schema import LoginRequestResponse, LoginRequestSchema
from app.core.jwt_handle import jwt_payload_handler, jwt_encode_handler
from app.core.schema import DataResponse

auth_router = APIRouter()


@cbv(auth_router)
class AuthApiView:

    @auth_router.post("/login", response_model=DataResponse[LoginRequestResponse])
    async def login(self, data: LoginRequestSchema):
        # extra login here
        timestamp = datetime.now().timestamp()
        payload = jwt_payload_handler({'id': data.username}, timestamp)
        return DataResponse(data={
            'token': jwt_encode_handler(payload)
        })
