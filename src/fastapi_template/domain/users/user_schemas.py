from typing import List, Optional

import pydantic

from fastapi_template.domain import base_schemas


class _Base(pydantic.BaseModel):
    email: pydantic.EmailStr = pydantic.Field(
        ...,
        description="The email to your account (can be changed later)",
        example="kristian@nymann.dev")
    name: Optional[str] = pydantic.Field(
        None,
        description="The full name of the user",
        example="Kristian Nymann")
    is_admin: Optional[bool] = pydantic.Field(
        False,
        description="Should the user be an administrator?",
        example=False)

    @pydantic.validator("name")
    def name_must_contain_space(cls, value: str):
        if ' ' not in value:
            raise ValueError("Name must contain a space")
        return value


class Create(_Base):
    password: pydantic.constr(min_length=8, max_length=50) = pydantic.Field(
        ...,
        description="The password of the user (minimum 8 chars, max 50.",
        example="SomeRandomPassword")


class Update(_Base):
    password: Optional[pydantic.SecretStr] = None
    email: Optional[pydantic.EmailStr] = None


class DB(_Base):
    identifier: pydantic.UUID4

    class Config:
        orm_mode = True


class Paginated(pydantic.BaseModel):
    results: List[DB]
    pagination: base_schemas.Pagination
