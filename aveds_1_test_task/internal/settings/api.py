import typing as t

from pathlib import Path
from multiprocessing import cpu_count

from .base import ConfigBase


class ApiConfig(ConfigBase):
    VERSION: str = "0.0.1"

    RELOAD: bool = True

    ENV: str = "dev"
    PROJECT_PATH: str = str(Path(__file__).parents[3])

    HOST: str = "0.0.0.0"
    PORT: int = 8090
    DEBUG: bool = True
    ALLOW_ORIGINS: list[str] = ["*"]

    WORKERS: int = cpu_count() * 2 + 1

    SECRET: str = "test"
    ALGORITHM: str = "HS256"

    API_ROOT_PATH: str = ""


class OpenAPIConfig(ConfigBase):
    NO_DOCS: bool = False

    title: str = "Aveds_1_test_task"
    description: str = "Sample API"
    docs_url: str = "/api/docs"
    # root_path: str = "/"

    if NO_DOCS:
        openapi_url: t.Optional[str] = None
    else:
        openapi_url: t.Optional[str] = "/api/openapi.json"


class CORSConfig(ConfigBase):
    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True


API_CONFIG = ApiConfig()
SWAGGER_CONFIG = OpenAPIConfig()
CORS_CONFIG = CORSConfig()
