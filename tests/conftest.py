import subprocess
import pathlib
import pytest
from starlette import testclient
from wert_api import create_app


@pytest.fixture
def client():
    cwd = pathlib.Path(__file__).parent.parent
    subprocess.check_call(["alembic", "upgrade", "head"], cwd=cwd)
    app = create_app()
    with testclient.TestClient(app) as client:
        yield client
    subprocess.check_call(["alembic", "downgrade", "base"], cwd=cwd)
