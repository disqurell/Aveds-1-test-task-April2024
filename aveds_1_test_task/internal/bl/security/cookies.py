from typing import Optional
from fastapi.responses import ORJSONResponse
from settings.api import API_CONFIG


def build_token_response(token, payload: Optional[dict] = None):
    body = {
        "message": "Authorized",
        "access_token": token,
        "token_type": "bearer"
    }
    if payload is not None:
        body.update(data=payload)

    response = ORJSONResponse(body)

    if API_CONFIG.ENV == "prod":
        response.set_cookie(
            "Authorization",
            f"bearer {token}",
            max_age=60 * 60 * 24,
            secure=True,
            httponly=True,
        )
    else:
        response.set_cookie(
            "Authorization",
            f"bearer {token}",
            max_age=60 * 60 * 24 * 7,
        )

    return response
