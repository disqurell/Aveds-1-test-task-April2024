from fastapi.responses import ORJSONResponse

from jose import JWTError

from utils.exceptions import (
    NotFoundError,
    InvalidPasswordError,
    AlreadyExist,
    TokenExpired,
    NoMatch,
)


async def except_nf(_, exc: NotFoundError):
    return ORJSONResponse({"message": exc.detail}, 404)


async def except_ip(_, exc: InvalidPasswordError):
    return ORJSONResponse({"message": exc.detail}, 403)


async def except_ae(_, exc: AlreadyExist):
    return ORJSONResponse({"message": exc.detail}, 409)


async def except_jwt_invalid(_, exc: JWTError):
    return ORJSONResponse({"message": "Invalid jwt token"}, 400)


async def except_token_expired(_, exc: TokenExpired):
    return ORJSONResponse({"message": "Token expired"}, 400)


async def except_password_match(_, exc: NoMatch):
    return ORJSONResponse({"message": "No match passwords, try again"}, 400)


EXCEPTION_HANDLER_STACK = {
    NotFoundError: except_nf,
    InvalidPasswordError: except_ip,
    AlreadyExist: except_ae,
    JWTError: except_jwt_invalid,
    TokenExpired: except_token_expired,
    NoMatch: except_password_match,
}
