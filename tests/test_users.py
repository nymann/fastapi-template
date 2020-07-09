"""Example Google style docstrings.

"""
import random
import string
import pydantic

ROUTE = "/users/"


def create_user(client, user: dict):
    return client.post(ROUTE, json=user)


def update_user(client, user: dict, identifier: pydantic.UUID4):
    return client.update(ROUTE + identifier, json=user)


def delete_user(client, identifier: pydantic.UUID4):
    return client.delete(ROUTE + identifier)


def get_user(client, identifier: pydantic.UUID4):
    return client.get(ROUTE + identifier)


def get_users(client, page: int = 1, page_size: int = 50):
    return client.get(ROUTE, params=dict(page=page, page_size=page_size))


def test_crud(client):
    """test_crud.

    Args:
        client:
    """
    user = _user(client=client)

    # create
    response = create_user(client, user)
    response.raise_for_status()
    data = response.json()
    identifier = data["identifier"]

    # retrieve
    response = get_user(client, identifier)
    response.raise_for_status()
    data = response.json()
    assert data["name"] == user["name"]
    assert data["email"] == user["email"].lower()

    # delete
    response = delete_user(client, identifier)
    response.raise_for_status()
    data = response.json()
    assert data["identifier"] == identifier
    #assert get_user(client, identifier).status_code == 404


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
