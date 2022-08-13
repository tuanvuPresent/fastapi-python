from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.jwt_handle import jwt_decode_handler, jwt_get_user


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            return self.verify_token(credentials.credentials)
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_token(self, token):
        try:
            payload = jwt_decode_handler(token)
            # extra logic here
            return jwt_get_user(payload)
        except:
            raise HTTPException(
                status_code=403,
                detail=f"Could not validate credentials",
            )
