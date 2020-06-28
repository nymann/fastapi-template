# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
import pytest
from starlette import testclient
import wert_api
import subprocess
import pathlib


@pytest.fixture
def app():
    """app.
    """
    return wert_api.create_app()


@pytest.fixture
def client(app):
    """client.

    Args:
        app:
    """
    cwd = pathlib.Path(__file__).parent.parent
    subprocess.check_call(["alembic", "upgrade", "head"], cwd=cwd)
    with testclient.TestClient(app) as client:
        yield client
    # TODO this should only be called if tests fail?
