"""Example Google style docstrings.

"""
import random
import string
import pytest
import pydantic
from requests import exceptions

ROUTE = "/users/"


def raise_for_status(func):

    def wrapper(*args, **kwargs):
        print(f"Called wrapper with function: '{func.__name__}'.")
        print(f"args: '{args}', kwargs '{kwargs}'.")
        response = func(*args, **kwargs)
        print(f"response saved, status code: {response.status_code}")
        response.raise_for_status()
        return response.json()

    return wrapper


@raise_for_status
def create_user(client, user: dict):
    return client.post(ROUTE, json=user)


@raise_for_status
def update_user(client, user: dict, identifier: pydantic.UUID4):
    return client.update(ROUTE + identifier, json=user)


@raise_for_status
def delete_user(client, identifier: pydantic.UUID4):
    return client.delete(ROUTE + identifier)


@raise_for_status
def get_user(client, identifier: pydantic.UUID4):
    return client.get(ROUTE + identifier)


@raise_for_status
def get_users(client, page: int = 1, page_size: int = 50):
    return client.get(ROUTE, params=dict(page=page, page_size=page_size))


def test_crud(client):
    """test_crud.

    Args:
        client:
    """
    user = _user(client=client)

    # create
    data = create_user(client=client, user=user)
    identifier = data["identifier"]

    # retrieve
    data = get_user(client=client, identifier=identifier)
    assert data["name"] == user["name"]
    assert data["email"] == user["email"].lower()

    # delete
    data = delete_user(client=client, identifier=identifier)
    assert data["identifier"] == identifier

    with pytest.raises(exceptions.HTTPError):
        get_user(client=client, identifier=identifier)


def _rand(length: int) -> str:
    """_rand.

    Args:
        length (int): length

    Returns:
        str:
    """
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def _user(client,
          full_name: str = None,
          email: pydantic.EmailStr = None,
          password: str = None,
          is_admin: bool = False):
    if full_name is None:
        full_name = f"{_rand(length=10)} {_rand(length=8)}"

    if email is None:
        email = str(full_name).replace(' ', '.')
        email += "@nymann.dev"

    if password is None:
        password = _rand(length=28)
    return dict(email=email,
                name=full_name,
                is_admin=is_admin,
                password=password)
