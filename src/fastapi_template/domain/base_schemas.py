"""Base schemas are common schemas inherited by domain specific schemas."""

import pydantic


class Pagination(pydantic.BaseModel):  # noqa: H601
    """Common pagination pydantic model."""

    more: bool
    total: int
