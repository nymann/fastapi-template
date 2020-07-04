# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import EmailType, generic_repr

from fastapi_template.models import DB

DB.UUID, DB.EmailType = (UUID, EmailType)


@generic_repr
class Base(DB.Model):
    """Base.
    """

    __abstract__ = True
    created_at = DB.Column(DB.DateTime,
                           default=datetime.utcnow,
                           server_default=DB.func.now())
