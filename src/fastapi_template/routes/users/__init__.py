# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
from typing import List
import fastapi

from fastapi_template.models.users import User
from fastapi_template import schemas

router = fastapi.APIRouter()


@router.get("/users", response_model=List[schemas.User])
async def get_users():
    """get_users.
    """
    users = await User.query.gino.all()
    return users


@router.post("/users", response_model=schemas.User)
async def add_user(user: schemas.UserCreate):
    """add_user.

    Args:
        user (schemas.UserCreate): user
    """
    user = await User.create(**user)
    return user


@router.get("/users/{email}", response_model=schemas.User)
async def get_user(email: str):
    """get_user.

    Args:
        email (str): email
    """
    user = await User.get_or_404(email)
    return user


@router.delete("/users/{email}")
async def delete_user(email: str):
    """delete_user.

    Args:
        email (str): email
    """
    user = await User.get_or_404(email)
    await user.delete()
    return dict(email=email)
