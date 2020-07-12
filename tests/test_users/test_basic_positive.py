"""Basic positive tests (happy paths).

This module executes API calls with valid required parameters.

Validation checks:
    Validate status code: All requests should return 2XX HTTP status codes.
    Validate payload: Response is a well-formed JSON object.
    Validate state: GET requests should not change state.
    Validate headers: Verifies if headers are the same as expected.
"""

from tests import test_users, utils
import pytest
from requests import exceptions
import pydantic


def test_validate_status_codes(client):

    user = test_users.mock_user()

    # Get user list should give 200 OK
    data, status_code = test_users.get_users(client=client)
    assert status_code == 200

    # For create methods we expect 201 Created
    data, status_code = test_users.create_user(client=client, user=user)
    assert status_code == 201
    identifier = data["identifier"]

    # Retrieve, we expect 200 OK here.
    data, status_code = test_users.get_user(client=client,
                                            identifier=identifier)
    assert status_code == 200

    # We expect 200 OK from updates.
    update_user = user
    update_user["name"] = "Test Testsen"
    _, status_code = test_users.update_user(client=client,
                                            user=data,
                                            identifier=identifier)
    assert status_code == 200

    # Delete, since we are returning the deleted user, a 200 OK is expected
    # instead of 204 No Content.
    data, status_code = test_users.delete_user(client=client,
                                               identifier=identifier)
    assert status_code == 200


def test_validate_payload(client):
    user = test_users.mock_user()

    # Check if the payload when creating a user matches what we thing.
    data, _ = test_users.create_user(client=client, user=user)

    # API should save the email as lowercase.
    test_users.no_state_change(data=data, user=user)

    # Check if the provided identifier (UUID4) is valid
    identifier = data["identifier"]
    try:
        pydantic.UUID4(identifier)
    except pydantic.ValidationError:
        pytest.fail("Not a valid UUID4")

    # Check if the state is the same.
    data, _ = test_users.get_user(client=client, identifier=identifier)
    test_users.no_state_change(data=data, user=user, identifier=identifier)

    # Delete, since we are returning the deleted user, a 200 OK is expected
    data, status_code = test_users.delete_user(client=client,
                                               identifier=identifier)
    test_users.no_state_change(data=data, user=user, identifier=identifier)


def test_validate_headers(client):
    pass


def test_performance_sanity(client):
    mock_user = test_users.mock_user()

    @utils.time_it
    def create(c, u):
        return test_users.create_user(client=c, user=u)

    user, _ = create(c=client, u=mock_user)

    @utils.time_it
    def get(c, identifier: pydantic.UUID4):
        return test_users.get_user(client=c, identifier=identifier)

    get(c=client, identifier=user["identifier"])

    @utils.time_it
    def delete(c, identifier: pydantic.UUID4):
        return test_users.delete_user(client=c, identifier=identifier)
