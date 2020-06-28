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
    route_id = f"{route}/{email}"
    # create
    response = client.post(route, json=dict(name=name, email=email))
    response.raise_for_status()
    data = response.json()

    # retrieve
    response = client.get(route_id)
    response.raise_for_status()
    data = response.json()
    assert data["name"] == name
    assert data["email"] == email
    # delete
    response = client.delete(route_id)
    response.raise_for_status()
    assert client.get(route_id).status_code == 404


def _rand(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
