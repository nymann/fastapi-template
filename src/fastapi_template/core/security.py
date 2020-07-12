"""This module is for all things security.

Access tokens, hashing passwords.
"""
from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from fastapi_template.core import config_loader

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(subject: Union[str, Any],
                        expires_delta: timedelta = None) -> str:
    """create_access_token.

    Args:
        subject (Union[str, Any]): subject
        expires_delta (timedelta): expires_delta

    Returns:
        str:
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=config_loader.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode,
                             config_loader.SECRET_KEY,
                             algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """verify_password.

    Args:
        plain_password (str): plain_password
        hashed_password (str): hashed_password

    Returns:
        bool:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """get_password_hash.

    Args:
        password (str): password

    Returns:
        str:
    """
    return pwd_context.hash(password)
