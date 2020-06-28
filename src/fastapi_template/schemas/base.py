# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
from datetime import datetime
import pydantic
import uuid


class Base(pydantic.BaseModel):
    """Base.
    """

    created_at: datetime

    class Config:
        """Config.
        """

        orm_mode = True
