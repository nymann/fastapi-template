# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
from typing import Optional
import uuid
import pydantic
import datetime as dt


class UserBase(pydantic.BaseModel):
    """UserBase.
    """
    email: pydantic.EmailStr
    name: Optional[str] = None
    admin: bool = False


class UserCreate(UserBase):
    """UserCreate.

    Properties to receive via API on creation.
    """
    password: str


class UserUpdate(UserBase):
    """UserUpdate.

    Properties to receive via API on update.
    """

    pass


class User(UserBase):
    """User.

    Additional properties to return in endpoints.
    """
    pass


class UserInDB(User):
    """UserInDB.

    Additional properties stored in the database.
    """
    created_at: dt.datetime
