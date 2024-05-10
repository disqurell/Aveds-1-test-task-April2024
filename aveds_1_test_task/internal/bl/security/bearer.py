from fastapi import Request
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException

from .jwt_token import decode_jwt_token

from models.dto.bearer import (
    TokenPayloadUserBasic,
)


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, req: Request):
        return self.validate_model(self.get_token_decoded(req))

    def validate_model(self, tok_decoded: dict) -> TokenPayloadUserBasic:
        payload = None
        try:
            payload = TokenPayloadUserBasic.model_validate(tok_decoded)
        except:
            pass

        if payload is None:
            raise HTTPException(400, "Invalid token format")

        return payload

    def get_token_decoded(self, req: Request):
        cookie_tok = self._get_token_from_req_cookie(req)
        header_tok = self._get_token_from_req_header(req)

        if (tok := cookie_tok or header_tok) is None:
            raise HTTPException(401, "Not authorized")

        tok_decoded = decode_jwt_token(tok)
        return tok_decoded

    def _get_token_from_req_header(self, req: Request):
        try:
            token = req.headers.get("Authorization")
            if token is not None:
                return token.split()[1]
        except:
            return None

    def _get_token_from_req_cookie(self, req: Request):
        try:
            token = req.cookies.get("Authorization")
            if token is not None:
                return token.split()[1]
        except:
            return None
