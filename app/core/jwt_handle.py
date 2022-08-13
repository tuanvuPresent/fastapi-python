from datetime import datetime, timedelta

from jose import jwt

from app.core.settings import settings


def jwt_encode_handler(payload):
    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        settings.JWT_ALGORITHM
    )


def jwt_decode_handler(token):
    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM]
    )


def jwt_payload_handler(user, timestamp):
    return {
        'user_id': user.get('id'),
        'exp': datetime.now() + timedelta(settings.JWT_EXPIRATION_DELTA),
        'orig_iat': timestamp
    }


def jwt_get_user(payload):
    return payload.get('user_id')
