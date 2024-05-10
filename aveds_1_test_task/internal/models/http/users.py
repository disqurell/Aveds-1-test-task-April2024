from typing import Optional

from pydantic import BaseModel


class UserPOST(BaseModel):
    email: str
    password: str


class UserPOSTRegister(UserPOST):
    username: str


class UserPUT(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class AddTgBot(BaseModel):
    tg_bot_token: str
