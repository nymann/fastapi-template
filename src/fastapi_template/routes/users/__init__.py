# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
import uuid
from typing import List

import fastapi

from fastapi_template.core import security
from fastapi_template.models.users import User as ORMUser
from fastapi_template.schemas import user as schemas

router = fastapi.APIRouter()


@router.get("/users", tags=["Users"], response_model=List[schemas.User])
async def get_users():
    """get_users.
    """
    users: List[ORMUser] = await ORMUser.query.gino.all()
    return users


@router.post("/users", tags=["Users"], response_model=schemas.User)
async def add_user(request: schemas.UserCreateIn):
    """add_user.

    Args:
        request (schemas.UserCreateIn): request
    """
    hashed_password = security.get_password_hash(request.password)
    user: ORMUser = await ORMUser.create(email=request.email,
                                         name=request.name,
                                         password=hashed_password)
    return schemas.User.from_orm(user)


@router.get("/users/{identifier}", tags=["Users"], response_model=schemas.User)
async def get_user(identifier: uuid.UUID):
    """get_user.

    Args:
        identifier (str): identifier
    """
    user: ORMUser = await ORMUser.get_or_404(identifier)
    return schemas.User.from_orm(user)


@router.delete("/users/{identifier}",
               tags=["Users"],
               response_model=schemas.User)
async def delete_user(identifier: uuid.UUID):
    """delete_user.

    Args:
        identifier (str): identifier
    """
    user: ORMUser = await ORMUser.get(identifier)
    deleted_user: schemas.User = schemas.User.from_orm(user)
    await user.delete()
    return deleted_user
