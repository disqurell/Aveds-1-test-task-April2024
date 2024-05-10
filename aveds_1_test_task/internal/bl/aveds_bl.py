from fastapi import Request

from models.db.users import UserCreate, UserUpdate, UserGet
from models.http.users import UserPOST, UserPUT, UserPOSTRegister, AddTgBot
from db.base import DbController
from bl.security.passwords import (
    hash_password,
    validate_password,
)
from bl.security.jwt_token import decode_jwt_token


class UsersDomain:
    controller = DbController

    async def get_token(self, req: Request):
        try:
            token = req.cookies.get("Authorization")
            if token is not None:
                return token.split()[1]
        except:
            return None

    async def find_user_by_field(self, field_name: str, field_value: str):
        user = self.controller.select_from_table_with_condition(
            "users", field_name, field_value
        )

        return user

    async def create_user(self, user_reg: UserPOSTRegister):
        new_user = UserCreate(
            password_hash=hash_password(user_reg.password), **user_reg.model_dump()
        ).model_dump()

        result = DbController.add(
            "users",
            str(tuple(new_user.keys())).replace("'", ""),
            tuple(new_user.values()),
        )

        return result

    async def add_tg_bot_to_user(self, req: Request, tg_bot: AddTgBot):
        token = await self.get_token(req)

        decoded_token = decode_jwt_token(token)

        DbController.update_table_with_condition(
            "users",
            "tg_bot_token",
            tg_bot.tg_bot_token,
            "uuid",
            decoded_token.get("uuid"),
        )

        return True

    async def get_tg_bot_token(self, req: Request):
        token = await self.get_token(req)

        decoded_token = decode_jwt_token(token)

        user = await self.find_user_by_field("uuid", decoded_token.get("uuid"))

        return user[0][-1]
