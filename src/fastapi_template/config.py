import uuid
from sqlalchemy.engine.url import URL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

DB_HOST = config("POSTGRES_HOST", default=None)
DB_PORT = config("POSTGRES_PORT", cast=int, default=None)
DB_USER = config("POSTGRES_USER", default=None)
DB_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret, default=None)
DB_DATABASE = config("POSTGRES_DATABASE", default=None)
DB_DSN = URL(
    drivername="postgresql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_DATABASE,
)

DB_POOL_MIN_SIZE = config("DB_POOL_MIN_SIZE", cast=int, default=1)
DB_POOL_MAX_SIZE = config("DB_POOL_MAX_SIZE", cast=int, default=16)
DB_ECHO = config("DB_ECHO", cast=bool, default=False)
DB_SSL = config("DB_SSL", default=None)
DB_USE_CONNECTION_FOR_REQUEST = config("DB_USE_CONNECTION_FOR_REQUEST",
                                       cast=bool,
                                       default=True)
DB_RETRY_LIMIT = config("DB_RETRY_LIMIT", cast=int, default=32)
DB_RETRY_INTERVAL = config("DB_RETRY_INTERVAL", cast=int, default=1)

ACCESS_TOKEN_EXPIRE_MINUTES = 60
SECRET_KEY = config("SECRET_KEY", default=str(uuid.uuid4()))
