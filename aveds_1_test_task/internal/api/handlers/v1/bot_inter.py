from fastapi import APIRouter, Depends, Request
from fastapi.responses import ORJSONResponse

from bl.security.bearer import JWTBearer
from utils.exceptions import (
    InvalidPasswordError,
    NotFoundError,
    AlreadyExist,
)
from models.http.users import AddTgBot
from bl.aveds_bl import UsersDomain


router = APIRouter(prefix="/bot")


@router.post(
    "/add",
    tags=["Bot interactions"],
    dependencies=[Depends(JWTBearer())],
)
async def add_bot(req: Request, tg_bot: AddTgBot):
    result = await UsersDomain().add_tg_bot_to_user(req, tg_bot)

    if result:
        return ORJSONResponse({"message": "Your tg bot token added successfully"}, 201)
    return ORJSONResponse({"message": "Something went wrong :("}, 404)


@router.get(
    "/mybottoken",
    tags=["Bot interactions"],
    dependencies=[Depends(JWTBearer())],
)
async def get_bot_token(req: Request):
    result = await UsersDomain().get_tg_bot_token(req)

    if result:
        return ORJSONResponse({"token": result}, 200)

    raise NotFoundError("No token found")
