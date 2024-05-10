from fastapi import APIRouter, Depends, Request
from fastapi.responses import ORJSONResponse

from models.http.users import UserPOST, UserPOSTRegister

from bl.security.bearer import JWTBearer
from bl.security.jwt_token import generate_jwt_token
from bl.security.passwords import (
    validate_password,
)
from bl.security.cookies import build_token_response
from bl.aveds_bl import UsersDomain

from utils.exceptions import (
    InvalidPasswordError,
    NotFoundError,
    AlreadyExist,
)


router = APIRouter(prefix="/auth")


@router.get(
    "/user/token/check",
    tags=["Auth users"],
    dependencies=[Depends(JWTBearer())],
)
async def check_users_token_basic():
    return ORJSONResponse({"message": "Authorized"})


@router.post(
    "/user/login",
    tags=["Auth users"],
)
async def login_user_basic(req: Request, user_login: UserPOST):
    user = await UsersDomain().find_user_by_field('email', user_login.email)

    if not user:
        raise NotFoundError("User not found")

    if not validate_password(user[0][2], user_login.password):
        raise InvalidPasswordError

    token = generate_jwt_token()(user[0][5])

    return build_token_response(token)


@router.post(
    "/user/register",
    tags=["Auth users"],
)
async def register_user_basic(req: Request, user_reg: UserPOSTRegister):
    user = await UsersDomain().find_user_by_field('email', user_reg.email)

    if user:
        raise AlreadyExist("User already exists")

    result = await UsersDomain().create_user(user_reg)

    if result:
        return ORJSONResponse({"message": "Registered"}, 201)

    return ORJSONResponse({"message": "Error"}, 400)
