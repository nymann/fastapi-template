# -*- coding: utf-8 -*-
"""Example Google style docstrings.

"""
from fastapi_template.models import DB
from sqlalchemy.dialects import postgresql as psql
from sqlalchemy import func


class User(DB.Model):
    """User.
    """

    __tablename__ = "users"

    identifier = DB.Column(psql.UUID(as_uuid=True), primary_key=True)
    email = DB.Column(DB.String(), unique=True, index=True, nullable=False)
    name = DB.Column(DB.String(), index=True)
    admin = DB.Column(DB.Boolean(), default=False)
    created_at = DB.Column(DB.DateTime(timezone=True),
                           server_default=func.now())
    password = DB.Column(DB.String(), nullable=False)

    def __init__(self,
                 email: str,
                 name: str,
                 password: str,
                 admin: bool = False):
        """__init__.

        Args:
            email (str): email
            name (str): name
            password (str): password
            admin (bool): admin
        """
        self.email = email
        self.name = name
        self.admin = admin
        self.password = password
