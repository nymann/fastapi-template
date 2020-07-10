"""

"""
from typing import Tuple, Dict, Any
import random
import string
import pytest
import pydantic
from requests import exceptions

from tests import utils

ROUTE = "/users/"


def raise_for_status(func):

    def wrapper(*args, **kwargs) -> Tuple[Dict[str, Any], int]:
        print(f"Called wrapper with function: '{func.__name__}'.")
        print(f"args: '{args}', kwargs '{kwargs}'.")
        response = func(*args, **kwargs)
        print(f"response saved, status code: {response.status_code}")
        response.raise_for_status()
        return response.json(), response.status_code

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


def mock_user(full_name: str = None,
              email: pydantic.EmailStr = None,
              password: str = None,
              is_admin: bool = False):
    if full_name is None:
        full_name = f"{utils.random_string(length=10)} {utils.random_string(length=8)}"

    if email is None:
        email = str(full_name).replace(' ', '.')
        email += "@nymann.dev"

    if password is None:
        password = utils.random_string(length=28)
    return dict(email=email,
                name=full_name,
                is_admin=is_admin,
                password=password)


def no_state_change(data: Dict[str, Any],
                    user: Dict[str, Any],
                    identifier: pydantic.UUID4 = None) -> None:
    assert user["email"].lower() == data["email"]
    assert user["name"] == data["name"]
    assert user["is_admin"] == data["is_admin"]
    assert data.get("password") is None
    if identifier:
        assert identifier == data["identifier"]
