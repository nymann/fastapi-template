"""Module for configuring tests."""
import pathlib
import subprocess  # noqa: S404 used for specific command, should be fine.

import pytest
from starlette import testclient

from fastapi_template import app as fastapi_template_app


@pytest.fixture
def app():
    """Yield the app.

    Returns:
        app
    """
    return fastapi_template_app.create_app()


@pytest.fixture
def client(app):  # noqa: WPS442
    """Get test client.

    Args:
        app: The fastapi_template app.

    Yields:
        app: Yields an instance of the app after running migrations
    """
    cwd = pathlib.Path(__file__).parent.parent
    command = ["alembic", "upgrade", "head"]
    subprocess.check_call(command, cwd=cwd)  # noqa: S603, S607
    with testclient.TestClient(app) as test_client:
        yield test_client
