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
    email = name + "@gmail.com"

    # create
    response = client.post("/users", json=dict(name=name, email=email))
    response.raise_for_status()
    data = response.json()
    # retrieve
    email = data["email"]
    url = f'/users/{email}'
    response = client.get(url)
    response.raise_for_status()
    data = response.json()
    assert data["name"] == name
    assert data["email"] == email
    # delete
    response = client.delete(url)
    response.raise_for_status()
    assert client.get(url).status_code == 404


def _rand(length: int) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
