# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""

import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations import sqlalchemy

from fastapi_template import version
from fastapi_template.models import DB
from fastapi_template.routes.users import router as user_router


def create_app() -> FastAPI:
    """create_app.

    Args:

    Returns:
        FastAPI:
    """
    app: FastAPI = FastAPI(title="fastapi_template",
                           version=version.__version__)
    _initalize_extensions(app=app)
    return _register_routes(app=app)


def _register_routes(app: FastAPI) -> FastAPI:
    """_register_routes.

    Args:
        app (FastAPI): app

    Returns:
        FastAPI:
    """
    app.include_router(user_router)
    return app


def _initalize_extensions(app: FastAPI):
    """_initalize_extensions.

    Args:
        app (FastAPI): app
    """
    DB.init_app(app=app)
    sentry_sdk.init(integrations=[
        sqlalchemy.SqlalchemyIntegration(),
    ])
