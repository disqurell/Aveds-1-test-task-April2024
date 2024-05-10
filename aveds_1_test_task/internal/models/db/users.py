from typing import Optional
from datetime import datetime
import uuid

from pydantic import BaseModel, computed_field


class UserCreate(BaseModel):
    username: str
    email: str
    password_hash: str
    tg_bot_token: Optional[str] = "null"

    @computed_field
    def created_at(self) -> int:
        return int(datetime.now().timestamp())

    @computed_field
    def updated_at(self) -> int:
        return int(datetime.now().timestamp())

    @computed_field
    def uuid(self) -> str:
        return str(uuid.uuid4())


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    tg_bot_token: Optional[str] = None

    @computed_field
    def updated_at(self) -> int:
        return int(datetime.now().timestamp())


class UserGet(UserUpdate):
    uuid: str
