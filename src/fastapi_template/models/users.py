# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
from fastapi_template.models import DB, base


class User(base.Base):
    """User.
    """

    __tablename__ = "users"

    identifier = DB.Column(DB.UUID(as_uuid=False), primary_key=True)
    email = DB.Column(DB.EmailType, unique=True, index=True, nullable=False)
    name = DB.Column(DB.String(), index=True)
    admin = DB.Column(DB.Boolean(), default=False)
    password = DB.Column(DB.String(), nullable=False)
