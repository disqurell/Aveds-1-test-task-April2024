from fastapi import APIRouter
from settings.api import API_CONFIG

from .auth import router as basic_router
from .bot_inter import router as bot_inter_router


v1_router = APIRouter(prefix=f"/v{API_CONFIG.VERSION}")
v1_router.include_router(basic_router)
v1_router.include_router(bot_inter_router)
