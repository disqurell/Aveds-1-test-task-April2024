from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from settings.api import API_CONFIG, CORS_CONFIG, SWAGGER_CONFIG

from .handlers.v1 import v1_router

from .exceptions import EXCEPTION_HANDLER_STACK


def create_api():
    main_router = APIRouter(prefix="/api")
    main_router.include_router(v1_router)

    @main_router.get("/version", tags=["Get api's version"])
    async def get_api_version():
        return API_CONFIG.VERSION

    api = FastAPI(
        **SWAGGER_CONFIG.model_dump(),
        debug=API_CONFIG.DEBUG,
        version=API_CONFIG.VERSION,
        root_path=API_CONFIG.API_ROOT_PATH,
    )

    api.exception_handlers.update(EXCEPTION_HANDLER_STACK)

    api.include_router(main_router)

    api.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_CONFIG.ALLOW_ORIGINS,
        allow_credentials=CORS_CONFIG.ALLOW_CREDENTIALS,
        allow_methods=CORS_CONFIG.ALLOW_METHODS,
        allow_headers=CORS_CONFIG.ALLOW_HEADERS,
    )

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        print("Starting init processions...")
        yield
        print("Starting shutdown processions...")

    return api


api = create_api()
