__all__ = [
    "TokenPayloadUserBasic",
]


from pydantic import BaseModel

from models.aliases import UnixTimestamp


class TokenPayloadUserBasic(BaseModel):
    uuid: str
    exp: UnixTimestamp
