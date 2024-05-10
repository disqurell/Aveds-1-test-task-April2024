from jose import jwt

from settings.api import API_CONFIG
from models.dto.bearer import (
    TokenPayloadUserBasic,
)

from utils.date_time import now
from datetime import timedelta


def generate_jwt_token():
    return _create_users_basic_token


def decode_jwt_token(token: str):
    decoded = jwt.decode(
        token, key=API_CONFIG.SECRET, algorithms=[API_CONFIG.ALGORITHM]
    )
    return decoded


def payload_tokenize(func):
    def wrap(*args, **kwargs):
        payload = func(*args, **kwargs)
        payload_enc = payload.model_dump()
        encoded_jwt = jwt.encode(
            payload_enc, API_CONFIG.SECRET, algorithm=API_CONFIG.ALGORITHM
        )
        return encoded_jwt

    return wrap


@payload_tokenize
def _create_users_basic_token(
    user_id: str,
    exp_time: timedelta = timedelta(minutes=30),
):
    exp = now() + exp_time.seconds
    return TokenPayloadUserBasic(uuid=user_id, exp=exp)
