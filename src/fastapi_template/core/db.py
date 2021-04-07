"""This module is for providing a common `DB` object."""

from gino.ext import starlette
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import EmailType

from fastapi_template.core import config_loader

DB = starlette.Gino(
    dsn=config_loader.DB_DSN,
    pool_min_size=config_loader.DB_POOL_MIN_SIZE,
    pool_max_size=config_loader.DB_POOL_MAX_SIZE,
    echo=config_loader.DB_ECHO,
    ssl=config_loader.DB_SSL,
    use_connection_for_request=config_loader.DB_USE_CONNECTION_FOR_REQUEST,
    retry_limit=config_loader.DB_RETRY_LIMIT,
    retry_interval=config_loader.DB_RETRY_INTERVAL,
)

DB.UUID = UUID
DB.EmailType = EmailType
