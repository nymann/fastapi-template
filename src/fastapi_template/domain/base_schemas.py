import pydantic


class Pagination(pydantic.BaseModel):
    more: bool
    total: int
