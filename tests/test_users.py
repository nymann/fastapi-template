# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
import random
import string


def test_crud(client):
    """test_crud.

    Args:
        client:
    """
    name = _rand(8)
    email = name + "@nymann.dev"
    route = "/users"

    # create
    user = dict(name=name, email=email, password=_rand(26))
    response = client.post(route, json=user)
    response.raise_for_status()
    data = response.json()
    identifier = data["identifier"]
    route_id = f"{route}/{identifier}"

    # retrieve
    response = client.get(route_id)
    response.raise_for_status()
    data = response.json()
    assert data["name"] == name
    assert data["email"] == email.lower()

    # delete
    response = client.delete(route_id)
    response.raise_for_status()
    data = response.json()
    assert data["identifier"] == identifier
    assert client.get(route_id).status_code == 404


def _rand(length: int) -> str:
    """_rand.

    Args:
        length (int): length

    Returns:
        str:
    """
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
