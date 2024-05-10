from typing import Optional


class ExceptionBase(Exception):
    detail_default: str

    def __init__(self, detail: Optional[str] = None):
        if self.detail_default is None:
            raise NotImplementedError("detail_default is not implemented")
        self.detail = detail or self.detail_default


class NotFoundError(ExceptionBase):
    detail_default: str = "Resource not found"


class InvalidPasswordError(ExceptionBase):
    detail_default: str = "Invalid password"


class AlreadyExist(ExceptionBase):
    detail_default: str = "Resource already exist"


class AuthorizationError(ExceptionBase):
    detail_default: str = "Unauthorized"


class TokenExpired(ExceptionBase):
    detail_default: str = "Token expired, please request a new one"


class NoMatch(ExceptionBase):
    detail_default: str = "No match passwords"
