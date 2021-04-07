"""Basic positive tests (happy paths)."""

from http import HTTPStatus

from fastapi.responses import Response


def test_validate_status_codes(client):
    """Validate that we can get to the docs page.

    Args:
        client: The test client
    """
    route = "/docs"
    response: Response = client.get(route)
    assert response.status_code == HTTPStatus.OK  # noqa: S101
